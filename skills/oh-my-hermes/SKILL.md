---
name: oh-my-hermes
description: >
  Multi-agent orchestration workflow (Research → Interview → Plan → Execution → Verification).
  Coordinates specialized sub-agents across complex phases. Use when running multi-agent tasks,
  swarm execution, or when user mentions "oh-my-hermes", "oh my hermes", "hermes orchestration",
  or "multi agent workflow".
argument-hint: "[research|interview|plan|execute|verify]"
license: MIT
---

# Oh-My-Hermes — Multi-Agent Phase Orchestration

Based on [witt3rd/oh-my-hermes](https://github.com/witt3rd/oh-my-hermes) (280 ★), **Oh-My-Hermes** structures agentic execution into distinct, specialized sub-agent phases.

## Execution Phases

1. **Research Agent**: Scans repo, external docs, and environment.
2. **Interview Agent**: Asks targeted questions to lock down design choices.
3. **Plan Agent**: Drafts step-by-step task breakdown.
4. **Execution Agent**: Implements code edits using `ponytail` minimal diffs.
5. **Verification Agent**: Runs test suite and validates against plan.
