---
name: loopy
description: >
  Autonomous iterative agent loops with explicit verification and stop conditions. Executes a
  "modify -> measure -> evaluate -> keep/revert -> check stop condition" cycle. Ideal for performance tuning,
  flaky test fixes, refactoring, and recurring optimization tasks. Use when user mentions "loopy",
  "agent loop", "iterative optimization", "auto fix loop", or "stop condition".
argument-hint: "[loop|optimize|measure|stop]"
license: MIT
---

# Loopy — Autonomous Iterative Agent Loops with Stop Conditions

Based on [Forward-Future/loopy](https://github.com/Forward-Future/loopy) (3k+ ★), **Loopy** orchestrates self-correcting execution loops for AI agents.

## The Loopy Cycle

```
┌─────────────────────────────────────────────────────────┐
│ 1. Make single targeted change                         │
│ 2. Measure metric (test suite / benchmark / typecheck)  │
│ 3. Evaluate: Did metric improve?                        │
│    ├── YES: Keep change & log progress                  │
│    └── NO: Revert change & try alternate hypothesis     │
│ 4. Check Stop Condition (e.g. 100% tests pass)          │
└─────────────────────────────────────────────────────────┘
```

---

## Installation & Execution

```bash
npx skills add Forward-Future/loopy --skill loopy --agent claude-code -g -y
```

---

## Use Cases

- **Performance Optimization**: Benchmark latency, apply optimization, keep only if faster.
- **Flaky Test Resolution**: Re-run failing tests with minor fixes until 100% pass rate achieved.
- **Dependency Upgrades**: Upgrade packages one by one, verifying build integrity at each step.
