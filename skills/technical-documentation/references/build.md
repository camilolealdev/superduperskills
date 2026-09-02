# Build Docs Playbook

Read `principles.md` first, then follow this execution flow.

## 1. Detect and align agent instruction and governance instructions

- Use `references/agent-and-contributing.md` as the source of truth for inventory, canonical/alias mapping, and precedence/conflict handling.
- Apply the symlink compatibility policy when in scope (`.agents` canonical directory with `.cursor` compatibility symlink when required by tooling).
- Long-running and extensive build investigations are acceptable when needed to resolve ambiguous or conflicting documentation sources.
- When available, use sub-agents for bounded parallel inventory/cross-check tasks and merge results into one canonical decision set.
- Capture required constraints before writing:
  - nested-agent rules, command/test requirements, PR workflow, and style checks.
- Use the same command and validation expectations in proposed snippets and examples.

## 2. Inventory product documentation surfaces (not governance only)

- For repo-wide builds, include docs content surfaces in addition to AGENTS/CONTRIBUTING.
- Inventory docs files and frameworks in scope (examples): `README*.md`, `docs/**`, `**/*.md`, `**/*.mdx`, `**/*.mdc`, `**/*.rst`, `**/*.rsc`, Fern/Mintlify config, Sphinx `conf.py`.
- Build a coverage map before drafting so governance and product docs are both represented.
- If scope is ambiguous, default to broader docs discovery first, then narrow intentionally.

## 3. Framework config and path mapping rules

- Detect framework/config first (for example Fern config, Sphinx `conf.py`, Mintlify config, or equivalent).
- Resolve every referenced path relative to the file/config that declares it, not assumed repo root.
- Treat filesystem paths and published URL routes as separate mappings; do not infer one from the other without config evidence.
- Validate both layers:
  - config -> file exists on disk
  - config/nav/routing -> URL path is consistent and reachable
- Record path-mapping assumptions and mismatches in handoff (`missing file`, `stale route`, `wrong base path`).

## 4. Define intent and success

- Audience, prerequisites, and job-to-be-done.
- Expected reader outcome immediately after completion.
- Doc type: tutorial, how-to, reference, explanation.
- Success criteria: what must be true after publish.

## 5. Build structure before prose

- Follow the funnel: what/why, quickstart, next steps.
- Keep headings informative and scannable.
- Open each section with the takeaway sentence.
- Add decision points with concrete branch guidance.
- For OpenClaw docs work, choose a page type from `references/openclaw.md` before drafting.
- Keep task-critical OpenClaw configuration inline; link exhaustive defaults, enums, schemas, generated references, and rare debugging workflows.

## 6. Build AGENTS.md and CONTRIBUTING.md intentionally

- Keep AGENTS.md structure consistent with `agents.md` ecosystem patterns:
  - include YAML frontmatter when present in repo style (`name`, `description`).
  - state persona scope and explicit instruction boundaries: `Always`, `Ask first`, `Never`.
  - include concrete commands, testing expectations, PR rules, and validation checks.
