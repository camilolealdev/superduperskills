# SKILL RECOVERY — Instrucciones para cualquier agente

Este documento permite a cualquier agente (Claude Code, Gemini CLI, Codex CLI, Cursor, etc.)
reconstruir la lista completa de skills disponibles y entender el sistema multi-conocimiento.

## Archivos clave

| Archivo | Propósito |
|---------|-----------|
| `UNIFIED-KNOWLEDGE.md` | Taxonomía multi-conocimiento unificada con todas las skills |
| `skills-inventory.md` | Inventario por repositorio de origen |

## Directorios donde buscar skills

Cada vez que un agente necesite un skill, debe buscar en estos directorios (ordenados por prioridad):

```
~/.agents/skills/                          # Skills de productividad, marketing, video
~/.config/opencode/skills/                 # Skills principales de OpenCode
~/.config/opencode/skills/backend-arch/skills-catalog/  # Pipeline Agile + auditorías (ln-*)
~/.config/opencode/skills/backend-skills/skills/        # Lenguajes, testing, arquitectura
~/.config/opencode/skills/frontend-jezweb/plugins/      # Frontend, Cloudflare, Shopify, WP
~/.config/opencode/skills/git-cicd/skills/              # Git, GitHub PRs
~/.config/opencode/skills/seo-agrici/                   # SEO audit pipeline
~/.config/opencode/skills/seo-ccforseo/                 # AI visibility, content briefs
~/.config/opencode/skills/seo-geo/                      # SEO writing, schema, rank tracking
~/.config/opencode/skills/impeccable/source/skills/     # Design enhancement suite
~/.config/opencode/skills/testcontainers/               # Testcontainers .NET + Go
~/.config/opencode/skills/docker/                       # Docker helper
~/.config/opencode/skills/token-optimizer/              # Prompt improvement
~/.claude/skills/ui-ux-pro-max/                         # Brand, slides, banners
```

## Comando para cargar skills

```bash
# Cargar un skill específico por nombre
# Usa el sistema de skills del agente correspondiente
```

## Notas

- Skills duplicados están documentados en UNIFIED-KNOWLEDGE.md sección "Duplicados: Merge Map"
- Para crear nuevos skills, usar `skill-creator` o `creating-skills`
- Para buscar skills por funcionalidad, revisar el "Mapa de Uso Rápido" en UNIFIED-KNOWLEDGE.md
