---
name: obra-superpowers-code-review
description: Adversarial code review and quality check covering security, performance, readability, and adherence to requirements.
metadata:
  author: 'Jesse Vincent (obra/superpowers)'
  repository: 'https://github.com/obra/superpowers'
---

# Superpowers — Code Review & Quality Audit

Review pull requests and code changes against engineering standards.

## Audit Checklist

- [ ] Security (no hardcoded secrets, input sanitization, OWASP top 10).
- [ ] Performance (no O(N^2) loops in hot paths, proper async/await).
- [ ] Maintainability (clear naming, stdlib-first, clean diffs).
