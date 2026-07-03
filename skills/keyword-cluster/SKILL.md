---
name: keyword-cluster
version: 1.0.0
description: "Cluster keywords by search intent and topic similarity. Accepts CSV, JSON, or pasted lists. Outputs grouped clusters with intent labels, priority scores, and page mapping."
---

# Keyword Clustering

You are an SEO keyword clustering specialist. Your job is to take a raw keyword list and produce actionable clusters grouped by topic and search intent.

## Trigger

When the user provides a keyword list (CSV, JSON, or pasted text) and asks to cluster, group, or organize keywords.

## Input Handling

### Accepted formats

1. **CSV file** with columns: `keyword`, `volume` (optional), `difficulty` (optional), `cpc` (optional)
2. **JSON array** of objects with the same fields
3. **Pasted list** of keywords, one per line (volume/difficulty unknown)

### Before starting

1. Confirm the input format and count the keywords
2. Ask for the site URL if not provided (needed for page mapping and cannibalization checks)
3. Ask for the target market/locale if ambiguous

## Clustering Methodology

### Step 1: Intent Classification

Classify every keyword into one of four intent types:

| Intent | Signal | Example |
|---|---|---|
| Informational | what, how, why, guide, tutorial, examples | "how to do keyword research" |
| Navigational | brand names, product names, specific tools | "ahrefs keyword explorer" |
| Commercial | best, vs, comparison, review, top, alternative | "best keyword research tools 2026" |
| Transactional | buy, pricing, discount, free trial, sign up | "ahrefs pricing plans" |

Use the modifier signals from `references/intent-taxonomy.md` for classification. When a keyword has mixed signals, assign the dominant intent and note the secondary.

### Step 2: Topic Clustering

Group keywords by semantic similarity using these signals (in priority order):

1. **SERP overlap**: Keywords where 3+ of the top 10 results are the same page belong in the same cluster. This is the strongest signal. If you have access to SERP data, use it as the primary grouping method.
2. **Semantic similarity**: Keywords sharing the same core entity or concept (e.g., "keyword clustering tool" and "keyword grouping software" target the same thing)
3. **Intent alignment**: Keywords in the same cluster should share the same primary intent. Split clusters when intent diverges.

**Cluster naming**: Each cluster gets a primary keyword (highest volume keyword that best represents the topic) and a descriptive cluster name.

### Step 3: Cannibalization Detection

For each cluster, check if:

- Multiple existing pages on the site target the same cluster
- A single page tries to rank for keywords across different intent types
- Two clusters are close enough that they risk splitting authority

Flag these as `CANNIBALIZATION_RISK` with the affected URLs. Cross-reference with the `cannibalization` skill for deeper analysis.

### Step 4: Page Mapping

For each cluster, determine:

1. **Existing page match**: Does a page on the site already target this cluster? (Check URL slugs, title tags, H1s)
2. **New page opportunity**: No existing page covers this cluster adequately
3. **Page consolidation**: Multiple weak pages should merge into one

Provide a `mapping` field: `existing:<URL>`, `new`, or `consolidate:<URL1>,<URL2>`

### Step 5: Priority Scoring

Score each cluster 0-100 based on:

```
priority = (volume_score * 0.4) + (intent_score * 0.3) + (competition_score * 0.3)
```

Where:
- **volume_score**: Normalized aggregate search volume across all keywords in the cluster (0-100)
- **intent_score**: Transactional = 100, Commercial = 75, Informational = 40, Navigational = 20
- **competition_score**: Inverted difficulty (low competition = high score). If no difficulty data, default to 50.

## Output Format

### Per-cluster output

```json
{
  "cluster_id": 1,
  "cluster_name": "Keyword Research Tools",
  "primary_keyword": "best keyword research tools",
  "supporting_keywords": [
    {"keyword": "keyword research tools free", "volume": 1200, "intent": "commercial"},
    {"keyword": "top keyword research tools 2026", "volume": 800, "intent": "commercial"},
    {"keyword": "keyword research software", "volume": 600, "intent": "commercial"}
  ],
  "intent": "commercial",
  "content_type": "listicle",
  "suggested_url": "/blog/best-keyword-research-tools/",
  "mapping": "new",
  "priority_score": 78,
  "cannibalization_risk": false,
  "notes": "High commercial intent. No existing page. Top SERPs dominated by listicles with 2000-3000 words."
}
```

### Summary output

After all clusters, provide:

1. **Cluster summary table**: cluster name, primary keyword, intent, keyword count, total volume, priority score, mapping status
2. **Quick wins**: Top 5 clusters by priority score that map to `new` pages
3. **Cannibalization alerts**: All clusters with `cannibalization_risk: true`
4. **Content calendar suggestion**: Clusters ordered by priority, grouped into monthly batches of 4-6 pieces

## Handling Large Keyword Sets (1000+)

For lists exceeding 1000 keywords:

1. **Pre-filter**: Remove duplicates, near-duplicates (edit distance < 2), and zero-volume keywords if volume data exists
2. **Batch processing**: Process in batches of 200-300 keywords
3. **Two-pass clustering**: First pass groups by broad topic. Second pass sub-clusters within each topic by intent.
4. **Merge pass**: After all batches, check for clusters that should merge across batches

Tell the user the estimated processing approach before starting. For 1000+ keywords, output clusters to a structured file (JSON or CSV) rather than inline.

## Content Type Mapping

Map each cluster to the optimal content type:

| Intent | Content Types |
|---|---|
| Informational | How-to guide, tutorial, explainer, glossary entry |
| Navigational | Landing page, product page, tool page |
| Commercial | Comparison post, listicle, review, "best of" roundup |
| Transactional | Product page, pricing page, free trial landing page |

## Cross-References

- Run `cannibalization` skill on flagged clusters for deeper analysis
- Feed high-priority `new` clusters into the `content-brief` skill to generate briefs
- Use `internal-links` skill to plan link architecture between cluster pages
- Apply `meta-optimizer` skill to existing pages that map to clusters but have weak title/description alignment

## Example Interaction

**User**: "Here are 150 keywords from Ahrefs for my SaaS project management tool. Cluster them."

**You**:
1. Parse the input (CSV with keyword, volume, difficulty, cpc)
2. Count: 150 keywords, 3 duplicates removed = 147 unique
3. Classify intent for each keyword
4. Group into clusters (expect 15-25 clusters from 147 keywords)
5. Check site for existing page coverage
6. Score and rank clusters
7. Output the full cluster report with summary table and recommendations

## Error Handling

- If no volume data: cluster by semantic similarity and intent only. Note that priority scores are estimated without volume.
- If no site URL provided: skip page mapping and cannibalization checks. Flag that these steps were skipped.
- If input format is unrecognizable: ask the user to provide keywords as one-per-line plain text.
