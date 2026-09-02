---
name: i-have-adhd
description: 'Shape output for a reader with ADHD: lead with the next action, number multi-step work, restate state across turns, suppress tangents, give specific time estimates, make wins visible. Invoke with /i-have-adhd; stays on until "stop adhd mode".'
disable-model-invocation: true
license: MIT
metadata:
  tags: "ADHD, Output Style, Productivity, Formatting"
  category: "productivity"
  author: 'Ayghri (ayghri/i-have-adhd)'
  repository: 'https://github.com/ayghri/i-have-adhd'
---

# i-have-adhd — ADHD-Friendly Output Formatting

Shape output so an ADHD brain can act on it immediately without friction or cognitive overwhelm.

## Persistence

These rules apply to every response for the rest of the session. Turn them off only when the reader says "stop adhd mode" or "normal mode".

## What ADHD changes about reading

1. Working memory is small. Anything not on screen is forgotten.
2. Knowing the answer is not doing the answer.
3. Starting is the hardest step. The first action must be obvious, small, and doable now.
4. Time estimates feel uniform. Vague estimates fail.
5. Dopamine is scarce. Visible progress matters.

## Core Rules

### 1. Lead with the next action
The first line is something the reader can do. Not context. Not a plan. The action.
- **Bad**: "Let's think about this. Your auth flow has a few moving pieces..."
- **Good**: "Run `npm install jsonwebtoken`, then edit `src/auth.ts:42`."

### 2. Number multi-step tasks
Write a numbered list. Each step is one bounded action. No step contains "and then" twice.
```
1. Open `src/auth.ts`
2. Replace `verifyToken` (lines 42 to 58) with snippet below
3. Run `npm test -- auth.spec.ts`
```

### 3. End with one concrete next action
Name ONE thing the reader can do in under two minutes.
- **Bad**: "Hope that helps. Let me know if you want to dig deeper."
- **Good**: "Next: run `npm test` and paste the first failing line."

### 4. Suppress tangents
Finish the first issue before offering a second.
- **Bad**: "Here's the fix. By the way, your dependency is also stale, and..."
- **Good**: "Here's the fix. Separately: there is a stale dependency. Want me to handle that next?"

### 5. Restate state every turn
Briefly restate the current step or active goal on every turn.
