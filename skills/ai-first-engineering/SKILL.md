---
name: ai-first-engineering
description: >
  Engineering operating model for development teams where AI agents generate a large share of implementation output.
  Focuses on code review rigor, automated test gates, and human oversight. Use when establishing AI-first dev practices,
  team guidelines, or when user mentions "ai-first-engineering", "ai first engineering", or "agentic dev process".
argument-hint: "[operating-model|review|testing|gates]"
license: MIT
---

# AI-First Engineering — Operating Model for Agent-Driven Teams

Based on [affaan-m/ai-first-engineering](https://skillrepo.dev/skills/affaan-m/ai-first-engineering) (v1.2B), this skill outlines organizational and technical guidelines for teams where AI agents handle primary code generation.

## Operating Principles

- **Human-in-the-Loop Approval**: Human engineers review and approve high-impact pull requests.
- **Automated Verification Gates**: All AI-generated code must pass linting, type checks, and unit tests before merging.
- **Documentation Hygiene**: Agents update `AGENTS.md` and inline docstrings as part of every feature delivery.
