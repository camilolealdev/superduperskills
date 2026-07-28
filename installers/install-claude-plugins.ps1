# ============================================================
#  CLAUDE CODE — INSTALADOR DE SKILLS NIVEL EMPRESA
#  Camilo | Full-Stack Freelancer Setup
#  Integrado en superduperskills — cubre backend, frontend,
#  UI/UX, seguridad, testing y debugging.
#  Ejecutar en PowerShell como administrador
# ============================================================

$ErrorActionPreference = "SilentlyContinue"

# Colores
function Write-Title   { param($t) Write-Host "`n=== $t ===" -ForegroundColor Cyan }
function Write-Step    { param($t) Write-Host "  -> $t" -ForegroundColor Yellow }
function Write-OK      { param($t) Write-Host "  OK $t" -ForegroundColor Green }
function Write-Warn    { param($t) Write-Host "  !! $t" -ForegroundColor Red }
function Write-Info    { param($t) Write-Host "    $t" -ForegroundColor Gray }

Clear-Host
Write-Host ""
Write-Host "  ============================================" -ForegroundColor Magenta
Write-Host "    CLAUDE CODE - SKILLS NIVEL EMPRESA 2026" -ForegroundColor Magenta
Write-Host "  ============================================" -ForegroundColor Magenta
Write-Host ""

# ─────────────────────────────────────────────
# 0. VERIFICAR CLAUDE CODE
# ─────────────────────────────────────────────
Write-Title "0. VERIFICANDO CLAUDE CODE"

$claudePath = "$env:USERPROFILE\.local\bin\claude.exe"
if (Test-Path $claudePath) {
    Write-OK "Claude Code encontrado: $claudePath"

    $currentPath = [Environment]::GetEnvironmentVariable("PATH", "User")
    $claudeBin   = "$env:USERPROFILE\.local\bin"
    if ($currentPath -notlike "*$claudeBin*") {
        [Environment]::SetEnvironmentVariable("PATH", "$currentPath;$claudeBin", "User")
        $env:PATH += ";$claudeBin"
        Write-OK "PATH actualizado con $claudeBin"
    } else {
        Write-OK "PATH ya contiene Claude Code"
    }
} else {
    Write-Warn "Claude Code no encontrado. Instalando..."
    irm https://claude.ai/install.ps1 | iex
    Start-Sleep -Seconds 5
    $env:PATH += ";$env:USERPROFILE\.local\bin"
    Write-OK "Claude Code instalado"
}

Write-Info "Reinicia tu terminal si claude sigue sin responder."

# ─────────────────────────────────────────────
# 1. CREAR DIRECTORIOS DE SKILLS
# ─────────────────────────────────────────────
Write-Title "1. CREANDO ESTRUCTURA DE DIRECTORIOS"

$skillDirs = @(
    "$env:USERPROFILE\.claude\skills",
    "$env:USERPROFILE\.claude\agents",
    "$env:USERPROFILE\.claude\commands"
)
foreach ($d in $skillDirs) {
    if (-not (Test-Path $d)) {
        New-Item -ItemType Directory -Path $d -Force | Out-Null
        Write-OK "Creado: $d"
    } else {
        Write-OK "Ya existe: $d"
    }
}

# ─────────────────────────────────────────────
# 2. TIER S — BASE OBLIGATORIA
# ─────────────────────────────────────────────
Write-Title "2. TIER S — BASE OBLIGATORIA"

$tierS = @(
    @{ name="Superpowers (TDD + metodologia)";    cmd="& `"$claudePath`" plugin marketplace add obra/superpowers; & `"$claudePath`" plugin install superpowers@claude-plugins-official" },
    @{ name="Karpathy Skills (anti-slop rules)";  cmd='npx @swarmclawai/andrej-karpathy-skills --agent claude --dest "$env:USERPROFILE\.claude"' }
)

foreach ($s in $tierS) {
    Write-Step $s.name
    try {
        Invoke-Expression $s.cmd 2>&1 | Out-Null
        Write-OK "Instalado: $($s.name)"
    } catch {
        Write-Warn "Manual: $($s.name) — ver instrucciones al final"
    }
}

# ─────────────────────────────────────────────
# 3. TOKEN SAVINGS & RENDIMIENTO
# ─────────────────────────────────────────────
Write-Title "3. TOKEN SAVINGS & RENDIMIENTO"

$tokenSkills = @(
    @{ name="Caveman (−65% output tokens)";       cmd="& `"$claudePath`" plugin marketplace add JuliusBrussee/caveman; & `"$claudePath`" plugin install caveman@caveman" },
    @{ name="Token Optimizer (9 features auto)";  cmd="& `"$claudePath`" plugin marketplace add alexgreensh/token-optimizer; & `"$claudePath`" plugin install token-optimizer@alexgreensh-token-optimizer" },
    @{ name="Headroom (comprime tool outputs)";   cmd="& `"$claudePath`" plugin marketplace add headroom" }
)

foreach ($s in $tokenSkills) {
    Write-Step $s.name
    try {
        Invoke-Expression $s.cmd 2>&1 | Out-Null
        Write-OK "Instalado: $($s.name)"
    } catch {
        Write-Warn "Manual requerido: $($s.name)"
    }
}

# CLAUDE.md terse (drop-in, sin dependencias)
Write-Step "claude-token-efficient (CLAUDE.md terse drop-in)"
$claudeMdUrl    = "https://raw.githubusercontent.com/drona23/claude-token-efficient/main/CLAUDE.md"
$claudeMdTarget = "$env:USERPROFILE\.claude\CLAUDE.md"
try {
    if (-not (Test-Path $claudeMdTarget)) {
        Invoke-WebRequest -Uri $claudeMdUrl -OutFile $claudeMdTarget
        Write-OK "CLAUDE.md terse instalado en $claudeMdTarget"
    } else {
        Write-OK "CLAUDE.md ya existe — no se sobreescribio (revisa manualmente)"
    }
} catch {
    Write-Warn "No se pudo descargar CLAUDE.md — agregar manualmente desde github.com/drona23/claude-token-efficient"
}

# ─────────────────────────────────────────────
# 4. FRONTEND & UI/UX
# ─────────────────────────────────────────────
Write-Title "4. FRONTEND & UI/UX"

$frontendSkills = @(
    @{ name="frontend-design (Anthropic oficial)"; cmd="& `"$claudePath`" plugin install frontend-design@anthropics" },
    @{ name="UI/UX Pro Max";                       cmd="& `"$claudePath`" plugin marketplace add ui-ux-pro-max-skill" }
)

foreach ($s in $frontendSkills) {
    Write-Step $s.name
    try {
        Invoke-Expression $s.cmd 2>&1 | Out-Null
        Write-OK "Instalado: $($s.name)"
    } catch {
        Write-Warn "Manual: $($s.name)"
    }
}

# ─────────────────────────────────────────────
# 5. CLONAR SKILL LIBRARIES (backend, frontend, ui/ux, seguridad, testing, debug)
# ─────────────────────────────────────────────
Write-Title "5. CLONANDO SKILL LIBRARIES (multi-categoria)"

$skillRepos = @(
    @{
        name = "mingrath (66+ skills: React, Next.js, PostgreSQL, API, A11y...)"
        repo = "https://github.com/mingrath/awesome-claude-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\mingrath-skills"
    },
    @{
        name = "jeffallan (66 fullstack skills: backend, frontend, seguridad, testing, debugging)"
        repo = "https://github.com/jeffallan/claude-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\jeffallan-skills"
    },
    @{
        name = "jezweb (frontend, Cloudflare, Shopify, WordPress, D1, design system)"
        repo = "https://github.com/jezweb/claude-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\jezweb-skills"
    },
    @{
        name = "impeccable (suite de mejora de diseno/UI: polish, harden, adapt, critique)"
        repo = "https://github.com/pbakaus/impeccable.git"
        dest = "$env:USERPROFILE\.claude\skills\impeccable-skills"
    },
    @{
        name = "ui-ux-pro-max-skill (brand, banners, slides, design tokens)"
        repo = "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git"
        dest = "$env:USERPROFILE\.claude\skills\ui-ux-pro-max-skills"
    },
    @{
        name = "wondelai (1.7k stars: refactoring-ui, hooked-ux, ux-heuristics, lean-ux, made-to-stick, top-design + biz strategy)"
        repo = "https://github.com/wondelai/skills.git"
        dest = "$env:USERPROFILE\.claude\skills\wondelai-skills"
    },
    @{
        name = "taste-skill (64.9k stars: anti-slop design taste, brandkit, minimalist/brutalist variants)"
        repo = "https://github.com/Leonxlnx/taste-skill.git"
        dest = "$env:USERPROFILE\.claude\skills\taste-skills"
    },
    @{
        name = "excalidraw-diagram-skill (4.1k stars: diagramas Excalidraw para arquitectura/flujos)"
        repo = "https://github.com/coleam00/excalidraw-diagram-skill.git"
        dest = "$env:USERPROFILE\.claude\skills\excalidraw-diagram-skills"
    },
    @{
        name = "anthropics/skills (oficial: canvas-design, theme-factory, frontend-design, brand-guidelines, mcp-builder)"
        repo = "https://github.com/anthropics/skills.git"
        dest = "$env:USERPROFILE\.claude\skills\anthropics-skills"
    },
    @{
        name = "humanizer (29.7k stars: quita marcas de escritura generada por IA)"
        repo = "https://github.com/blader/humanizer.git"
        dest = "$env:USERPROFILE\.claude\skills\humanizer-skills"
    },
    @{
        name = "ux-ui-agent-skills (444 stars: design tokens DTCG, 138 design systems, WCAG 2.2)"
        repo = "https://github.com/plugin87/ux-ui-agent-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\ux-ui-agent-skills"
    },
    @{
        name = "supabase agent-skills (backend/DB: Auth, Postgres, Edge Functions, Realtime)"
        repo = "https://github.com/supabase/agent-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\supabase-skills"
    },
    @{
        name = "testcontainers (testing de integracion: .NET y Go)"
        repo = "https://github.com/testcontainers/claude-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\testcontainers-skills"
    },
    @{
        name = "agentic-qe (408 stars: QA fleet completo, contract/E2E/API testing, a11y)"
        repo = "https://github.com/proffesor-for-testing/agentic-qe.git"
        dest = "$env:USERPROFILE\.claude\skills\agentic-qe-skills"
    },
    @{
        name = "levnikolaevich backend-arch (pipeline agile, auditorias de seguridad/testing/debug, ln-*)"
        repo = "https://github.com/levnikolaevich/claude-code-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\backend-arch-skills"
    },
    @{
        name = "ring (202 stars: TDD, systematic debugging, code review, 10-gate dev cycle)"
        repo = "https://github.com/LerianStudio/ring.git"
        dest = "$env:USERPROFILE\.claude\skills\ring-skills"
    },
    @{
        name = "ponytail (82.9k stars: anti-over-engineering, YAGNI, code simplicity/review/audit)"
        repo = "https://github.com/DietrichGebert/ponytail.git"
        dest = "$env:USERPROFILE\.claude\skills\ponytail-skills"
    },
    @{
        name = "project-architect (251 stars: SPECIFICATION/IMPLEMENTATION/TASKS/BRANDING = PRD+TRD+dev-plan+UI)"
        repo = "https://github.com/ersinkoc/project-architect.git"
        dest = "$env:USERPROFILE\.claude\skills\project-architect-skills"
    },
    @{
        name = "the-architect (374 stars: entrevista por fases, genera blueprint + CLAUDE.md del proyecto objetivo)"
        repo = "https://github.com/Hainrixz/the-architect.git"
        dest = "$env:USERPROFILE\.claude\skills\the-architect-skills"
    },
    @{
        name = "mattpocock/skills (189k stars: to-spec/PRD, wayfinder, implement, domain-modeling, tdd, diagnosing-bugs)"
        repo = "https://github.com/mattpocock/skills.git"
        dest = "$env:USERPROFILE\.claude\skills\mattpocock-skills"
    },
    @{
        name = "andrej-karpathy-skills (196k stars: karpathy-guidelines, anti-overengineering)"
        repo = "https://github.com/multica-ai/andrej-karpathy-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\karpathy-skills-repo"
    },
    @{
        name = "claude-ads (7.5k stars: auditorias de ads en 12 plataformas: Google, Meta, Amazon, Apple, TikTok...)"
        repo = "https://github.com/AgriciDaniel/claude-ads.git"
        dest = "$env:USERPROFILE\.claude\skills\claude-ads-skills"
    },
    @{
        name = "claudekit-skills (2.2k stars: 45 skills variados de ClaudeKit.cc)"
        repo = "https://github.com/mrgoonie/claudekit-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\claudekit-skills"
    },
    @{
        name = "notebooklm-skill (7.5k stars: automatiza Google NotebookLM via browser)"
        repo = "https://github.com/PleasePrompto/notebooklm-skill.git"
        dest = "$env:USERPROFILE\.claude\skills\notebooklm-skill-repo"
    },
    @{
        name = "claude-code-prompt-improver (1.8k stars: mejora prompts vagos antes de ejecutar)"
        repo = "https://github.com/severity1/claude-code-prompt-improver.git"
        dest = "$env:USERPROFILE\.claude\skills\prompt-improver-skill-repo"
    },
    @{
        name = "dev-agent-skills (git workflow, CI/CD, PR review)"
        repo = "https://github.com/fvadicamo/dev-agent-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\git-cicd-skills"
    },
    @{
        name = "BehiSecc (OWASP, STRIDE threat modeling, secret scanning)"
        repo = "https://github.com/BehiSecc/awesome-claude-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\behisecc-security-skills"
    },
    @{
        name = "claude-code-owasp (277 stars: OWASP Top 10:2025, ASVS 5.0, Agentic AI security)"
        repo = "https://github.com/agamm/claude-code-owasp.git"
        dest = "$env:USERPROFILE\.claude\skills\owasp-security-skills"
    },
    @{
        name = "antigravity-fullstack-hq (10 agentes: frontend, backend, db, architect, security...)"
        repo = "https://github.com/sabahattink/antigravity-fullstack-hq.git"
        dest = "$env:USERPROFILE\.claude\skills\antigravity-fullstack-hq"
    },
    @{
        name = "harness-skills (CI/CD oficial Harness.io, 23+ skills)"
        repo = "https://github.com/harness/harness-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\harness-skills"
    },
    @{
        name = "ui-skills (6.6k stars: baseline-ui, fixing-motion-performance, fixing-accessibility)"
        repo = "https://github.com/ibelick/ui-skills.git"
        dest = "$env:USERPROFILE\.claude\skills\ui-skills-repo"
    },
    @{
        name = "awesome-design-md (105k stars: 74 DESIGN.md de marcas conocidas)"
        repo = "https://github.com/VoltAgent/awesome-design-md.git"
        dest = "$env:USERPROFILE\.claude\skills\awesome-design-md-repo"
    },
    @{
        name = "fabricioctelles/skills (38 stars: design-md-validator y otros)"
        repo = "https://github.com/fabricioctelles/skills.git"
        dest = "$env:USERPROFILE\.claude\skills\fabricioctelles-skills"
    }
)

foreach ($r in $skillRepos) {
    Write-Step $r.name
    if (-not (Test-Path $r.dest)) {
        git clone $r.repo $r.dest 2>&1 | Out-Null
        if (Test-Path $r.dest) {
            Write-OK "Clonado -> $($r.dest)"
        } else {
            Write-Warn "Fallo el clone — verifica git e internet"
        }
    } else {
        Push-Location $r.dest
        git pull 2>&1 | Out-Null
        Pop-Location
        Write-OK "Actualizado -> $($r.dest)"
    }
}

# the-architect ships as a CLAUDE.md-driven agent with no native SKILL.md —
# write the wrapper so Claude Code's skill discovery (and build_index.py) can find it.
$architectSkillMd = "$env:USERPROFILE\.claude\skills\the-architect-skills\SKILL.md"
if ((Test-Path "$env:USERPROFILE\.claude\skills\the-architect-skills") -and -not (Test-Path $architectSkillMd)) {
    Write-Step "Escribiendo wrapper SKILL.md para the-architect"
    $architectSkillContent = @'
---
name: the-architect
description: >
  Interviews the user about what they want to build (phased discovery Q&A), classifies the
  project into an archetype (SaaS webapp, marketing site, mobile app, API backend, internal
  tool, content platform), and produces a self-contained blueprint .md that another Claude
  Code instance can build autonomously — plus a ready-to-paste CLAUDE.md for the target
  project. Use when the user wants to plan a new project from scratch, needs an
  architecture.md / project blueprint, wants tech-stack recommendations with trade-off
  analysis, or asks "help me design this before I start coding". Complements
  project-architect (which produces SPECIFICATION/IMPLEMENTATION/TASKS/BRANDING docs) —
  use the-architect when the ask is specifically "interview me and generate the blueprint +
  CLAUDE.md for a brand-new project", and project-architect when the ask is "write a formal
  spec/implementation-plan/task-breakdown".
metadata:
  source: https://github.com/Hainrixz/the-architect
  original_format: CLAUDE.md-driven agent (no native SKILL.md) — wrapped here so the
    superduperskills bundler and Claude Code's skill discovery can find it.
---

# The Architect

This skill's full operating protocol lives in [`CLAUDE.md`](CLAUDE.md) in this same
directory — read it in full before starting. Summary of the flow:

1. **Phase 1 — Discovery**: read `questions/phase-1-discovery.md`, ask 2-3 questions at a
   time, classify the project into an archetype from `knowledge/archetypes/`.
2. **Phase 2 — Deep dive**: read `questions/phase-2-branches.md` for the identified
   archetype, ask 3-5 targeted questions, consult `knowledge/building-blocks/*.md` for
   specific decisions (auth, database, deployment, frontend stack, etc.).
3. **Phase 3 — Architecture**: read `questions/phase-3-confirmation.md`, propose the tech
   stack and architecture with rationale, confirm with the user.
4. **Phase 4 — Generate**: write the blueprint from `templates/blueprint-template.md` into
   `output/`, including a complete `CLAUDE.md` for the target project (using
   `templates/claude-md-template.md`) and a "Skills to Use During Build" table populated
   from `knowledge/skills-registry.md`.

`knowledge/stack-compatibility.md` has compatibility rules between stack choices to check
before finalizing recommendations.

**Project-specific note:** when populating "Skills to Use During Build", always check
whether the target environment has `caveman`, `ponytail`, `harness`, `graphify`, or other
token-efficiency/quality skills installed and include them in the recommendation table
alongside the domain-specific ones from `knowledge/skills-registry.md` — that registry lists
generic upstream skills and won't know about a specific machine's local install.
'@
    Set-Content -Path $architectSkillMd -Value $architectSkillContent
    Write-OK "Wrapper creado -> $architectSkillMd"
}

# ─────────────────────────────────────────────
# 6. SEGURIDAD
# ─────────────────────────────────────────────
Write-Title "6. SEGURIDAD"

Write-Step "AgentShield — escaneo de vulnerabilidades en config Claude Code"
try {
    npx ecc-agentshield scan 2>&1 | Out-Null
    Write-OK "AgentShield disponible: npx ecc-agentshield scan"
} catch {
    Write-Info "AgentShield: npx ecc-agentshield scan (ejecutar cuando necesites auditar)"
}

$secNote = @(
    "owasp-security       -- OWASP Top 10:2025, ASVS 5.0, Agentic AI security (owasp-security-skills, 277 stars)",
    "skill-threat-model   -- STRIDE, PenTest, 8 fases de analisis (behisecc-security-skills)",
    "secure-code-guardian -- JWT, bcrypt, CSP, CORS, SQLi prevention (jeffallan-skills)",
    "ln-621/ln-760        -- security-auditor / security-setup (backend-arch-skills)",
    "varlock              -- secrets nunca en sesiones, logs ni git"
)
Write-Info "Skills de seguridad disponibles tras el clonado:"
foreach ($n in $secNote) { Write-Info "  - $n" }

# ─────────────────────────────────────────────
# 7. TESTING & DEBUGGING
# ─────────────────────────────────────────────
Write-Title "7. TESTING & DEBUGGING"

$testNote = @(
    "agentic-qe-skills            -- QA fleet (408 stars): contract/E2E/API testing, a11y-ally, coverage",
    "test-master, senior-qa       -- unit/integration/E2E, Jest, Playwright, Vitest",
    "testcontainers-skills        -- contenedores de integracion .NET / Go",
    "ring-skills                  -- systematic-debugging, TDD, 10-gate dev cycle (202 stars)",
    "debugging-wizard             -- stack traces, root cause analysis, log correlation",
    "ln-404/ln-514/ln-63x         -- test-executor, test-log-analyzer, auditores de cobertura (backend-arch-skills)",
    "chaos-engineer               -- inyeccion de fallos, game days"
)
Write-Info "Skills de testing/debug disponibles tras el clonado:"
foreach ($n in $testNote) { Write-Info "  - $n" }

# ─────────────────────────────────────────────
# 8. ARQUITECTURA & FULLSTACK EXTRA
# ─────────────────────────────────────────────
Write-Title "8. ARQUITECTURA & FULLSTACK EXTRA"

Write-Step "firecrawl-lean (5 skills fusionados en 1, token-efficient)"
try {
    npx skills add https://github.com/alexsmedile/firecrawl-lean 2>&1 | Out-Null
    Write-OK "firecrawl-lean instalado"
} catch {
    Write-Warn "npx no disponible — instalar manualmente: github.com/alexsmedile/firecrawl-lean"
}

# ─────────────────────────────────────────────
# 9. ECC — HARNESS COMPLETO (OPCIONAL)
# ─────────────────────────────────────────────
Write-Title "9. ECC — HARNESS COMPLETO (OPCIONAL / PESADO)"
Write-Info "ECC tiene 60+ agentes, 229 skills, hooks, memoria, seguridad."
Write-Info "Instalar solo si quieres el sistema completo (puede ser overwhelming al inicio)."
Write-Info ""
Write-Info "Cuando estes listo:"
Write-Info "  git clone https://github.com/affaan-m/ecc"
Write-Info "  cd ecc"
Write-Info "  node scripts/install-apply.js --target claude-code --profile standard"

# ─────────────────────────────────────────────
# 10. HABILITAR PROMPT CACHING
# ─────────────────────────────────────────────
Write-Title "10. PROMPT CACHING (ahorra tokens en sesiones largas)"

$claudeEnvPath = "$env:USERPROFILE\.claude\.env"
if (-not (Test-Path (Split-Path $claudeEnvPath))) {
    New-Item -ItemType Directory -Path (Split-Path $claudeEnvPath) -Force | Out-Null
}
$cacheContent = "ENABLE_PROMPT_CACHING_1H=1`n"
if (-not (Test-Path $claudeEnvPath) -or (Get-Content $claudeEnvPath) -notlike "*ENABLE_PROMPT_CACHING*") {
    Add-Content -Path $claudeEnvPath -Value $cacheContent
    Write-OK "Prompt caching habilitado en $claudeEnvPath"
} else {
    Write-OK "Prompt caching ya estaba habilitado"
}

# ─────────────────────────────────────────────
# 11. SINCRONIZAR CON EL BUNDLE superduperskills
# ─────────────────────────────────────────────
Write-Title "11. SINCRONIZAR CON EL BUNDLE superduperskills"
Write-Info "Despues de clonar, corre desde la raiz del repo superduperskills:"
Write-Info "  python build_index.py"
Write-Info "Esto escanea ~/.claude/skills (incluyendo las carpetas clonadas arriba),"
Write-Info "dedupe por nombre y regenera skills/ + SKILLS-INDEX.md."

# ─────────────────────────────────────────────
# RESUMEN FINAL
# ─────────────────────────────────────────────
Write-Host ""
Write-Host "  ============================================" -ForegroundColor Green
Write-Host "              INSTALACION COMPLETA" -ForegroundColor Green
Write-Host "  ============================================" -ForegroundColor Green
Write-Host ""
Write-Host "  PROXIMOS PASOS:" -ForegroundColor White
Write-Host "  1. Reinicia tu terminal (para que el PATH tome efecto)" -ForegroundColor Gray
Write-Host "  2. Ejecuta: claude" -ForegroundColor Gray
Write-Host "  3. Dentro de Claude Code, habilita el auto-update:" -ForegroundColor Gray
Write-Host "     /plugin -> Marketplaces -> Enable auto-update" -ForegroundColor Gray
Write-Host ""
Write-Host "  COMANDOS UTILES:" -ForegroundColor White
Write-Host "  /caveman          — activar modo token-efficient" -ForegroundColor Gray
Write-Host "  /caveman-stats    — ver tokens ahorrados" -ForegroundColor Gray
Write-Host "  /token-optimizer  — setup inicial de hooks" -ForegroundColor Gray
Write-Host "  /harness-audit    — auditar configuracion (si instalas ECC)" -ForegroundColor Gray
Write-Host ""
Write-Host "  SKILLS CLONADOS EN:" -ForegroundColor White
Write-Host "  $env:USERPROFILE\.claude\skills\" -ForegroundColor Gray
Write-Host ""
