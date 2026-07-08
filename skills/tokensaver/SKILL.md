---
name: tokensaver
description: Runtime context optimization - structured summarization, tool output pruning, importance-based retention
license: MIT
compatibility: opencode
---

# TokenSaver

**Optimize context to reduce token costs.**

⚠️ **This skill does NOT automatically reduce tokens.** You must actively apply these strategies.

---

## 🚨 When to Activate This Skill

| Trigger | Action |
|---------|--------|
| Context > 50% of model limit | Start monitoring |
| Context > 70% of model limit | Proactively compress |
| After subtask completion | Summarize and prune |
| Before expensive operations | Clean up context |
| Long-running session | Periodic cleanup |

---

## Core Principle: Tokens-Per-Task

```
❌ Wrong: Minimize tokens per request
✅ Right: Minimize total tokens to complete task

Aggressive compression that loses information → Re-fetching → MORE tokens wasted
```

**Optimize for:** Enough compression to save money, enough preservation to avoid re-work.

---

## Strategy 1: Structured Summarization

Replace old messages with this format:

```markdown
## Session Summary

### User Intent
[1-2 sentences - what user wants to accomplish]

### Files Modified
- `path/file.ts`: [what changed, 1 line]
- `path/other.ts`: [what changed, 1 line]

### Key Decisions
- [Decision 1]: [rationale]
- [Decision 2]: [rationale]

### Current State
[What's working, what's blocked, next steps]

### Must Preserve
- File paths: [...]
- Function names: [...]
- Error messages: [...]
- Critical context: [...]
```

**When to summarize:**
- 20+ tool calls in session
- Repeated file reads
- Task phase completed

---

## Strategy 2: Tool Output Pruning

### Remove Redundant Reads

```
❌ Keep: 5 read results for same file
✅ Keep: Only latest read, prune earlier ones

Rule: If you read file X 3 times, keep only the last read.
```

### Compress After Write

```
❌ Keep: write content + later read content
✅ Prune: write content, keep only read result

Rule: After writing and later reading same file, the write is redundant.
```

### Clean Old Errors

After 4+ turns, prune failed input (keep error message):

```
❌ Keep: 500 lines of failed input + error message
✅ Keep: "[Input pruned - 500 lines] Error: cannot read property 'x'"
```

---

## Strategy 3: Avoid Re-Exploration

**Don't explore the same pattern twice.**

```
❌ Bad flow:
   grep "auth" → results → later grep "auth" again → same results

✅ Good flow:
   grep "auth" → remember: "Auth patterns in src/middleware/auth.ts"
   Later: Use memory, don't re-explore
```

### Memory Checkpoints

After each discovery, mentally checkpoint:

```
✓ Auth: src/middleware/auth.ts
✓ Database: src/models/
✓ Tests: Vitest framework
✓ API: Express routes in src/routes/
```

When context grows, consolidate into one summary.

---

## Strategy 4: Priority-Based Retention

| Priority | Content Type | Action |
|----------|--------------|--------|
| **P1** | File paths, function names, error messages | NEVER prune |
| **P1** | User's core intent | NEVER prune |
| **P2** | Decisions made + rationale | Summarize |
| **P2** | Files modified + changes | Summarize |
| **P3** | Exploration process logs | Compress heavily |
| **P3** | Failed attempts | Keep only lesson |
| **P4** | Duplicate tool outputs | Prune entirely |

---

## Practical Application

### Before Each Major Action, Ask:

- [ ] Context > 70% of limit? → Consider compression
- [ ] Read same file 3+ times? → Prune older reads
- [ ] Task phase done? → Summarize and prune
- [ ] 10+ error outputs? → Clean old ones
- [ ] Verbose output? → Replace with summary

---

## Token Estimation

| Content | Ratio |
|---------|-------|
| English text | ~4 chars/token |
| Code | ~3 chars/token |
| Chinese/Japanese | ~1.5 chars/token |

### Model Limits

| Model | Context Window | Safe Threshold |
|-------|----------------|----------------|
| GPT-4o | 128K | 100K tokens |
| Claude 3.5 | 200K | 150K tokens |
| GPT-4-turbo | 128K | 100K tokens |
| GPT-3.5-turbo | 16K | 12K tokens |

---

## Before/After Example

### Before (50,000 tokens)
```
[20 messages of file exploration]
[15 read tool results, some duplicates]
[8 failed attempts with full error logs]
[5 write operations with full content]
[10 messages of "let me check X, then Y"]
```

### After (8,000 tokens)
```markdown
## Session Summary

### User Intent
Implement JWT authentication for REST API

### Files Modified
- `src/middleware/auth.ts`: Added JWT validation
- `src/routes/auth.ts`: Login/logout endpoints
- `tests/auth.test.ts`: 12 auth tests

### Key Decisions
- httpOnly cookies (XSS protection)
- Token expiry: 15min access, 7 days refresh
- Rate limiting: 100 req/min per IP

### Current State
- 12/15 tests passing
- Remaining: 3 token refresh edge cases

### Must Preserve
- JWT secret: process.env.JWT_SECRET
- Algorithm: HS256
- Error line 47: null check needed
```

---

## Anti-Patterns

| ❌ Don't | Result |
|----------|--------|
| Keep everything | Bloat, high cost, slow |
| Compress aggressively | Lost info, re-fetch, MORE cost |
| Ignore this skill | Reading = wasted tokens |
| Unstructured summary | Critical details lost |

---

## Integration with Plugin

For **automatic** context optimization, combine with:
[opencode-dynamic-context-pruning](https://github.com/Opencode-DCP/opencode-dynamic-context-pruning)

This skill = Manual strategies
Plugin = Automatic pruning

**Best results:** Use both together.

---

## Quick Reference

```
1. SUMMARIZE old context → Structured format
2. PRUNE duplicates and errors
3. PRESERVE P1 content (paths, errors, intent)
4. CHECK before expensive operations
5. APPLY actively - reading ≠ applying

Key Metric: Tokens-per-task, not tokens-per-request
```
