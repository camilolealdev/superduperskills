---
name: minions
description: >
  Local Kanban task dashboard for agent task orchestration (runs on localhost:6969).
  Manages In Progress, Review, and Done states with human approval gates. Use when orchestrating
  multi-task agent workflows, visual task management, or when user mentions "minions", "minionsai",
  "kanban board", or "agent task manager".
argument-hint: "[start|board|tasks|approve]"
license: MIT
---

# Minions — Local Kanban Task Manager for Agents

Based on [agent37-platform/minions](https://github.com/agent37-platform/minions) (628 ★), **Minions** provides a visual Kanban dashboard for agent task tracking.

## Features

- **Local Host UI**: Runs locally on `http://localhost:6969`.
- **Three-Column Workflow**: `In Progress` → `Review` → `Done`.
- **Human Approval Gate**: Requires human verification before marking tasks complete.

```bash
# Launch Minions dashboard:
npx minionsai
```
