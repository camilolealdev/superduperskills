---
name: clickhouse-io
description: >
  ClickHouse column-oriented database patterns, query optimization, MergeTree engines, materialization, and analytics.
  Use when designing ClickHouse schemas, optimizing OLAP SQL queries, or when user mentions "clickhouse-io",
  "clickhouse sql", "mergetree", or "olap analytics".
argument-hint: "[mergetree|queries|schema|olap|projections]"
license: MIT
---

# ClickHouse IO — Column-Oriented Analytical Database Patterns

Based on [affaan-m/clickhouse-io](https://skillrepo.dev/skills/affaan-m/clickhouse-io) (v1.2A), this skill provides best practices for high-throughput OLAP analytics in ClickHouse.

## Core Rules

1. **Primary Key Ordering**: Choose `ORDER BY (tenant_id, created_at, event_type)` to optimize range filtering and compression ratios.
2. **Table Engines**: Standardize on `ReplacingMergeTree` for deduplication or `SummingMergeTree` for realtime aggregation.
3. **Array & Tuple Vectorization**: Utilize `arrayMap` and `arrayFilter` over subqueries for sub-millisecond query performance.
