# SKILL RECOVERY — Instrucciones para cualquier agente

Este documento permite a cualquier agente (Claude Code, Gemini CLI, Codex CLI, Cursor, etc.)
reconstruir la lista completa de skills disponibles y entender el sistema multi-conocimiento.

## Archivos clave

| Archivo | Propósito |
|---------|-----------|
| `UNIFIED-KNOWLEDGE.md` | Taxonomía multi-conocimiento unificada con todas las skills |
| `skills-inventory.md` | Inventario por repositorio de origen |

## Directorios donde buscar skills

**Aviso:** el layout exacto varía por máquina — depende de si los skills llegaron via marketplace/plugin (carpeta plana `~/.claude/skills/<nombre>/SKILL.md`) o via clone manual con los instaladores de este repo (carpeta `<fuente>-skills/` con subcarpetas). No asumas que las rutas de abajo existen tal cual en toda máquina: usa `SKILLS-INDEX.md` (columna "Location"/"GitHub") como fuente de verdad portable, ya que cada fila indica la ruta real dentro de `skills/` de este repo sin importar de dónde vino.

Cada vez que un agente necesite un skill, debe buscar en estos directorios (ordenados por prioridad):

```
~/.agents/skills/                          # Skills de productividad, marketing, video (si existe)
~/.config/opencode/skills/                 # Skills de OpenCode (mayoría en carpetas planas por skill)
~/.claude/skills/                          # Skills de Claude Code (mayoría en carpetas planas por skill)
```

Skill-libraries clonadas explícitamente por `installers/install-claude-plugins.ps1` / `install-opencode-plugins.ps1` (carpetas con sufijo `-skills`, dentro de los dos directorios de arriba):

```
mingrath-skills/            # React, Next.js, PostgreSQL, API, A11y
jeffallan-skills/           # 66 skills fullstack: backend, frontend, seguridad, testing, debugging
jezweb-skills/              # Frontend, Cloudflare, Shopify, WordPress, D1
impeccable-skills/          # Suite de mejora de diseño/UI (polish, harden, adapt, critique)
ui-ux-pro-max-skills/       # Brand, banners, slides, design tokens
ux-ui-agent-skills/         # Design tokens DTCG, 138 design systems, WCAG 2.2 (★444)
supabase-skills/            # Backend/DB: Auth, Postgres, Edge Functions, Realtime
testcontainers-skills/      # Testing de integración .NET y Go
agentic-qe-skills/          # QA fleet: contract/E2E/API testing, a11y (★408)
backend-arch-skills/        # Pipeline agile + auditorías de seguridad/testing/debug (ln-*)
ring-skills/                # TDD, systematic-debugging, code review, 10-gate dev cycle (★202)
git-cicd-skills/            # Git workflow, CI/CD, PR review
behisecc-security-skills/   # OWASP, STRIDE threat modeling, secret scanning
owasp-security-skills/      # OWASP Top 10:2025, ASVS 5.0, Agentic AI security (★277)
antigravity-fullstack-hq/   # 10 agentes: frontend, backend, db, architect, security
harness-skills/             # CI/CD oficial Harness.io
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
