---
name: claimable-postgres
description: >
  Provisions instant temporary PostgreSQL databases via Claimable Postgres by Neon (neon.new) without login or signup.
  Use when running quick SQL tests, provisioning sandbox DBs for CI, or when user mentions "claimable-postgres",
  "instant postgres", "neon.new", or "temporary database".
argument-hint: "[provision|neon|database|connection-string]"
license: MIT
---

# Claimable Postgres — Instant Sandbox Database Provisioning

Based on [neondatabase/claimable-postgres](https://skillrepo.dev/skills/neondatabase/claimable-postgres) (v1.1B), this skill provisions instant temporary Postgres databases via Neon (`neon.new`).

## Instant Workflow

1. **One-Command Provision**: Calls the Neon API to create a live connection string in under 1 second.
2. **Ephemeral Lifecycle**: Active for 24 hours (can be claimed to a permanent Neon account anytime).
3. **PG-Compatible**: Returns standard `postgres://` connection URI ready for Drizzle, Prisma, or psql.
