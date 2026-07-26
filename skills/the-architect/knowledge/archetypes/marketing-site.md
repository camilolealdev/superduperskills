# Archetype: Marketing / Landing Page Site

## Default Stack Recommendation

| Layer | Default | Alternative | When to Switch |
|-------|---------|-------------|----------------|
| Framework | Astro 5 | Next.js 15 | Need heavy interactivity or existing Next.js ecosystem |
| Language | TypeScript | — | Always |
| Styling | Tailwind CSS v4 | — | Always Tailwind for marketing sites |
| Components | Astro components + React islands | shadcn/ui + Next.js | Choosing Next.js path |
| CMS | Sanity | Contentful, MDX files | Contentful for enterprise, MDX for dev-managed content |
| Forms | Resend + React Hook Form | Formspree, Mailchimp | No backend needed → Formspree |
| Analytics | Plausible | Vercel Analytics, GA4 | Privacy-first → Plausible, free → Vercel Analytics |
| Hosting | Vercel | Netlify, Cloudflare Pages | Netlify for form handling, CF for edge performance |
| Package Manager | pnpm | npm | Simplicity |

## Default Directory Structure

```
src/
  pages/
    index.astro               # Landing page
    about.astro               # About page
    pricing.astro             # Pricing page
    contact.astro             # Contact form
    blog/
      index.astro             # Blog listing
      [slug].astro            # Blog post page
    404.astro                 # Custom 404
  components/
    layout/
      Header.astro            # Navigation bar
      Footer.astro            # Footer
      BaseLayout.astro        # HTML wrapper (head, meta, fonts)
    sections/
      Hero.astro              # Hero section
      Features.astro          # Features grid
      Testimonials.astro      # Social proof
      CTA.astro               # Call-to-action section
      Pricing.astro           # Pricing cards
      FAQ.astro               # FAQ accordion
    ui/
      Button.astro            # Button variants
      Card.astro              # Card component
      Badge.astro             # Badge/tag
    forms/
      ContactForm.tsx         # React island — interactive form
      NewsletterForm.tsx      # React island — email signup
  content/
    blog/                     # MDX or Sanity content
  styles/
    globals.css               # Tailwind base + custom properties
  lib/
    sanity.ts                 # CMS client (if using Sanity)
    resend.ts                 # Email sending
public/
  fonts/                      # Self-hosted fonts
  images/                     # Optimized images
  og-image.png                # Default OG image
  favicon.svg
```

## Common Patterns

### Performance First
- Static generation by default (Astro = zero JS unless opted in)
- React islands ONLY for interactive components (forms, animations)
- Self-host fonts (no Google Fonts flash)
- Optimize all images (Astro `<Image>` component)

### SEO
- Proper `<head>` metadata on every page (title, description, OG, canonical)
- Sitemap via `@astrojs/sitemap`
- JSON-LD structured data for organization and articles
- Clean URL structure, no trailing slashes

### Lead Capture
- Forms submit to API endpoint → Resend email + optional CRM webhook
- Success/error states with clear messaging
- Honeypot field for spam prevention (no CAPTCHA for UX)

## Build Order

1. **Scaffolding**: `npm create astro@latest`, install Tailwind, configure base layout
2. **Design system**: Colors, fonts, spacing — set CSS custom properties
3. **Layout**: Header (nav) + Footer + BaseLayout wrapper
4. **Landing page**: Hero → Features → Social proof → CTA — section by section
5. **Inner pages**: About, Pricing (if applicable)
6. **Contact form**: React island with validation, API endpoint for email
7. **Blog** (if needed): Content collection setup, listing page, post template
8. **SEO**: Metadata, sitemap, OG images, structured data
9. **Testing**: E2E smoke test — all pages load, forms submit, links work (Playwright)
10. **Performance**: Lighthouse audit, image optimization, font optimization
11. **Deploy**: Vercel/Netlify, custom domain, analytics

## Common Pitfalls

- **Don't use a SPA framework for a marketing site.** Astro or static Next.js. JS overhead kills performance.
- **Don't skip mobile.** Design mobile-first. Marketing sites get 50%+ mobile traffic.
- **Don't use stock photography without processing.** Compress, resize, use modern formats (WebP/AVIF).
- **Don't forget OG images.** Every shared link needs a good preview.

## Skills for Build Phase

| Skill | When |
|-------|------|
| `/frontend-design` | Every section of the landing page |
| `/ui-ux-pro-max` | Design system, color palette, typography |
| `/seo-audit` | After site is built — full audit |
| `/humanizer` | If writing marketing copy |

## See Also

- `knowledge/building-blocks/frontend-stacks.md` — Astro vs Next.js for static sites
- `knowledge/building-blocks/deployment-patterns.md` — Vercel, Netlify, Cloudflare Pages comparison
- `knowledge/building-blocks/styling-systems.md` — Tailwind v4 setup, typography system
- `knowledge/building-blocks/testing-patterns.md` — E2E smoke tests for marketing sites
