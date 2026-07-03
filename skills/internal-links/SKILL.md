---
name: internal-links
version: 1.0.0
description: "Analyze internal linking structure, find orphan pages, audit anchor text, map hub-spoke topology, and generate prioritized link insertion recommendations with suggested anchor text and context sentences."
---

# Internal Links Analysis & Optimization

## When to Use

Run this skill when you need to:
- Audit the internal linking structure of a site
- Find orphan pages that receive zero internal links
- Identify hub pages with weak spoke connections
- Fix anchor text issues (over-optimized, generic, missing)
- Reduce click depth for high-priority pages
- Generate a prioritized list of link insertions with exact placement suggestions

Cross-references: Use `seo-audit` for broader technical issues. Use `cannibalization` to check if internal links compete for the same keywords. Use `keyword-cluster` to define topical clusters before running link analysis.

## Prerequisites

You need one of the following as input:
1. **A crawl export** (Screaming Frog, Sitebulb, or similar) with columns: source URL, target URL, anchor text, status code, link type (navigation/content/footer)
2. **A sitemap URL** (the skill will crawl internal links from the sitemap)
3. **A list of URLs** to analyze (minimum 20 pages for meaningful analysis)

Optional but useful:
- Google Search Console export (to weight pages by organic clicks)
- Keyword-to-URL mapping (from `keyword-cluster` skill output)
- Content taxonomy or category structure

## Step-by-Step Analysis

### 1. Build the Link Graph

Crawl or parse the provided data to build a directed graph where:
- Each node is a unique URL (normalized: lowercase, trailing slash consistent, no query params unless defined as separate pages)
- Each edge is an internal link with properties: anchor text, link position (nav/content/footer/sidebar), follow/nofollow status

Exclude from analysis:
- External links
- Links to non-HTML resources (PDFs, images, CSS, JS)
- Self-referencing links (page linking to itself)
- Pagination links (unless they form the primary navigation path)

### 2. Orphan Page Detection

An orphan page receives zero internal links from any other indexed page.

**Detection method:**
```
For each URL in sitemap or URL list:
  Count inbound internal links (in-degree = 0)
  Flag as orphan if:
    - Zero content links point to it
    - OR only navigation/footer links point to it (weak orphan)
```

**Output format:**
| Orphan URL | Page Type | Organic Clicks (30d) | In Sitemap | Action |
|---|---|---|---|---|
| /blog/old-post/ | Blog | 12 | Yes | Add links from 3 related posts |
| /features/hidden/ | Landing | 0 | No | Add to nav OR merge with parent |

**Priority:** Pages with organic traffic but zero internal links are the highest priority. They rank despite poor internal support and will respond well to link additions.

### 3. Link Equity Distribution Analysis

Calculate link equity flow using a simplified PageRank-style model:

**Metrics per page:**
- **In-degree**: Number of unique pages linking to this URL
- **Out-degree**: Number of unique internal links on this page
- **Link depth**: Minimum clicks from homepage
- **Link equity score**: Relative score (0-100) based on in-degree weighted by linking page authority

**Identify problems:**
- **Equity sinks**: Pages with high in-degree but zero or near-zero out-degree (absorb equity, distribute nothing). Common culprits: contact pages, thank-you pages.
- **Equity deserts**: Important pages (by traffic or revenue) with low in-degree relative to their value.
- **Over-linked pages**: Pages receiving 50+ internal links while similar pages receive under 5. Usually indicates navigation bloat.

**Output format:**
| URL | In-degree | Out-degree | Link Depth | Equity Score | Issue |
|---|---|---|---|---|---|
| /pricing/ | 47 | 2 | 1 | 89 | Equity sink (low out-degree) |
| /blog/high-value/ | 1 | 8 | 4 | 12 | Equity desert (under-linked) |

### 4. Anchor Text Analysis

Classify every internal link's anchor text:

| Category | Definition | Example | Issue Level |
|---|---|---|---|
| Exact match | Anchor = target page's primary keyword | "keyword research tools" | Warning if >30% of links to that URL |
| Partial match | Contains keyword variant | "best keyword tools for SEO" | Healthy |
| Branded | Contains site/brand name | "ccforseo guide" | Neutral |
| Generic | Non-descriptive | "click here", "read more", "learn more", "this" | Bad for SEO |
| Naked URL | Raw URL as anchor | "https://example.com/page" | Bad for SEO |
| Image (no alt) | Image link without alt text | `<a><img></a>` | Bad for SEO and accessibility |
| Descriptive | Unique, contextual, keyword-adjacent | "internal linking audit checklist" | Ideal |

**Per-URL anchor text report:**
```
Target: /blog/keyword-research-guide/
  Anchors:
    "keyword research" (exact) - 12 links (48%) [WARNING: over-optimized]
    "click here" (generic) - 5 links (20%) [FIX]
    "keyword research for beginners" (partial) - 4 links (16%) [OK]
    "our guide to finding keywords" (descriptive) - 4 links (16%) [IDEAL]

  Recommendation: Replace 3+ exact-match anchors with descriptive variants.
  Replace all generic anchors with contextual descriptions.
```

### 5. Hub-Spoke Model Validation

A hub page is a pillar/category page that should link to and receive links from all its spoke pages (individual articles or sub-pages in that topic).

**How to identify hubs:**
- Pages at depth 1-2 with broad topic coverage (e.g., /technical-seo/, /content-marketing/)
- Category or tag index pages
- Pages the user defines as pillar content

**Validation checks:**
1. Does the hub link to all its spokes? List missing outbound links.
2. Do all spokes link back to the hub? List spokes missing hub backlinks.
3. Do spokes interlink with each other? Count spoke-to-spoke links. Goal: each spoke links to 2-3 sibling spokes minimum.

**Output format:**
```
Hub: /technical-seo/ (12 spokes identified)

  Missing hub -> spoke links:
    - /blog/core-web-vitals-guide/ (no link from hub)
    - /blog/xml-sitemap-best-practices/ (no link from hub)

  Missing spoke -> hub links:
    - /blog/robots-txt-guide/ (doesn't link back to /technical-seo/)
    - /blog/structured-data-faq/ (doesn't link back to /technical-seo/)

  Spoke-to-spoke linking:
    - Average: 1.3 sibling links per spoke (target: 2-3)
    - Worst: /blog/hreflang-tags/ links to 0 siblings
```

### 6. Topical Cluster Linking

If keyword cluster data is available (from `keyword-cluster` skill), validate that pages in the same cluster interlink.

**Process:**
1. Map each URL to its assigned keyword cluster
2. For each cluster, build a sub-graph of internal links
3. Identify disconnected pages within the same cluster
4. Suggest links between topically related but unlinked pages

**Output:** Same format as hub-spoke, grouped by cluster.

### 7. Link Depth Analysis

Calculate minimum click depth from homepage for every indexed URL.

**Thresholds:**
| Depth | Status | Action |
|---|---|---|
| 0 | Homepage | N/A |
| 1 | Ideal for top-level pages | None needed |
| 2 | Good for important content | None needed |
| 3 | Acceptable for most pages | Monitor |
| 4+ | Too deep for important pages | Reduce depth |
| Unreachable | Critical | Add links immediately |

**Flag pages where:**
- Depth 4+ AND organic clicks > 50/month (important but buried)
- Depth 4+ AND page is a target landing page
- Any page unreachable from homepage through internal links alone

### 8. Broken Internal Link Detection

Find all internal links returning non-200 status codes:

| Source URL | Broken Link URL | Anchor Text | Status Code | Fix |
|---|---|---|---|---|
| /blog/seo-guide/ | /tools/old-tool/ | "our SEO tool" | 404 | Update to /tools/new-tool/ or remove |
| /about/ | /team/john/ | "John Smith" | 301 -> /team/john-smith/ | Update to final URL |

**Priority order:**
1. 404/410 links (broken, losing equity)
2. 301/302 redirects (working but leaking equity through redirect chains)
3. 5xx errors (server issues)

Cross-reference: Use `seo-audit` for a complete broken link audit including external links.

### 9. Contextual Link Suggestions

The highest-value output. For each suggested link, provide:

**Output format (prioritized list):**
```
Priority: HIGH
Source: /blog/technical-seo-checklist/
Target: /blog/core-web-vitals-guide/
Suggested anchor: "Core Web Vitals optimization"
Context sentence: "After fixing crawl errors, the next step is [Core Web Vitals optimization] to ensure your pages meet Google's performance thresholds."
Reason: Same topic cluster, source has 340 monthly clicks, target is currently an orphan page with 89 monthly clicks.

Priority: MEDIUM
Source: /blog/keyword-research-guide/
Target: /tools/keyword-clustering/
Suggested anchor: "keyword clustering tool"
Context sentence: "Once you have your raw keyword list, run it through a [keyword clustering tool] to group terms by search intent."
Reason: Natural semantic connection, target page has low in-degree (2), source is high-authority (in-degree 23).
```

**Prioritization factors (weighted):**
1. Target page value: organic traffic, conversion rate, business priority (weight: 3x)
2. Source page authority: in-degree, traffic, equity score (weight: 2x)
3. Topical relevance: same cluster, semantic similarity (weight: 2x)
4. Current link gap: target has low in-degree relative to importance (weight: 1.5x)
5. Natural fit: a contextual sentence exists without forcing the link (weight: 1x)

### 10. Silo Structure Analysis

Evaluate whether the site follows a clean silo (topical directory) structure:

**Check for:**
- **Cross-silo leaks**: Pages in /technical-seo/ linking heavily to /content-marketing/ but not to sibling pages (weakens topical authority signals)
- **Silo integrity score**: Percentage of internal links that stay within the same silo vs. cross-silo
- **Missing silo pages**: Topics covered in one silo that lack corresponding coverage in related silos

**Output:**
```
Silo: /technical-seo/ (8 pages)
  Internal silo links: 24 (75%)
  Cross-silo links: 8 (25%)
  Top cross-silo targets: /content-marketing/ (5 links), /tools/ (3 links)
  Silo integrity: GOOD (>60% internal)

Silo: /blog/ (45 pages)
  Internal silo links: 12 (15%)
  Cross-silo links: 68 (85%)
  Silo integrity: WEAK (blog posts link outward but rarely to each other)
  Fix: Add "related posts" section to each blog post with 2-3 sibling links
```

## Final Output Structure

Deliver results in this order:

1. **Executive Summary**: Total pages analyzed, orphan count, average link depth, broken link count, overall internal linking health score (0-100)
2. **Critical Issues**: Orphan pages, broken links, unreachable pages (fix first)
3. **High-Priority Recommendations**: Top 10 link insertions by impact
4. **Full Analysis Tables**: All sections above with complete data
5. **Link Insertion Spreadsheet**: Every suggested link with source, target, anchor, context sentence, priority score

## Automation Notes

For recurring audits:
- Re-run monthly or after any major content publish
- Compare link graph snapshots over time to track improvements
- Track in-degree changes for priority pages
- Alert on new orphan pages (published content that was never linked to)

Cross-reference with `meta-optimizer` for anchor text that aligns with optimized title tags. Use `content-brief` output to pre-plan internal links before writing new content.
