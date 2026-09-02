---
name: ai-regression-testing
description: >
  Regression testing strategies for AI-assisted development. Implements sandbox-mode API testing without DB dependencies,
  automated bug-check workflows, and regression prevention patterns. Use when setting up automated regression tests,
  preventing AI-introduced bugs, or when user mentions "ai-regression-testing", "ai regression test", or "bug check workflow".
argument-hint: "[test|sandbox|regression|workflow]"
license: MIT
---

# AI Regression Testing — Automated Safeguards for Agent Code

Based on [affaan-m/ai-regression-testing](https://skillrepo.dev/skills/affaan-m/ai-regression-testing) (v1.2A), this skill provides testing strategies to prevent AI-generated code from introducing silent regressions.

## Key Strategies

- **Sandbox API Mocks**: Tests external API integrations without touching production databases or live credentials.
- **Diff Regression Auditing**: Runs targeted unit tests against modified functions and their immediate callers.
- **Snapshot Testing**: Validates UI component output and API responses before and after refactoring.
