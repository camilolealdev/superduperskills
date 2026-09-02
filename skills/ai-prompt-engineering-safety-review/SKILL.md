---
name: ai-prompt-engineering-safety-review
description: >
  Comprehensive AI prompt engineering safety review. Analyzes system prompts, skill instructions, and agent rules
  for safety, bias, security vulnerabilities (prompt injection, jailbreaks), and performance optimization.
  Use when auditing system prompts, hardening agent rules, or when user mentions "prompt safety review",
  "ai-prompt-engineering-safety-review", "prompt injection audit", or "prompt security".
argument-hint: "[audit|safety|injection|review]"
license: MIT
---

# AI Prompt Engineering Safety Review — Prompt Hardening & Audit

Based on [github/ai-prompt-engineering-safety-review](https://skillrepo.dev/skills/github/ai-prompt-engineering-safety-review) (v1.0B), this skill audits AI prompts and agent instructions for safety and resilience.

## Audit Targets

1. **Prompt Injection Resilience**: Checks if untrusted user inputs can override system directives.
2. **Boundary Enforcement**: Verifies that out-of-scope tasks are explicitly rejected.
3. **Data Leak Prevention**: Ensures prompts do not leak system instructions or private keys.
