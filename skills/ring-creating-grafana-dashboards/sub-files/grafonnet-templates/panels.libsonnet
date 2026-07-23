// Index of reusable panel templates for Lerian Grafana dashboards.
// Imported by theme dashboards: `local panels = import 'panels.libsonnet';`
//
// Every template:
//   - Accepts the metric name and label/attribute names from the telemetry dictionary
//   - Templates tenant_id queries via `$tenant_id` Grafana variable when tenantFilter=true
//   - Uses $__rate_interval (Grafana auto-computes from time range) — never hardcode intervals
//   - Returns a panel object that the dashboard composes via gridPos

{
  ratePanel: (import 'rate-panel.libsonnet').ratePanel,
  errorRatePanel: (import 'rate-panel.libsonnet').errorRatePanel,
  latencyHeatmap: (import 'latency-heatmap.libsonnet').latencyHeatmap,
  latencyQuantiles: (import 'latency-heatmap.libsonnet').latencyQuantiles,
  errorBudgetBurn: (import 'error-budget.libsonnet').errorBudgetBurn,
  saturationGauge: (import 'saturation-gauge.libsonnet').saturationGauge,
  currentValueStat: (import 'saturation-gauge.libsonnet').currentValueStat,
  logStream: (import 'log-stream-panel.libsonnet').logStream,
}
