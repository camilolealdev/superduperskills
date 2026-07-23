# CI Drift Gate — Spec & Setup

The drift gate is **BLOCKING** from day 1. Any divergence between regenerated dictionary
and committed `docs/dashboards/telemetry-dictionary.md` fails the PR. This file specifies
the workflow, the regenerate script, and the contributor experience when CI fails.

---

## Why Blocking from Day 1

This skill is greenfield — there's no installed base of dashboards or dictionaries to
retrofit. Every metric, span, and log field that lands under this regime knows the rules:

> If you add or change telemetry, regenerate the dictionary in the same PR.

The only friction is the first few PRs after adoption, where contributors learn the
`make telemetry-dictionary` workflow. Acceptable cost for a contract that doesn't rot.

---

## Workflow File

`.github/workflows/telemetry-drift.yml`:

```yaml
name: telemetry-drift
on:
  pull_request:
    paths:
      - "internal/**"
      - "cmd/**"
      - "pkg/**"
      - "go.mod"
      - "go.sum"
      - "docs/dashboards/telemetry-dictionary.md"
      - ".github/workflows/telemetry-drift.yml"
      - "scripts/regenerate-telemetry-dictionary.sh"

jobs:
  drift:
    runs-on: ubuntu-latest
    timeout-minutes: 10
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-go@v5
        with:
          go-version-file: go.mod
          cache: true

      - name: Install Grafonnet toolchain
        run: |
          curl -L https://github.com/google/jsonnet/releases/latest/download/jsonnet-bin-Linux-x86_64.tar.gz | tar xz -C /usr/local/bin
          go install github.com/jsonnet-bundler/jsonnet-bundler/cmd/jb@latest

      - name: Regenerate telemetry dictionary
        run: scripts/regenerate-telemetry-dictionary.sh

      - name: Compare against committed dictionary
        id: drift
        run: |
          # Strip non-deterministic fields (generated_at, source_commit_sha) from both sides
          sed -E 's/^(  generated_at|  source_commit_sha):.*/\1: <REDACTED>/' docs/dashboards/telemetry-dictionary.md > /tmp/committed.md
          sed -E 's/^(  generated_at|  source_commit_sha):.*/\1: <REDACTED>/' /tmp/regen-dictionary.md > /tmp/regen.md

          if diff -u /tmp/committed.md /tmp/regen.md > /tmp/drift.diff; then
            echo "✓ Dictionary in sync with code."
          else
            echo "::error::Telemetry dictionary drift detected."
            echo "Diff between committed and code-regenerated:"
            cat /tmp/drift.diff
            echo ""
            echo "Fix locally:"
            echo "  make telemetry-dictionary"
            echo "  git add docs/dashboards/telemetry-dictionary.md"
            echo "  git commit"
            exit 1
          fi

      - name: Compile Grafonnet dashboards
        run: |
          for theme_dir in docs/dashboards/*/; do
            theme=$(basename "$theme_dir")
            if [ -f "$theme_dir/$theme.libsonnet" ]; then
              echo "Compiling $theme..."
              jsonnet -J vendor -o "$theme_dir/$theme.json" "$theme_dir/$theme.libsonnet"
            fi
          done

      - name: Verify dashboards reference only documented primitives
        run: scripts/verify-dashboard-primitives.sh
```

---

## Regenerate Script

`scripts/regenerate-telemetry-dictionary.sh`:

```bash
#!/usr/bin/env bash
# Regenerate docs/dashboards/telemetry-dictionary.md from the current codebase.
# Called by:
#   - CI drift gate (compares output to committed)
#   - Local contributor workflow: `make telemetry-dictionary`

set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# Phase 1 sweep — invoke ring:creating-grafana-dashboards in scripted mode.
# In scripted mode, the skill runs Gates 0-3 only (recon → sweep → assembly → render),
# skipping the interactive PM gates. Output goes to /tmp.
#
# Implementation note: this requires a CLI entry point. Phase 7 of the skill
# documents the bootstrapping. For now, this script delegates to the orchestrator
# via a headless harness:

if ! command -v ring >/dev/null 2>&1; then
  echo "error: 'ring' CLI not found. Install via Lerian dev tools." >&2
  exit 1
fi

ring telemetry-inventory \
  --target "$REPO_ROOT" \
  --output-json /tmp/regen-dictionary.json \
  --output-md /tmp/regen-dictionary.md \
  --schema-version 1.0.0

# In CI: leave /tmp output for the diff step.
# Locally: copy over the committed file so the contributor can `git add`.
if [ "${CI:-}" != "true" ]; then
  cp /tmp/regen-dictionary.md docs/dashboards/telemetry-dictionary.md
  echo "✓ Regenerated docs/dashboards/telemetry-dictionary.md"
  echo "  Run 'git diff docs/dashboards/telemetry-dictionary.md' to review."
fi
```

The `ring telemetry-inventory` CLI is the headless equivalent of Gates 0-3 of this skill.
If the CLI doesn't exist yet, the script can shell out to a fallback Python or Go
implementation; the SCHEMA in `dictionary-schema.md` is the contract either way.

---

## Makefile Target

Add to `Makefile`:

```makefile
.PHONY: telemetry-dictionary
telemetry-dictionary: ## Regenerate telemetry dictionary from code (writes docs/dashboards/telemetry-dictionary.md)
	@scripts/regenerate-telemetry-dictionary.sh

.PHONY: dashboards
dashboards: ## Compile all theme libsonnet to JSON
	@for theme_dir in docs/dashboards/*/; do \
		theme=$$(basename "$$theme_dir"); \
		if [ -f "$$theme_dir/$$theme.libsonnet" ]; then \
			echo "Compiling $$theme..."; \
			jsonnet -J vendor -o "$$theme_dir/$$theme.json" "$$theme_dir/$$theme.libsonnet"; \
		fi; \
	done
```

---

## .gitignore Additions

Compiled dashboard JSON is a build artifact, not source:

```
docs/dashboards/*/*.json
!docs/dashboards/*/dashboard-plan.md
```

Theme `.libsonnet` files and `README.md` files ARE committed; the compiled `.json` is not.

---

## Primitive Verification Script

`scripts/verify-dashboard-primitives.sh` — runs in CI to verify dashboards only reference documented primitives:

```bash
#!/usr/bin/env bash
# Parse PromQL/LogQL from compiled dashboard JSON, verify every metric name
# referenced exists in the telemetry dictionary.

set -euo pipefail

DICTIONARY="docs/dashboards/telemetry-dictionary.md"
EXIT_CODE=0

# Extract metric names from dictionary (### headers under metrics sections)
DOCUMENTED=$(awk '
  /^## (Counters|Histograms|Gauges)$/ { section=1; next }
  /^## / { section=0 }
  section && /^### / { print $2 }
' "$DICTIONARY" | sort -u)

# Walk compiled dashboards
for json in docs/dashboards/*/*.json; do
  theme=$(basename "$(dirname "$json")")

  # Extract metric names from PromQL strings — heuristic: match identifier_with_underscores( or {
  REFERENCED=$(jq -r '..|.expr? // empty' "$json" 2>/dev/null \
    | grep -oE '[a-z][a-z0-9_]*(_total|_seconds|_bytes|_count|_sum|_bucket)?' \
    | sort -u || true)

  for metric in $REFERENCED; do
    # Strip histogram suffixes
    base="${metric%_bucket}"
    base="${base%_count}"
    base="${base%_sum}"

    if ! echo "$DOCUMENTED" | grep -qx "$base"; then
      echo "::error file=$json::Dashboard '$theme' references undocumented metric: $metric (expected base: $base)"
      EXIT_CODE=1
    fi
  done
done

exit $EXIT_CODE
```

---

## Contributor Experience

When CI fails on drift, the failure message tells contributors exactly what to do:

```
::error::Telemetry dictionary drift detected.

Diff between committed and code-regenerated:
+++ /tmp/regen.md
@@ ledger_transactions_total
-  description: Total ledger transactions posted
+  description: Total ledger transactions posted, partitioned by type
   labels:
     - tenant_id
+    - transaction_type
     - result

Fix locally:
  make telemetry-dictionary
  git add docs/dashboards/telemetry-dictionary.md
  git commit
```

The contributor:
1. Pulls the branch
2. Runs `make telemetry-dictionary`
3. Reviews the diff (it should match what they changed in code)
4. Stages the regenerated file alongside their code change
5. Pushes — CI passes

If the regenerated file looks WRONG (e.g., they expected a label change to be additive but it's destructive), the right move is to investigate the code change, not edit the dictionary by hand. The dictionary is a derived artifact.

---

## What This Gate Does NOT Catch

The drift gate verifies **the dictionary matches the code**. It does NOT verify:

- Whether new telemetry has SLO targets defined
- Whether dashboards exist for the new telemetry (that's a Gate 4-6 concern, not CI)
- Whether the new telemetry's labels make semantic sense (PM judgment)
- Whether bucket boundaries are sensible for the workload

These are PM-iteration concerns (Gate 5). Drift CI is mechanical: code says X, dictionary says Y, must match. Semantic quality lives upstream in the skill, not in CI.

---

## Idempotence

When Gate 7 of the skill installs the workflow:

1. If `.github/workflows/telemetry-drift.yml` exists → diff against canonical content. Update only if drifted.
2. If `scripts/regenerate-telemetry-dictionary.sh` exists → leave alone (contributor may have customized).
3. If `Makefile` already has `telemetry-dictionary` target → leave alone.
4. If `.gitignore` already excludes `docs/dashboards/*/*.json` → leave alone.

Gate 7 surfaces a summary of what was created vs left alone. PM can re-run safely.
