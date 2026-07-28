# Astro v7 Features

Complete reference for all major features introduced in Astro v7.

---

## 1. Vite 8 + Rolldown

Astro v7 ships with **Vite 8**, which replaces the previous esbuild + Rollup bundling pipeline with **Rolldown** — a Rust-based bundler.

### Key Points

- **Rust-based bundler** replacing both esbuild (transform) and Rollup (bundling) in a single tool
- **10-30x faster** than Rollup for production builds
- **Same plugin API** — fully backwards compatible with existing Vite/Rollup plugins
- **Compatibility layer** auto-converts `build.rollupOptions` and esbuild-specific options to their Rolldown equivalents

### Migration

No changes required for most projects. If you use `vite.build.rollupOptions` in `astro.config.mjs`, the compatibility layer handles the conversion automatically. Warnings are emitted for any options that cannot be directly mapped.

```js
// astro.config.mjs — works as before
import { defineConfig } from 'astro/config';

export default defineConfig({
  vite: {
    build: {
      // Automatically converted to Rolldown equivalents
      rollupOptions: {
        output: {
          manualChunks: { vendor: ['react', 'react-dom'] }
        }
      }
    }
  }
});
```

---

## 2. Rust Compiler

The Astro template compiler has been rewritten in **Rust**, replacing the previous Go-based compiler. Built on **oxc** (JavaScript/TypeScript parser) and **Lightning CSS**.

### Key Points

- **Native binaries** for all major platforms with **WASM fallback** for unsupported architectures
- **Strict parsing**: unclosed tags are now errors (no HTML auto-correction)
- **JSX whitespace rules**: newlines between inline elements produce no whitespace in output
- **CSS differences**: minor cosmetic changes to color serialization and `url()` quoting (output-only, no behavioral change)

### Breaking Changes

#### Strict HTML Parsing

```astro
<!-- ❌ Error in v7 — unclosed tag -->
<div>
  <p>Hello world
</div>

<!-- ✅ Correct -->
<div>
  <p>Hello world</p>
</div>
```

#### JSX Whitespace Rules

```astro
<!-- In v7, newline between inline elements = no space in output -->
<span>Hello</span>
<span>World</span>
<!-- Renders: "HelloWorld" -->

<!-- Add explicit space -->
<span>Hello</span>{' '}
<span>World</span>
<!-- Renders: "Hello World" -->
```

#### CSS Cosmetic Differences

```css
/* v6 output */
background: url(image.png);
color: #ff0000;

/* v7 output (functionally identical) */
background: url("image.png");
color: red;
```

---

## 3. Sätteri (Markdown/MDX in Rust)

**Sätteri** is Astro v7's default Markdown and MDX processor, replacing the unified/remark/rehype pipeline with a Rust-native implementation.

### Key Points

- Built on **pulldown-cmark** (Markdown parsing) + **oxc** (MDX/JSX)
- Default processor — no configuration needed for standard usage
- Replaces unified/remark/rehype with dramatically faster processing

### Built-in Features

| Feature | Description |
|---------|-------------|
| GFM | Tables, strikethrough, task lists, autolinks |
| Smart punctuation | Curly quotes, em/en dashes |
| Heading IDs | Auto-generated anchor IDs |
| Directives | Container/leaf/text directives (`::: note`, etc.) |
| Math | LaTeX math blocks (`$$...$$`) and inline (`$...$`) |
| Frontmatter | YAML frontmatter parsing |
| Superscript/Subscript | `^super^` and `~sub~` syntax |
| Wikilinks | `[[page]]` and `[[page|text]]` syntax |

### Configuration

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import { satteri } from '@astrojs/markdown-satteri';

export default defineConfig({
  markdown: {
    processor: satteri({
      gfm: true,
      smartPunctuation: true,
      headingIds: true,
      math: true,
      wikilinks: true,
      directives: true,
    })
  }
});
```

### Plugin API

Sätteri plugins declare which node types they handle, skipping all others. This is significantly cheaper than unified's visitor pattern.

```js
// my-satteri-plugin.js
export default function myPlugin() {
  return {
    name: 'my-plugin',
    nodes: ['heading', 'paragraph'], // only visit these types
    transform(node, context) {
      if (node.type === 'heading') {
        // transform heading nodes
      }
    }
  };
}
```

### Fallback to unified/remark/rehype

For projects relying on existing remark/rehype plugins:

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import remarkToc from 'remark-toc';
import rehypePrism from 'rehype-prism';

export default defineConfig({
  markdown: {
    processor: unified({
      remarkPlugins: [remarkToc],
      rehypePlugins: [rehypePrism],
    })
  }
});
```

### Docker Deployment Note

Sätteri ships native bindings only for **glibc** (`@bruits/satteri-linux-x64-gnu`). Alpine Linux uses musl — there is no musl binding. Docker build stages MUST use `node:22-slim` (Debian/glibc), not `node:22-alpine`. This affects all Astro v7 projects using Sätteri (the default), including Starlight sites.

Projects using `unified()` explicitly are NOT affected (they bypass Sätteri entirely).

---

## 4. Queued Rendering

Astro v7's rendering engine uses a **queue/stack-based** approach instead of recursive rendering.

### Key Points

- **~2.4x faster** for expression-dense pages (many dynamic expressions, loops, conditionals)
- **Now stable and default** — no configuration needed
- Eliminates deep call-stack issues on complex component trees
- Reduces memory pressure through iterative processing

### Migration

No action required. This is an internal engine change that is fully transparent to user code.

---

## 5. Advanced Routing (`src/fetch.ts`)

Astro v7 introduces a **standard fetch handler pattern** for advanced routing control, following the same conventions as Cloudflare Workers, Deno, and Bun.

### Key Points

- Define a `src/fetch.ts` file to take full control of the request pipeline
- Compose individual pieces: `i18n()`, `actions()`, `middleware()`, `pages()`
- Full control over request pipeline order
- Compatible with Hono for complex routing scenarios

### Basic Routing

```ts
// src/fetch.ts
import { astro, FetchState } from 'astro/fetch';

export default astro((request: Request, state: FetchState) => {
  // Compose the pipeline in your preferred order
  return state.pipeline(
    i18n(),
    middleware(),
    actions(),
    pages()
  );
});
```

### Hono Integration

```ts
// src/fetch.ts
import { astro } from 'astro/hono';
import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';

const app = new Hono();

app.use('*', logger());
app.use('/api/*', cors());

app.get('/api/health', (c) => c.json({ status: 'ok' }));

// Hand off to Astro for everything else
export default astro(app);
```

### Composing Middleware

```ts
// src/fetch.ts
import { astro, FetchState } from 'astro/fetch';
import { i18n, actions, middleware, pages } from 'astro/fetch';

export default astro((request: Request, state: FetchState) => {
  const url = new URL(request.url);

  // Custom routing logic
  if (url.pathname.startsWith('/api/')) {
    return state.pipeline(
      actions()
    );
  }

  // Full pipeline for pages
  return state.pipeline(
    i18n(),
    middleware(),
    actions(),
    pages()
  );
});
```

---

## 6. Route Caching (Stable)

Route-level caching is now **stable** in Astro v7, providing fine-grained control over page caching with tag-based invalidation.

### Key Points

- In-memory cache available out of the box
- Per-page caching with `Astro.cache.set()`
- Declarative `routeRules` in config
- Tag-based invalidation
- Integration with live content collections

### Config-Level Setup

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import { memoryCache } from 'astro/config';

export default defineConfig({
  cache: memoryCache(),
  routeRules: {
    '/blog/**': { cache: { maxAge: 3600, swr: 86400, tags: ['blog'] } },
    '/products/**': { cache: { maxAge: 600, tags: ['products'] } },
    '/about': { cache: { maxAge: 86400 } },
  }
});
```

### Per-Page Caching

```astro
---
// src/pages/blog/[slug].astro
const { slug } = Astro.params;
const post = await getEntry('blog', slug);

Astro.cache.set({
  maxAge: 3600,       // 1 hour
  swr: 86400,         // stale-while-revalidate: 24 hours
  tags: ['blog', `post:${slug}`]
});
---

<article>
  <h1>{post.data.title}</h1>
  <Content />
</article>
```

### Webhook Invalidation

```ts
// src/pages/api/revalidate.ts
import type { APIRoute } from 'astro';
import { cache } from 'astro:cache';

export const POST: APIRoute = async ({ request }) => {
  const { secret, tags, path } = await request.json();

  if (secret !== import.meta.env.REVALIDATION_SECRET) {
    return new Response('Unauthorized', { status: 401 });
  }

  // Invalidate by tags
  if (tags) {
    await cache.invalidate({ tags });
  }

  // Invalidate by path
  if (path) {
    await cache.invalidate({ path });
  }

  return new Response(JSON.stringify({ revalidated: true }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
};
```

### Live Content Collections Integration

```js
// astro.config.mjs
import { defineConfig } from 'astro/config';
import { memoryCache } from 'astro/config';

export default defineConfig({
  cache: memoryCache(),
  content: {
    collections: {
      blog: {
        // When content changes, invalidate matching cache tags
        onUpdate: (entry) => cache.invalidate({ tags: ['blog', `post:${entry.slug}`] })
      }
    }
  }
});
```

---

## 7. CDN Cache Providers (Experimental)

CDN-level cache providers push cache directives to the edge, allowing cached responses to be served **without invoking the server**.

### Key Points

- Edge-level caching — hits never reach your application server
- Platform-specific providers for Netlify, Vercel, and Cloudflare
- Works with the same `routeRules` and `Astro.cache.set()` API

### Providers

```js
// Netlify
import { cacheNetlify } from '@astrojs/netlify/cache';

export default defineConfig({
  cache: cacheNetlify(),
});
```

```js
// Vercel
import { cacheVercel } from '@astrojs/vercel/cache';

export default defineConfig({
  cache: cacheVercel(),
});
```

```js
// Cloudflare (private beta)
import { cacheCloudflare } from '@astrojs/cloudflare/cache';

export default defineConfig({
  cache: cacheCloudflare(),
});
```

### How It Works

1. On first request: server renders the page, cache provider stores response at the edge
2. On subsequent requests: CDN serves cached response directly (no server invocation)
3. On invalidation: cache is purged via provider API, next request triggers fresh render

---

## 8. AI Enhancements

Astro v7 includes first-class support for AI-assisted development workflows.

### Key Points

- **Background dev server**: auto-detects when running inside AI agents and optimizes output
- **JSON logging**: configurable, composable log output for machine consumption
- See `ai-dev-server.md` for full details

### Background Dev Server

When Astro detects it's running inside an AI agent environment, it automatically:

- Switches to structured JSON log output
- Suppresses interactive UI elements (progress bars, spinners)
- Provides machine-readable error messages with file/line references
- Exposes a lightweight status API for agent polling

### JSON Logging

```js
// astro.config.mjs
export default defineConfig({
  devToolbar: { enabled: false },
  logging: {
    format: 'json', // 'pretty' | 'json' | 'minimal'
    level: 'info',
  }
});
```

---

## 9. Performance Benchmarks

Real-world build time improvements measured on production sites (Astro v6 → v7):

| Site | v6 | v7 | Improvement |
|------|----|----|-------------|
| docs.astro.build | 114s | 73s | **36% faster** |
| astro.build | 62s | 24s | **61% faster** |
| biomejs.dev | 176s | 150s | **15% faster** |
| developers.cloudflare.com | 387s | 262s | **32% faster** |

### Contributing Factors

- **Rolldown bundler**: 10-30x faster than Rollup for the bundling phase
- **Rust compiler**: eliminates Go→WASM overhead, native binary execution
- **Sätteri**: Markdown/MDX processing in Rust vs. JavaScript-based unified pipeline
- **Queued rendering**: 2.4x faster for expression-dense templates

### Impact by Project Size

- Small sites (< 100 pages): 15-25% faster builds
- Medium sites (100-1000 pages): 30-45% faster builds
- Large sites (1000+ pages): 40-60% faster builds

The largest gains are seen in content-heavy sites with extensive Markdown processing and complex component trees.
