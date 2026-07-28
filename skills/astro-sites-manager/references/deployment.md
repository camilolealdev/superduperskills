# Deployment Guide

> Astro 7 deployment across all major platforms. Covers adapters, route caching, and platform-specific gotchas.

---

## 1. General Build

```bash
astro build    # output in dist/
astro preview  # test production build locally
```

Key config in `astro.config.mjs`:

```js
import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://example.com',
  base: '/',
  trailingSlash: 'never', // 'always' | 'never' | 'ignore'
});
```

- `site` — full production URL (required for sitemaps, canonical URLs, RSS)
- `base` — subpath when deploying to a subdirectory (e.g., `/docs`)
- `trailingSlash` — MUST match hosting platform expectations to avoid redirect loops

---

## 2. Cloudflare Pages

**Adapter:** `@astrojs/cloudflare`

```bash
npx astro add cloudflare
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

export default defineConfig({
  output: 'server',
  adapter: cloudflare(),
});
```

**Route Caching (private beta):**

```js
// astro.config.mjs
import { cacheCloudflare } from '@astrojs/cloudflare/cache';

export default defineConfig({
  output: 'server',
  adapter: cloudflare(),
  experimental: {
    serverIslands: true,
  },
  routeCache: cacheCloudflare(),
});
```

**Deploy:**
- Connect git repo in Cloudflare Dashboard → Pages → Create a project
- Build command: `astro build`
- Build output directory: `dist`
- Node.js compatibility flag is set automatically by the adapter

---

## 3. Vercel

**Adapter:** `@astrojs/vercel`

```bash
npx astro add vercel
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import vercel from '@astrojs/vercel';
import { cacheVercel } from '@astrojs/vercel/cache';

export default defineConfig({
  output: 'server',
  adapter: vercel(),
  routeCache: cacheVercel(),
});
```

**ISR via routeRules:**

```js
// astro.config.mjs
export default defineConfig({
  output: 'server',
  adapter: vercel({
    isr: true, // enable ISR globally
  }),
  routeCache: cacheVercel({
    routeRules: {
      '/blog/**': { revalidate: 60 },   // revalidate every 60s
      '/static/**': { prerender: true }, // fully static at build
    },
  }),
});
```

**Deploy:**
- Connect repo via Vercel Dashboard or `vercel` CLI
- Framework preset: Astro (auto-detected)

---

## 4. Netlify

**Adapter:** `@astrojs/netlify`

```bash
npx astro add netlify
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import netlify from '@astrojs/netlify';
import { cacheNetlify } from '@astrojs/netlify/cache';

export default defineConfig({
  output: 'server',
  adapter: netlify(),
  routeCache: cacheNetlify(),
});
```

**Deploy:**
- Connect repo in Netlify Dashboard
- Build command: `astro build`
- Publish directory: `dist`
- Functions auto-detected from adapter output

---

## 5. Firebase Hosting

**Static only** — no adapter needed for SSG output.

```js
// astro.config.mjs
export default defineConfig({
  output: 'static',
  trailingSlash: 'never', // CRITICAL: must match Firebase config
});
```

**firebase.json:**

```json
{
  "hosting": {
    "public": "dist",
    "ignore": ["firebase.json", "**/.*", "**/node_modules/**"],
    "trailingSlash": false,
    "rewrites": [
      { "source": "**", "destination": "/404.html" }
    ]
  }
}
```

**Deploy:**

```bash
astro build
firebase deploy --only hosting
```

### CRITICAL: trailingSlash Alignment

Mismatch between Firebase and Astro causes **infinite redirect loops**.

| Firebase `trailingSlash` | Astro `trailingSlash` | Result |
|---|---|---|
| `false` | `'never'` | ✅ Works |
| `true` | `'always'` | ✅ Works |
| `false` | `'always'` | ❌ Redirect loop |
| `true` | `'never'` | ❌ Redirect loop |

---

## 6. GitHub Pages

**Static output only** — no adapter needed.

```js
// astro.config.mjs
export default defineConfig({
  site: 'https://username.github.io',
  base: '/repo-name', // omit for username.github.io root
  output: 'static',
});
```

**GitHub Actions workflow** (`.github/workflows/deploy.yml`):

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: dist

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - id: deployment
        uses: actions/deploy-pages@v4
```

---

## 7. Docker / Self-Hosted (Coolify)

**Adapter:** `@astrojs/node`

```bash
npx astro add node
```

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import node from '@astrojs/node';

export default defineConfig({
  output: 'server',
  adapter: node({
    mode: 'standalone',
  }),
  server: {
    host: '0.0.0.0', // REQUIRED for Docker
    port: 4321,
  },
});
```

**Dockerfile:**

```dockerfile
FROM node:22-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:22-alpine AS runtime
WORKDIR /app
COPY --from=build /app/dist ./dist
COPY --from=build /app/node_modules ./node_modules
COPY --from=build /app/package.json ./
ENV HOST=0.0.0.0
ENV PORT=4321
EXPOSE 4321
HEALTHCHECK --interval=30s --timeout=3s CMD wget -qO- http://localhost:4321/api/health || exit 1
CMD ["node", "./dist/server/entry.mjs"]
```

**Health check endpoint** (`src/pages/api/health.ts`):

```ts
import type { APIRoute } from 'astro';

export const GET: APIRoute = () => {
  return new Response(JSON.stringify({ status: 'ok' }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' },
  });
};
```

**Coolify:** Set Dockerfile build pack, expose port 4321, configure health check to `/api/health`.

---

## 8. Azure Static Web Apps

Works with **static output** (SSG). For SSR, use Azure Functions integration.

**GitHub Actions workflow** (`.github/workflows/azure-swa.yml`):

```yaml
name: Azure Static Web Apps

on:
  push:
    branches: [main]

jobs:
  build_and_deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
          cache: npm
      - run: npm ci
      - run: npm run build
      - uses: Azure/static-web-apps-deploy@v1
        with:
          azure_static_web_apps_api_token: ${{ secrets.AZURE_SWA_TOKEN }}
          repo_token: ${{ secrets.GITHUB_TOKEN }}
          action: upload
          app_location: /
          output_location: dist
          skip_app_build: true
```

The `skip_app_build: true` pattern means we build ourselves (for control over Node version and env vars) and only upload the output.

**staticwebapp.config.json:**

```json
{
  "navigationFallback": {
    "rewrite": "/404.html"
  },
  "globalHeaders": {
    "X-Frame-Options": "DENY",
    "X-Content-Type-Options": "nosniff"
  },
  "routes": [
    {
      "route": "/api/*",
      "allowedRoles": ["authenticated"]
    }
  ]
}
```

For **private registry auth** (private npm packages):

```yaml
      - run: |
          echo "//npm.pkg.github.com/:_authToken=${{ secrets.NPM_TOKEN }}" >> .npmrc
      - run: npm ci
```

---

## 9. Pre-Deploy Checklist

- [ ] `astro build` exits 0
- [ ] `astro check` reports no errors
- [ ] `astro preview` works correctly (test production build locally)
- [ ] Images use `<Image/>` component or are in `public/`
- [ ] SEO metadata present on all pages (title, description, og tags)
- [ ] `src/pages/404.astro` exists
- [ ] Environment variables set on target platform
- [ ] `trailingSlash` matches hosting platform expectations
- [ ] Sitemap generating correctly (`@astrojs/sitemap`)
- [ ] RSS feed working if applicable (`@astrojs/rss`)
- [ ] Route caching configured for SSR pages (platform-specific cache helper)
- [ ] `robots.txt` present and correct
- [ ] HTTPS redirect configured on platform
- [ ] Custom domain DNS configured and propagated
