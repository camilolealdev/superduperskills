---
name: ai-visibility
version: 1.0.0
description: "Check if your brand and content appear in AI-generated answers across Google AI Overviews, ChatGPT, Perplexity, Claude, Copilot, and Gemini. Audit citation-readiness, crawl access, and content extractability. Get prioritized fixes."
---

# AI Visibility & Citation Audit

## When to Use

Run this skill when you need to:
- Check whether your brand or content gets cited in AI search responses
- Audit your site's readiness for AI crawlers and citation extraction
- Compare your AI visibility against competitors
- Build a GEO (Generative Engine Optimization) action plan
- Track citation presence across ChatGPT, Perplexity, Google AI Overviews, Claude, Copilot, and Gemini

Cross-references: Use `seo-audit` for traditional technical SEO issues. Use `schema-gen` to add structured data that improves AI extractability. Use `content-brief` to plan citation-ready content from scratch.

## Prerequisites

**Required:**
- Target brand name and domain
- 10-20 target queries your content should appear for (mix of branded and non-branded)
- List of 3-5 competitor domains

**Optional but useful:**
- Google Search Console export (queries + pages with clicks)
- Current robots.txt file
- Content inventory (URL + primary keyword per page)

## How AI Search Engines Select Sources

Each AI search platform uses a different search backend and ranking logic. Understanding this determines where to focus.

| Platform | Search Backend | Index Source | Citation Style |
|---|---|---|---|
| Google AI Overviews | Google Search | Google index | Inline links to source pages |
| ChatGPT (Browse) | Bing + internal | Bing index (primarily) | Footnote citations with URLs |
| Perplexity | Multi-source (Google, Bing, Brave, own crawler) | Blended index | Numbered inline citations |
| Claude (web search) | Brave Search | Brave index | Inline source references |
| Microsoft Copilot | Bing Search | Bing index | Numbered citations with snippets |
| Gemini | Google Search | Google index | Inline links, similar to AI Overviews |

**Key takeaway:** Optimizing for Google index covers AI Overviews + Gemini. Optimizing for Bing index covers ChatGPT + Copilot. Perplexity and Claude use independent indices. You need visibility across all three index families.

See `references/platform-ranking-factors.md` for detailed per-platform optimization tactics.

## Step-by-Step Audit

### 1. AI Bot Access Check

AI crawlers must be able to access your content. Check robots.txt for these user agents:

| Bot | User-Agent String | Platform | Default if Missing |
|---|---|---|---|
| GPTBot | `GPTBot` | ChatGPT training + Browse | Allowed |
| ChatGPT-User | `ChatGPT-User` | ChatGPT Browse (live) | Allowed |
| PerplexityBot | `PerplexityBot` | Perplexity | Allowed |
| ClaudeBot | `ClaudeBot` | Claude web search | Allowed |
| Google-Extended | `Google-Extended` | Gemini training | Allowed |
| Googlebot | `Googlebot` | AI Overviews (uses main index) | Allowed |
| Bingbot | `bingbot` | Copilot + ChatGPT | Allowed |

**Audit steps:**
1. Fetch `https://yourdomain.com/robots.txt`
2. Parse each user-agent block
3. Flag any `Disallow` rules that block AI bots
4. Check for blanket `User-agent: *` disallow rules that would affect all bots
5. Verify `X-Robots-Tag` HTTP headers for noindex directives on key pages

**Output format:**
```
robots.txt AI Bot Access:
  GPTBot: ALLOWED
  ChatGPT-User: ALLOWED
  PerplexityBot: BLOCKED (Disallow: /) [FIX: Remove block]
  ClaudeBot: ALLOWED
  Google-Extended: BLOCKED (Disallow: /) [WARNING: Blocks Gemini training]
  Googlebot: ALLOWED
  Bingbot: ALLOWED

  Issues: 2 bots blocked. You are invisible to Perplexity answers.
```

**Recommendation framework:**
- Block training bots (`GPTBot`, `Google-Extended`) only if you have a specific IP reason
- Never block live search bots (`ChatGPT-User`, `PerplexityBot`, `Googlebot`, `Bingbot`) as this removes you from AI search results entirely
- `ClaudeBot` serves both training and search; blocking it removes you from Claude's web search citations

### 2. Citation Presence Check

For each target query, check whether your domain appears in AI-generated responses.

**Process per platform:**
1. Run each target query through the AI platform
2. Record: Was your domain cited? Which URL? What context? What position (1st citation, 2nd, etc.)?
3. Record: Which competitor domains were cited instead?

**Output format:**
```
Query: "how to do a technical seo audit"

  Google AI Overview:
    Your domain: NOT CITED
    Cited sources: semrush.com (#1), ahrefs.com (#2), moz.com (#3)

  ChatGPT:
    Your domain: CITED - /blog/technical-seo-checklist/ (citation #4 of 6)
    Context: "For a step-by-step checklist, see [source]"

  Perplexity:
    Your domain: NOT CITED
    Cited sources: searchengineland.com (#1), semrush.com (#2), backlinko.com (#3)

  Claude:
    Your domain: NOT CITED
    Cited sources: web.dev (#1), ahrefs.com (#2)

  Copilot:
    Your domain: NOT CITED
    Cited sources: moz.com (#1), semrush.com (#2)

  Gemini:
    Your domain: NOT CITED
    Cited sources: google.com/search-central (#1), semrush.com (#2)
```

**Summary table across all queries:**
| Query | AI Overviews | ChatGPT | Perplexity | Claude | Copilot | Gemini | Score |
|---|---|---|---|---|---|---|---|
| technical seo audit | No | #4 | No | No | No | No | 1/6 |
| keyword clustering | No | No | No | No | No | No | 0/6 |
| internal linking strategy | No | No | #2 | No | No | No | 1/6 |

**AI Visibility Score:** (total citations / total possible) as percentage. Example: 2/18 = 11% visibility.

### 3. Content Extractability Audit

AI engines extract content that is structured, self-contained, and directly answers a question. Audit each priority page for these patterns.

**Citation-ready content checklist per page:**

| Signal | What to Check | Scoring |
|---|---|---|
| Definition blocks | Does the page contain a 50-70 word paragraph that directly defines/answers the topic? | +10 if yes |
| Self-contained paragraphs | Can any paragraph be extracted and still make sense without surrounding context? | +10 per qualifying paragraph |
| Comparison tables | Are comparisons in table format (not paragraph form)? | +10 per table |
| Numbered steps | Are processes written as numbered lists with action verbs? | +10 if yes |
| Statistics with sources | Are stats cited inline with source and date? | +5 per cited stat |
| FAQ section | Does the page have an FAQ with concise answers? | +10 if yes |
| Entity definitions | Are key terms defined on first use? ("Claude Code is Anthropic's CLI tool for...") | +5 per definition |
| Heading-answer pairs | Does each H2 contain a direct answer in its first paragraph? | +10 per H2 that qualifies |

**Extractability score per page:** Sum of signals, max 100. Pages scoring under 40 need structural rework.

**Princeton GEO research findings** (use these benchmarks):
- Adding citations to content increases AI citation likelihood by **40%**
- Including statistics improves citation rates by **37%**
- Adding expert quotes improves citation rates by **30%**
- Fluent, well-structured writing outperforms keyword-stuffed content

Source: Princeton "GEO: Generative Engine Optimization" research paper.

**Output format:**
```
Page: /blog/technical-seo-checklist/
Extractability Score: 62/100

  Present:
    - Definition block in intro (score: +10)
    - 3 comparison tables (score: +30)
    - FAQ section with 5 questions (score: +10)
    - 4 heading-answer pairs (score: +40... capped contribution)

  Missing:
    - No cited statistics (add 3-5 industry stats with sources)
    - No numbered step lists (convert "how to" sections)
    - Entity definitions missing for 3 key terms

  Priority fixes:
    1. Add 3+ statistics with inline citations (+37% citation likelihood)
    2. Define "crawl budget", "render queue", "canonicalization" on first use
    3. Convert paragraph-form comparisons in section 4 to table format
```

### 4. Citation-Readiness Score

Combine bot access, content extractability, and authority signals into a single score per page.

**Scoring model:**

| Factor | Weight | Scoring Criteria |
|---|---|---|
| Bot access | 20% | All AI bots allowed = 100. Each blocked bot = -15 |
| Extractability | 30% | Score from Section 3 audit |
| Authority signals | 25% | Referring domains, Domain Rating/Authority, brand mentions |
| Content freshness | 15% | Updated within 90 days = 100, 180 days = 70, 365 days = 40, older = 10 |
| Schema markup | 10% | Article + FAQ + BreadcrumbList schema present = 100. Missing elements = proportional reduction |

**Output:** Sorted table of all audited pages with composite citation-readiness score (0-100).

Cross-reference: Use `schema-gen` to fix missing structured data. Use `meta-optimizer` to align page titles with target queries.

### 5. Competitor Citation Analysis

For each query where your domain is not cited, analyze what the cited competitors do differently.

**Per competitor citation, record:**
- URL that was cited
- Content format (list, table, paragraph, FAQ)
- Word count of the cited section
- Whether the cited content contains: stats, quotes, definitions, tables
- Domain authority / referring domains
- Content freshness (last updated date)

**Pattern analysis:**
```
Across 20 queries, competitor citations share these patterns:
  - 85% of cited pages contain comparison tables
  - 90% of cited pages have content updated within 90 days
  - 70% of cited pages include inline statistics with sources
  - Average word count of cited pages: 2,400 words
  - 60% of cited pages have FAQ schema

Your pages vs. cited competitor pages:
  - Your avg extractability score: 38
  - Competitor avg extractability score: 72
  - Gap: Tables (-80%), statistics (-65%), freshness (-40%)
```

### 6. Recommended Fixes: Three Pillars

Organize all recommendations into three pillars. Each fix includes effort estimate and expected impact.

#### Pillar 1: Structure (Make Content Extractable)

AI engines need content they can cleanly extract and quote.

| Fix | Effort | Impact | Pages Affected |
|---|---|---|---|
| Add 50-70 word definition block under each H2 | Medium | High | All content pages |
| Convert paragraph comparisons to tables | Low | High | 8 pages identified |
| Add FAQ section with 4-6 questions | Medium | High | 12 pages missing FAQ |
| Add numbered steps to how-to content | Low | Medium | 6 pages identified |
| Define key entities on first mention | Low | Medium | All content pages |

#### Pillar 2: Authority (Make Content Citable)

AI engines prefer content with demonstrated expertise and sourced claims.

| Fix | Effort | Impact | Pages Affected |
|---|---|---|---|
| Add inline statistics with source citations | Medium | High (+37% citation rate) | 15 pages with zero stats |
| Add expert quotes or original data | High | High (+30% citation rate) | Feature pages |
| Add Article + FAQ schema markup | Low | Medium | Pages missing schema |
| Build referring domains to priority pages | High | High | Pages with DR < 20 |
| Update content within 90-day freshness window | Medium | Medium | 9 stale pages |

#### Pillar 3: Presence (Make Content Visible to AI)

AI engines can only cite what they can find and crawl.

| Fix | Effort | Impact | Pages Affected |
|---|---|---|---|
| Unblock AI bots in robots.txt | Low | Critical | Entire site (if blocked) |
| Remove noindex from content pages | Low | Critical | Pages with noindex |
| Submit updated pages to Google/Bing for re-crawling | Low | Medium | Recently updated pages |
| Ensure Bing Webmaster Tools is configured | Low | Medium | Entire site |
| Add site to Brave Search submission | Low | Medium | Entire site |
| Internal link to priority pages | Medium | Medium | Orphan pages (use `internal-links` skill) |

## Tracking Over Time

Set up a monthly cadence:

1. Re-run citation presence checks on the same 10-20 queries
2. Track AI Visibility Score month-over-month
3. Record which new pages gained citations and which lost them
4. Compare against competitor citation changes
5. Correlate citation gains with specific fixes applied

**Monthly dashboard format:**
```
AI Visibility Report - March 2026
  Overall Score: 22% (up from 11% last month)
  Citations gained: 4 (ChatGPT: 2, Perplexity: 1, AI Overview: 1)
  Citations lost: 1 (Copilot: competitor content fresher)
  Top gaining page: /blog/technical-seo-checklist/ (now cited in 3/6 platforms)
  Fix impact: Table additions correlated with 3 of 4 new citations
```

## Automation Notes

- Schedule citation checks weekly for top 10 queries, monthly for full query set
- Alert when a competitor gains a citation on a query you target
- Re-audit extractability after any content update
- Cross-reference with `seo-audit` for technical blockers and `internal-links` for link equity to priority pages
