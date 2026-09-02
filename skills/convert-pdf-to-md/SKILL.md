---
name: convert-pdf-to-md
description: >
  Converts PDF (.pdf) documents into structured Markdown so their contents can be analyzed, summarized, searched, or extracted.
  Use when processing PDF files, converting PDF to text/markdown, or when user mentions "convert-pdf-to-md", "pdf to markdown",
  or "read pdf".
argument-hint: "[pdf|extract|markdown|convert]"
license: MIT
---

# Convert PDF to MD — Structured PDF Markdown Extraction

Based on [github/convert-pdf-to-md](https://skillrepo.dev/skills/github/convert-pdf-to-md) (v1.0B), this skill extracts PDF document contents into clean Markdown.

## Conversion Strategy

- **Hierarchy Retention**: Translates PDF font weights and sizes into `#`, `##`, `###` headings.
- **Table Preservation**: Extracts PDF table structures into GitHub Flavored Markdown tables.
- **Code & List Format**: Normalizes bullet points and indented code blocks.
