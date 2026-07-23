// Counter rate panels. Two variants:
//   - ratePanel: time-series of rate(metric_total[interval]) by groupLabels
//   - errorRatePanel: stat panel of error fraction (errors / total) over a window
//
// Lerian convention: counters always end in `_total`. Use $__rate_interval for the
// rate window — Grafana auto-computes from the dashboard time range, avoiding the
// hardcoded-interval anti-pattern flagged in reference.md §8.

local g = import 'github.com/grafana/grafonnet/gen/grafonnet-latest/main.libsonnet';

{
  // ratePanel(title, metric, groupLabels, [tenantFilter])
  //   metric:        counter base name (e.g., 'http_server_request_duration_seconds_count')
  //                  Grafonnet auto-handles _total / _count suffix per primitive type
  //   groupLabels:   array of label names to sum-by (e.g., ['route', 'method'])
  //   tenantFilter:  bool, when true injects {tenant_id=~"$tenant_id"}
  ratePanel(title, metric, groupLabels, tenantFilter=false)::
    local filter = if tenantFilter then '{tenant_id=~"$tenant_id"}' else '';
    local groupBy = std.join(', ', groupLabels);
    g.panel.timeSeries.new(title)
    + g.panel.timeSeries.queryOptions.withTargets([
        g.query.prometheus.new('${datasource}', 'sum by (' + groupBy + ') (rate(' + metric + filter + '[$__rate_interval]))')
        + g.query.prometheus.withLegendFormat('{{ ' + groupLabels[0] + ' }}'),
      ])
    + g.panel.timeSeries.standardOptions.withUnit('reqps')
    + g.panel.timeSeries.options.legend.withDisplayMode('table')
    + g.panel.timeSeries.options.legend.withPlacement('right')
    + g.panel.timeSeries.options.tooltip.withMode('multi'),

  // errorRatePanel(title, totalMetric, errorLabel, [errorValue], [tenantFilter])
  //   Computes error fraction: rate(metric{result=errorValue}) / rate(metric)
  //   Renders as stat panel with red threshold above 1%.
  errorRatePanel(title, totalMetric, errorLabel='result', errorValue='error', tenantFilter=false)::
    local filter = if tenantFilter then ',tenant_id=~"$tenant_id"' else '';
    local errFilter = '{' + errorLabel + '="' + errorValue + '"' + filter + '}';
    local totalFilter = if tenantFilter then '{tenant_id=~"$tenant_id"}' else '';
    g.panel.stat.new(title)
    + g.panel.stat.queryOptions.withTargets([
        g.query.prometheus.new(
          '${datasource}',
          'sum(rate(' + totalMetric + errFilter + '[5m])) / sum(rate(' + totalMetric + totalFilter + '[5m]))',
        ),
      ])
    + g.panel.stat.standardOptions.withUnit('percentunit')
    + g.panel.stat.standardOptions.withDecimals(2)
    + g.panel.stat.standardOptions.thresholds.withMode('absolute')
    + g.panel.stat.standardOptions.thresholds.withSteps([
        { color: 'green', value: null },
        { color: 'yellow', value: 0.005 },
        { color: 'red', value: 0.01 },
      ])
    + g.panel.stat.options.withColorMode('background')
    + g.panel.stat.options.withGraphMode('area'),
}
