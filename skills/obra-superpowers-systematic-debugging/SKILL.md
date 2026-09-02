---
name: obra-superpowers-systematic-debugging
description: Root-cause driven debugging workflow. Inspects raw logs, forms empirical hypotheses, and verifies fixes with tests.
metadata:
  author: 'Jesse Vincent (obra/superpowers)'
  repository: 'https://github.com/obra/superpowers'
---

# Superpowers — Systematic Debugging

Diagnose and resolve failures strictly based on empirical evidence and log traces.

## 4-Step Debug Protocol

1. **Read Log Output**: Never guess root causes without reading full error stack traces.
2. **Isolate Failures**: Reproduce the bug with the smallest possible test case.
3. **Fix Root Cause**: Fix underlying contracts instead of wrapping errors in silent fallbacks.
4. **Automated Verification**: Run tests to confirm resolution and prevent regressions.
