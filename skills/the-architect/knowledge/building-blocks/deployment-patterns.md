# Building Block: Deployment Patterns

## Decision Matrix

| Platform | Best For | Pros | Cons | Cost |
|----------|----------|------|------|------|
| **Vercel** | Next.js, Astro, frontend | Zero-config, preview deploys, edge, analytics | Expensive at scale, vendor lock-in | Free hobby, $20/mo Pro |
| **Railway** | Full-stack, backend, Docker | Easy Docker deploys, databases included, logs | Less edge network, smaller ecosystem | $5/mo + usage |
| **Fly.io** | Global edge, Docker | Multi-region, low latency, persistent volumes | Steeper learning curve, CLI-heavy | Free tier, pay per use |
| **Cloudflare Pages** | Static, Workers | Fastest edge, free, Workers for API | Limited server-side features | Generous free tier |
| **AWS (ECS/Lambda)** | Enterprise, complex infra | Full control, any architecture | Complex setup, expensive knowledge cost | Pay per use |
| **Self-hosted (Docker)** | On-prem, data sovereignty | Full control, no vendor lock | Ops burden, security responsibility | Server cost |

## Deployment Patterns by Project Type

### SaaS / Web App (Vercel)
```
Production: main branch → auto-deploy to vercel.com
Preview: PR branches → preview-{branch}.vercel.app
Environment vars: Vercel dashboard → Settings → Environment Variables
Custom domain: Vercel → Domains → Add → configure DNS
```

### API / Backend (Railway)
```
Production: main branch → auto-deploy
Database: Railway Postgres addon
Redis: Railway Redis addon
Environment vars: Railway dashboard → Variables
Custom domain: Railway → Settings → Domains
Health check: /health endpoint configured in Railway
```

### Static / Marketing (Cloudflare Pages or Vercel)
```
Build: npm run build → output directory
Deploy: git push → auto-build → CDN distribution
Custom domain: DNS → CNAME to platform
Headers: _headers file or platform config (cache, security)
```

## CI/CD Patterns

### Minimal (Recommended for MVPs)
- Push to main → auto-deploy to production
- PR → preview deploy → review → merge
- No staging environment (preview deploys ARE staging)

### Standard (Recommended for Production)
```
PR → lint + test + preview deploy
Merge to main → deploy to staging
Manual promote → deploy to production
```

### Enterprise
```
PR → lint + test + security scan + preview deploy
Merge to develop → deploy to staging
Release branch → deploy to pre-prod
Tag → deploy to production (with rollback plan)
```

## Environment Management

### Minimum Variables (every project)
```env
DATABASE_URL=             # Database connection string
NEXT_PUBLIC_APP_URL=      # Public app URL (for OG images, redirects)
```

### Common Variables by Service
```env
# Auth (Clerk)
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=

# Auth (Supabase)
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# Payments (Stripe)
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=

# Email (Resend)
RESEND_API_KEY=

# Search (Algolia)
NEXT_PUBLIC_ALGOLIA_APP_ID=
ALGOLIA_ADMIN_KEY=
```

### Rules
- NEVER commit `.env` files
- Use `.env.example` with placeholder values
- `NEXT_PUBLIC_` prefix for client-exposed vars in Next.js
- Validate all env vars at startup with Zod
