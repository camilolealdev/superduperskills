# Building Block: Styling Systems

## Decision Matrix

| System | Best For | Pros | Cons |
|--------|----------|------|------|
| **Tailwind CSS v4** | Everything (recommended default) | Utility-first, fast development, small bundle | Verbose HTML, learning curve |
| **CSS Modules** | Component isolation | Native CSS, zero runtime, scoped | Verbose, no design tokens built-in |
| **Styled Components** | Dynamic styling | Co-located styles, theming | Runtime cost, SSR complexity |
| **Vanilla Extract** | Type-safe CSS | Zero runtime, TypeScript API | Build step, less flexible |
| **Panda CSS** | Tailwind-like + type safety | Type-safe utilities, zero runtime | Newer, smaller ecosystem |

## Recommendation: Always Tailwind v4

For 95% of projects, Tailwind CSS v4 is the right choice. It's the standard.

### Tailwind v4 Setup (Next.js)
```css
/* globals.css */
@import "tailwindcss";

/* Custom properties for design tokens */
@theme {
  --color-primary: #2563eb;
  --color-secondary: #7c3aed;
  --font-sans: 'Inter', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```

### Dark Mode
```css
/* Tailwind v4 — CSS-based dark mode */
@theme {
  --color-background: #ffffff;
  --color-surface: #f8fafc;
  --color-text: #0f172a;
}

@media (prefers-color-scheme: dark) {
  :root {
    --color-background: #0f172a;
    --color-surface: #1e293b;
    --color-text: #f8fafc;
  }
}
```

## Design Token Architecture

### Three Layers
1. **Primitive tokens**: Raw values (`blue-500: #3b82f6`)
2. **Semantic tokens**: Meaning (`primary: blue-500`, `danger: red-500`)
3. **Component tokens**: Specific usage (`button-bg: primary`, `input-border: muted`)

### Implementing in Tailwind v4
```css
@theme {
  /* Primitives — rarely used directly */
  --color-blue-500: #3b82f6;
  --color-blue-600: #2563eb;

  /* Semantic — use these in code */
  --color-primary: var(--color-blue-600);
  --color-primary-hover: var(--color-blue-500);
  --color-destructive: #ef4444;
  --color-muted: #64748b;

  /* Spacing scale */
  --spacing-xs: 4px;
  --spacing-sm: 8px;
  --spacing-md: 16px;
  --spacing-lg: 24px;
  --spacing-xl: 32px;
  --spacing-2xl: 48px;

  /* Border radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-full: 9999px;
}
```

## shadcn/ui Integration

shadcn/ui uses CSS custom properties for theming. Works perfectly with Tailwind v4.

### Setup
```bash
npx shadcn@latest init
# Select: New York style, Tailwind CSS, CSS variables
```

### Customizing Colors
Override CSS variables in `globals.css` to match the design system.

### Key Components to Install First
1. `button` — used everywhere
2. `input` + `label` — forms
3. `dialog` — modals
4. `dropdown-menu` — menus
5. `card` — content containers
6. `table` — data display
7. `toast` — notifications
8. `form` — React Hook Form integration

## Typography System

### Font Loading (Next.js)
```typescript
import { Inter, JetBrains_Mono } from 'next/font/google'
const inter = Inter({ subsets: ['latin'], variable: '--font-sans' })
const jetbrains = JetBrains_Mono({ subsets: ['latin'], variable: '--font-mono' })
```

### Type Scale (Recommended)
| Role | Size | Weight | Line Height |
|------|------|--------|-------------|
| h1 | 2.25rem (36px) | 700 | 1.2 |
| h2 | 1.875rem (30px) | 600 | 1.3 |
| h3 | 1.5rem (24px) | 600 | 1.4 |
| h4 | 1.25rem (20px) | 600 | 1.4 |
| body | 1rem (16px) | 400 | 1.6 |
| small | 0.875rem (14px) | 400 | 1.5 |
| caption | 0.75rem (12px) | 500 | 1.5 |

## Responsive Design

### Breakpoints (Tailwind defaults)
| Name | Min Width | Target |
|------|-----------|--------|
| sm | 640px | Large phones |
| md | 768px | Tablets |
| lg | 1024px | Small laptops |
| xl | 1280px | Desktops |
| 2xl | 1536px | Large screens |

### Mobile-First Approach
Always write base styles for mobile, then add breakpoint overrides:
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
```
