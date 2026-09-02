---
name: obra-superpowers-writing-plans
description: Generates implementation plans designed for systematic subagent execution, stressing TDD, YAGNI, and DRY.
metadata:
  author: 'Jesse Vincent (obra/superpowers)'
  repository: 'https://github.com/obra/superpowers'
---

# Superpowers — Writing Implementation Plans

Produce detailed, step-by-step engineering plans that break complex tasks into atomic, verifiable implementation steps.

## Plan Rules

1. **Atomic Tasks**: Each step must specify single file edits or unit test additions.
2. **TDD Driven**: Every feature task must be preceded by a failing test task.
3. **YAGNI & Simplicity**: Eliminate unnecessary abstractions or unused helper methods.
