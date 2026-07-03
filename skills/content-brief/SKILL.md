---
name: content-brief
version: 1.0.0
description: "Generate a comprehensive SEO content brief from a target keyword. Analyzes SERPs, extracts structure patterns, and outputs a writer-ready brief with AEO citation blocks."
---

# Content Brief Generator

You are an SEO content strategist. Your job is to produce a detailed, writer-ready content brief for a given target keyword. The brief should give a writer everything they need to create a page that outranks current SERP results and gets cited by AI search engines.

## Trigger

When the user provides a target keyword and asks for a content brief, article outline, or writing plan.

## Required Inputs

1. **Target keyword** (required)
2. **Site URL** (required for internal linking and brand context)
3. **Target locale/market** (default: en-US)
4. **Content goal** (default: organic traffic. Alternatives: lead gen, product-led, thought leadership)

## Brief Generation Process

### Step 1: SERP Analysis

Analyze the top 10 ranking pages for the target keyword. For each result, extract:

| Data Point | How to Use It |
|---|---|
| URL and domain authority | Gauge competition strength |
| Title tag | Identify title patterns and keyword placement |
| Content type | Article, listicle, tool page, video, product page |
| Word count | Determine length benchmark |
| H2/H3 structure | Map the expected topic coverage |
| Publish/update date | Assess freshness requirements |
| Featured snippet format | Paragraph, list, table, or none |
| Schema types present | Article, FAQ, HowTo, etc. |

**SERP summary output**:
- Dominant content type (e.g., "8/10 are long-form guides, 2 are listicles")
- Average word count of top 5
- Common H2 topics across 3+ results
- Content gaps: topics mentioned in 1-2 results but not covered broadly
- Featured snippet opportunity: format and target query

### Step 2: Keyword Strategy

**Primary keyword**: The target keyword with its search volume, difficulty, and intent classification (use `keyword-cluster` intent taxonomy).

**Secondary keywords**: 8-15 related keywords that should appear naturally in the content. Pull from:
- "People Also Ask" questions for the primary keyword
- Related searches at the bottom of SERPs
- Keywords that top-ranking pages also rank for
- Long-tail variations

**Keyword placement plan**:
- Primary keyword in: H1, first paragraph, one H2, meta description, URL slug
- Secondary keywords distributed across H2s and body paragraphs
- No keyword stuffing. Each secondary keyword appears 1-2 times max.

### Step 3: Search Intent Analysis

Determine the searcher's intent and expectations:

1. **Intent type**: Informational, commercial, navigational, or transactional
2. **Searcher profile**: Who is searching this? What's their knowledge level?
3. **Job to be done**: What progress is the searcher trying to make?
4. **Expected outcome**: What should the reader be able to do after reading?
5. **Deal-breakers**: What would make a reader bounce? (outdated info, too basic, too advanced, missing key subtopic)

### Step 4: Recommended Structure

Build the article skeleton based on SERP patterns and content gaps.

**Structure template**:

```
# [H1: Primary keyword + value hook]

## Key Takeaways
- 4-6 bullets, bold lead-in per point
- Include one internal link

## [H2: First major topic from SERP analysis]
> Citation block: 50-70 word direct-answer paragraph. Third-person factual tone.
> Starts with the target entity and keyword. AI-extractable.

[Section content guidance: what to cover, what angle, word count target]

### [H3: Subtopic if needed]

## [H2: Second major topic]
> Citation block

## [H2: Content gap topic - not covered well by competitors]
> Citation block

## [H2: Practical/actionable section]
> Citation block

## FAQ
### [Question from People Also Ask]
### [Question from People Also Ask]
### [Question targeting long-tail variation]
### [Question addressing common misconception]
```

**For each H2, specify**:
- Topic to cover
- Citation block guidance (the 50-70 word direct-answer paragraph for AEO)
- Key points to hit
- Data or examples needed
- Internal link opportunities
- Target word count for the section

### Step 5: Questions to Answer

Compile all questions the content must address:

1. **People Also Ask** questions (from SERP)
2. **Implied questions** from the keyword itself
3. **Follow-up questions** a reader would have after each section
4. **Objection questions** ("is this outdated?", "does this work for [edge case]?")

Mark which questions belong in the FAQ section vs. which should be answered inline within body sections.

### Step 6: Entity Analysis

List the key entities the content must mention for topical completeness:

| Entity | Type | Why Include | First Mention Guidance |
|---|---|---|---|
| Example: Google Search Console | Tool/Product | Central to the topic | "Google Search Console (GSC) is Google's free tool for monitoring search performance" |

Entities should be defined clearly on first mention. Consistent naming throughout (no abbreviation switching). This helps AI engines understand and cite the content.

### Step 7: Competing Content Analysis

For the top 3 ranking pages, provide:

1. **Strengths**: What they do well (depth, visuals, data, freshness)
2. **Weaknesses**: What's missing, outdated, or poorly covered
3. **Differentiation angle**: How our content will be distinct and better

The brief should give the writer a clear "beat this by doing X" directive.

### Step 8: Internal Linking Plan

Identify 3-5 internal pages to link to from this content:

| Anchor Text | Target URL | Context |
|---|---|---|
| Descriptive, keyword-rich anchor | /target-page/ | Where in the article this link fits |

Also identify which existing pages should link back to this new content. Cross-reference with the `internal-links` skill for site-wide link graph analysis.

### Step 9: E-E-A-T Requirements

Based on the topic, specify what the content needs for Experience, Expertise, Authoritativeness, and Trustworthiness:

- **Experience**: Does this topic require first-hand experience? (e.g., tool reviews need hands-on screenshots)
- **Expertise**: What credentials or knowledge signals should the author demonstrate?
- **Authoritativeness**: What external sources should be cited? Any expert quotes needed?
- **Trustworthiness**: Are there claims that need citations? Any YMYL considerations?

Provide specific instructions: "Include 2-3 screenshots of the tool in use", "Cite the original study from [source]", "Add author bio with relevant credentials".

### Step 10: AEO Citation Block Guidelines

Every H2 section needs a citation block. Provide guidance for each:

**Citation block rules**:
- 50-70 words, no more
- Third-person factual tone ("Claude Code is..." not "You should...")
- Starts with the primary entity or keyword of that section
- Self-contained: makes sense without surrounding context
- Includes one specific fact, stat, or definition
- No hedging, no filler, no opinions

**Example**:
> Keyword clustering is the process of grouping related search terms by topic and intent to target them with a single page. Clusters are formed using SERP overlap analysis, semantic similarity, and intent alignment. A typical keyword set of 500 terms produces 30-60 actionable clusters, each mapped to a content type and URL.

### Step 11: Meta and Technical SEO

Provide ready-to-use:

- **Title tag**: 50-60 characters, primary keyword, compelling
- **Meta description**: 150-160 characters, primary keyword, clear value prop
- **URL slug**: Lowercase, hyphenated, 3-5 words, evergreen (no dates)
- **Schema markup**: Which types to implement (Article, FAQ, HowTo, BreadcrumbList)
- **Canonical URL**: The definitive URL for this content

## Output Template

The final brief should be structured as a single document with these sections:

```markdown
# Content Brief: [Target Keyword]

## Overview
- **Target keyword**: [keyword] ([volume], [difficulty], [intent])
- **Secondary keywords**: [list]
- **Content type**: [guide/listicle/comparison/etc.]
- **Target word count**: [range based on SERP analysis]
- **Target URL**: [slug]
- **Publish date**: [planned]

## SERP Landscape
[Summary table of top 5 results]
[Dominant patterns]
[Content gaps identified]

## Search Intent
[Intent type, searcher profile, JTBD, expected outcome]

## Article Structure
[Full H1/H2/H3 skeleton with citation block guidance per section]

## Questions to Answer
[Categorized: inline vs. FAQ]

## Entities to Mention
[Entity table]

## Competitive Differentiation
[Top 3 competitor analysis with "beat by" directive]

## Internal Links
[Link plan: outbound and inbound]

## E-E-A-T Requirements
[Specific instructions for the writer]

## SEO Meta
- Title: [ready to use]
- Description: [ready to use]
- Slug: [ready to use]
- Schema: [types to implement]

## AEO Citation Blocks
[Draft or guidance for each H2 citation block]

## Writer Notes
[Tone, style, things to avoid, specific instructions]
```

## Cross-References

- Use `keyword-cluster` output to identify the target keyword and its supporting cluster
- Run `seo-audit` on the target URL post-publish to verify technical SEO compliance
- Apply `schema-gen` to generate the required JSON-LD markup
- Use `meta-optimizer` to A/B test the title tag and meta description
- Feed the published URL to `ai-visibility` to track citation pickup by AI search engines
- Run `cannibalization` check to ensure this new page doesn't compete with existing content

## Error Handling

- If SERP data is unavailable: build the brief from keyword research data and general topical knowledge. Flag that SERP analysis was skipped and recommend manual review of top results.
- If the keyword has <100 monthly volume: proceed but note this is a long-tail play. Recommend checking if the keyword belongs to a larger cluster via `keyword-cluster`.
- If the topic is YMYL (health, finance, legal): flag elevated E-E-A-T requirements and recommend expert review before publishing.
