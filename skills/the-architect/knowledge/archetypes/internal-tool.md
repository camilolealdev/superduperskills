# Archetype: Internal Tool / Admin Dashboard

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Framework | Next.js 15 (App Router) | Retool, Refine | Retool for no-code, Refine for rapid admin CRUD |
| Language | TypeScript | — | Always |
| Styling | Tailwind CSS v4 | — | Always |
| Components | shadcn/ui | Tremor (for dashboards) | Tremor when heavy on charts/metrics |
| Charts | Recharts | Chart.js, Tremor charts | Tremor if using Tremor components |
| Tables | TanStack Table | AG Grid | AG Grid for enterprise-grade tables |
| Database | Direct connection (Postgres) | Existing database | Usually connects to existing data |
| ORM | Prisma | Drizzle | — |
| Auth | Clerk | NextAuth v5, basic email/password | NextAuth for full self-hosted control, basic auth for < 10 users |
| Hosting | Vercel | Self-hosted (Docker) | Self-hosted if data can't leave network |
| Package Manager | pnpm | npm | — |

## Default Directory Structure

```
src/
  app/
    login/page.tsx             # Simple login page
    (dashboard)/
      page.tsx                 # Overview dashboard (KPIs, charts)
      [resource]/
        page.tsx               # Resource list (table with filters)
        [id]/page.tsx          # Resource detail/edit
        new/page.tsx           # Create new resource
      settings/page.tsx        # App settings
      users/page.tsx           # User management (if multi-user)
      layout.tsx               # Dashboard layout (sidebar + header)
    api/
      [resource]/route.ts      # CRUD API routes
      export/route.ts          # CSV/PDF export endpoints
    layout.tsx                 # Root layout
  components/
    ui/                        # shadcn/ui primitives
    dashboard/
      StatsCard.tsx            # KPI card
      Chart.tsx                # Reusable chart wrapper
      DataTable.tsx            # Generic data table with sorting/filtering/pagination
      FilterBar.tsx            # Filter controls
    forms/
      ResourceForm.tsx         # Generic form with validation
    layout/
      Sidebar.tsx              # Navigation sidebar
      Header.tsx               # Top bar with search + user menu
  lib/
    db.ts                      # Database client
    auth.ts                    # Auth helpers
    export.ts                  # CSV/PDF generation utilities
    utils.ts                   # Formatting, date helpers
  types/
    index.ts
  middleware.ts                # Auth middleware
```

## Common Patterns

### Dashboard Layout
- Fixed sidebar (collapsible on mobile) with navigation links
- Top header with breadcrumbs, search, user menu
- Main content area with consistent padding

### Data Tables
- TanStack Table with server-side pagination, sorting, filtering
- Column visibility toggle
- Bulk actions (select multiple → action)
- Export to CSV button

### CRUD Pattern
- List page: table with filters → click row → detail page
- Detail page: read view with edit button → edit mode (inline or separate page)
- Create page: form with validation → redirect to detail on success
- Delete: confirmation dialog → soft delete (set `deleted_at`)

### Exports
- CSV export: stream large datasets, don't load all into memory
- PDF export: use server-side HTML-to-PDF (Playwright or Puppeteer)

## Build Order

1. **Scaffolding**: Next.js, Tailwind, shadcn/ui, path aliases
2. **Auth**: Simple login page + middleware (can be basic email/password for internal)
3. **Layout**: Sidebar + header + responsive shell
4. **Dashboard**: Overview page with placeholder KPI cards and charts
5. **First resource CRUD**: Full list → detail → create → edit → delete flow
6. **Data table**: Generic DataTable component with pagination, sorting, filtering
7. **Charts**: Wire up real data to dashboard charts (Recharts)
8. **Export**: CSV export for tables, PDF for reports
9. **User management** (if multi-user): Invite, roles, permissions
10. **Polish**: Loading states, empty states, error handling
11. **Deploy**: Vercel or Docker, environment config

## Common Pitfalls

- **Don't over-design internal tools.** Function over form. Users need speed, not animations.
- **Don't skip pagination.** Internal databases often have millions of rows. Always paginate.
- **Don't forget audit logging.** Track who changed what and when. Critical for internal tools.
- **Don't build real-time unless needed.** Polling every 30s is fine for most dashboards.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/shadcn-ui` | Setting up table, form, and dialog components |
| `/frontend-design` | Dashboard layout and data visualization |
| `/ui-ux-pro-max` | Color system for data visualization |

## See Also

- `knowledge/building-blocks/auth-patterns.md` — Clerk setup, role-based access patterns
- `knowledge/building-blocks/database-patterns.md` — Schema design, pagination, naming conventions
- `knowledge/building-blocks/state-management.md` — Server Components for data display, Zustand for UI state
- `knowledge/building-blocks/testing-patterns.md` — E2E tests for core workflows
