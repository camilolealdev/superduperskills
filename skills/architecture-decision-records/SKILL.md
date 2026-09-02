---
name: architecture-decision-records
description: >
  Captures architectural decisions made during development sessions as structured Architecture Decision Records (ADRs).
  Auto-detects decision moments, records context, options considered, trade-offs, and consequences into doc/adr/.
  Use when documenting architectural choices, writing ADRs, or when user mentions "adr", "architecture decision record",
  or "record architectural decision".
argument-hint: "[record|detect|template|list]"
license: MIT
---

# Architecture Decision Records (ADR) — Decision Tracking System

Based on [affaan-m/architecture-decision-records](https://skillrepo.dev/skills/affaan-m/architecture-decision-records) (v1.2B), this skill automatically records significant architectural choices into `doc/adr/XXXX-title.md`.

## ADR Structure

1. **Title**: `ADR-0001: Use D1 and Drizzle ORM for Edge Storage`
2. **Status**: Proposed / Accepted / Superseded by ADR-0004
3. **Context**: What problem are we solving? What constraints exist?
4. **Options Considered**: List alternatives evaluated with pros/cons.
5. **Decision & Consequences**: Chosen path and trade-offs accepted.
