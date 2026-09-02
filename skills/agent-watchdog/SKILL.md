---
name: agent-watchdog
description: >
  Audits, reviews, compares, or fixes another agent's work from a Codex session ID, Claude Code session transcript,
  or chat link. Use when babysitting background agents, reviewing subagent outputs, debugging failed agent sessions,
  or when user mentions "agent-watchdog", "babysit agent", "audit agent session", or "watchdog".
argument-hint: "[audit|review|compare|fix|session]"
license: MIT
---

# Agent Watchdog — Agent Execution Oversight & Quality Guard

Based on [BuilderIO/agent-watchdog](https://skillrepo.dev/skills/BuilderIO/agent-watchdog) (v1.0B), **Agent Watchdog** inspects transcript logs, diffs, and execution steps of background subagents to detect errors, loops, or incomplete tasks.

## Key Capabilities

1. **Transcript Audit**: Reads JSONL transcripts (`transcript.jsonl`) to trace decisions and identify where an agent went off track.
2. **Diff Verification**: Compares proposed file modifications against project rules (`AGENTS.md` / `ponytail`).
3. **Session Recovery**: Generates correction prompts to resume or fix stuck background tasks.
