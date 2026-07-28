---
name: awesome-design-md
description: >
  Reference library of DESIGN.md files documenting the visual language of
  74 well-known products and brands (design-md/<brand>/DESIGN.md — e.g.
  Stripe, Linear, Apple, Notion, Vercel, Spotify, Tesla, and others). Use
  when the user wants a coding agent to match a specific brand's look and
  feel ("make it feel like Stripe", "give me a Linear-style dashboard",
  "match Apple's design language"), wants to compare design systems, or
  is looking for a DESIGN.md template to adapt for their own project.
  Drop the matching brand's DESIGN.md into a project so frontend-design/
  design-void/apply-aesthetic-style skills have concrete tokens to follow,
  rather than guessing. Pair with design-md-validator to lint a DESIGN.md
  for spec compliance before relying on it.
metadata:
  source: https://github.com/VoltAgent/awesome-design-md
---

# awesome-design-md — brand DESIGN.md reference library

This skill's actual content lives in the `design-md/<brand>/` folders next
to this file — each has a `DESIGN.md` (the design-system breakdown) and a
`README.md`. There are 74 brands covered as of this writing (run
`ls design-md/` for the current list — new ones get added upstream).

## How to use

1. Ask the user which brand's aesthetic they want to match, or infer it
   from their request ("make it feel premium like X").
2. Read `design-md/<brand>/DESIGN.md` for that brand's documented palette,
   typography, spacing, and component conventions.
3. Apply those tokens when building the interface — treat the file as a
   design-token reference, not boilerplate to copy verbatim into unrelated
   projects (these describe real companies' visual identities; use them to
   inform an original interface, not to impersonate the brand).
4. If the user wants their OWN project's design system documented in the
   same format (for consistency, or to hand to another coding agent), use
   this repo's structure as the template and write a project-specific
   `DESIGN.md` — see `design-void` in this bundle for a worked example of
   reverse-engineering one from an existing site.
5. Before trusting a hand-written or generated `DESIGN.md`, validate it
   with `design-md-validator` (checks spec compliance, WCAG contrast,
   token references).
