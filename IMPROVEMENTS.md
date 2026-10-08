# IMPROVEMENTS — Mejoras pendientes para ejecutar en el futuro

> Última actualización: 2026-10-07 (post integración de vercel-labs/skills, NVIDIA/skillspector,
> emilkowalski/skills y Hainrixz/all-deploy).
> Estado de partida: 3,330 skills · audit 24/24 PASSED · doctor all PASS · SKILLS-INDEX.md
> regenerado en modo reproducible.

## Cómo ejecutar una mejora

1. Elegir un ítem de abajo (respetar prioridad P0 → P2).
2. Implementar y verificar con el inspector: `python scripts/superduper_cli.py audit --json`
   y `doctor --json`.
3. Si toca `skills/` o `scripts/build_index.py`, regenerar el índice SIEMPRE con
   `python scripts/build_index.py --source repo` (nunca en modo `auto`: arrastra drift local
   de los home dirs y contamina el repo con skills renombradas `Codex-*`).
4. Commit por mejora, mensaje enfocado en el "por qué".

## Pendientes

### P0 — Rápidos y de alto impacto

- [ ] **P0-1 · Actualizar `manifest.json`**: dice "Catálogo de **2,608** skills" y hoy son
  **3,330**. Es metadata visible de la PWA (`index.html`). Fix de 1 línea, o mejor: derivar el
  número del build (p. ej. que `build_index.py` reescriba ese campo) para que no vuelva a
  quedar viejo.
- [ ] **P0-2 · Modo `--check` para CI en `build_index.py`**: variante de `--source repo` que
  regenera `SKILLS-INDEX.md` en memoria/temporal y hace diff contra el commiteado; exit 1 si
  difieren. Evita índices desincronizados con `skills/` (p. ej. skills añadidas a mano sin
  regenerar). Job sugerido: en cada PR, `python scripts/build_index.py --source repo --check`.
- [ ] **P0-3 · Documentar `--source repo` en README.md** como el modo canónico de build
  (reproducible en CI/clone fresco). Hoy está implementado pero solo se sabe por leer el script.

### P1 — Estructura y calidad del índice

- [ ] **P1-1 · Pasada de cobertura de categorías**: `Other` = 784 skills (~24%, la categoría
  más grande de lejos). Añadir regexes en `CATEGORIES` de `scripts/build_index.py` para los
  grupos más grandes (ver los nombres concretos en `SKILLS-INDEX.md → ### Other`).
  Cuidado con el sobredimensionamiento inverso: `Integrations & Automation` ya captura 827
  (regex `(-automation$| Automation$)` probablemente demasiado ancho) y `Productivity & People`
  tiene solo 9. Objetivo orientativo: ninguna categoría por encima de ~600 ni "Other" < 15%.
- [ ] **P1-2 · Decidir el destino de `skills-lock.json`**: tiene solo **5 entradas de 3,330**.
  Dos opciones: (a) completarlo con `{source, sourceType, computedHash}` por skill — da
  auditoría de integridad y conecta con `skill-inspector` recién incorporado — o (b) quitarlo
  del repo para no dar falsa impresión de lockfile completo. (a) es preferible; se puede
  generar en el mismo `build_index.py --source repo`.
- [ ] **P1-3 · Sanitizar nombres/descripciones al indexar**: algunas descripciones llegan
  truncadas con `...` (límite 200 chars del `parse_skill`); revisar que no rompa celdas de
  tabla Markdown con `|` o saltos internos (ya hay escape básico; probar con casos reales de
  `Other`).

### P2 — Deseables

- [ ] **P2-1 · Integrar repos restantes mencionados por el usuario (no solicitados
  explícitamente en su día)**: `claude-webkit`, `last30days-skill`, `open-design`,
  `andrej-karpathy-skills`, `agent-skills-for-context-engineering`, `stitch-mcp`,
  `claude-video-vision`, `banana-claude`, `claude-banana`, `social-media-skills`,
  `marketingskills`, `higgsfield`. Para cada uno: descargar raw de GitHub, escaneo de
  seguridad (patrones de exfiltración/instrucciones inyectadas), frontmatter `name:` correcto,
  entrada en `GITHUB_URLS` + regex de categoría de `build_index.py`, filas en
  `skills-inventory.md`/`UNIFIED-KNOWLEDGE.md`/`AGENTS.md`, y regenerar índice con `--source repo`.
- [ ] **P2-2 · `SKILLS-INDEX.md` pesa 1.37 MB**: valorar partirlo (un archivo por categoría
  bajo `docs/` + un índice-resumen raíz) o generar una versión HTML navegable a partir del
  mismo build. Mantener siempre un único archivo fuente de verdad o explicitar cuál es.
- [ ] **P2-3 · Normalizar finales de línea**: `SKILLS-INDEX.md` genera warning
  `CRLF will be replaced by LF`. Garantizar en `.gitattributes` la regla para `*.md`/`*.py`
  y regenerar de una vez para que el warning no reaparezca en cada diff.
- [ ] **P2-4 · Test mínimo de humo del pipeline**: test pytest barato (sin red) que corra
  `parse_skill` y `categorize` sobre 3-5 skills fijas y afirme nombre/categoría. Previene
  regresiones al tocar `build_index.py` (como la que motivó el modo `--source repo`).

## Completadas (no repetir)

- 2026-10-07: Integradas 4 skills nuevas (skill-inspector, break-ui, mobile-native,
  publish-website) con atribución y categorías; `build_index.py` con modo `--source repo`
  reproducible + `_ORIGIN_MAP`; `SKILLS-INDEX.md` regenerado (3,330); taxonomía actualizada
  en `UNIFIED-KNOWLEDGE.md`, `skills-inventory.md` y `AGENTS.md`; inspector en verde.
