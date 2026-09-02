---
name: ai-ready
description: >
  Makes any repository AI-ready. Analyzes codebase structure and automatically generates AGENTS.md,
  copilot-instructions.md, CI workflows, and issue templates by mining historical PR reviews and commit history.
  Use when onboarding a repository to AI coding workflows, or when user mentions "ai-ready", "ai ready",
  "make repo ai ready", or "setup agent docs".
argument-hint: "[analyze|setup|generate|ci]"
license: MIT
---

# AI-Ready — Automated Repository Onboarding for Agents

Based on [github/ai-ready](https://skillrepo.dev/skills/github/ai-ready) (v1.0B), **AI-Ready** scans a codebase and generates all instruction files required for seamless AI agent operation.

## Generated Artifacts

- **`AGENTS.md` / `CLAUDE.md`**: Project instructions, build scripts, test commands, and non-negotiables.
- **`.github/copilot-instructions.md`**: Inline suggestion guidelines for GitHub Copilot.
- **CI Workflows**: GitHub Actions configuration for automated lint and test verification.
