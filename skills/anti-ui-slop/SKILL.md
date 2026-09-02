---
name: anti-ui-slop
description: >
  Stops AI models from shipping generic, boring UI by leveraging UIZZE's public catalog of 800,000+ real web and iOS screens.
  Use when designing production-grade interfaces, preventing AI UI slop, or when user mentions "anti-ui-slop",
  "anti ui slop", "prevent generic UI", or "uizze catalog".
argument-hint: "[catalog|audit|custom|typography|spacing]"
license: MIT
---

# Anti UI Slop — Prevention of Generic AI Frontend Interfaces

Based on [github/anti-ui-slop](https://skillrepo.dev/skills/github/anti-ui-slop) (v1.0A), this skill prevents AI models from outputting repetitive, generic "Bootstrap/Tailwind default" layouts.

## Prevention Rules

1. **No Standard System Colors**: Ban raw `#000`, `#fff`, `bg-blue-500`, and `bg-gray-100`. Require custom HSL/OKLCH color scales with distinct hue shifts.
2. **Typography Hierarchy**: Prohibit using default system sans-serif everywhere. Pair a high-character display font (e.g. Outfit, Syne, Instrument Serif) with an ultra-readable body typeface.
3. **Tactile Micro-Details**: Mandate subtle 1px inner borders (`border-white/10`), dynamic backdrop blur, and custom SVG iconography over generic generic icons.
