---
name: design-dna
description: >
  Brand identity and design system extraction skill. Extracts color palettes, typography scales,
  component primitives, and design tokens from websites or screenshots into structured JSON/CSS.
  Use when reverse-engineering brand design systems, establishing design tokens, or when user mentions
  "design dna", "design-dna", "extract design tokens", "brand profile", or "design extraction".
argument-hint: "[extract|tokens|palette|typography|components]"
license: MIT
---

# Design DNA — Brand & Design System Extraction

Based on [zanwei/design-dna](https://github.com/zanwei/design-dna), **Design DNA** extracts and codifies visual brand identity into production-ready Design Tokens (DTCG format, CSS custom properties, and Tailwind theme extensions).

## Core Capabilities

- **Color Palette Extraction**: Detects primary, secondary, neutral, and accent colors with WCAG contrast ratio validation.
- **Typography Scale Mapping**: Identifies font families, line heights, font weights, and fluid modular scales.
- **Elevation & Radius Tokens**: Captures shadow scales, border radii, and surface elevation treatments.
- **Export Formats**: Outputs Tailwind v4 CSS variables, W3C Design Tokens JSON, and SCSS primitives.
