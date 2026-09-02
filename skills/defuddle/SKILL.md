---
name: defuddle
description: >
  Converts cluttered HTML web pages into clean, readable Markdown. Strips cookie banners,
  ads, nav menus, scripts, and layout bloat (by kepano / Obsidian lead). Use when fetching web content
  for agent context, reading documentation, web research, or when user mentions "defuddle",
  "clean markdown", "parse web page", or "web to markdown".
argument-hint: "[parse|url]"
license: MIT
---

# Defuddle — Clean Web Content to Markdown Converter

Based on [kepano/defuddle](https://github.com/kepano/defuddle) (9k+ ★) by Steph Ango (CEO of Obsidian), **Defuddle** parses web pages and strips layout noise, cookie notices, popups, and sidebar ads, returning pure, semantic Markdown.

## Usage

```bash
npx defuddle parse https://example.com/article --markdown
```

---

## Agent Benefits

- **Token Economy**: Reduces raw HTML (which can be 200KB+) down to 5KB of clean Markdown, saving up to **95% of input tokens**.
- **Context Clarity**: Removes clutter so the model focuses strictly on article prose, code snippets, and documentation tables.
- **Obsidian / Knowledge Base Compatibility**: Output is formatted cleanly for insertion into Markdown vaults and notes.
