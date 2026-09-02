---
name: addyosmani
description: >
  Senior engineering habits & full lifecycle suite by Addy Osmani (Google Chrome Lead).
  Enforces a structured lifecycle: /spec → /plan → /build → /test → /review → /ship,
  along with web performance audits (/webperf). Use for production features, Core Web Vitals,
  code reviews, and multi-day feature development. Use when user mentions "addy osmani",
  "addyosmani", "webperf", "senior habits", or full-lifecycle agent workflows.
argument-hint: "[spec|plan|build|test|review|ship|webperf]"
license: MIT
---

# Addy Osmani Agent Skills — Senior Engineering Lifecycle & WebPerf

Based on [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) (89k+ ★) by Addy Osmani (Google Chrome engineering team), this skill enforces senior engineering habits and disciplined execution for production-grade software.

## The Senior Lifecycle Loop

```
/spec  ──>  /plan  ──>  /build  ──>  /test  ──>  /review  ──>  /ship
  │                                                                ▲
  └────────────────────────── /webperf ────────────────────────────┘
```

---

## Slash Commands & Workflows

### 1. `/spec` — Requirements & Scope Boundaries
Establishes user goals, acceptance criteria, and out-of-scope boundaries before touching code.

### 2. `/plan` — Architecture & Component Breakdown
Maps out file changes, data structures, and state management in small, manageable tasks.

### 3. `/build` — Disciplined Feature Construction
Executes planned tasks incrementally without speculative abstractions.

### 4. `/test` — Verification & Coverage Checks
Ensures automated unit, integration, and visual tests pass before declaring completion.

### 5. `/review` — Code Quality & Security Audit
Audits code diffs against WCAG accessibility, security standards, and performance budgets.

### 6. `/ship` — Production Release Readiness
Prepares pull requests, changelogs, and deployment verification checks.

### 7. `/webperf` — Web Performance & Core Web Vitals Audit
Measures LCP (Largest Contentful Paint), INP (Interaction to Next Paint), and CLS (Cumulative Layout Shift) before and after code changes.
