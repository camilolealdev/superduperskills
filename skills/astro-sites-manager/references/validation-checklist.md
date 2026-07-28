# Validation Checklist

Complete checklist for validating an Astro installation/upgrade. Run these checks in the project root.

---

## 1. Build Validation

```bash
# Full production build — must exit 0 with no errors
npx astro build

# Type checking (requires @astrojs/check)
npx astro check

# Verify no unclosed tags (Rust compiler is strict about this)
find src -name "*.astro" -exec grep -Pn '<(img|br|hr|input|meta|link|source|area|base|col|embed|param|track|wbr)[^/]*[^/]>' {} +

# Check for HTML nesting issues (div/section/article inside p)
grep -rPn '<p[^>]*>[\s\S]*?<(div|section|article|ul|ol|table|blockquote|h[1-6])' src/**/*.astro
```

**Expected:** All commands pass with no errors or matches.

---

## 2. Breaking Pattern Detection

### Unclosed HTML tags

```bash
# Find self-closing tags that are NOT void elements (common breakage)
grep -rPn '<(div|span|p|a|section|main|footer|header|nav|ul|li)\s[^>]*/>' src/ --include="*.astro"
```

### Block elements inside `<p>`

```bash
grep -rPn '<p[^>]*>[\s\S]*?<(div|section|article|ul|ol|dl|table|blockquote|pre|h[1-6]|form|fieldset|hr)' src/ --include="*.astro"
```

### Whitespace-dependent inline layouts

```bash
# Look for adjacent inline elements that rely on whitespace rendering
grep -rPn '</(span|a|strong|em|code)>\s*<(span|a|strong|em|code)' src/ --include="*.astro"
```

### src/fetch.ts conflict

```bash
# Astro reserves src/fetch.ts — check if it exists
find src -maxdepth 1 -name "fetch.ts" -o -name "fetch.js"
```

### @astrojs/db usage (removed in Astro 5+)

```bash
grep -rn "@astrojs/db" package.json src/ --include="*.{ts,js,astro}"
```

### Deprecated transition imports

```bash
# TRANSITION_* named exports removed
grep -rPn 'TRANSITION_[A-Z_]+' src/ --include="*.{ts,js,astro}"

# isTransition*() helpers removed
grep -rPn 'isTransition\w+\(' src/ --include="*.{ts,js,astro}"
```

### getContainerRenderer() from package root

```bash
# Must now import from /container subpath
grep -rn "getContainerRenderer" src/ --include="*.{ts,js}" | grep -v "/container"
```

### Experimental flags that should be removed

```bash
# Check astro.config for experimental flags that graduated to stable
grep -A 20 'experimental:' astro.config.{mjs,ts,js} 2>/dev/null | grep -P '(contentLayer|serverIslands|actions|env|fonts|responsiveImages|svg)'
```

---

## 3. Deprecated Pattern Detection

| Pattern | grep command | Fix |
|---------|-------------|-----|
| `Astro.glob()` | `grep -rn "Astro.glob" src/ --include="*.astro"` | Replace with `import.meta.glob()` or Content Collections |
| `Astro.fetchContent()` | `grep -rn "Astro.fetchContent" src/ --include="*.astro"` | Replace with Content Collections |
| `getStaticPaths` without `paginate` import | `grep -rn "getStaticPaths" src/ --include="*.astro"` | Verify using new pagination API |
| Legacy content collections (`src/content/config.ts` with `defineCollection` using `schema` only) | `grep -rn "defineCollection" src/content/config.ts` | Migrate to `type: 'content_layer'` or new loader API |
| `@astrojs/image` | `grep -rn "@astrojs/image" package.json` | Use built-in `astro:assets` |
| `integrations: [image()]` | `grep -rn "image()" astro.config.*` | Remove — use built-in `<Image>` component |
| `<Markdown>` component | `grep -rn "<Markdown" src/ --include="*.astro"` | Use MDX or Content Collections |
| `set:html` on component | `grep -rPn 'set:html' src/ --include="*.astro"` | Verify it's on HTML elements only |
| `class:list` with nested arrays | `grep -rPn 'class:list=\{.*\[.*\[' src/ --include="*.astro"` | Flatten to single array |

---

## 4. Markdown/MDX Validation

### Remark/Rehype plugin migration

```bash
# Check if custom remark/rehype plugins are configured
grep -Pn '(remarkPlugins|rehypePlugins)' astro.config.{mjs,ts,js} 2>/dev/null

# If found, verify @astrojs/markdown-remark is installed
grep -n "@astrojs/markdown-remark" package.json
```

**Fix:** If custom plugins exist but `@astrojs/markdown-remark` is missing:
```bash
npx astro add @astrojs/markdown-remark
```

### Shiki (syntax highlighting) compatibility

```bash
# Check for custom Shiki config — API may have changed
grep -A 10 'shikiConfig' astro.config.{mjs,ts,js} 2>/dev/null
```

### GFM features (tables, strikethrough, autolinks)

```bash
# GFM is built-in — check there's no redundant remark-gfm
grep -rn "remark-gfm" package.json astro.config.{mjs,ts,js} 2>/dev/null
```

**Fix:** Remove `remark-gfm` from plugins — GFM is included by default.

### Test MDX rendering

```bash
# Verify MDX integration is present if .mdx files exist
find src -name "*.mdx" | head -1 && grep -n "@astrojs/mdx" package.json
```

---

## 5. Performance Validation

### Compare build times

```bash
# Time the build (run before and after upgrade)
time npx astro build 2>&1 | tail -5
```

### Verify queued rendering is active

```bash
# Queued rendering should be default in Astro 5+ — check it's not disabled
grep -n "queuedRendering" astro.config.{mjs,ts,js} 2>/dev/null
```

**Expected:** No results (uses default) or `true`. If set to `false`, remove it.

### Check Vite 6+ bundle output

```bash
# Verify build output structure
ls -la dist/ 2>/dev/null || ls -la dist/_astro/ 2>/dev/null

# Check chunk sizes
find dist -name "*.js" -exec wc -c {} + | sort -n | tail -10

# Verify no duplicate framework chunks
find dist -name "*.js" | xargs grep -l "react" 2>/dev/null | wc -l
```

### Verify no dev-only code in production build

```bash
grep -rn "import.meta.env.DEV" dist/ 2>/dev/null
```

---

## Quick Full Validation Script

```bash
#!/usr/bin/env bash
set -e
echo "=== Astro Validation ==="

echo "[1/5] Build..."
npx astro build

echo "[2/5] Type check..."
npx astro check || echo "WARN: astro check failed"

echo "[3/5] Breaking patterns..."
grep -rn "@astrojs/db" src/ --include="*.{ts,js,astro}" && echo "FAIL: @astrojs/db found" || true
grep -rPn 'TRANSITION_[A-Z_]+' src/ --include="*.{ts,js,astro}" && echo "FAIL: deprecated transitions" || true
find src -maxdepth 1 -name "fetch.ts" -o -name "fetch.js" | grep . && echo "FAIL: src/fetch conflict" || true

echo "[4/5] Deprecated APIs..."
grep -rn "Astro.glob\|Astro.fetchContent\|@astrojs/image" src/ package.json && echo "FAIL: deprecated APIs" || true

echo "[5/5] Performance..."
time npx astro build 2>&1 | tail -3

echo "=== Done ==="
```
