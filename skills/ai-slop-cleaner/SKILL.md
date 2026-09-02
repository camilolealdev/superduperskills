---
name: ai-slop-cleaner
description: >
  Cleans AI-generated code slop with a regression-safe, deletion-first workflow and optional reviewer-only mode.
  Strips redundant try/catch blocks, unused interfaces, over-commented boilerplate, and dead fallbacks.
  Use when refactoring AI-generated code, removing slop, or when user mentions "ai-slop-cleaner", "clean slop",
  "deletion first", or "code slop".
argument-hint: "[clean|audit|deletion|review]"
license: MIT
---

# AI Slop Cleaner — Deletion-First Refactoring for AI Code

Based on [Yeachan-Heo/ai-slop-cleaner](https://skillrepo.dev/skills/Yeachan-Heo/ai-slop-cleaner) (v1.1A), **AI Slop Cleaner** removes AI-generated code bloat while preserving test integrity.

## Deletion-First Workflow

1. **Slop Audit**: Identifies over-abstracted single-use factories, speculative interface definitions, swallowed exceptions, and redundant inline comments.
2. **Deletion Pass**: Deletes dead fallbacks and speculative wrappers before modifying logic.
3. **Regression Safety Check**: Re-runs test suite after each deletion to guarantee no breaking changes.
