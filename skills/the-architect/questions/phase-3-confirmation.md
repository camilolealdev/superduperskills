# Phase 3: Architecture Confirmation

Before generating the blueprint, present the proposed architecture and get user approval. This phase is a conversation, not a questionnaire.

---

## What to Present

Summarize your proposed architecture in a compact format:

1. **Tech stack table** — every layer with your recommendation and a one-line rationale
2. **High-level architecture** — how the pieces connect (1-2 paragraphs or a simple diagram)
3. **Core features list** — what the first version includes (and what it doesn't)
4. **Build approach** — rough phase breakdown (e.g., "I'd build auth first, then the core data model, then the dashboard, then payments")

Keep it to ONE message. Dense, scannable, under 40 lines.

---

## Confirmation Questions

### Q1: Architecture Fit
"Does this match your vision? Anything you'd change, add, or remove?"

### Q2: Design Direction (only for projects with a frontend UI)
"Any design preferences? Minimal and clean? Bold and colorful? Dark mode? Reference a site you like?"

**Skip this question entirely for API-only or backend-only projects.**

After the user responds, invoke `/ui-ux-pro-max` to select: color palette, font pairing, and component style based on their preferences.

### Q3: Hard Constraints (only if not covered)
"Any libraries or tools you definitely want — or definitely don't want?"

---

## After Confirmation

Once the user confirms (or you've integrated their feedback):
1. State: "I'll generate your blueprint now."
2. Proceed to Phase 4: GENERATE.

If the user has significant changes, adjust and re-present. Don't loop more than twice — if alignment is hard, ask what the sticking point is directly.
