---
name: baoyu-url-to-markdown
description: >
  Fetches any public URL and converts content to clean markdown using site-specific adapters (X/Twitter, YouTube transcripts,
  HackerNews, GitHub). Use when scraping web content, converting articles to markdown, or when user mentions
  "baoyu-url-to-markdown", "url to markdown", or "fetch page markdown".
argument-hint: "[url|fetch|adapters|markdown]"
license: MIT
---

# Baoyu URL-to-Markdown — Web Content Extractor & Markdown Converter

Based on [jimliu/baoyu-url-to-markdown](https://skillrepo.dev/skills/jimliu/baoyu-url-to-markdown) (v1.0B), this skill converts live web pages into clean Markdown files.

## Features

- **Site Adapters**: Native extractors for X/Twitter tweets, YouTube transcripts, and GitHub READMEs.
- **Noise Stripping**: Strips sidebars, ad popups, navigation headers, and tracking parameters.
- **YAML Frontmatter**: Includes page title, publication date, author, and source URL metadata.
