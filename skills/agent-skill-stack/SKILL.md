---
name: agent-skill-stack
description: >
  Finds, evaluates, and assembles the smallest compatible set of AI Agent Skills for an end-to-end natural language goal.
  Use when user wants to discover, bundle, or combine skills for complex multi-step tasks, or when user mentions
  "agent-skill-stack", "skill stack", "assemble skills", or "skill combination".
argument-hint: "[evaluate|assemble|bundle|goal]"
license: MIT
---

# Agent Skill Stack — Minimal Skill Set Assembler

Based on [github/agent-skill-stack](https://skillrepo.dev/skills/github/agent-skill-stack) (v1.0A), this skill analyzes a user's multi-step objective and selects the smallest, non-overlapping subset of skills needed to fulfill it.

## Assembly Principles

- **Minimal Context Overhead**: Avoids loading duplicate or conflicting skills.
- **Dependency Resolution**: Ensures prerequisite skills (e.g. `spec-kit` before `harness`) are ordered logically.
- **Conflict Avoidance**: Detects overlapping rules and picks the highest-rated skill for the domain.
