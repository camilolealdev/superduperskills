---
name: agents-md
description: >
  Creates and maintains concise AGENTS.md and CLAUDE.md project instruction files.
  Use when initializing agent rules in a repo, updating AGENTS.md, setting up project instructions,
  or when user mentions "agents-md", "agents.md", "create agents.md", or "claude.md".
argument-hint: "[init|update|audit|rules]"
license: MIT
---

# AGENTS.md — Project Instruction Generator & Maintainer

Based on [getsentry/agents-md](https://skillrepo.dev/skills/getsentry/agents-md) (v1.0A), this skill creates and maintains clear, concise `AGENTS.md` and `CLAUDE.md` files for repositories.

## Best Practices for AGENTS.md

1. **Be Concise**: Keep instructions under 150 lines to save prompt token budgets.
2. **Focus on Non-Negotiables**: Define build commands, test runners, code style rules, and directory structures.
3. **Reference Core Suite**: Mandate consulting `caveman`, `ponytail`, `spec-kit`, `token-savings`, `harness`, `mem`, `rtk`, and `graphify`.
