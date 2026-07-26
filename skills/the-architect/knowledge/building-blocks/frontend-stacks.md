# Building Block: Frontend Stacks

## Decision Matrix

| Framework | Best For | Rendering | Learning Curve | Ecosystem |
|-----------|----------|-----------|---------------|-----------|
| **Next.js 15** | Full-stack web apps, SaaS | SSR, SSG, ISR, Client | Medium | Largest |
| **Astro 5** | Content sites, marketing | Static + islands | Low | Growing |
| **Nuxt 4** | Vue ecosystem | SSR, SSG, ISR | Medium | Large (Vue) |
| **SvelteKit** | Performance-critical, DX | SSR, SSG | Low | Smaller |
| **Remix** | Data-heavy web apps | SSR | Medium | Growing |
| **Vite + React** | SPAs, internal tools | Client only | Low | Large |

## Recommendation

| Project Type | Framework | Why |
|-------------|-----------|-----|
| SaaS / Web App | **Next.js 15** | Full-stack, Vercel deploy, largest ecosystem |
| Marketing / Landing | **Astro 5** | Zero JS default, fastest performance |
| Blog / Docs | **Astro 5** | Content collections, MDX, fast |
| Internal Dashboard | **Next.js 15** | Server Components for data, shadcn/ui |
| E-commerce | **Next.js 15** | SEO, performance, Stripe integration |
| Portfolio | **Astro 5** | Simple, fast, low maintenance |

## Component Libraries

| Library | Style | Best For | Works With |
|---------|-------|----------|------------|
| **shadcn/ui** | Radix + Tailwind, copy-paste | Any React project | Next.js, Remix, Vite |
| **Radix UI** | Unstyled primitives | Custom design systems | Any React |
| **Tremor** | Dashboard-focused | Data visualization, admin | Next.js, React |
| **Headless UI** | Unstyled, Tailwind-friendly | Custom components | React, Vue |
| **DaisyUI** | Tailwind plugin, themed | Fast prototyping | Any Tailwind project |
| **Ark UI** | Headless, framework-agnostic | Multi-framework | React, Vue, Solid |

## Rendering Strategies

### Server Components (Default in Next.js 15)
- Fetch data directly in the component (no API call)
- Zero client-side JavaScript
- Use for: pages, layouts, data display
- Cannot use: onClick, useState, useEffect, browser APIs

### Client Components ("use client")
- Use for: interactivity, forms, real-time, browser APIs
- Keep them small and leaf-level
- Wrap only the interactive part, not the whole page

### Static Generation (SSG)
- Pre-built at build time
- Use for: marketing pages, blog posts, docs
- Fastest possible load time

### Incremental Static Regeneration (ISR)
- Static + revalidation after N seconds
- Use for: content that changes occasionally (blog, product pages)
- `revalidate: 3600` (refresh every hour)

### Server-Side Rendering (SSR)
- Rendered on every request
- Use for: personalized pages, real-time data, search results
- `dynamic = 'force-dynamic'`

## Key Patterns for Next.js 15

### File Structure Convention
```
app/
  (group)/           # Route group (no URL segment)
  @modal/            # Parallel route (for modals)
  loading.tsx        # Loading UI (Suspense boundary)
  error.tsx          # Error UI (Error boundary)
  not-found.tsx      # 404 UI
  layout.tsx         # Shared layout
  page.tsx           # Page component
```

### Data Fetching
```typescript
// Server Component — direct fetch
async function Page() {
  const data = await db.query.posts.findMany()
  return <PostList posts={data} />
}

// Client Component — TanStack Query or SWR
'use client'
function PostList() {
  const { data } = useQuery({ queryKey: ['posts'], queryFn: fetchPosts })
  return ...
}
```

### Forms
```typescript
// Server Action (recommended for Next.js)
async function createPost(formData: FormData) {
  'use server'
  // validate, insert, revalidatePath
}

// Client-side with React Hook Form + Zod
'use client'
const form = useForm({ resolver: zodResolver(schema) })
```
