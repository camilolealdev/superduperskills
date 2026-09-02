---
name: agent-reach
description: >
  Web & social intelligence scraper for AI agents. Enables agents to search and inspect
  content across X/Twitter, Reddit, YouTube, and GitHub without paid API keys. Use when
  conducting market research, competitor sentiment tracking, topic discovery, or when user
  mentions "agent-reach", "agent reach", "social listening", "reddit search", "x search",
  or "community sentiment".
argument-hint: "[twitter|reddit|youtube|github|search]"
license: MIT
---

# Agent-Reach — Social & Community Intelligence

Based on [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) (74k+ ★), this skill provides web and social intelligence tools for AI agents, allowing them to search, scrape, and analyze public discussions across social networks without requiring expensive API subscriptions.

## Capabilities

- **Twitter / X Listening**: Search public tweets, user timelines, and trending hashtags.
- **Reddit Discussion Mining**: Extract top threads, comments, and community discussions from specific subreddits.
- **YouTube Insight Extraction**: Search video titles, descriptions, and community commentary.
- **GitHub Repository & Discussion Search**: Inspect public repos, trending topics, and issue discussions.

---

## Operating Guidelines

1. **Input Parameters**: Provide target topic, keywords, platforms, and date filters.
2. **Analysis Output**: Synthesizes community sentiment, common pain points, feature requests, and competitor perception into clean Markdown summaries.
3. **Respect Rate Limits**: Use caching and respectful request pacing to avoid IP throttles.
