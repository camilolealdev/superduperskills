---
name: ai-team-orchestration
description: >
  Bootstrap and run a multi-agent AI development team. Sets up parallel dev/QA agents, sprint management,
  and task assignment protocols for multi-agent software projects. Use when starting projects with agent teams,
  orchestrating parallel subagents, or when user mentions "ai-team-orchestration", "ai team", "agent team",
  or "parallel dev team".
argument-hint: "[bootstrap|roles|sprint|parallel]"
license: MIT
---

# AI Team Orchestration — Multi-Agent Development Team Setup

Based on [github/ai-team-orchestration](https://skillrepo.dev/skills/github/ai-team-orchestration) (v1.0B), this skill structures a team of specialized sub-agents working in parallel.

## Team Architecture

- **Lead Architect Agent**: Defines specs and technical plans (paired with `spec-kit`).
- **Development Sub-Agents**: Implement individual tasks in isolated worktrees (`git-worktree-manager`).
- **QA & Security Sub-Agents**: Run automated tests and code reviews (`harness` & `cybersecurity`).
