---
name: autofix
description: >
  Safely reviews and applies CodeRabbit PR review-thread feedback from GitHub with per-change approval.
  Use when applying PR comments, fixing reviewer feedback, or when user mentions "autofix", "coderabbit autofix",
  or "apply pr feedback".
argument-hint: "[review|pr|apply|thread]"
license: MIT
---

# AutoFix — CodeRabbit PR Review Feedback Application

Based on [coderabbitai/autofix](https://skillrepo.dev/skills/coderabbitai/autofix) (v1.0B), **AutoFix** parses PR review comments and safely applies target code fixes.

## Workflow

1. **Review Thread Extraction**: Fetches inline PR comments via GitHub CLI (`gh api`).
2. **Impact Assessment**: Inspects target file and line range to verify issue still exists.
3. **Targeted Fix & Verification**: Applies change and runs test suite before committing.
