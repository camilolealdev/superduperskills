# CLAUDE.md Template for Target Projects

Use this template when generating Section 15 of the blueprint. Fill in every section. The generated CLAUDE.md must give Claude Code complete context to build autonomously.

---

## Template

```markdown
# {Project Name}

{One-line description of what this project is.}

## Commands

- `{package-manager} dev` — Start development server
- `{package-manager} build` — Production build
- `{package-manager} lint` — Run linter
- `{package-manager} test` — Run tests
- `{package-manager} db:push` — Push schema to database (if applicable)
- `{package-manager} db:generate` — Generate types from schema (if applicable)

## Tech Stack

{Framework} + {Language} + {Styling} + {Components} + {Database} + {Auth} + {Hosting}

## Architecture

### Directory Structure
- `src/app/` — {App Router pages and layouts}
- `src/components/` — {UI components organized by domain}
- `src/lib/` — {Utilities, database client, auth helpers}
- `src/types/` — {Shared TypeScript types}
- `public/` — {Static assets}

### Data Flow
{How data moves: client → API route → database, or server component → direct query}

### Key Patterns
- {Pattern 1 — e.g., Server Components by default, Client Components only when needed}
- {Pattern 2 — e.g., All database queries go through lib/db.ts}
- {Pattern 3 — e.g., Auth middleware in middleware.ts protects /app/* routes}

## Code Organization Rules

1. **One component per file.** Max 300 lines. If longer, extract sub-components.
2. **Path alias:** Use `@/` for `src/` imports.
3. **No barrel exports.** Import directly from the source file.
4. **Server Components by default.** Only add "use client" when the component needs interactivity.
5. **Colocate related files.** Keep page-specific components next to their page.

## Design System

### Colors
{List all color tokens with hex values}

### Typography
- Headings: {font}, {weights}
- Body: {font}, {size}

### Style
- Border radius: {value}
- Shadows: {values}
- Spacing base: {value}
- Aesthetic: {description — e.g., clean, minimal, rounded corners, subtle shadows}

## Environment Variables

| Variable | Description |
|----------|-------------|
| `{VAR}` | {what it's for} |

## Reglas No Negociables

1. {Rule 1}
2. {Rule 2}
3. {Rule 3}
4. {Rule 4}
5. {Rule 5}
```

---

## Guidelines for Generating CLAUDE.md

- Keep it under 120 lines. Dense, scannable, no fluff.
- Commands section first — the builder needs to know how to run things immediately.
- Tech stack as a single line — quick reference, not a table.
- Architecture section should explain HOW things connect, not just list folders.
- Code organization rules must be specific and actionable — "keep files short" is bad, "max 300 lines per component" is good.
- Design system must include actual values (hex codes, px sizes) not vague descriptions.
- Reglas are non-negotiable constraints. Include only rules that, if broken, would cause real problems.
