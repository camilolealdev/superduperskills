# Reference Mode — Grafana Dashboard Authoring

Load sections relevant to the question. Each section is self-contained.

---

## 1. RED Methodology

For **request-driven services** (HTTP, gRPC, async consumers).

| Letter | Meaning | Primitive | Panel |
|--------|---------|-----------|-------|
| **R** | Rate — requests per second | Counter (`*_total`) | Time-series, `rate(metric[5m])` |
| **E** | Errors — error rate or error percentage | Counter labeled with status | Time-series, `rate(metric{result="error"}[5m]) / rate(metric[5m])` |
| **D** | Duration — request latency distribution | Histogram (`*_duration_seconds`) | Heatmap or quantile time-series, `histogram_quantile(0.99, rate(metric_bucket[5m]))` |

**When to apply:** every endpoint, every consumer, every entry point. RED is the default for HTTP/gRPC dashboards.

**Lerian convention:** the framework instrumentation (Angle 7) usually emits all three for HTTP and gRPC automatically. Manual RED is only needed for application-level operations (e.g., `ledger_post_transaction_total`).

---

## 2. USE Methodology

For **resource-constrained components** (DB pools, queues, worker pools, caches).

| Letter | Meaning | Primitive | Panel |
|--------|---------|-----------|-------|
| **U** | Utilization — fraction of capacity in use | Gauge | Stat panel or time-series |
| **S** | Saturation — extra work queued | Gauge or counter (queue depth, wait time) | Time-series or threshold gauge |
| **E** | Errors — resource-level failures | Counter | Time-series |

**When to apply:** DB connection pools, RabbitMQ consumer prefetch, worker channels, Redis connection counts.

**Distinction from RED:** USE asks "is the resource healthy?" RED asks "is the request flow healthy?" A dashboard for an endpoint uses RED; a dashboard for the database pool feeding that endpoint uses USE.

---

## 3. Panel Pattern Catalog

Mapping primitive type → recommended panel pattern → Grafonnet template.

| Primitive | Pattern | Grafonnet template | Key PromQL/LogQL |
|-----------|---------|--------------------|--------------------|
| Counter (rate) | Time-series rate | `rate-panel.libsonnet` | `sum by (label) (rate(metric_total[$__rate_interval]))` |
| Counter (rate, errors only) | Stat panel — error rate % | `rate-panel.libsonnet` (variant) | `sum(rate(metric_total{result="error"}[5m])) / sum(rate(metric_total[5m]))` |
| Histogram (latency) | Heatmap | `latency-heatmap.libsonnet` | `sum by (le) (rate(metric_bucket[$__rate_interval]))` |
| Histogram (quantiles) | Time-series quantile | `latency-heatmap.libsonnet` (variant) | `histogram_quantile(0.99, sum by (le) (rate(metric_bucket[5m])))` |
| Histogram (SLO budget) | Burn-rate gauge | `error-budget.libsonnet` | Multi-window multi-burn-rate per Google SRE workbook |
| Gauge (utilization) | Threshold gauge | `saturation-gauge.libsonnet` | `metric / metric_capacity` |
| Gauge (current value) | Stat panel | `saturation-gauge.libsonnet` (variant) | `metric` |
| Span (trace search) | Logs/Traces panel with trace link | `trace-search-link.libsonnet` (TODO if needed) | Tempo TraceQL query |
| Log field (log stream) | Logs panel | `log-stream-panel.libsonnet` | LogQL `{service="X"} \| json \| field=~"$field_var"` |

For each panel: PromQL/LogQL is templated; the libsonnet abstracts away the boilerplate (titles, units, thresholds, panel sizing). See `grafonnet-templates/`.

---

## 4. Theme Decision Tree (Gate 4 LLM heuristics)

When proposing themes from the dictionary in Gate 4, apply these heuristics:

```
1. Group counters/histograms by metric name prefix (the substring before the first `_`)
   → Each prefix is a candidate theme. Examples:
     - http_*           → "http_traffic" theme
     - ledger_*         → "ledger" theme
     - amqp_consume_*   → "messaging" theme
     - db_pool_*        → "infrastructure/db" theme

2. For counters with high `result` label cardinality (success/error/timeout/...),
   propose a dedicated "errors_and_slis" theme that aggregates error patterns
   across domains.

3. If `tenant_scoped: true` covers > 50% of metrics, propose a "tenant_health" theme
   that templates dashboards on a tenant_id Grafana variable.

4. If framework_instrumentation includes HTTP server with histograms,
   ALWAYS propose an "sla" theme with RED panels per route.

5. If gauges include resource-pool primitives (db_pool_*, channel_depth_*,
   worker_*), propose "infrastructure" theme with USE panels.

6. If structured logs include error-level fields with high frequency,
   propose a "errors_drilldown" theme combining log panels + trace links.

7. Themes with < 3 dashboards are weak — either merge into a sibling theme or
   propose enriching with cross-cutting panels.
```

The LLM in Gate 4 outputs theme proposals AS SUGGESTIONS. PM in Gate 5 has final say — rename, merge, split, reject freely.

---

## 5. Grafonnet Conventions

### Naming

- Theme directory: `docs/dashboards/{theme}/` — kebab-case theme name
- Main file: `docs/dashboards/{theme}/{theme}.libsonnet`
- Compiled artifact (gitignored): `docs/dashboards/{theme}/{theme}.json`
- README: `docs/dashboards/{theme}/README.md` — required, explains audience and SLIs

### Composition

```jsonnet
local g = import 'g.libsonnet';
local panels = import '../../../pm-team/skills/creating-grafana-dashboards/sub-files/grafonnet-templates/panels.libsonnet';

g.dashboard.new('Theme — Subtitle')
+ g.dashboard.withTags(['lerian', 'theme-name'])
+ g.dashboard.withVariables([
    g.dashboard.variable.query.new('tenant_id')
    + g.dashboard.variable.query.withDatasource('Prometheus', 'label_values(metric_name, tenant_id)')
    + g.dashboard.variable.query.generalOptions.withIncludeAll(),
  ])
+ g.dashboard.withPanels([
    panels.ratePanel('Requests by route', 'http_request_duration_seconds_count', ['route', 'method']) + g.panel.timeSeries.gridPos.withX(0) + g.panel.timeSeries.gridPos.withY(0) + g.panel.timeSeries.gridPos.withW(12) + g.panel.timeSeries.gridPos.withH(8),
    panels.latencyHeatmap('Latency p99', 'http_request_duration_seconds_bucket') + g.panel.timeSeries.gridPos.withX(12) + g.panel.timeSeries.gridPos.withY(0) + g.panel.timeSeries.gridPos.withW(12) + g.panel.timeSeries.gridPos.withH(8),
  ])
```

### Tenant Templating

Every primitive with `tenant_scoped: true` MUST be queried with a `tenant_id` Grafana variable. Templates accept a `tenantFilter` parameter that injects `{tenant_id="$tenant_id"}` (or `{tenant_id=~"$tenant_id"}` for multi-select with all-option). PM in Gate 5 decides whether the variable defaults to `All` or to a specific tenant.

### Variables Convention

| Variable | Source | Default |
|----------|--------|---------|
| `tenant_id` | `label_values(<one tenant-scoped metric>, tenant_id)` | All |
| `interval` | Custom: `1m,5m,10m,30m,1h` | `5m` |
| `__rate_interval` | Built-in (Grafana auto-computes from time range) | — |
| Domain-specific (e.g., `transaction_type`) | `label_values(...)` | All |

---

## 6. Alert Threshold Heuristics

Not every panel deserves an alert. PM in Gate 5 selects which.

| Primitive type | Default alert posture | Suggested threshold |
|---------------|----------------------|---------------------|
| Counter `*_total` | Error-rate alerts only | `error_rate > 1%` over 5m |
| Histogram `*_duration_seconds` | Latency SLO alerts | `p99 > 2× normal` over 10m, or burn-rate alerts |
| Gauge utilization | Saturation alerts | `utilization > 85%` over 5m |
| Counter `*_dlq_*` (dead-letter) | Always alert | `> 0` over 1m |
| Span error_recording=always | Already error-counted; no separate alert | — |

**Burn-rate alerts** (preferred over static thresholds for SLOs):
- Fast burn: 14.4× over 1h (burns 1% of monthly budget in 1h)
- Slow burn: 6× over 6h (burns 5% of monthly budget in 6h)
- Both must fire to alert — reduces noise.

PM decides escalation tiers: PAGE (immediate) vs TICKET (next business day) vs INFO (dashboard-only).

---

## 7. Cross-cutting Patterns

### Tenant Variable Pattern

```jsonnet
// In dashboard, inject tenant variable
+ g.dashboard.withVariables([
    g.dashboard.variable.query.new('tenant_id')
    + g.dashboard.variable.query.withDatasourceFromVariable('datasource')
    + g.dashboard.variable.query.queryTypes.withLabelValues('tenant_id', 'http_server_request_duration_seconds_count')
    + g.dashboard.variable.query.generalOptions.withIncludeAll()
    + g.dashboard.variable.query.selectionOptions.withMulti(),
  ])

// In panel queries, reference $tenant_id
'sum by (route) (rate(http_server_request_duration_seconds_count{tenant_id=~"$tenant_id"}[$__rate_interval]))'
```

### Trace Exemplars on Histograms

Grafana automatically renders exemplars on histogram panels IF:
1. The histogram metric was recorded inside an active span (Angle 6 reports `metric_exemplar_capable_count`)
2. Prometheus is configured with `--enable-feature=exemplar-storage`
3. The panel datasource has Tempo wired as the exemplar destination

Exemplars are clickable — they jump from the spike on the latency heatmap into the actual trace that caused it. **Highest-leverage feature in modern dashboards.** Surface this to PM in Gate 5 if Angle 6 reports exemplar capability.

### Log-to-Trace Links

Logs panels can link to traces via the `derivedFields` datasource config (Loki-side). The link is on `trace_id` field, jumping into Tempo. Configure in Loki datasource, not the dashboard. Reference in README per theme.

---

## 8. Anti-pattern Catalog

Six failure modes to ban from generated dashboards:

1. **Vanity panels** — count of total HTTP requests since deploy. Pretty number, no operational signal. **Reject in Gate 5.**
2. **Static thresholds without context** — `p99 > 1s` alert on a metric that has no SLO. Either define the SLO and use burn-rate, or drop the alert.
3. **Cardinality bombs** — labeling histogram by `request_id` or `transaction_id`. Explodes Prometheus storage. Angle 1/2 flags `unbounded` cardinality; never propose a panel grouping by those.
4. **Auto-counter panels** — proposing a manual counter panel for something the framework already auto-emits. Angle 7 reports redundancies; the dictionary should already deduplicate.
5. **Untemplated tenant queries** — querying tenant-scoped metrics without a `tenant_id` variable. Multi-tenant services need per-tenant slicing or aggregate-with-filter.
6. **Stat-panel overload** — replacing a dashboard with a wall of single-number panels. Stats hide trends. Pair stats with sparklines or time-series.

The Grafonnet panel templates encode resistance to these (e.g., the `rate-panel.libsonnet` always uses `$__rate_interval`, not a hardcoded interval). Gate 6 dispatches reject any panel that violates these.
