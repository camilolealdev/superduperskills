---
name: cannibalization
version: 1.0.0
description: "Detect keyword cannibalization across your site using GSC data and SERP analysis. Scores severity, recommends resolution (consolidate, differentiate, canonicalize, or noindex), and outputs an action plan."
---

# Cannibalization Check

Find pages on your site that compete against each other for the same keywords. Keyword cannibalization splits ranking authority, confuses Google about which page to surface, and suppresses both pages in SERPs.

## When to Use

- Rankings plateau or drop despite good content
- GSC shows the same query driving impressions to multiple URLs
- After publishing new content that overlaps with existing pages
- During a content audit or site migration
- When a page flip-flops between positions (ranking volatility)

## Inputs

Ask the user for:

1. **Domain**: The site to analyze
2. **GSC data export** (preferred): CSV or API access with query, page, clicks, impressions, position columns
3. **Specific keywords to check** (optional): Focus analysis on a known set of terms
4. **Sitemap URL** (optional): For cross-referencing indexed pages

If no GSC data is available, fall back to site-search and SERP-based detection methods.

## What Cannibalization Is

Two or more pages on the same domain target the same keyword and compete for the same SERP position. Google picks one to rank, sometimes switches between them, and often ranks neither as high as a single authoritative page would.

Cannibalization is NOT:
- Two pages ranking for different intents of the same keyword (one informational, one transactional)
- A category page and a product page both appearing for a branded query (this is site-link behavior)
- Intentional multi-ranking where both pages hold top-3 positions (rare but valid)

## Detection Methods

### Method 1: GSC Query Overlap (Primary)

This is the most reliable method. Requires GSC data with query + page dimensions.

1. Export GSC performance data: queries with page-level breakdowns (last 3 months)
2. Group by query
3. Flag any query where 2+ URLs received impressions
4. For each flagged query, pull clicks, impressions, CTR, and average position per URL

```
Filter criteria:
- Query has 2+ URLs with impressions > 10
- At least one URL has position between 5-30 (ranking but not dominating)
- Both URLs received clicks (not a one-off impression blip)
```

### Method 2: Site Search

For each target keyword:

```
site:domain.com "target keyword"
```

If Google returns multiple pages from the domain, those pages are candidates for cannibalization. Check whether they target different intents or genuinely overlap.

### Method 3: SERP Position Check

Search for the target keyword without `site:` and check if multiple pages from the domain appear in the top 100. If Google is surfacing two of your pages, it has not decided which one is authoritative.

### Method 4: Internal Content Overlap

Compare the following across all pages:
- Title tags containing the same keyword
- H1 headings targeting the same topic
- URL slugs with overlapping terms
- Content body covering the same subtopics

Use **meta-optimizer** output to identify title-level overlaps quickly.

## Severity Scoring

Score each cannibalization instance:

### High Severity
- Both pages rank positions 5-15 for the query
- Neither breaks into the top 5
- Combined clicks suggest a single page would rank higher
- Both pages have similar content depth and intent
- **Impact**: Consolidating could push a single page into top 5

### Medium Severity
- One page clearly dominates (top 5) but the other pulls some impressions/clicks
- The weaker page drains crawl budget and link equity
- **Impact**: Resolving frees authority for the dominant page and eliminates confusion

### Low Severity
- One page ranks strongly (top 3), the other barely appears (position 30+, minimal impressions)
- Or the two pages target legitimately different intents
- **Impact**: Minor. Monitor but low priority to fix.

## Resolution Strategies

### 1. Consolidate (Merge + Redirect)

**When**: Both pages cover the same topic with similar intent and neither dominates.

Steps:
1. Pick the stronger URL (more backlinks, better engagement, cleaner URL)
2. Merge the best content from both pages into the winner
3. 301 redirect the weaker URL to the stronger one
4. Update all internal links pointing to the old URL
5. Resubmit the updated page in GSC

**Best for**: Blog posts that evolved into overlapping topics, duplicate landing pages, old vs new versions of the same guide.

### 2. Differentiate (Re-target Keywords)

**When**: Both pages have value but target overlapping keywords. Each could own a distinct angle.

Steps:
1. Assign a unique primary keyword to each page using your keyword map
2. Rewrite titles, H1s, and first paragraphs to target distinct keywords
3. Adjust internal linking so each page is the clear authority for its keyword
4. Differentiate content depth: one page goes broad (pillar), the other goes deep (specific subtopic)

**Best for**: A pillar page and a related blog post, category vs product pages, guide vs tutorial on similar topics.

### 3. Canonicalize

**When**: You need both pages to exist (different audiences, different funnels) but want Google to consolidate ranking signals to one.

Steps:
1. Add `<link rel="canonical" href="https://domain.com/preferred-page">` to the secondary page
2. Keep both pages accessible to users
3. The canonical page receives consolidated ranking signals

**Best for**: Print vs web versions, parameterized URLs, syndicated content, localized landing pages with identical content.

### 4. Noindex

**When**: The weaker page serves no SEO purpose and does not need organic traffic.

Steps:
1. Add `<meta name="robots" content="noindex, follow">` to the weaker page
2. The page stays accessible via direct links but exits the index
3. Link equity still flows through the page's outbound links

**Best for**: Internal tool pages, outdated content you want to keep live but not rank, thin pages that exist for UX reasons only.

### 5. Internal Linking Reinforcement

**When**: One page should dominate but lacks internal link authority.

Steps:
1. Add 5-10 internal links from relevant pages pointing to the preferred URL
2. Use keyword-rich anchor text matching the target keyword
3. Reduce or remove internal links to the competing page
4. Cross-reference with **internal-links** skill for full link graph analysis

**Best for**: New pages competing with established ones, cases where content is already differentiated but signals are split.

## Decision Framework

```
Do both pages serve the same search intent?
├── YES
│   ├── Is one page clearly stronger (more links, better content)?
│   │   ├── YES → Consolidate (merge weaker into stronger, 301 redirect)
│   │   └── NO → Consolidate (pick the better URL, merge both)
│   └── Do both pages need to exist for non-SEO reasons?
│       ├── YES → Canonicalize the weaker to the stronger
│       └── NO → Consolidate
└── NO (different intents)
    ├── Are titles/keywords overlapping despite different intent?
    │   ├── YES → Differentiate (re-target keywords, rewrite titles)
    │   └── NO → Low severity, monitor only
    └── Does the weaker page need organic traffic?
        ├── YES → Differentiate
        └── NO → Noindex
```

## Output Format

### Cannibalization Report Table

```
| Keyword | URL 1 | Clicks (U1) | Impr (U1) | Pos (U1) | URL 2 | Clicks (U2) | Impr (U2) | Pos (U2) | Severity | Action |
|---------|-------|-------------|-----------|----------|-------|-------------|-----------|----------|----------|--------|
| claude code seo | /blog/guide | 45 | 1200 | 8.3 | /blog/tutorial | 28 | 980 | 11.7 | High | Consolidate → /blog/guide |
| seo audit tool | /tools | 120 | 3400 | 4.1 | /blog/audit | 15 | 890 | 18.2 | Medium | Differentiate keywords |
| meta tags seo | /blog/meta | 210 | 5600 | 3.2 | /blog/title-tags | 3 | 120 | 34.5 | Low | Monitor |
```

### Per-Issue Detail Block

For each High or Medium severity case, provide:

```
Keyword:     "claude code seo"
Competing:   /blog/guide (pos 8.3, 45 clicks) vs /blog/tutorial (pos 11.7, 28 clicks)
Severity:    HIGH
Why:         Both pages rank 5-15. Neither breaks top 5. Combined 73 clicks suggest
             a merged page could reach top 5 and capture 150+ clicks.
Action:      Consolidate. Merge /blog/tutorial content into /blog/guide. 301 redirect.
Steps:
  1. Audit both pages for unique content worth preserving
  2. Add missing sections from /blog/tutorial into /blog/guide
  3. Update internal links pointing to /blog/tutorial
  4. Set up 301 redirect: /blog/tutorial → /blog/guide
  5. Resubmit /blog/guide in GSC
  6. Monitor position changes over 4-6 weeks
```

## Prevention: Keyword Mapping

Cannibalization stems from publishing without a keyword map. Prevent it:

1. Maintain a keyword map: one spreadsheet with every page, its primary keyword, and secondary keywords
2. Before publishing new content, check the map for existing pages targeting the same keyword
3. If overlap exists, either update the existing page or target a different keyword for the new one
4. Review the keyword map quarterly against GSC data to catch drift

Use **keyword-cluster** to build the initial keyword map by grouping related terms and assigning each cluster to a single page.

## Cross-References

- **keyword-cluster**: Build keyword maps that prevent cannibalization from the start
- **meta-optimizer**: Fix title-level overlaps that signal cannibalization to Google
- **internal-links**: Redistribute internal link authority toward preferred pages
- **content-brief**: When differentiating pages, generate new briefs with distinct keyword targets
- **seo-audit**: Catch cannibalization signals during full-site technical audits
- **ai-visibility**: Check if AI engines are confused about which page to cite for a topic

## Example Session

```
User: Here's my GSC export (CSV). Find cannibalization issues.