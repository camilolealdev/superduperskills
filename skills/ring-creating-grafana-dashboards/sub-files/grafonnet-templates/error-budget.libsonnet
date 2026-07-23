// SLO error-budget burn-rate panel.
// Multi-window multi-burn-rate per Google SRE workbook (Ch 5: Alerting on SLOs).
//
// Inputs:
//   - SLI: success/total ratio computed from a counter
//   - SLO target: e.g., 99.9% over 30d
//
// The panel renders the current burn rate over fast (1h) and slow (6h) windows,
// stacked. Alert candidate: fast > 14.4 AND slow > 6 simultaneously → page.

local g = import 'github.com/grafana/grafonnet/gen/grafonnet-latest/main.libsonnet';

{
  // errorBudgetBurn(title, totalMetric, errorLabel, errorValue, sloTarget, [tenantFilter])
  //   sloTarget: float in (0, 1), e.g., 0.999 for 99.9%
  errorBudgetBurn(title, totalMetric, errorLabel='result', errorValue='error', sloTarget=0.999, tenantFilter=false)::
    local errorBudget = 1 - sloTarget;
    local tenantClause = if tenantFilter then ',tenant_id=~"$tenant_id"' else '';
    local errFilter = '{' + errorLabel + '="' + errorValue + '"' + tenantClause + '}';
    local totalFilter = if tenantFilter then '{tenant_id=~"$tenant_id"}' else '';
    local burnRate(window) = '(' +
      'sum(rate(' + totalMetric + errFilter + '[' + window + '])) / ' +
      'sum(rate(' + totalMetric + totalFilter + '[' + window + ']))' +
      ') / ' + std.toString(errorBudget);
    g.panel.timeSeries.new(title)
    + g.panel.timeSeries.queryOptions.withTargets([
        g.query.prometheus.new('${datasource}', burnRate('1h'))
        + g.query.prometheus.withLegendFormat('1h burn rate'),
        g.query.prometheus.new('${datasource}', burnRate('6h'))
        + g.query.prometheus.withLegendFormat('6h burn rate'),
      ])
    + g.panel.timeSeries.standardOptions.withUnit('none')
    + g.panel.timeSeries.standardOptions.withDecimals(2)
    + g.panel.timeSeries.standardOptions.thresholds.withMode('absolute')
    + g.panel.timeSeries.standardOptions.thresholds.withSteps([
        { color: 'green', value: null },
        { color: 'yellow', value: 1 },
        { color: 'orange', value: 6 },
        { color: 'red', value: 14.4 },
      ])
    + g.panel.timeSeries.fieldConfig.defaults.custom.withDrawStyle('line')
    + g.panel.timeSeries.fieldConfig.defaults.custom.withLineWidth(2)
    + g.panel.timeSeries.fieldConfig.defaults.custom.thresholdsStyle.withMode('line')
    + g.panel.timeSeries.options.legend.withDisplayMode('table')
    + g.panel.timeSeries.options.legend.withCalcs(['mean', 'max', 'last']),
}
