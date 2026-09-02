---
name: autoresearch
description: >
  Autonomous iterative experimentation loop for programming and optimization tasks. Guides users through goal definition,
  measurable metrics, and scope constraints, then runs autonomous experiment iterations. Use when conducting performance tuning,
  algorithm optimization, or when user mentions "autoresearch", "autonomous research loop", or "experiment loop".
argument-hint: "[loop|experiment|metric|optimize]"
license: MIT
---

# AutoResearch — Autonomous Iterative Research & Experimentation Loop

Based on [github/autoresearch](https://skillrepo.dev/skills/github/autoresearch) (v1.0B), **AutoResearch** executes controlled experimentation cycles to optimize target metrics.

## Loop Protocol

```
┌─────────────────────────────────────────────────────────┐
│ 1. Define Hypothesis & Measurable Target Metric        │
├─────────────────────────────────────────────────────────┤
│ 2. Run Baseline Benchmark & Record Initial Score        │
├─────────────────────────────────────────────────────────┤
│ 3. Execute Candidate Mutation / Code Tweak             │
├─────────────────────────────────────────────────────────┤
│ 4. Re-run Evaluation & Compare Delta                    │
├─────────────────────────────────────────────────────────┤
│ 5. Keep (if metric improves) or Revert (if degrades)   │
└─────────────────────────────────────────────────────────┘
```
