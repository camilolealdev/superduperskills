---
name: design-void
description: Cyber-brutalism / high-contrast dark-mode design system reverse-engineered from the "VOID — Avant-Garde Web Creators" landing page. Use when the user wants an experimental, premium, tech-forward dark UI with a single vibrant accent color, custom cursor interactions, grain/noise texture overlay, and geometric sans-serif typography (Space Grotesk). Trigger on "cyber-brutalism", "avant-garde landing page", "dark mode with neon accent", "custom cursor site", "noise texture UI", "VOID style", or when redesigning a page toward a premium experimental agency aesthetic.
---

# Design System: VOID

This Design System documentation is reverse-engineered from the "VOID — Avant-Garde Web Creators" landing page source code.

## 1. Core Principles
The VOID design system is rooted in **Cyber-Brutalism** and **High-Contrast Minimalism**. It prioritizes a "dark mode" experience that feels experimental, premium, and tech-forward.
*   **Avant-Garde Aesthetic**: Uses non-standard UI patterns (custom cursors, noise textures) to signal creativity.
*   **High Energy/Low Friction**: The use of a singular, vibrant accent color against a near-black background creates immediate visual impact.
*   **Tactile Digitalism**: The inclusion of a grain/noise overlay adds a physical, film-like quality to the digital interface.

## 2. Color Palette

The system uses a restricted, high-contrast palette defined via CSS variables for consistency.

| Role | Hex Code | Tailwind Class (Approx) | Usage |
| :--- | :--- | :--- | :--- |
| **Background** | `#0A0A0A` | `bg-[#0A0A0A]` | Primary canvas color; deep matte black. |
| **Accent** | `#CCFF00` | `bg-[#CCFF00]` | "Electric Lime"; used for calls to action, cursors, and highlights. |
| **Text (Primary)** | `#F5F5F5` | `text-[#F5F5F5]` | Off-white; high readability against dark background. |
| **Overlay** | `RGBA(0,0,0,0.04)` | N/A | Noise texture used to break digital gradients. |

## 3. Typography
The system relies on a single, highly geometric sans-serif font family that balances technical precision with modern flair.

*   **Primary Font**: `Space Grotesk`, sans-serif.
*   **Weights**:
    *   `300` (Light) - Used for subheaders or fine print.
    *   `400` (Regular) - Body copy.
    *   `500` (Medium) - UI elements/Buttons.
    *   `700` (Bold) - Primary headings.
*   **Scale**: (Inferred)
    *   **H1**: Large, likely tracking-tight (e.g., `text-6xl` or `text-7xl`).
    *   **Body**: Standard readability (e.g., `text-base`).

## 4. Spacing & Layout
*   **Container**: Uses a full-width approach with `overflow-x: hidden` to allow for bleeding edge animations.
*   **Scrolling**: `scroll-smooth` is enabled for a fluid, premium navigation experience.
*   **Grid/Flex**: Standard Tailwind utility patterns are expected for layout alignment.

## 5. Components

### Custom Cursor (Signature Component)
A sophisticated interaction pattern that replaces the default browser pointer.
*   **Cursor Follower**: A small 8px solid dot (`var(--accent)`).
*   **Cursor Ring**: A 40px hollow ring that follows the dot with a slight lag.
*   **Interaction**: Uses `mix-blend-mode: difference` to ensure visibility across different background elements and provide a "negative" color effect over text.

### Noise Overlay
A global `::before` pseudo-element on the `.noise` class.
*   **Pattern**: SVG-based fractal noise.
*   **Opacity**: 4% (`0.04`).
*   **Behavior**: Fixed position, covers the entire viewport, pointer-events disabled.

### Navigation Items (Inferred)
*   Likely text-based with hover states that trigger cursor expansion or color shifts to `var(--accent)`.

## 6. Iconography
*   **Style**: Likely minimalist, stroke-based icons (e.g., Lucide or Phosphor) to match the geometric nature of Space Grotesk.
*   **Color**: Default to `#F5F5F5`, shifting to `#CCFF00` on interaction.

---

## Reference HTML

```html
<!DOCTYPE html>
<html lang="en" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>VOID — Avant-Garde Web Creators</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://unpkg.com/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --accent: #CCFF00; /* Electric Lime */
            --bg: #0A0A0A;
            --text: #F5F5F5;
        }

        body {
            font-family: 'Space Grotesk', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            cursor: none; /* Custom cursor implementation */
            overflow-x: hidden;
        }

        /* Noise Texture Overlay */
        .noise::before {
            content: "";
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: url('data:image/svg+xml,%3Csvg viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg"%3E%3Cfilter id="noiseFilter"%3E%3CfeTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="3" stitchTiles="stitch"/%3E%3C/filter%3E%3Crect width="100%25" height="100%25" filter="url(%23noiseFilter)"/%3E%3C/svg%3E');
            opacity: 0.04;
            pointer-events: none;
            z-index: 9999;
        }

        /* Custom Cursor */
        .cursor-follower {
            position: fixed;
            width: 8px;
            height: 8px;
            background-color: var(--accent);
            border-radius: 50%;
            pointer-events: none;
            z-index: 10000;
            transition: transform 0.1s ease-out, width 0.3s ease, height 0.3s ease;
            mix-blend-mode: difference;
        }

        .cursor-ring {
            position: fixed;
            width: 40px;
```

> The source document this was reverse-engineered from cuts off mid-declaration right here (`.cursor-ring { position: fixed; width: 40px;` — no closing brace, no `<body>`). That truncation is in the original file, not an artifact of this copy. Section 5 above ("Custom Cursor") describes the intended behavior (40px hollow ring, `mix-blend-mode: difference`, slight lag) — use that as the spec and reimplement the rest of `.cursor-ring` and the page body (hero, nav, sections) from the color/typography/component rules above rather than assuming exact undocumented values.
