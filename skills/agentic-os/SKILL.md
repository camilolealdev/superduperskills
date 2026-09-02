---
name: agentic-os
description: >
  Build persistent multi-agent operating systems on Claude Code / Antigravity. Covers kernel architecture,
  specialist sub-agents, slash commands, file-based memory, and scheduled background tasks.
  Use when architecting agent fleets, multi-agent systems, or when user mentions "agentic-os", "agentic os",
  "multi agent operating system", or "agent kernel".
argument-hint: "[kernel|subagents|commands|memory|scheduler]"
license: MIT
---

# Agentic OS — Persistent Multi-Agent Operating System Architecture

Based on [affaan-m/agentic-os](https://skillrepo.dev/skills/affaan-m/agentic-os) (v1.1B), **Agentic OS** defines architectural patterns for multi-agent environments.

## Operating Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    AGENTIC OS KERNEL                         │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│ Specialist  │ Specialist  │ Specialist  │ Memory Layer      │
│ Agent: Dev  │ Agent: QA   │ Agent: Sec  │ (File-based JSON) │
├─────────────┴─────────────┴─────────────┴───────────────────┤
│ Scheduler (Cron / Timers)  │ Slash Command Dispatcher       │
└────────────────────────────┴────────────────────────────────┘
```

- **Kernel Router**: Dispatches incoming requests to specialist sub-agents.
- **Shared Memory Layer**: File-based persistence in `.agents/memory/`.
- **Scheduled Automations**: Recurring tasks powered by background timers.
