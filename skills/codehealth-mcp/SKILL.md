---
name: codehealth-mcp
description: >
  Real-time structural Code Health analysis via CodeScene MCP. Reviews code complexity before edits, verifies score deltas
  after changes, and gates commits/PRs against technical debt accumulation. Use when checking code health, measuring technical debt,
  or when user mentions "codehealth-mcp", "codescene", or "code health score".
argument-hint: "[score|complexity|tech-debt|review|codescene]"
license: MIT
---

# Code Health MCP — Structural Code Health & Debt Auditor

Based on [affaan-m/codehealth-mcp](https://skillrepo.dev/skills/affaan-m/codehealth-mcp) (v1.1B), this skill uses CodeScene MCP to measure structural code health.

## Key Metrics

- **Code Health Score (1 - 10)**: Evaluates file size, cyclomatic complexity, deeply nested conditionals, and Brain Methods.
- **Delta Verification**: Re-evaluates health score after edits to prevent score degradation.
- **Hotspot Detection**: Flags high-churn, low-health modules requiring immediate refactoring.
