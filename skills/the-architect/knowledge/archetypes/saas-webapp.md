# Archetype: SaaS Web Application

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Framework | Next.js 15 (App Router) | Nuxt 4 | User prefers Vue |
| Language | TypeScript (strict) | — | Never compromise on this |
| Styling | Tailwind CSS v4 | — | Always Tailwind. It's the standard. |
| Components | shadcn/ui | Radix + custom | User wants full control |
| Database | Supabase (Postgres) | PlanetScale (MySQL) | Team knows MySQL better |
| ORM | Prisma | Drizzle | Performance-critical, wants SQL-like syntax |
| Auth | Clerk | NextAuth v5 | Budget-constrained or needs full customization |
| Payments | Stripe | Lemonsqueezy | Simpler billing, don't want to handle taxes |
| Email | Resend | SendGrid | Enterprise compliance requirements |
| Hosting | Vercel | Railway | Need persistent servers or Docker |
| Package Manager | pnpm | npm | Simplicity over speed |

## Default Directory Structure

```
src/
  app/
    (marketing)/              # Public pages — no auth required
      page.tsx                # Landing page
      pricing/page.tsx        # Pricing page
      layout.tsx              # Marketing layout (navbar + footer)
    (app)/                    # Authenticated app — protected by middleware
      dashboard/page.tsx      # Main dashboard
      settings/
        page.tsx              # User settings
        billing/page.tsx      # Billing/subscription management
      [feature]/              # Core feature pages
        page.tsx
        [id]/page.tsx
      layout.tsx              # App layout (sidebar + topbar)
    api/
      webhooks/
        stripe/route.ts       # Stripe webhook handler
      [feature]/route.ts      # REST API routes
    layout.tsx                # Root layout
    globals.css               # Tailwind imports + CSS variables
  components/
    ui/                       # shadcn/ui primitives (button, dialog, etc.)
    marketing/                # Landing page components
    app/                      # App-specific components (dashboard widgets, etc.)
    shared/                   # Used in both marketing and app
  lib/
    supabase/
      client.ts               # Browser Supabase client
      server.ts               # Server Supabase client
      middleware.ts            # Auth middleware helper
    stripe/
      client.ts               # Stripe instance
      helpers.ts              # Price/subscription utilities
    utils.ts                  # General utilities (cn, formatDate, etc.)
  types/
    index.ts                  # Shared TypeScript types
    database.ts               # Auto-generated from Prisma/Supabase
  middleware.ts               # Next.js middleware (auth + redirects)
prisma/
  schema.prisma               # Database schema (if using Prisma)
public/
  logo.svg
  og-image.png
```

## Common Patterns

### Auth Flow
1. User lands on marketing page → CTA to sign up
2. Sign-up via Clerk → redirect to onboarding (if needed) → dashboard
3. Middleware checks auth on all `/(app)/*` routes
4. Session available server-side via `auth()`, client-side via `useAuth()`

### Data Layer
- Server Components fetch data directly (no API call needed)
- Mutations go through Server Actions or API routes
- Optimistic updates via `useOptimistic` or React Query

### Billing
- Pricing page shows plans → Stripe Checkout → webhook confirms subscription
- `user.subscription` field tracks plan (free/pro/enterprise)
- Webhook handler at `/api/webhooks/stripe` processes: `checkout.session.completed`, `customer.subscription.updated`, `customer.subscription.deleted`

## Build Order

1. **Scaffolding**: `npx create-next-app@latest`, install Tailwind v4, configure path aliases, init shadcn/ui
2. **Database**: Create Supabase project, define schema (users, core entities), generate types
3. **Auth**: Set up Clerk (sign-up, sign-in, middleware, protected routes)
4. **Layouts**: Marketing layout (navbar/footer) + App layout (sidebar/topbar)
5. **Core CRUD**: Build the main feature — create, read, update, delete the primary entity
6. **Dashboard**: List view of the core entity with filters/search
7. **Detail pages**: Individual entity view + edit
8. **Stripe**: Pricing page, checkout flow, webhook handler, billing portal
9. **Settings**: Profile page, billing management, account deletion
10. **Landing page**: Hero, features, testimonials, CTA — using marketing layout
11. **Polish**: Loading states, error boundaries, empty states, responsive design
12. **Deploy**: Vercel deployment, environment variables, custom domain

## Common Pitfalls

- **Don't build auth from scratch.** Use Clerk or NextAuth. Custom auth is a rabbit hole.
- **Don't over-abstract early.** Build the first feature end-to-end, THEN extract patterns.
- **Webhook reliability.** Always verify Stripe webhook signatures. Use idempotency keys.
- **Rate limiting.** Add rate limiting to auth and API routes from day one — not after abuse.
- **SEO on marketing pages.** Use proper metadata, OG images, sitemap. SaaS landing pages need SEO.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/frontend-design` | Building the landing page and app layouts |
| `/shadcn-ui` | Setting up and customizing shadcn components |
| `/ui-ux-pro-max` | Design system decisions during build |
| `/seo-audit` | After landing page is built |

## See Also

- `knowledge/building-blocks/auth-patterns.md` — Clerk vs NextAuth decision details
- `knowledge/building-blocks/database-patterns.md` — Schema design, ORM comparison, migration strategy
- `knowledge/building-blocks/state-management.md` — Server Components + TanStack Query + Zustand (recommended combo)
- `knowledge/building-blocks/deployment-patterns.md` — Vercel config, CI/CD, environment management
- `knowledge/building-blocks/styling-systems.md` — Tailwind v4 setup, design tokens, shadcn/ui integration
