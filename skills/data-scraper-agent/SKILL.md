---
name: data-scraper-agent
description: >
  Build automated AI-powered data collection agents for public web sources (job boards, pricing, news, GitHub, sports).
  Runs on a schedule, enriches collected data, handles rate limits, and persists structured output.
  Use when building web scrapers, data collection agents, or when user mentions "data-scraper-agent", "ai web scraper", or "data collection agent".
argument-hint: "[scrape|enrich|schedule|puppeteer|cheerio]"
license: MIT
---

# Data Scraper Agent — Automated AI Web Data Extraction

Based on [affaan-m/data-scraper-agent](https://skillrepo.dev/skills/affaan-m/data-scraper-agent) (v2.0B), this skill builds reliable web scraping pipelines.

## Resilient Scraping Guidelines

- **Polite Crawling**: Respect rate limits and apply backoff retries (`backoff: 2s -> 4s -> 8s`).
- **Resilient Selectors**: Prefer semantic attributes (`data-testid`, ARIA roles) over brittle nested CSS class selectors.
- **LLM Extraction**: Use structured JSON schema output for un-structured HTML text blocks.
