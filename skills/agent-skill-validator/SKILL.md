---
name: agent-skill-validator
description: >
  Validates SKILL.md files against the official agentskills.io specification before publishing. Checks YAML frontmatter,
  name formatting, description clarity, argument hint syntax, and file structure. Use when creating or editing skills,
  running CI skill validation, or when user mentions "agent-skill-validator", "validate skill", or "skill spec check".
argument-hint: "[validate|file|check|spec]"
license: MIT
---

# Agent Skill Validator — Spec Compliance Checker

Based on [skillrepo/agent-skill-validator](https://skillrepo.dev/skills/skillrepo/agent-skill-validator) (v1.1A), this tool audits `SKILL.md` files against the specification.

## Validation Checks

1. **Frontmatter Integrity**: Ensures `name` and `description` are present and formatted correctly.
2. **Naming Constraints**: Checks that skill names are lowercase, kebab-case, and match directory names.
3. **Trigger Quality**: Verifies description contains actionable trigger phrases and scope boundaries.
4. **File Structure**: Confirms supporting directories (`scripts/`, `resources/`, `examples/`) adhere to guidelines.
