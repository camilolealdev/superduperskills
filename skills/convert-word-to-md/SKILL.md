---
name: convert-word-to-md
description: >
  Converts Word (.docx) documents into structured Markdown so their contents can be analyzed, summarized, searched, or extracted.
  Use when processing Word documents, converting docx to markdown, or when user mentions "convert-word-to-md", "word to markdown",
  or "docx to md".
argument-hint: "[docx|word|extract|markdown|convert]"
license: MIT
---

# Convert Word to MD — Word (.docx) Document Extractor

Based on [github/convert-word-to-md](https://skillrepo.dev/skills/github/convert-word-to-md) (v1.0A), this skill converts `.docx` documents into structured Markdown.

## Features

- **Styles to Markdown**: Maps Word Heading 1-6 styles to `#` through `######`.
- **Inline Formatting**: Preserves bold, italic, strikethrough, inline code, and hyperlinks.
- **Embedded Media**: Extracts images from the `.docx` archive and embeds relative file links.
