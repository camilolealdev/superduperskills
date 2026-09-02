---
name: datadog-cli
description: >
  Datadog CLI for searching production logs, querying APM metrics, tracing requests, and inspecting dashboards.
  Use when debugging production issues, checking Datadog telemetry, or when user mentions "datadog-cli",
  "datadog logs", "datadog trace", or "datadog metrics".
argument-hint: "[logs|metrics|trace|dashboard|search]"
license: MIT
---

# Datadog CLI — Telemetry & Production Observability Toolkit

Based on [softaworks/datadog-cli](https://skillrepo.dev/skills/softaworks/datadog-cli) (v1.1B), this skill interfaces with Datadog CLI tools for production troubleshooting.

## Commands & Queries

- **Log Search**: `datadog-cli logs search --query "status:error service:payment-api" --time-range 1h`
- **APM Traces**: Trace latency bottlenecks across microservices using span IDs.
- **Metric Queries**: Query p99 latency and request volume metrics over time.
