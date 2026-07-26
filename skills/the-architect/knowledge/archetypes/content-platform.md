# Archetype: Content Platform / CMS

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Framework | Next.js 15 (App Router) | Astro 5 | No interactivity needed, pure content |
| Language | TypeScript | — | Always |
| Styling | Tailwind CSS v4 | — | Always |
| Components | shadcn/ui | Custom | — |
| CMS | Sanity Studio | Contentful, Keystatic, MDX | Contentful for enterprise, Keystatic for git-based, MDX for dev-managed |
| Search | Algolia | Meilisearch (self-hosted) | Meilisearch if budget-constrained |
| Database | Supabase (Postgres) | — | For user data, comments, analytics |
| Auth | Clerk | NextAuth | Clerk for social features, NextAuth for basic |
| CDN/Media | Cloudinary | Uploadthing, Supabase Storage | Uploadthing for simplicity |
| Hosting | Vercel | — | Default for Next.js |
| Package Manager | pnpm | npm | — |

## Default Directory Structure

```
src/
  app/
    page.tsx                    # Homepage — featured/latest content
    [category]/
      page.tsx                  # Category listing with filters
    [category]/[slug]/
      page.tsx                  # Content detail page
    authors/
      [id]/page.tsx             # Author profile + their content
    search/page.tsx             # Search results page
    (auth)/
      login/page.tsx            # Login (if user accounts)
      register/page.tsx
    (dashboard)/                # Creator dashboard (if UGC)
      my-content/page.tsx
      new/page.tsx
      edit/[id]/page.tsx
    api/
      search/route.ts           # Search endpoint
      content/route.ts          # Content CRUD (if UGC)
      comments/route.ts         # Comments API
    layout.tsx
  components/
    ui/                         # shadcn/ui primitives
    content/
      ContentCard.tsx           # Card for content listings
      ContentBody.tsx           # Rich content renderer (MDX/portable text)
      TableOfContents.tsx       # Auto-generated TOC
      ShareButtons.tsx          # Social sharing
    layout/
      Header.tsx                # Global nav
      Footer.tsx                # Footer
      Sidebar.tsx               # Category nav / related content
    social/
      CommentSection.tsx        # Comments (if enabled)
      AuthorBio.tsx             # Author card
      LikeButton.tsx            # Like/save interaction
  lib/
    sanity/
      client.ts                 # Sanity client
      queries.ts                # GROQ queries
      schemas/                  # Sanity schema definitions
    search.ts                   # Search client (Algolia/Meilisearch)
    mdx.ts                      # MDX processing (if using MDX)
    utils.ts
  types/
    content.ts                  # Content types
    index.ts
sanity/                         # Sanity Studio config (if using Sanity)
  schemas/
  sanity.config.ts
```

## Common Patterns

### Content Rendering
- Sanity → Portable Text renderer with custom components
- MDX → Next.js MDX with custom components
- Support: code blocks with syntax highlighting, images with captions, embeds, callouts

### SEO (Critical for Content)
- Dynamic metadata per content page (title, description, OG image)
- JSON-LD article schema
- Sitemap with all content URLs
- RSS feed
- Canonical URLs

### Search
- Algolia: index content on publish, InstantSearch React components
- Meilisearch: self-hosted, similar API, no usage limits

### User-Generated Content (if applicable)
- Markdown editor (Tiptap or MDXEditor)
- Draft → Review → Published workflow
- Content moderation (manual or automated)

## Build Order

1. **Scaffolding**: Next.js, Tailwind, shadcn/ui
2. **CMS setup**: Sanity project + schemas, or MDX content collection
3. **Content model**: Define content types (articles, categories, authors)
4. **Layout**: Header, footer, content page layout
5. **Homepage**: Featured content grid, latest content feed
6. **Content page**: Full article view with TOC, author bio, share buttons
7. **Category pages**: Listing with filters, pagination
8. **Search**: Algolia/Meilisearch integration, search page
9. **SEO**: Metadata, sitemap, RSS, JSON-LD, OG images
10. **Testing**: E2E smoke tests for content rendering, search, and navigation (Playwright)
11. **Social features** (if scope includes them): Comments, likes, bookmarks
12. **Creator dashboard** (if scope includes UGC): Content editor, my content, drafts
13. **Deploy**: Vercel, CDN config, analytics

## Common Pitfalls

- **Don't render markdown on the client.** Server-render all content for SEO and performance.
- **Don't skip content caching.** Use ISR (Incremental Static Regeneration) for content pages.
- **Don't forget image optimization.** Use Next.js `<Image>` or Cloudinary transforms.
- **Don't build search from scratch.** Use Algolia or Meilisearch. Full-text search in Postgres is a trap at scale.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/frontend-design` | Content pages, homepage layout |
| `/seo-audit` | After content pages are built |
| `/ui-ux-pro-max` | Typography and reading experience design |
| `/humanizer` | If writing sample/seed content |

## See Also

- `knowledge/building-blocks/frontend-stacks.md` — Next.js vs Astro for content sites
- `knowledge/building-blocks/database-patterns.md` — Full-text search, content schema design
- `knowledge/building-blocks/deployment-patterns.md` — CDN, ISR configuration
- `knowledge/building-blocks/testing-patterns.md` — E2E smoke tests for content rendering
