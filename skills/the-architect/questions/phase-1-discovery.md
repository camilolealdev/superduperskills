# Phase 1: Discovery Questions

These questions identify WHAT the user wants to build and classify it into an archetype. Ask conversationally — 2-3 questions at a time, not all at once.

---

## Core Questions

### Q1: The Vision
**Ask:** "What are you building? Describe it in your own words — what does it do, what problem does it solve?"

**Why:** This is open-ended on purpose. Let the user paint the picture. Listen for keywords that signal the archetype.

**Archetype signals:**
- "users sign up", "subscription", "dashboard", "SaaS" → **saas-webapp**
- "landing page", "marketing", "convert", "launch" → **marketing-site**
- "iOS", "Android", "mobile", "app store" → **mobile-app**
- "API", "endpoints", "microservice", "backend" → **api-backend**
- "admin panel", "internal", "dashboard for our team" → **internal-tool**
- "blog", "content", "articles", "documentation" → **content-platform**

### Q2: The Audience
**Ask:** "Who will use this? End users? Your internal team? Other developers? How many users are you expecting?"

**Why:** Determines scale, auth complexity, and UX expectations. A tool for 5 internal users is fundamentally different from a public SaaS.

### Q3: The Stage
**Ask:** "What stage is this? Quick prototype to validate an idea, or production-ready from day one?"

**Why:** MVP means smart defaults and speed. Production means error handling, testing, monitoring, CI/CD.

### Q4: Tech Preferences (if not already clear)
**Ask:** "Do you have any tech preferences or constraints? Existing stack, favorite framework, hosting requirement?"

**Why:** Some users have strong opinions (must use Vue, must deploy on AWS). Others want a recommendation. Adapt accordingly.

### Q5: Timeline (optional — ask only if relevant)
**Ask:** "What's the timeline? Weekend project or multi-week build?"

**Why:** Affects scope of the blueprint. Weekend project = minimal viable set. Multi-week = full architecture.

---

## Classification Logic

After Q1-Q3, you should be able to classify. If ambiguous, ask one clarifying question rather than guessing.

| If the project is primarily... | Archetype |
|-------------------------------|-----------|
| A web app where users create accounts and use features | `saas-webapp` |
| A static or semi-static site to present/sell something | `marketing-site` |
| A native or cross-platform mobile app | `mobile-app` |
| A headless API consumed by other services/apps | `api-backend` |
| A tool used internally by a team (not public-facing) | `internal-tool` |
| Centered around creating, organizing, or displaying content | `content-platform` |

**Hybrid projects:** If a project spans archetypes (e.g., SaaS with a marketing landing page), use the PRIMARY archetype and note the secondary in the blueprint. The build order will address both.

---

## After Classification

1. Tell the user which archetype you've identified and why
2. Read `knowledge/archetypes/<archetype>.md`
3. Proceed to Phase 2
