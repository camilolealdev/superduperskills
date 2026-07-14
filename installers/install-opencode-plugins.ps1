# ============================================================
#  OPENCODE — INSTALADOR DE SKILLS NIVEL EMPRESA
#  Camilo | Full-Stack Freelancer Setup
#  Integrado en superduperskills — cubre backend, frontend,
#  UI/UX, seguridad, testing y debugging.
#  Ejecutar en PowerShell como administrador
# ============================================================

$ErrorActionPreference = "SilentlyContinue"

function Write-Title { param($t) Write-Host "`n=== $t ===" -ForegroundColor Cyan }
function Write-Step  { param($t) Write-Host "  -> $t" -ForegroundColor Yellow }
function Write-OK    { param($t) Write-Host "  OK $t" -ForegroundColor Green }
function Write-Warn  { param($t) Write-Host "  !! $t" -ForegroundColor Red }
function Write-Info  { param($t) Write-Host "    $t" -ForegroundColor Gray }

Clear-Host
Write-Host ""
Write-Host "  ============================================" -ForegroundColor Magenta
Write-Host "    OPENCODE - SKILLS NIVEL EMPRESA 2026" -ForegroundColor Magenta
Write-Host "  ============================================" -ForegroundColor Magenta
Write-Host ""

# ─────────────────────────────────────────────
# 0. VERIFICAR / INSTALAR OPENCODE
# ─────────────────────────────────────────────
Write-Title "0. VERIFICANDO OPENCODE"

$ocCmd = Get-Command opencode -ErrorAction SilentlyContinue
if ($ocCmd) {
    Write-OK "OpenCode ya instalado: $($ocCmd.Source)"
} else {
    Write-Warn "OpenCode no encontrado. Instalando via npm..."
    try {
        npm install -g opencode-ai 2>&1 | Out-Null
        Write-OK "OpenCode instalado via npm"
    } catch {
        Write-Warn "npm fallo. Intentando con bun..."
        try {
            bun add -g opencode-ai 2>&1 | Out-Null
            Write-OK "OpenCode instalado via bun"
        } catch {
            Write-Warn "Instala manualmente: npm install -g opencode-ai"
            Write-Info "O visita: https://opencode.ai"
        }
    }
}

# ─────────────────────────────────────────────
# 1. RUTAS DE CONFIGURACION
# ─────────────────────────────────────────────
Write-Title "1. PREPARANDO ESTRUCTURA DE DIRECTORIOS"

$ocConfigDir = "$env:APPDATA\.opencode"
$ocSkillsDir = "$ocConfigDir\skills"
$ocAgentsDir = "$ocConfigDir\agents"
$ocCommandDir = "$ocConfigDir\commands"
$ocPluginDir  = "$ocConfigDir\plugin"

foreach ($d in @($ocConfigDir, $ocSkillsDir, $ocAgentsDir, $ocCommandDir, $ocPluginDir)) {
    if (-not (Test-Path $d)) {
        New-Item -ItemType Directory -Path $d -Force | Out-Null
        Write-OK "Creado: $d"
    } else {
        Write-OK "Ya existe: $d"
    }
}

# ─────────────────────────────────────────────
# 2. GENERAR opencode.json BASE
# ─────────────────────────────────────────────
Write-Title "2. CONFIGURACION BASE opencode.json"

$ocJsonPath = "$ocConfigDir\opencode.json"

if (-not (Test-Path $ocJsonPath)) {
    $ocJsonContent = @'
{
  "$schema": "https://opencode.ai/config.json",
  "model": "anthropic/claude-sonnet-4-6",
  "small_model": "anthropic/claude-haiku-4-5",
  "plugin": [
    "opencode-skills-collection",
    "opencode-agent-skills",
    "token-optimizer-opencode",
    "caveman-opencode"
  ],
  "instructions": [
    "skills/tdd-workflow/SKILL.md",
    "skills/security-review/SKILL.md",
    "skills/frontend-design/SKILL.md"
  ],
  "agent": {
    "coder": {
      "model": "anthropic/claude-sonnet-4-6"
    },
    "task": {
      "model": "anthropic/claude-haiku-4-5"
    }
  }
}
'@
    Set-Content -Path $ocJsonPath -Value $ocJsonContent
    Write-OK "opencode.json creado en $ocJsonPath"
} else {
    Write-OK "opencode.json ya existe — no se sobreescribio"
    Write-Info "Revisa manualmente: $ocJsonPath"
}

# ─────────────────────────────────────────────
# 3. PLUGINS PRINCIPALES (token savings + skills)
# ─────────────────────────────────────────────
Write-Title "3. PLUGINS PRINCIPALES (token savings + skills)"

$ocPlugins = @(
    @{
        name = "opencode-skills-collection (1595+ skills, auto-sync)"
        npm  = "opencode-skills-collection"
        info = "Coleccion universal de 1595+ skills con lazy loading. No carga todo al inicio (evita ~80k tokens)."
    },
    @{
        name = "opencode-agent-skills (skills dinamicos + Superpowers)"
        npm  = "opencode-agent-skills"
        info = "Carga skills bajo demanda con semantic matching automatico."
    },
    @{
        name = "token-optimizer-opencode"
        npm  = "token-optimizer-opencode"
        info = "Puerto de token-optimizer para OpenCode. Comprime outputs, skeletoniza codigo repetido."
    },
    @{
        name = "caveman-opencode (−65% output tokens)"
        npm  = "caveman-opencode"
        info = "Puerto caveman para OpenCode. Activa con /caveman."
    },
    @{
        name = "opencode-skill-creator (crear/testear/optimizar skills)"
        npm  = "opencode-skill-creator"
        info = "Eval-driven development para skills. Mide trigger accuracy y optimiza descripciones."
    }
)

foreach ($p in $ocPlugins) {
    Write-Step $p.name
    Write-Info $p.info
    Write-OK "Declarado en opencode.json — se instalara al iniciar OpenCode"
}

Write-Host ""
Write-Info "NOTA: OpenCode auto-instala plugins via npm/bun al arrancar."
Write-Info "No necesitas instalarlos manualmente — solo aparecen en opencode.json."

# ─────────────────────────────────────────────
# 4. CLONAR SKILL LIBRARIES (backend, frontend, ui/ux, seguridad, testing, debug)
# ─────────────────────────────────────────────
Write-Title "4. CLONANDO SKILL LIBRARIES (multi-categoria)"

$skillRepos = @(
    @{
        name = "mingrath (66+ skills: React, Next.js, PostgreSQL, API, A11y...)"
        repo = "https://github.com/mingrath/awesome-claude-skills.git"
        dest = "$ocSkillsDir\mingrath-skills"
    },
    @{
        name = "jeffallan (66 fullstack skills: backend, frontend, seguridad, testing, debugging)"
        repo = "https://github.com/jeffallan/claude-skills.git"
        dest = "$ocSkillsDir\jeffallan-skills"
    },
    @{
        name = "jezweb (frontend, Cloudflare, Shopify, WordPress, D1, design system)"
        repo = "https://github.com/jezweb/claude-skills.git"
        dest = "$ocSkillsDir\jezweb-skills"
    },
    @{
        name = "impeccable (suite de mejora de diseno/UI: polish, harden, adapt, critique)"
        repo = "https://github.com/pbakaus/impeccable.git"
        dest = "$ocSkillsDir\impeccable-skills"
    },
    @{
        name = "ui-ux-pro-max-skill (brand, banners, slides, design tokens)"
        repo = "https://github.com/nextlevelbuilder/ui-ux-pro-max-skill.git"
        dest = "$ocSkillsDir\ui-ux-pro-max-skills"
    },
    @{
        name = "ux-ui-agent-skills (444 stars: design tokens DTCG, 138 design systems, WCAG 2.2)"
        repo = "https://github.com/plugin87/ux-ui-agent-skills.git"
        dest = "$ocSkillsDir\ux-ui-agent-skills"
    },
    @{
        name = "supabase agent-skills (backend/DB: Auth, Postgres, Edge Functions, Realtime)"
        repo = "https://github.com/supabase/agent-skills.git"
        dest = "$ocSkillsDir\supabase-skills"
    },
    @{
        name = "testcontainers (testing de integracion: .NET y Go)"
        repo = "https://github.com/testcontainers/claude-skills.git"
        dest = "$ocSkillsDir\testcontainers-skills"
    },
    @{
        name = "agentic-qe (408 stars: QA fleet completo, contract/E2E/API testing, a11y)"
        repo = "https://github.com/proffesor-for-testing/agentic-qe.git"
        dest = "$ocSkillsDir\agentic-qe-skills"
    },
    @{
        name = "levnikolaevich backend-arch (pipeline agile, auditorias de seguridad/testing/debug, ln-*)"
        repo = "https://github.com/levnikolaevich/claude-code-skills.git"
        dest = "$ocSkillsDir\backend-arch-skills"
    },
    @{
        name = "ring (202 stars: TDD, systematic debugging, code review, 10-gate dev cycle)"
        repo = "https://github.com/LerianStudio/ring.git"
        dest = "$ocSkillsDir\ring-skills"
    },
    @{
        name = "ponytail (82.9k stars: anti-over-engineering, YAGNI, code simplicity/review/audit)"
        repo = "https://github.com/DietrichGebert/ponytail.git"
        dest = "$ocSkillsDir\ponytail-skills"
    },
    @{
        name = "dev-agent-skills (git workflow, CI/CD, PR review)"
        repo = "https://github.com/fvadicamo/dev-agent-skills.git"
        dest = "$ocSkillsDir\git-cicd-skills"
    },
    @{
        name = "BehiSecc (OWASP, STRIDE threat modeling, secret scanning)"
        repo = "https://github.com/BehiSecc/awesome-claude-skills.git"
        dest = "$ocSkillsDir\behisecc-security-skills"
    },
    @{
        name = "claude-code-owasp (277 stars: OWASP Top 10:2025, ASVS 5.0, Agentic AI security)"
        repo = "https://github.com/agamm/claude-code-owasp.git"
        dest = "$ocSkillsDir\owasp-security-skills"
    },
    @{
        name = "antigravity-fullstack-hq (10 agentes: frontend, backend, db, architect...)"
        repo = "https://github.com/sabahattink/antigravity-fullstack-hq.git"
        dest = "$ocSkillsDir\antigravity-fullstack-hq"
    },
    @{
        name = "harness-skills (CI/CD oficial Harness.io, 23+ skills)"
        repo = "https://github.com/harness/harness-skills.git"
        dest = "$ocSkillsDir\harness-skills"
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

# ─────────────────────────────────────────────
# 5. SEGURIDAD / TESTING / DEBUG — INSTRUCTIONS SUGERIDAS
# ─────────────────────────────────────────────
Write-Title "5. SEGURIDAD, TESTING Y DEBUG"

$catNotes = @(
    "SEGURIDAD  -- owasp-security-skills (277★), behisecc-security-skills, jeffallan-skills/secure-code-guardian, backend-arch-skills/ln-621 y ln-760",
    "TESTING    -- agentic-qe-skills (408★), testcontainers-skills, jeffallan-skills/test-master, backend-arch-skills/ln-63x",
    "DEBUG      -- ring-skills (202★, systematic-debugging/TDD), jeffallan-skills/debugging-wizard, backend-arch-skills/ln-514",
    "UI/UX      -- ux-ui-agent-skills (444★, design tokens/WCAG), impeccable-skills, ui-ux-pro-max-skills",
    "FRONTEND   -- jezweb-skills, mingrath-skills",
    "BACKEND    -- jeffallan-skills (lenguajes/frameworks), supabase-skills, backend-arch-skills"
)
foreach ($n in $catNotes) { Write-Info "  - $n" }

# ─────────────────────────────────────────────
# 6. ACTUALIZAR opencode.json CON INSTRUCTIONS
# ─────────────────────────────────────────────
Write-Title "6. AGREGANDO INSTRUCTIONS A opencode.json"

$skillInstructions = @(
    "  `"instructions`": [",
    "    `"skills/mingrath-skills/frontend/frontend-design/SKILL.md`",",
    "    `"skills/mingrath-skills/database/schema-designer/SKILL.md`",",
    "    `"skills/mingrath-skills/database/query-optimizer/SKILL.md`",",
    "    `"skills/jeffallan-skills/SKILL.md`",",
    "    `"skills/jezweb-skills/SKILL.md`",",
    "    `"skills/behisecc-security-skills/SKILL.md`",",
    "    `"skills/testcontainers-skills/SKILL.md`""",
    "  ]"
)

Write-Info "Agrega esto a tu opencode.json segun tus necesidades:"
foreach ($line in $skillInstructions) { Write-Info $line }
Write-Info ""
Write-Info "Ruta del config: $ocJsonPath"

# ─────────────────────────────────────────────
# 7. ECC PARA OPENCODE
# ─────────────────────────────────────────────
Write-Title "7. ECC PARA OPENCODE (harness completo, opcional)"

Write-Info "ECC tiene soporte nativo para OpenCode:"
Write-Info "  git clone https://github.com/affaan-m/ecc"
Write-Info "  cd ecc"
Write-Info "  npm install"
Write-Info "  node scripts/install-apply.js --target opencode --profile standard"
Write-Info ""
Write-Info "El config base de ECC para OpenCode queda en:"
Write-Info "  $ocConfigDir\opencode.json  (se mergea con el tuyo)"

# ─────────────────────────────────────────────
# 8. OPENCODE.JSON FINAL COMPLETO
# ─────────────────────────────────────────────
Write-Title "8. GENERANDO opencode.json COMPLETO OPTIMIZADO"

$ocJsonFinal = "$ocConfigDir\opencode-empresa.json"
$ocJsonFullContent = @'
{
  "$schema": "https://opencode.ai/config.json",

  "model": "anthropic/claude-sonnet-4-6",
  "small_model": "anthropic/claude-haiku-4-5",

  "plugin": [
    "opencode-skills-collection",
    "opencode-agent-skills",
    "token-optimizer-opencode",
    "caveman-opencode",
    "opencode-skill-creator"
  ],

  "instructions": [
    "skills/jeffallan-skills/SKILL.md",
    "skills/jezweb-skills/SKILL.md",
    "skills/behisecc-security-skills/SKILL.md",
    "skills/antigravity-fullstack-hq/SKILL.md"
  ],

  "agent": {
    "frontend-specialist": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Experto en React, Next.js, Tailwind, accesibilidad y performance frontend"
    },
    "backend-specialist": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Experto en Node.js, APIs REST/GraphQL, autenticacion y microservicios"
    },
    "database-specialist": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Experto en PostgreSQL: schemas, indices, query optimization, migraciones"
    },
    "uiux-specialist": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Diseno de interfaces, design systems, accesibilidad WCAG, tokens de marca"
    },
    "security-auditor": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Revision OWASP Top 10, STRIDE, analisis de vulnerabilidades"
    },
    "qa-engineer": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Tests unitarios/integracion/E2E, coverage, testcontainers, debugging"
    },
    "devops-engineer": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Docker, CI/CD, n8n, Nginx, VPS deployment, Harness pipelines"
    },
    "architect": {
      "model": "anthropic/claude-sonnet-4-6",
      "description": "Diseño de sistemas, diagramas, decisiones de arquitectura fullstack"
    },
    "task": {
      "model": "anthropic/claude-haiku-4-5",
      "description": "Tareas rapidas: rename, refactor simple, busqueda en archivos"
    }
  },

  "tools": {
    "skills*": true
  }
}
'@

Set-Content -Path $ocJsonFinal -Value $ocJsonFullContent
Write-OK "Config empresa guardado en: $ocJsonFinal"
Write-Info "Copia este archivo sobre tu opencode.json cuando estes listo:"
Write-Info "  Copy-Item '$ocJsonFinal' '$ocJsonPath'"

# ─────────────────────────────────────────────
# 9. SINCRONIZAR CON EL BUNDLE superduperskills
# ─────────────────────────────────────────────
Write-Title "9. SINCRONIZAR CON EL BUNDLE superduperskills"
Write-Info "Despues de clonar, corre desde la raiz del repo superduperskills:"
Write-Info "  python build_index.py"
Write-Info "Esto escanea ~/.config/opencode/skills (incluyendo las carpetas clonadas arriba),"
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
Write-Host "  1. Aplica el config empresa:" -ForegroundColor Gray
Write-Host "     Copy-Item '$ocJsonFinal' '$ocJsonPath'" -ForegroundColor DarkGray
Write-Host "  2. Entra a tu proyecto y ejecuta: opencode" -ForegroundColor Gray
Write-Host "  3. OpenCode descargara los plugins automaticamente al arrancar" -ForegroundColor Gray
Write-Host ""
Write-Host "  COMANDOS DENTRO DE OPENCODE:" -ForegroundColor White
Write-Host "  /caveman          — activar respuestas tersas (menos tokens)" -ForegroundColor Gray
Write-Host "  /brainstorming    — planear antes de codear (Superpowers)" -ForegroundColor Gray
Write-Host "  /token-optimizer  — configurar compresion automatica" -ForegroundColor Gray
Write-Host ""
Write-Host "  SKILLS DISPONIBLES EN:" -ForegroundColor White
Write-Host "  $ocSkillsDir" -ForegroundColor Gray
Write-Host ""
