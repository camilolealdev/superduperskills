---
name: agent-skill-generator
description: >
  Analyzes the current codebase and automatically generates a reusable AI agent skill capturing
  project-specific patterns, conventions, and workflows. Use when distilling a project's architecture
  into a permanent agent skill, packaging conventions, or when user mentions "agent-skill-generator",
  "generate skill from codebase", or "skillrepo".
argument-hint: "[analyze|generate|conventions|patterns]"
license: MIT
---

# Agent Skill Generator — Codebase Pattern Distillation

Based on [skillrepo/agent-skill-generator](https://skillrepo.dev/skills/skillrepo/agent-skill-generator) (v1.2A), this skill analyzes a repository's AST, directory layout, naming patterns, and test structures to automatically generate a standardized `SKILL.md` file.

## Generation Workflow

1. **AST & Pattern Mining**: Scans target modules for architectural conventions (e.g. repository pattern, handler signatures, state management).
2. **Convention Extraction**: Captures project-specific non-negotiables (error handling wrappers, logger usages, environment configs).
3. **Spec-Compliant SKILL.md Output**: Generates valid YAML frontmatter, trigger phrases, persistence rules, and execution steps.
