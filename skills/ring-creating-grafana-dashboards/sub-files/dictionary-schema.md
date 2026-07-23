# Telemetry Dictionary Schema

The contract between sweep output (Gate 1), validation (Gate 2), rendering (Gate 3),
authoring (Gate 6), and drift CI (Gate 7). Every consumer assumes this exact shape.

**Schema version:** `1.0.0`. Breaking changes require coordinated update of all consumers.

---

## Two Forms

The dictionary lives in **two forms**:

| Form | Path | Audience | Purpose |
|------|------|----------|---------|
| Markdown (canonical) | `docs/dashboards/telemetry-dictionary.md` | Humans + CI diff | Reviewable, committed, drift-checked |
| JSON (intermediate) | `/tmp/dashboards-dictionary.json` | Skill internals + dev tooling | Phase 2 → Phase 3 → Phase 6 handoff |

The Markdown is **rendered FROM** the JSON deterministically. Drift CI regenerates JSON from code, re-renders Markdown, byte-compares against committed Markdown. Both must match.

---

## Determinism Rules (THESE ARE WHY DRIFT CI WORKS)

The Markdown rendering MUST be byte-identical for the same input. To guarantee this:

1. **Sort keys alphabetically** in every YAML block (no insertion order).
2. **Sort lists alphabetically** for non-semantic-order fields: labels, attributes, log_levels.
3. **Preserve order** ONLY for semantic-order fields: histogram boundaries, parent_span_pattern chain.
4. **Numeric formatting**: integers are bare; floats use minimal representation (`1.0` not `1.00`); boundaries are `[0.005, 0.01, ...]` with one space after comma, no trailing zeros.
5. **String escaping**: use double quotes for YAML strings only when needed (special chars). Otherwise bare. Be consistent.
6. **Trailing whitespace**: NONE. Every line ends with `\n` only.
7. **Section separator**: exactly `\n---\n\n` between sections, exactly `\n\n` between primitives within a section.
8. **Headers**: `### {primitive_name}` exactly, no surrounding whitespace.
9. **Frontmatter timestamp**: `_meta.generated_at` is the ONLY non-deterministic field; drift CI ignores it (compares everything else).

The renderer in Gate 3 follows these rules verbatim. If you find drift CI failing on cosmetic differences, the renderer is broken — fix the renderer, not the schema.

---

## Markdown Form

```markdown
---
_meta:
  schema_version: "1.0.0"
  service_name: <string>
  source_commit_sha: <string>
  lib_commons_version: <string>
  generated_at: <ISO-8601 UTC>  # ignored by drift CI
  primitive_counts:
    counters: <int>
    histograms: <int>
    gauges: <int>
    spans: <int>
    log_fields: <int>
---

# Telemetry Dictionary — <service_name>

> Auto-generated from code via `ring:creating-grafana-dashboards`. Do NOT edit by hand.
> To regenerate: `make telemetry-dictionary` (or `scripts/regenerate-telemetry-dictionary.sh`).

## Counters

### <metric_name>

```yaml
description: <string>
emission_sites:
  - file: <relative path>
    function: <symbol>
    line: <int>
instrument_type: Int64Counter | Float64Counter
label_cardinality_estimate: low | medium | high | unbounded
labels:
  - <label_name>
  - ...
tenant_scoped: true | false
unit: <string>
```

(blank line, then next metric)

---

## Histograms

### <metric_name>

```yaml
boundaries:
  - <float>
  - ...
boundaries_source: explicit | default
description: <string>
emission_sites:
  - file: <relative path>
    function: <symbol>
    line: <int>
instrument_type: Float64Histogram | Int64Histogram
label_cardinality_estimate: low | medium | high | unbounded
labels:
  - <label_name>
tenant_scoped: true | false
unit: <string>
```

---

## Gauges

### <metric_name>

```yaml
callback_source: <expression>  # observable gauges only; omit for synchronous
description: <string>
emission_sites:
  - file: <relative path>
    function: <symbol>
    line: <int>
instrument_type: Int64UpDownCounter | Float64UpDownCounter | Int64ObservableGauge | Float64ObservableGauge
label_cardinality_estimate: low | medium | high | unbounded
labels:
  - <label_name>
synchronous: true | false
tenant_scoped: true | false
unit: <string>
```

---

## Spans

### <span_name>

```yaml
attribute_cardinality_estimate: low | medium | high | unbounded
attributes:
  - <attribute_name>
description: <string>
emission_sites:
  - file: <relative path>
    function: <symbol>
    line: <int>
error_recording: always | on_failure | none
parent_span_pattern: http.handler | grpc.handler | amqp.consumer | root | internal
span_kind: Internal | Server | Client | Producer | Consumer
tenant_scoped: true | false
```

---

## Log Fields

### <field_name>

```yaml
emission_sites:
  - file: <relative path>
    level: debug | info | warn | error | fatal
    line: <int>
level_distribution:
  debug: <int>
  error: <int>
  fatal: <int>
  info: <int>
  warn: <int>
pii_risk: true | false
trace_correlated: true | false
type_observed: string | int | float | bool | object
```

---

## Cross-cutting

### Tenant Propagation

```yaml
inconsistencies:
  - issue: <string>
    site: <file:line>
metric_labels_with_tenant:
  - <metric_name>
source_call: <function name>
span_attributes_with_tenant:
  - <span_name>
log_fields_with_tenant_correlation_pct: <float>
```

### Trace Correlation

```yaml
broken_propagation_sites: []
log_to_trace_coverage_pct: <float>
metric_exemplar_capable_count: <int>
```

### Error Attribution

```yaml
complete_attribution_sites:
  - file: <relative path>
    line: <int>
    primitive_set:
      - log
      - metric
      - span
no_attribution_sites:
  - file: <relative path>
    line: <int>
partial_attribution_sites:
  - file: <relative path>
    line: <int>
    missing:
      - <primitive>
```

---

## Framework Instrumentation

```yaml
database_instrumented:
  auto_spans:
    - <span_name>
  mongodb: command-monitor | none
  postgres: pgx-otel | otelsql | none
grpc_server_instrumented:
  auto_metrics:
    - <metric_name>
  auto_spans:
    - <span_name>
  instrumented: true | false
  interceptor_site: <file:line>
http_server_instrumented:
  auto_metrics:
    - <metric_name>
  auto_spans:
    - <span_name>
  framework: fiber | echo | gin | net/http | none
  manual_overrides: []
  middleware_site: <file:line>
outgoing_http_instrumented:
  instrumented: true | false
  wrapper_site: <file:line>
rabbitmq_consumer_instrumented:
  auto_spans:
    - <span_name>
  instrumented: true | false
  wrapper_site: <file:line>
```
```

---

## JSON Form (Internal)

`/tmp/dashboards-dictionary.json` is a flat aggregate of the seven angle outputs:

```json
{
  "_meta": { "schema_version": "1.0.0", "service_name": "...", "source_commit_sha": "...", "lib_commons_version": "...", "generated_at": "..." },
  "counters": [ { ...counter primitive } ],
  "histograms": [ ... ],
  "gauges": [ ... ],
  "spans": [ ... ],
  "log_fields": [ ... ],
  "cross_cutting": { ...angle 6 output },
  "framework_instrumentation": { ...angle 7 output }
}
```

Within each list, primitives are sorted by `name` lexicographically before rendering.

---

## Validation Rules (Gate 2)

The orchestrator enforces these in Gate 2; failures re-dispatch the responsible angle:

| Rule | Applies to | Failure mode |
|------|-----------|--------------|
| `name` matches `^[a-z][a-z0-9_]*$` | counters, histograms, gauges, log_fields | Re-dispatch with naming correction |
| `name` matches `^[a-z][a-z0-9_.-]*$` | spans | Re-dispatch with naming correction |
| `description` length ≥ 30 chars | all primitives | Re-dispatch requesting description quality |
| `unit` non-empty for histograms | histograms | Re-dispatch with unit inference |
| `boundaries` non-empty when `boundaries_source: explicit` | histograms | Re-dispatch with boundary capture |
| No duplicate `(name, kind)` pair | all | Merge or reject duplicates |
| `tenant_scoped: true` ⇒ `tenant_id` in labels/attributes | counters, histograms, gauges, spans | Re-dispatch with consistency check |
| `error_recording != none` ⇒ `result` or status label present (recommended) | counters, histograms | Warning, not blocking |
| Cross-cutting inconsistencies count tracked | angle 6 | Surface to PM in Gate 5 |

---

## Drift CI Comparison Algorithm

The drift gate (Gate 7 setup) executes:

```bash
# 1. Regenerate from current code
ring telemetry-inventory --output /tmp/regen-dictionary.json

# 2. Render Markdown deterministically
ring telemetry-render /tmp/regen-dictionary.json > /tmp/regen-dictionary.md

# 3. Strip the generated_at timestamp from both sides (only non-deterministic field)
sed -E 's/generated_at:.*/generated_at: <REDACTED>/' docs/dashboards/telemetry-dictionary.md > /tmp/committed-canonicalized.md
sed -E 's/generated_at:.*/generated_at: <REDACTED>/' /tmp/regen-dictionary.md > /tmp/regen-canonicalized.md

# 4. Byte-compare
diff -u /tmp/committed-canonicalized.md /tmp/regen-canonicalized.md

# Exit 0 → no drift → CI passes
# Exit 1 → drift → CI fails, contributor regenerates locally
```

This is the entire drift detection. No semantic comparison, no field-by-field walking — just byte diff after timestamp redaction. Determinism in rendering is what makes this safe.

---

## Schema Evolution

If a sweep angle adds a new field to a primitive type:

1. Bump `_meta.schema_version` (semver: minor for additive, major for breaking).
2. Update this file's primitive YAML block to include the new field with sort position.
3. Update the renderer in Gate 3 to emit the new field.
4. Update the validation rules in Gate 2.
5. The next CI run will fail on every existing service until they regenerate. **This is correct.** The dictionary is a contract; contract changes require regeneration.

The reason the schema is versioned: a service pinned to lib-commons v5.3 may sweep with schema 1.0.0 while a service on v5.5 sweeps with 1.1.0. Drift CI checks `_meta.schema_version` matches the renderer it's using; mismatch → fail with "regenerate dictionary against current skill version".
