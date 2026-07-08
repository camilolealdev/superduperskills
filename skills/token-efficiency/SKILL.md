---
name: token-efficiency
description: Use always as a background discipline to minimize token usage and API costs — controls verbosity, avoids re-reading files, prevents unnecessary tool calls
---

# Token Efficiency

## Overview

Every token costs money. AI agents waste tokens in predictable ways: re-reading
files they already have in context, producing verbose explanations nobody asked for,
making redundant tool calls, and reading entire files when they only need a few lines.

This skill enforces habits that keep costs low without sacrificing quality.

**This is a background discipline, not something you invoke explicitly.** These
rules should be followed at all times.

## The Rules

### 1. Don't Re-Read What You Already Have

```
BEFORE calling Read, Grep, Glob, or any file-reading tool:
  - Check: Do I already have this file's content in my context?
  - Check: Did I read this file earlier in this conversation?
  - If YES to either: Use what you have. Do NOT re-read.
```

The most common token waste is reading the same file multiple times in one session.

### 2. Read Surgically, Not Wholesale

```
WHEN you need to read a file:
  - If you need specific lines: use offset and limit parameters
  - If you need to find something: use Grep first, then read only the relevant section
  - Do NOT read a 500-line file to find one function
  - Do NOT read an entire directory listing when you know the filename
```

**Bad:** Read the entire 2000-line file to check one import
**Good:** Grep for the import pattern, then read 10 lines around the match

### 3. Be Concise in Responses

```
WHEN responding to the user:
  - Lead with the answer, not the reasoning
  - Skip preamble ("Great question!", "Let me help you with that!")
  - Don't repeat back what the user just said
  - Don't explain what you're about to do — just do it
  - After making changes, summarize briefly — don't echo the full diff
```

**Bad:** "I'll now read the file to understand the structure, then I'll look at
the function you mentioned, and after that I'll make the necessary changes..."
**Good:** *[makes the changes]* "Fixed the null check in `handleAuth` on line 42."

### 4. Batch Tool Calls

```
WHEN you need multiple independent pieces of information:
  - Make all independent tool calls in a single message
  - Do NOT call tools one at a time when they don't depend on each other
```

**Bad:** Read file A. Wait. Read file B. Wait. Read file C.
**Good:** Read files A, B, and C in parallel in one message.

### 5. Don't Over-Explore

```
WHEN investigating a codebase:
  - Start with the most likely file, not a broad search
  - Stop exploring when you have enough context to act
  - You don't need to understand the entire codebase to fix one bug
  - Trust file names and directory structure — don't verify the obvious
```

### 6. Avoid Unnecessary Confirmation Loops

```
WHEN you're confident about a change:
  - Make the change directly instead of asking "should I proceed?"
  - Don't ask permission for low-risk, reversible operations
  - Don't present 3 options when one is clearly correct
```

Asking "Want me to go ahead?" on every small change doubles the conversation
length and token usage.

### 7. Use Small Model Where Appropriate

OpenCode can be configured with a `small_model` for lightweight tasks. The
small model is used automatically for things like generating session titles.
Don't fight this — let cheap tasks use cheap models.

### 8. Keep Context Clean

```
WHEN a conversation gets long:
  - Don't re-summarize previous work unless asked
  - Don't repeat tool outputs in your response text
  - Reference previous results by description, not by copying them
  - Let compaction handle context management — don't manually summarize
```

## Cost Awareness Signals

When token usage seems high, consider:
- Am I reading files I've already read?
- Am I producing paragraphs when a sentence would do?
- Am I exploring broadly when I could go directly to the right file?
- Am I asking the user questions I could answer myself?
- Am I making sequential tool calls that could be parallel?

## What NOT to Sacrifice

Being concise does not mean being sloppy:
- Still write proper error handling
- Still write tests when the TDD skill says to
- Still do security checks when the security skill says to
- Still explain complex decisions when the user would benefit
- Don't skip steps in skills to "save tokens" — that defeats the purpose

The goal is eliminating waste, not cutting corners.
