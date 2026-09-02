# SEO y rendimiento del sitio

**Actualizado:** 2026-09-02

## Alcance

Revisión estática de las páginas principales:

- `index.html` / `web/skills-site.html`: catálogo público.
- `web/qualifier.html`: selector de skills.
- `docs/index.html`: copia documental del sitio.

## Cambios aplicados

- Metadatos `title`, `description`, `robots` y canonical en las páginas indexables.
- Open Graph y Twitter Card en la página principal y qualifier.
- JSON-LD `WebApplication` en el catálogo principal.
- Enlace explícito al sitemap desde cada página pública.
- Preconnect y carga no bloqueante de Google Fonts con fallback `noscript`.
- `lang` correcto (`en` para catálogo y `es` para qualifier).
- Un único `h1` por página revisada.
- Estados `:focus-visible` para teclado y soporte de `prefers-reduced-motion`.
- Corrección de variables CSS faltantes en qualifier (`--border-card`, `--text-muted`, `--accent-cyan`).

## Validación realizada

- Parseo HTML con `html.parser`: correcto en `index.html`, `web/skills-site.html` y `web/qualifier.html`.
- Cada página revisada contiene un único `<title>`, una descripción y un `<h1>`.
- `git diff --check`: sin errores de whitespace.

## Pendientes

- Ejecutar Lighthouse desde Chrome contra el sitio servido para obtener métricas reales de LCP, INP, CLS y accesibilidad.
- Regenerar las variantes minificadas (`index.min.html`, `web/skills-site.min.html`) cuando corresponda; no deben editarse manualmente sin conservar la fuente HTML.
- Verificar en producción que `/qualifier.html`, `/manifest.json`, iconos y `/sitemap.xml` devuelvan `200`.
