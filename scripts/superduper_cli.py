#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 SUPERDUPERSKILLS AGENTIC CLI & CONTROL CENTER v4.0
================================================================================
 Comprehensive Terminal UI & Discovery Engine for AI Agent Skills Governance.

 Agent 1: Modern ASCII branding, animated banner, version display
 Agent 2: Rich help system, usage examples, --version/--json flags
 Agent 3: Interactive TUI with progress indicators, confirmations, status bars
 Agent 4: New subcommands: init, doctor, export, profile, stats
 Agent 5: Desktop integration hooks (Electron stubs, tray icon config)

 - Deep Project & Monorepo Stack Discovery
 - Mandatory Invariant Core Suite (19 Skills)
 - Interactive Skill Manager (1-by-1 & Category Toggles across 2,700+ Skills)
 - Skill Seekers & Remote Ingestion Engine
 - Multi-CLI Synchronizer (Claude, Gemini, Cursor, Codex, OpenCode)
 - Agent Compliance & view_file Audit Gate
================================================================================
"""

import os
import sys
import json
import glob
import re
import shutil
import argparse
import time
import platform
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# AGENT 1: VERSION & ASCII BRANDING
# =============================================================================
__version__ = "4.0.0"
__codename__ = "HyperDrive"

# --- ANSI COLOR CODES ---
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    ITALIC  = "\033[3m"
    UNDER   = "\033[4m"
    
    # Foreground
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"
    
    # Background
    BG_BLUE    = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN    = "\033[46m"
    BG_DARK    = "\033[100m"
    BG_GREEN   = "\033[42m"

# --- ASCII ART LOGO ---
LOGO_ART = f"""{C.CYAN}{C.BOLD}       _____ _____ _____ _____ _____ _____ _____ _____ _____ _____       {C.RESET}
{C.CYAN}{C.BOLD}      / ____/ ____/ ____/ ____/ ____/ ____/ ____/ ____/ ____/ ____|      {C.RESET}
{C.BLUE}{C.BOLD}     | (___| (___| (___| (___| (___| (___| (___| (___| (___| (___        {C.RESET}
{C.BLUE}{C.BOLD}      \\___ \\\\___ \\\\___ \\\\___ \\\\___ \\\\___ \\\\___ \\\\___ \\\\___ \\\\___ \\       {C.RESET}
{C.MAGENTA}{C.BOLD}      ____) )___) )___) )___) )___) )___) )___) )___) )___) )___)      {C.RESET}
{C.MAGENTA}{C.BOLD}     |_____/_____/_____/_____/_____/_____/_____/_____/_____/_____/       {C.RESET}
{C.WHITE}{C.BOLD}      ____ ____  _    ____ _____ _     ___ _   _ _____ ____              {C.RESET}
{C.GREEN}{C.BOLD}     / ___/ ___|| |  |  _ \\_   _| |   |_ _| \\ | | ____/ ___|             {C.RESET}
{C.GREEN}{C.BOLD}    | |   \\___ \\| |  | |_) || | | |    | ||  \\| |  _| \\___ \\             {C.RESET}
{C.YELLOW}{C.BOLD}    | |___ ___) | |__|  __/ | | | |___| || |\\  | |___ ___) |            {C.RESET}
{C.RED}{C.BOLD}     \\____|____/\\____|_|    |_| |_____|___|_| \\_|_____|____/             {C.RESET}
{C.GRAY}      ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀         {C.RESET}"""

MINI_LOGO = f"""{C.CYAN}{C.BOLD}╔═══════════════════════════════════════════════════════════════╗
║  {C.WHITE}🚀 SUPERDUPERSKILLS {C.CYAN}v{__version__} {C.YELLOW}«{__codename__}»{C.CYAN}{C.BOLD}                       ║
║  {C.GRAY}Agentic CLI & Discovery Control Center                        {C.CYAN}{C.BOLD}║
║  {C.GREEN}2,700+ Skills | 8 Agent Harnesses | 1 Command                  {C.CYAN}{C.BOLD}║
╚═══════════════════════════════════════════════════════════════╝{C.RESET}"""

QUICK_STATUS_BAR = (
    f"  {C.DIM}{chr(9504)}{chr(9472) * 62}{chr(9508)}{C.RESET}\n"
    f"  {C.DIM}{chr(9474)}{C.RESET} {C.BOLD}{C.CYAN}Workspace:{C.RESET} {{ws}}\n"
    f"  {C.DIM}{chr(9474)}{C.RESET} {C.BOLD}{C.GREEN}Active:{C.RESET}   {{active_count}} skills ({{core_count}} core + {{spec_count}} specialized)\n"
    f"  {C.DIM}{chr(9474)}{C.RESET} {C.BOLD}{C.MAGENTA}Catalog:{C.RESET}  {{catalog_count}} skills indexed\n"
    f"  {C.DIM}{chr(9474)}{C.RESET} {C.BOLD}{C.YELLOW}Version:{C.RESET}  v{{version}} «{{codename}}»\n"
    f"  {C.DIM}{chr(9524)}{chr(9472) * 62}{chr(9527)}{C.RESET}"
)

WORKSPACE_DIR = os.getcwd()
SKILLS_DIR = os.path.join(WORKSPACE_DIR, 'skills')
AGENTS_DIR = os.path.join(WORKSPACE_DIR, '.agents')
ACTIVE_MANIFEST = os.path.join(AGENTS_DIR, 'ACTIVE-SKILLS.json')
QUALIFICATION_DOC = os.path.join(AGENTS_DIR, 'PROJECT-QUALIFICATION.md')
PROFILES_DIR = os.path.join(AGENTS_DIR, 'profiles')
DESKTOP_CONFIG = os.path.join(AGENTS_DIR, 'desktop.json')

# =============================================================================
# 1. MANDATORY INVARIANT CORE SUITE (19 SKILLS)
# =============================================================================
MANDATORY_CORE_SUITE = [
    {"name": "caveman", "reason": "Output Compression (-75% token reduction)", "category": "CORE", "icon": "🪨"},
    {"name": "ponytail", "reason": "YAGNI & Simplicity Architecture (Minimal Diffs)", "category": "CORE", "icon": "🦝"},
    {"name": "spec-kit", "reason": "Spec-Driven Development & Task Breakdown", "category": "CORE", "icon": "📋"},
    {"name": "token-savings", "reason": "Context Budget & Skill Filtering", "category": "CORE", "icon": "💰"},
    {"name": "harness", "reason": "Automated Verification & Test Harness Loop", "category": "CORE", "icon": "🔗"},
    {"name": "claude-mem", "reason": "Persistent Session & Architecture Memory", "category": "CORE", "icon": "🧠"},
    {"name": "rtk", "reason": "Terminal Log Compression (Rust Token Killer)", "category": "CORE", "icon": "⚡"},
    {"name": "graphify", "reason": "Codebase Knowledge Graph Indexing", "category": "CORE", "icon": "🕸️"},
    {"name": "archify", "reason": "Interactive System Diagrams (Trigger: 3 Commits)", "category": "CORE", "icon": "🏗️"},
    {"name": "skill-seekers", "reason": "Ingesta & Búsqueda Activa de Skills Remotas", "category": "CORE", "icon": "🔍"},
    {"name": "skill-vault", "reason": "Bóveda Persistente de Skills", "category": "CORE", "icon": "🔐"},
    {"name": "all-deploy", "reason": "Despliegues Universales Multicloud", "category": "CORE", "icon": "🚀"},
    {"name": "context-mode", "reason": "Gestión & Compresión de Ventana de Contexto", "category": "CORE", "icon": "📦"},
    {"name": "aprende-skill", "reason": "Aprendizaje Acelerado Agentico", "category": "CORE", "icon": "📚"},
    {"name": "agentshield", "reason": "Escudo de Seguridad & Prompt Sanitization", "category": "CORE", "icon": "🛡️"},
    {"name": "modo-tdah", "reason": "Ejecución Ultra-Focalizada sin Explicaciones Infladas", "category": "CORE", "icon": "🎯"},
    {"name": "agentic-awesome-skills", "reason": "Catálogo de Patrones Agenticos Autónomos", "category": "CORE", "icon": "🤖"},
    {"name": "gsd-core", "reason": "Get Shit Done (GSD) Execution Framework", "category": "CORE", "icon": "💥"},
    {"name": "i-have-adhd", "reason": "Formateo de Salida Action-First", "category": "CORE", "icon": "⚡"}
]

# =============================================================================
# 2. SPECIALIZED CATEGORIES & HIGH-VALUE SKILL MAPPINGS
# =============================================================================
CATEGORY_REGISTRY = {
    "DESIGN_UI": {
        "title": "🎨 Diseño & UI Craft (Anti-Slop / Motion / Design Systems)",
        "icon": "🎨",
        "skills": [
            ("emil-design-eng", "Filosofía UI de Emil Kowalski: Micro-detalles & polish"),
            ("animate", "Animaciones web fluidas e interruptibles (Emil Kowalski)"),
            ("animate-expo", "Animaciones React Native & Expo con Reanimated"),
            ("review-animations", "Auditoría de curvas y performance de animaciones"),
            ("improve-animations", "Hoja de ruta y corrección de motion"),
            ("find-animation-opportunities", "Detección de elementos que deberían animarse"),
            ("animation-vocabulary", "Glosario técnico de motion y micro-interacciones"),
            ("apple-design", "Principios de diseño Apple (iOS, macOS, Depth, Springs)"),
            ("pick-ui-library", "Selección inteligente de librería UI sin sobrecarga"),
            ("prototype", "Prototipado rápido de interfaces de alta fidelidad"),
            ("ask-sonner", "Patrones y troubleshooting del sistema de toasts Sonner"),
            ("clone-website", "Reverse-engineer y clonado pixel-perfect de sitios via agentes builder"),
            ("impeccable", "Suite Paul Bakaus (23 comandos de UI design polish)"),
            ("taste-skill", "Framework frontend anti-slop y jerarquía tipográfica"),
            ("cult-ui", "Componentes UI con estética brutalista y audaz"),
            ("huashu-design", "Micro-diseño y precisión estética contemporánea"),
            ("tododeia-animaciones", "Presets diarios de animación UI y transiciones"),
            ("gsap-framer-scroll-animation", "Animaciones avanzadas con GSAP y Framer Motion"),
            ("high-end-visual-design", "Diseño visual de nivel agencia AAA"),
            ("design-void", "Design system cyber-brutalismo reverse-engineered"),
            ("tailwind-theme-builder", "Tokens de diseño y configuración Tailwind v4")
        ]
    },
    "SECURITY_OWASP": {
        "title": "🛡️ Seguridad, OWASP & Threat Modeling",
        "icon": "🛡️",
        "skills": [
            ("agentshield", "Escudo contra prompt injection y comandos destructivos"),
            ("cybersecurity", "Auditoría de seguridad general y escaneo de vulnerabilidades"),
            ("owasp-top10", "Verificación exhaustiva de OWASP Top 10:2025"),
            ("threat-model-analyst", "Modelado de amenazas STRIDE y vectores de ataque"),
            ("security-auditor", "Auditoría estricta de código y sanitización de inputs"),
            ("secret-scanner", "Detección y prevención de fuga de API keys y credenciales"),
            ("cors-csrf-hardening", "Protección de cabeceras, CORS y tokens anti-CSRF"),
            ("auth-patterns", "Patrones seguros de autenticación (JWT, OAuth, Sessions)")
        ]
    },
    "BACKEND_API": {
        "title": "⚡ Backend, APIs & Bases de Datos",
        "icon": "⚡",
        "skills": [
            ("nodejs-backend-patterns", "Patrones de arquitectura Node.js / Express / Fastify"),
            ("python-patterns", "Desarrollo idiomático en Python / FastAPI / Django"),
            ("golang-patterns", "Concurrencia, goroutines y microservicios en Go"),
            ("rust-patterns", "Arquitectura segura y rendimiento en Rust"),
            ("dotnet-patterns", "Patrones enterprise en .NET 8 / C#"),
            ("postgres-patterns", "Modelado, índices y optimización de consultas PostgreSQL"),
            ("database-optimizer", "Tuning de consultas SQL y planes de ejecución EXPLAIN"),
            ("redis-caching", "Estrategias de caché distribuida y rate limiting con Redis"),
            ("graphql-architect", "Diseño de schemas GraphQL y optimización DataLoader"),
            ("rest-api-design", "Diseño de contratos RESTful, versionado y documentación OpenAPI")
        ]
    },
    "MOBILE_DESKTOP": {
        "title": "📱 Mobile & Aplicaciones de Escritorio",
        "icon": "📱",
        "skills": [
            ("expo-overview", "Desarrollo multiplataforma con Expo & React Native"),
            ("expo-router", "Navegación declarativa basada en archivos en Expo"),
            ("flutter-apply-architecture-best-practices", "Arquitectura en capas para Flutter"),
            ("flutter-build-responsive-layout", "Layouts adaptativos para móviles, tablets y desktop"),
            ("write-swift", "Swift 6 moderno, concurrencia y SwiftUI"),
            ("android-cli", "Tooling y gestión de emuladores y SDKs Android"),
            ("electron-desktop", "Empaquetado y seguridad en aplicaciones Electron"),
            ("tauri-apps", "Aplicaciones de escritorio ligeras con Rust & Tauri")
        ]
    },
    "DEVOPS_CLOUD": {
        "title": "🚀 DevOps, Cloud, CI/CD & Infraestructura",
        "icon": "🚀",
        "skills": [
            ("all-deploy", "Despliegue universal multicloud (VPS Docker, Vercel, Railway)"),
            ("docker-patterns", "Construcción de imágenes multi-stage y docker-compose"),
            ("kubernetes-dev", "Manifiestos K8s, Helm charts e ingress controllers"),
            ("cloudflare-worker-builder", "Serverless Edge computing en Cloudflare Workers y D1"),
            ("terraform-patterns", "Infraestructura como código (IaC) modular con Terraform"),
            ("github-actions-cicd", "Pipelines automatizados de test, build y deployment"),
            ("sre-incident-responder", "Monitorización, SLIs/SLOs y respuesta ante incidentes")
        ]
    },
    "AI_AGENTS": {
        "title": "🤖 Inteligencia Artificial & Sistemas Multi-Agente",
        "icon": "🤖",
        "skills": [
            ("agentic-awesome-skills", "Patrones y herramientas curadas para agentes autónomos"),
            ("antigravity-guide", "Guía del ecosistema Google Antigravity (AGY 2.0)"),
            ("gemini-api-dev", "Integración con Google Gemini Multimodal y Function Calling"),
            ("langchain-architect", "Cadenas, herramientas y memoria con LangChain / LangGraph"),
            ("rag-pipeline-expert", "Recuperación aumentada por generación (RAG) y embeddings"),
            ("prompt-improver", "Optimización y estructuración de prompts complejos"),
            ("subagent-driven-development", "Descomposición y delegación de tareas en sub-agentes")
        ]
    },
    "TESTING_QA": {
        "title": "🧪 Testing, Calidad de Software & QA",
        "icon": "🧪",
        "skills": [
            ("harness", "Arnés de pruebas y verificación continua automatizada"),
            ("browser-harness", "Automatización y testing visual E2E en navegador real"),
            ("tdd-workflow", "Desarrollo guiado por pruebas (Test-Driven Development)"),
            ("e2e-testing", "Pruebas E2E completas con Playwright y Cypress"),
            ("systematic-debugging", "Aislamiento causal y resolución sistemática de bugs"),
            ("performance-benchmarking", "Métricas de estrés, carga y profiling de memoria")
        ]
    },
    "GROWTH_SEO_LEGAL": {
        "title": "📈 Growth, SEO, Copywriting & Legal",
        "icon": "📈",
        "skills": [
            ("claude-seo", "SEO técnico, Schema.org markup y GEO"),
            ("editor-pro-max", "Edición profesional de estilo y copywriting"),
            ("claude-for-legal", "Análisis de contratos y cumplimiento normativo"),
            ("humanizer", "Eliminación de marcas artificiales de escritura de IA"),
            ("gtm-0-to-1-launch", "Estrategia Go-To-Market y tracción temprana"),
            ("neuro-persuasion-toolkit", "Neuromarketing y psicología de conversión")
        ]
    }
}

# =============================================================================
# 3. PROGRESS INDICATOR (AGENT 3)
# =============================================================================
class Spinner:
    """Animated spinner for long operations."""
    FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    def __init__(self, message: str = "Working..."):
        self.message = message
        self.idx = 0
        self._active = False
    
    def start(self):
        self._active = True
        return self
    
    def stop(self, final_msg: str = ""):
        self._active = False
        if final_msg:
            sys.stdout.write(f"\r{C.GREEN}✓{C.RESET} {final_msg}{' ' * 20}\n")
            sys.stdout.flush()
    
    def tick(self, msg: str = ""):
        if not self._active:
            return
        frame = self.FRAMES[self.idx % len(self.FRAMES)]
        display = msg or self.message
        sys.stdout.write(f"\r{C.CYAN}{frame}{C.RESET} {display}...")
        sys.stdout.flush()
        self.idx += 1

def run_with_spinner(message: str, func, *args, **kwargs):
    """Run a function with a spinner animation."""
    spinner = Spinner(message).start()
    result = None
    # Simulate work with brief spinner display
    for _ in range(3):
        spinner.tick()
        time.sleep(0.1)
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        spinner.stop(f"{C.RED}Error: {e}{C.RESET}")
        return None
    spinner.stop(f"{message} done")
    return result

def print_confirm(message: str, default_yes: bool = False) -> bool:
    """Print a styled confirmation prompt."""
    suffix = "[Y/n]" if default_yes else "[y/N]"
    try:
        ans = input(f"{C.CYAN}?{C.RESET} {message} {C.GRAY}{suffix}{C.RESET} ").strip().lower()
        if not ans:
            return default_yes
        return ans in ['y', 'yes', 'si', 's']
    except (KeyboardInterrupt, EOFError):
        return False

# =============================================================================
# 4. DEEP PROJECT DISCOVERY ENGINE
# =============================================================================
class ProjectDiscovery:
    """Escanea el workspace y detecta stack, monorepos, microservicios y métricas."""
    
    @staticmethod
    def inspect(root_path: str = WORKSPACE_DIR) -> Dict[str, Any]:
        report = {
            "root": root_path,
            "languages": [],
            "frameworks": [],
            "frontend_ui": [],
            "backend": [],
            "mobile": [],
            "databases": [],
            "devops": [],
            "architecture": "Monolito Estándar",
            "is_monorepo": False,
            "monorepo_type": None,
            "metrics": {
                "total_files": 0,
                "code_files": 0,
                "test_files": 0,
                "has_git": os.path.isdir(os.path.join(root_path, '.git')),
                "has_docker": False,
                "has_ci": False
            },
            "recommended_skills": []
        }
        
        # Monorepo detection
        for cfg, name, arch in [
            ('pnpm-workspace.yaml', 'pnpm workspaces', 'Monorepo (pnpm)'),
            ('turbo.json', 'Turborepo', 'Monorepo (Turbo)'),
            ('nx.json', 'Nx', 'Monorepo (Nx)'),
            ('lerna.json', 'Lerna', 'Monorepo (Lerna)')
        ]:
            if os.path.isfile(os.path.join(root_path, cfg)):
                report["is_monorepo"] = True
                report["monorepo_type"] = name
                report["architecture"] = arch
                break
        
        # Package.json / Node detection
        pkg_path = os.path.join(root_path, 'package.json')
        if os.path.isfile(pkg_path):
            report["languages"].append("JavaScript / TypeScript")
            try:
                with open(pkg_path, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                    deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
                    
                    framework_map = {
                        'react': ("React", ["emil-design-eng", "animate", "taste-skill"]),
                        'next': ("Next.js", ["claude-seo", "high-end-visual-design"]),
                        'vue': ("Vue.js", []),
                        'svelte': ("Svelte", []),
                        '@sveltejs/kit': ("SvelteKit", []),
                        'astro': ("Astro", ["claude-seo"]),
                    }
                    
                    for dep, (name, skills) in framework_map.items():
                        if dep in deps:
                            report["frameworks"].append(name)
                            report["recommended_skills"].extend(skills)
                    
                    ui_map = {
                        'tailwindcss': ("Tailwind CSS", ["tailwind-theme-builder"]),
                        '@tailwindcss/vite': ("Tailwind CSS", ["tailwind-theme-builder"]),
                        'framer-motion': ("Framer Motion", ["animate"]),
                        'motion': ("Framer Motion", ["animate"]),
                        'gsap': ("GSAP", ["gsap-framer-scroll-animation"]),
                        'sonner': ("Sonner Toasts", ["ask-sonner"]),
                    }
                    
                    for dep, (name, skills) in ui_map.items():
                        if dep in deps:
                            report["frontend_ui"].append(name)
                            report["recommended_skills"].extend(skills)
                    
                    backend_map = {
                        'express': ("Node.js API", ["nodejs-backend-patterns"]),
                        'fastify': ("Node.js API", ["nodejs-backend-patterns"]),
                        'koa': ("Node.js API", ["nodejs-backend-patterns"]),
                        '@nestjs/core': ("NestJS", []),
                        'prisma': ("Prisma ORM", []),
                        '@prisma/client': ("Prisma ORM", []),
                        'drizzle-orm': ("Drizzle ORM", []),
                        'pg': ("PostgreSQL", ["postgres-patterns"]),
                        'postgres': ("PostgreSQL", ["postgres-patterns"]),
                        'react-native': ("Expo / React Native", ["expo-overview", "animate-expo"]),
                        'expo': ("Expo / React Native", ["expo-overview", "animate-expo"]),
                    }
                    
                    for dep, (name, skills) in backend_map.items():
                        if dep in deps:
                            if 'react-native' in deps or 'expo' in deps:
                                report["mobile"].append(name)
                            elif dep in ('prisma', '@prisma/client', 'drizzle-orm', 'pg', 'postgres'):
                                report["databases"].append(name)
                            elif dep in ('express', 'fastify', 'koa', '@nestjs/core'):
                                report["backend"].append(name)
                            else:
                                report["frameworks"].append(name)
                            report["recommended_skills"].extend(skills)
            except Exception:
                pass

        # Python detection
        py_files = ['requirements.txt', 'pyproject.toml', 'Pipfile', 'setup.py', 'poetry.lock']
        if any(os.path.isfile(os.path.join(root_path, f)) for f in py_files):
            report["languages"].append("Python")
            report["recommended_skills"].append("python-patterns")
            for req_file in ['requirements.txt', 'pyproject.toml']:
                p = os.path.join(root_path, req_file)
                if os.path.isfile(p):
                    try:
                        content = open(p, 'r', encoding='utf-8', errors='ignore').read().lower()
                        for fw in ['fastapi', 'django', 'flask']:
                            if fw in content:
                                report["frameworks"].append(fw.title())
                        if 'sqlalchemy' in content:
                            report["databases"].append("SQLAlchemy")
                    except Exception:
                        pass

        # Go
        if os.path.isfile(os.path.join(root_path, 'go.mod')):
            report["languages"].append("Go")
            report["backend"].append("Go Microservices")
            report["recommended_skills"].append("golang-patterns")

        # Rust
        if os.path.isfile(os.path.join(root_path, 'Cargo.toml')):
            report["languages"].append("Rust")
            report["backend"].append("Rust Engine")
            report["recommended_skills"].append("rust-patterns")

        # .NET
        if glob.glob(os.path.join(root_path, '*.csproj')) or glob.glob(os.path.join(root_path, '*.sln')):
            report["languages"].append("C# / .NET")
            report["backend"].append(".NET Core")
            report["recommended_skills"].append("dotnet-patterns")

        # Flutter
        if os.path.isfile(os.path.join(root_path, 'pubspec.yaml')):
            report["languages"].append("Dart")
            report["mobile"].append("Flutter")
            report["recommended_skills"].extend(["flutter-apply-architecture-best-practices", "flutter-build-responsive-layout"])

        # DevOps
        if os.path.isfile(os.path.join(root_path, 'Dockerfile')) or os.path.isfile(os.path.join(root_path, 'docker-compose.yml')):
            report["devops"].append("Docker")
            report["metrics"]["has_docker"] = True
            report["recommended_skills"].append("docker-patterns")
        
        if os.path.isdir(os.path.join(root_path, '.github', 'workflows')):
            report["devops"].append("GitHub Actions")
            report["metrics"]["has_ci"] = True
            report["recommended_skills"].append("github-actions-cicd")
            
        if os.path.isfile(os.path.join(root_path, 'wrangler.toml')) or os.path.isfile(os.path.join(root_path, 'wrangler.json')):
            report["devops"].append("Cloudflare Workers")
            report["recommended_skills"].append("cloudflare-worker-builder")

        report["recommended_skills"] = list(dict.fromkeys(report["recommended_skills"]))
        return report

# =============================================================================
# 5. ACTIVE SKILL MANIFEST CONTROLLER
# =============================================================================
class ManifestController:
    """Gestiona la carga, guardado, activación y desactivación de skills del proyecto."""
    
    @staticmethod
    def load_active_manifest() -> Dict[str, Any]:
        if os.path.isfile(ACTIVE_MANIFEST):
            try:
                with open(ACTIVE_MANIFEST, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                pass
        
        default_skills = []
        for c in MANDATORY_CORE_SUITE:
            default_skills.append({
                "name": c["name"],
                "category": c["category"],
                "reason": c["reason"],
                "is_core": True,
                "mandatory_view": True
            })
        
        return {
            "project_name": os.path.basename(WORKSPACE_DIR),
            "project_phase": "0-to-1 MVP / Desarrollo Activo",
            "objectives": ["YAGNI Architecture", "UI Polish", "Automated Testing", "Security Compliance"],
            "active_skills": default_skills,
            "mandatory_protocol": "EL AGENTE AI DEBE INVOCAR view_file EN CADA SKILL.md ANTES DE ESCRIBIR CÓDIGO."
        }

    @staticmethod
    def save_active_manifest(data: Dict[str, Any]) -> None:
        os.makedirs(AGENTS_DIR, exist_ok=True)
        
        existing_names = {s["name"] for s in data.get("active_skills", [])}
        for core in MANDATORY_CORE_SUITE:
            if core["name"] not in existing_names:
                data["active_skills"].insert(0, {
                    "name": core["name"],
                    "category": core["category"],
                    "reason": core["reason"],
                    "is_core": True,
                    "mandatory_view": True
                })
        
        with open(ACTIVE_MANIFEST, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        ManifestController._write_qualification_doc(data)

    @staticmethod
    def _write_qualification_doc(data: Dict[str, Any]) -> None:
        with open(QUALIFICATION_DOC, 'w', encoding='utf-8') as f:
            f.write(f"# 🛡️ Manifiesto de Cualificación del Proyecto — SuperDuperSkills\n\n")
            f.write(f"**Proyecto:** `{data.get('project_name', os.path.basename(WORKSPACE_DIR))}`\n")
            f.write(f"**Fase Actual:** {data.get('project_phase', 'Desarrollo')}\n")
            f.write(f"**Objetivos Clave:** {', '.join(data.get('objectives', []))}\n\n")
            f.write(f"## ⛔ Protocolo de Seguridad y Lectura Mandatoria\n")
            f.write(f"> [!IMPORTANT]\n")
            f.write(f"> **TODO AGENTE AI TIENE PROHIBIDO ESCRIBIR CÓDIGO** sin haber invocado antes `view_file` en cada uno de los archivos `SKILL.md` listados en esta matriz.\n\n")
            f.write(f"| # | Categoría | Skill | Propósito / Razón | Estado | Ruta Local |\n")
            f.write(f"|---|-----------|-------|-------------------|--------|------------|\n")
            
            for idx, sk in enumerate(data.get("active_skills", []), 1):
                sk_name = sk["name"]
                sk_cat = sk.get("category", "CUSTOM")
                sk_reason = sk.get("reason", "Activada manualmente por el usuario.")
                path_local = os.path.join(SKILLS_DIR, sk_name, 'SKILL.md')
                exists_icon = "✅ Localizada" if os.path.isfile(path_local) else "⚠️ Pendiente Ingesta"
                link_url = f"[`skills/{sk_name}/SKILL.md`](file:///{path_local.replace(chr(92), '/')})"
                f.write(f"| {idx:02d} | {sk_cat} | `{sk_name}` | {sk_reason} | {exists_icon} | {link_url} |\n")

    @staticmethod
    def toggle_skill(skill_name: str, force_state: Optional[bool] = None) -> Tuple[bool, str]:
        manifest = ManifestController.load_active_manifest()
        skills = manifest.get("active_skills", [])
        
        if any(c["name"] == skill_name for c in MANDATORY_CORE_SUITE):
            return False, f"{C.YELLOW}⚠️  '{skill_name}' is CORE — cannot be disabled.{C.RESET}"
            
        for idx, s in enumerate(skills):
            if s["name"] == skill_name:
                if force_state is True:
                    return True, f"{C.GRAY}ℹ️  '{skill_name}' is already active.{C.RESET}"
                skills.pop(idx)
                ManifestController.save_active_manifest(manifest)
                return True, f"{C.RED}🔴 '{skill_name}' deactivated.{C.RESET}"
        
        if force_state is False:
            return True, f"{C.GRAY}ℹ️  '{skill_name}' is already inactive.{C.RESET}"
        skills.append({
            "name": skill_name,
            "category": "USER_SELECTED",
            "reason": "Enabled interactively by user.",
            "is_core": False,
            "mandatory_view": True
        })
        ManifestController.save_active_manifest(manifest)
        return True, f"{C.GREEN}🟢 '{skill_name}' activated and added to manifest.{C.RESET}"

# =============================================================================
# 6. SKILL VAULT SEARCH & REMOTE INGESTION
# =============================================================================
class SkillVaultEngine:
    """Busca en el repositorio local o ingesta nuevas habilidades remotas."""
    
    @staticmethod
    def search_local(query: str, limit: int = 30) -> List[Dict[str, str]]:
        query_norm = query.lower().strip()
        results = []
        
        if not os.path.isdir(SKILLS_DIR):
            return results
            
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        try:
            with os.scandir(SKILLS_DIR) as entries:
                for entry in entries:
                    if entry.is_dir():
                        name = entry.name
                        if query_norm in name.lower():
                            # Try to read the first line of SKILL.md for preview
                            preview = f"Skill '{name}' in SuperDuperSkills vault."
                            sk_md = os.path.join(SKILLS_DIR, name, 'SKILL.md')
                            if os.path.isfile(sk_md):
                                try:
                                    with open(sk_md, 'r', encoding='utf-8', errors='ignore') as sf:
                                        for line in sf:
                                            line = line.strip()
                                            if line and not line.startswith('---') and not line.startswith('#') and not line.startswith('name:') and not line.startswith('description:'):
                                                preview = line[:100]
                                                break
                                except Exception:
                                    pass
                            
                            results.append({
                                "name": name,
                                "active": name in active_names,
                                "is_core": any(c["name"] == name for c in MANDATORY_CORE_SUITE),
                                "preview": preview
                            })
                            if len(results) >= limit:
                                return results
        except Exception:
            pass
        return results

    @staticmethod
    def ingest_remote_skill(name_or_url: str, category: str = "INGESTED") -> Tuple[bool, str]:
        clean_name = re.sub(r'[^a-zA-Z0-9\-_]', '', name_or_url.split('/')[-1].lower())
        if not clean_name:
            clean_name = "custom-skill"
            
        target_dir = os.path.join(SKILLS_DIR, clean_name)
        os.makedirs(target_dir, exist_ok=True)
        sk_path = os.path.join(target_dir, 'SKILL.md')
        
        content = f"""---
name: {clean_name}
description: Habilidad ingerida y registrada via SuperDuperSkills CLI ({name_or_url})
metadata:
  source: '{name_or_url}'
  category: '{category}'
---

# {clean_name.replace('-', ' ').title()}

Habilidad creada e integrada por el usuario a través del orquestador.
"""
        with open(sk_path, 'w', encoding='utf-8') as f:
            f.write(content.strip() + "\n")
            
        ManifestController.toggle_skill(clean_name, force_state=True)
        return True, f"{C.GREEN}✨ Skill '{clean_name}' ingested at {sk_path} and activated.{C.RESET}"

# =============================================================================
# 7. MULTI-CLI AGENT SYNCHRONIZER
# =============================================================================
class MultiCLISync:
    """Sincroniza las skills activas hacia los entornos de los agentes más populares."""
    
    @staticmethod
    def sync_all() -> Dict[str, str]:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        results = {}
        
        # Cursor Rules Sync
        cursor_dir = os.path.join(WORKSPACE_DIR, '.cursor', 'rules')
        os.makedirs(cursor_dir, exist_ok=True)
        cursor_file = os.path.join(cursor_dir, 'superduperskills.mdc')
        with open(cursor_file, 'w', encoding='utf-8') as f:
            f.write(f"---\ndescription: SuperDuperSkills Active Matrix Rules\nglobs: *\n---\n\n")
            f.write(f"# SuperDuperSkills — Active Matrix Governance\n\n")
            f.write(f"Before editing code, the Cursor Agent MUST consult and execute `view_file` on:\n")
            for sk in active_skills:
                f.write(f"- `skills/{sk['name']}/SKILL.md` ({sk.get('reason', '')})\n")
        results["Cursor"] = cursor_file

        # OpenCode / Claude compatibility
        opencode_file = os.path.join(AGENTS_DIR, 'opencode-active.json')
        with open(opencode_file, 'w', encoding='utf-8') as f:
            json.dump({
                "source": "superduperskills",
                "version": __version__,
                "active_count": len(active_skills),
                "skills": [s["name"] for s in active_skills]
            }, f, indent=2)
        results["OpenCode & Claude"] = opencode_file
        
        return results

    @staticmethod
    def audit_compliance() -> Dict[str, Any]:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        
        missing = []
        found = []
        
        for sk in active_skills:
            p = os.path.join(SKILLS_DIR, sk["name"], "SKILL.md")
            if os.path.isfile(p):
                found.append(sk["name"])
            else:
                missing.append(sk["name"])
                
        return {
            "total_active": len(active_skills),
            "found_count": len(found),
            "missing_count": len(missing),
            "missing_skills": missing,
            "status": "PASSED" if not missing else "WARNING_MISSING_FILES"
        }

    @staticmethod
    def doctor_check() -> Dict[str, Any]:
        """Environment health check (Agent 4: doctor command)."""
        checks = []
        
        # Python version
        py_ver = platform.python_version()
        py_ok = sys.version_info >= (3, 8)
        checks.append({
            "name": "Python Version",
            "status": "PASS" if py_ok else "FAIL",
            "detail": f"Python {py_ver}" + ("" if py_ok else " (requires >= 3.8)")
        })
        
        # Skills directory
        skills_exist = os.path.isdir(SKILLS_DIR)
        skill_count = 0
        if skills_exist:
            try:
                skill_count = sum(1 for e in os.scandir(SKILLS_DIR) if e.is_dir())
            except Exception:
                pass
        checks.append({
            "name": "Skills Directory",
            "status": "PASS" if skills_exist and skill_count > 0 else "WARN" if skills_exist else "FAIL",
            "detail": f"{skill_count} skills found in {SKILLS_DIR}" if skills_exist else f"Missing: {SKILLS_DIR}"
        })
        
        # .agents directory
        agents_exist = os.path.isdir(AGENTS_DIR)
        checks.append({
            "name": ".agents Directory",
            "status": "PASS" if agents_exist else "WARN",
            "detail": f"Found at {AGENTS_DIR}" if agents_exist else "Run 'init' to create"
        })
        
        # Active manifest
        manifest_exists = os.path.isfile(ACTIVE_MANIFEST)
        checks.append({
            "name": "Active Manifest",
            "status": "PASS" if manifest_exists else "WARN",
            "detail": ACTIVE_MANIFEST if manifest_exists else "Run 'init' or 'scan' to generate"
        })
        
        # Git
        git_exists = os.path.isdir(os.path.join(WORKSPACE_DIR, '.git'))
        checks.append({
            "name": "Git Repository",
            "status": "PASS" if git_exists else "INFO",
            "detail": "Initialized" if git_exists else "Not a git repo"
        })
        
        # Disk space
        try:
            disk = shutil.disk_usage(WORKSPACE_DIR)
            free_gb = disk.free / (1024**3)
            checks.append({
                "name": "Disk Space",
                "status": "PASS" if free_gb > 1 else "WARN",
                "detail": f"{free_gb:.1f} GB free"
            })
        except Exception:
            pass
        
        return {
            "checks": checks,
            "all_pass": all(c["status"] == "PASS" for c in checks),
            "has_warnings": any(c["status"] == "WARN" for c in checks),
            "has_failures": any(c["status"] == "FAIL" for c in checks)
        }

    @staticmethod
    def get_stats() -> Dict[str, Any]:
        """Collect statistics about skills usage (Agent 4: stats command)."""
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        
        # Count skills on disk
        total_disk = 0
        if os.path.isdir(SKILLS_DIR):
            try:
                total_disk = sum(1 for e in os.scandir(SKILLS_DIR) if e.is_dir())
            except Exception:
                pass
        
        # Category breakdown
        cat_counts = {}
        for sk in active_skills:
            cat = sk.get("category", "CUSTOM")
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
        
        # Core vs specialized
        core_count = sum(1 for sk in active_skills if sk.get("is_core", False))
        spec_count = len(active_skills) - core_count
        
        return {
            "total_catalog": total_disk,
            "total_active": len(active_skills),
            "core_count": core_count,
            "specialized_count": spec_count,
            "categories": cat_counts,
            "manifest_path": ACTIVE_MANIFEST,
            "project_name": manifest.get("project_name", "unknown")
        }


# =============================================================================
# 8. DESKTOP APP INTEGRATION (AGENT 5)
# =============================================================================
class DesktopIntegration:
    """Desktop app support hooks — Electron wrapper config, tray icon, auto-scan."""
    
    @staticmethod
    def generate_electron_config() -> Dict[str, Any]:
        """Generate Electron wrapper configuration."""
        return {
            "name": "SuperDuperSkills Desktop",
            "version": __version__,
            "main": "main.js",
            "window": {
                "width": 1200,
                "height": 800,
                "title": f"SuperDuperSkills v{__version__} — Agentic CLI Hub",
                "icon": os.path.join(WORKSPACE_DIR, "icon-512.png"),
                "darkTheme": True
            },
            "tray": {
                "enabled": True,
                "icon": os.path.join(WORKSPACE_DIR, "icon-192.png"),
                "tooltip": f"SuperDuperSkills v{__version__}",
                "menu": ["Open CLI", "Scan Project", "View Active Skills", "Quit"]
            },
            "autoScan": {
                "enabled": True,
                "onLaunch": True,
                "intervalMinutes": 30
            },
            "terminal": {
                "type": "xterm",
                "fontSize": 14,
                "fontFamily": "JetBrains Mono, Fira Code, monospace",
                "theme": {
                    "background": "#0c0e13",
                    "foreground": "#e8e6e1",
                    "cursorAccent": "#00e5a0",
                    "selectionBackground": "rgba(0, 229, 160, 0.3)"
                }
            }
        }
    
    @staticmethod
    def save_desktop_config():
        """Save desktop integration config to .agents/desktop.json."""
        os.makedirs(AGENTS_DIR, exist_ok=True)
        config = DesktopIntegration.generate_electron_config()
        with open(DESKTOP_CONFIG, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        return DESKTOP_CONFIG
    
    @staticmethod
    def generate_electron_main() -> str:
        """Generate the Electron main.js entry point."""
        return '''// SuperDuperSkills Desktop — Electron Main Process
const { app, BrowserWindow, Tray, Menu, shell } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let tray;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    title: 'SuperDuperSkills Desktop',
    icon: path.join(__dirname, '..', 'icon-512.png'),
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    backgroundColor: '#0c0e13'
  });

  mainWindow.loadURL('data:text/html,<html><body style="background:#0c0e13;color:#e8e6e1;font-family:monospace;display:flex;align-items:center;justify-content:center;height:100vh;"><h1>🚀 SuperDuperSkills Desktop</h1><p>Terminal launching...</p></body></html>');
  
  // Open external links in browser
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

function createTray() {
  tray = new Tray(path.join(__dirname, '..', 'icon-192.png'));
  tray.setToolTip('SuperDuperSkills v4.0');
  
  const contextMenu = Menu.buildFromTemplate([
    { label: 'Open CLI', click: () => mainWindow?.show() },
    { label: 'Scan Project', click: () => { /* trigger scan */ } },
    { type: 'separator' },
    { label: 'Quit', click: () => app.quit() }
  ]);
  
  tray.setContextMenu(contextMenu);
  tray.on('double-click', () => mainWindow?.show());
}

app.whenReady().then(() => {
  createWindow();
  createTray();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
'''


# =============================================================================
# 9. TUI DISPLAY FUNCTIONS (AGENT 3: IMPROVED UX)
# =============================================================================
def print_header(title: str, show_status: bool = True):
    """Print the styled header with optional status bar."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(MINI_LOGO)
    print(f"  {C.CYAN}{C.BOLD}▸ {title}{C.RESET}")
    print(f"  {C.GRAY}{'─' * 60}{C.RESET}\n")
    
    if show_status:
        manifest = ManifestController.load_active_manifest()
        active = manifest.get("active_skills", [])
        core_count = sum(1 for s in active if s.get("is_core", False))
        spec_count = len(active) - core_count
        
        # Count catalog
        cat_count = 0
        if os.path.isdir(SKILLS_DIR):
            try:
                cat_count = sum(1 for e in os.scandir(SKILLS_DIR) if e.is_dir())
            except Exception:
                pass
        
        print(f"  {C.GRAY}├─{C.RESET} {C.DIM}Workspace:{C.RESET} {C.WHITE}{WORKSPACE_DIR}{C.RESET}")
        print(f"  {C.GRAY}├─{C.RESET} {C.DIM}Active:{C.RESET}   {C.GREEN}{C.BOLD}{len(active)}{C.RESET} skills {C.GRAY}({core_count} core + {spec_count} specialized){C.RESET}")
        print(f"  {C.GRAY}├─{C.RESET} {C.DIM}Catalog:{C.RESET}  {C.CYAN}{cat_count}{C.RESET} skills indexed")
        print(f"  {C.GRAY}└─{C.RESET} {C.DIM}Version:{C.RESET}  {C.YELLOW}v{__version__} «{__codename__}»{C.RESET}\n")

def print_divider(char: str = "─", width: int = 60):
    print(f"  {C.GRAY}{char * width}{C.RESET}")

def print_section(title: str):
    print(f"\n  {C.BOLD}{C.CYAN}{title}{C.RESET}")
    print_divider()

def print_cmd_hint(cmd: str, desc: str):
    print(f"    {C.GREEN}$ sds {cmd:<24}{C.RESET} {C.GRAY}{desc}{C.RESET}")

def print_footer():
    print(f"\n  {C.GRAY}{'─' * 60}{C.RESET}")
    print(f"  {C.DIM}Tip: Use {C.CYAN}sds <command> --help{C.DIM} for command details{C.RESET}")
    print(f"  {C.DIM}Tip: Run {C.CYAN}sds{C.DIM} without arguments for interactive TUI{C.RESET}\n")


# =============================================================================
# 10. INTERACTIVE TUI INTERFACE (AGENT 3: IMPROVED)
# =============================================================================
def run_interactive_tui():
    """Bucle principal de la interfaz interactiva con menús mejorados."""
    while True:
        print_header("COMMAND CENTER — MAIN MENU")
        
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        active_count = len(active_skills)
        core_count = sum(1 for s in active_skills if s.get("is_core", False))
        
        # Menu items with icons and descriptions
        menu_items = [
            ("1", "🔍", "Deep Project Discovery",    "Scan stack, monorepos & frameworks"),
            ("2", "🔒", "Core Invariant Suite",       "View & verify 19 mandatory skills"),
            ("3", "🎛️ ", "Category Manager & Toggle",  "Enable/disable by category"),
            ("4", "🔎", "Vault Search",               "Search 2,700+ skills in real-time"),
            ("5", "📥", "Skill Seekers — Ingest",     "Import remote skill by URL"),
            ("6", "🔄", "Multi-CLI Sync",             "Sync to Cursor, Claude, Gemini, Codex"),
            ("7", "🧪", "Compliance Audit",           "Verify SKILL.md files exist"),
            ("8", "🧙", "Qualification Wizard",       "Full Socratic interview wizard"),
            ("9", "📊", "Stats & Dashboard",          "View usage statistics"),
            ("d", "🩺", "Doctor — Health Check",      "Environment diagnostics"),
            ("e", "📤", "Export Manifest",            "Export to JSON or Markdown"),
            ("i", "📦", "Init Project",               "Initialize .agents/ directory"),
            ("p", "💼", "Profile Manager",            "Save/load skill profiles"),
        ]
        
        for num, icon, title, desc in menu_items:
            color = C.YELLOW if num.isdigit() else C.MAGENTA
            print(f"  {color}{C.BOLD}[{num:>2}]{C.RESET} {icon} {C.BOLD}{title:<28}{C.RESET} {C.GRAY}{desc}{C.RESET}")
        
        print(f"\n  {C.RED}{C.BOLD}[ 0]{C.RESET} 🚪 {C.BOLD}Exit{C.RESET}")
        
        choice = input(f"\n  {C.CYAN}{C.BOLD}❯{C.RESET} {C.CYAN}Select option:{C.RESET} ").strip().lower()
        
        handlers = {
            '1': view_project_discovery,
            '2': view_core_suite,
            '3': view_category_manager,
            '4': view_vault_search,
            '5': view_skill_ingestion,
            '6': view_sync_multicli,
            '7': view_compliance_audit,
            '8': lambda: run_qualification_wizard(),
            '9': view_stats_dashboard,
            'd': view_doctor,
            'e': view_export,
            'i': view_init_project,
            'p': view_profile_manager,
        }
        
        if choice in ('0', 'q', 'exit', 'quit'):
            print(f"\n  {C.GREEN}✨ Session ended. Happy hacking!{C.RESET}\n")
            break
        elif choice in handlers:
            try:
                handlers[choice]()
            except KeyboardInterrupt:
                print(f"\n  {C.GRAY}Cancelled.{C.RESET}")
            except Exception as e:
                print(f"\n  {C.RED}Error: {e}{C.RESET}")
            input(f"\n  {C.GREEN}Press ENTER to return...{C.RESET}")
        else:
            input(f"\n  {C.RED}⚠️  Unknown option. Press ENTER to retry...{C.RESET}")


def view_project_discovery():
    print_header("DEEP PROJECT DISCOVERY")
    
    report = run_with_spinner("Analyzing project structure", ProjectDiscovery.inspect)
    if report is None:
        report = ProjectDiscovery.inspect()
    
    print_section("📋 Scan Results")
    
    fields = [
        ("📦 Architecture", report['architecture'], C.CYAN),
        ("💻 Languages", ', '.join(report['languages']) or 'Agnostic', C.WHITE),
        ("⚛️  Frameworks", ', '.join(report['frameworks']) or 'None detected', C.GREEN),
        ("🎨 UI & Motion", ', '.join(report['frontend_ui']) or 'Standard CSS', C.MAGENTA),
        ("⚡ Backend & DB", ', '.join(report['backend'] + report['databases']) or 'N/A', C.YELLOW),
        ("🚀 DevOps/Infra", ', '.join(report['devops']) or 'No Docker/CI', C.BLUE),
    ]
    
    for label, value, color in fields:
        print(f"    {C.BOLD}{label}:{C.RESET}  {color}{value}{C.RESET}")
    
    if report["recommended_skills"]:
        print_section("🎯 Recommended Skills for This Stack")
        for idx, s in enumerate(report["recommended_skills"], 1):
            print(f"    {C.GREEN}[{idx:02d}]{C.RESET} {C.BOLD}{s}{C.RESET}")
        
        if print_confirm("Activate all recommended skills automatically?", default_yes=True):
            for s in report["recommended_skills"]:
                ManifestController.toggle_skill(s, force_state=True)
            print(f"\n    {C.GREEN}✅ All recommended skills activated!{C.RESET}")
    else:
        print(f"\n    {C.GRAY}No specific skill recommendations for this directory.{C.RESET}")


def view_core_suite():
    print_header("🔒 CORE INVARIANT SUITE — 19 MANDATORY SKILLS")
    
    print(f"  {C.GRAY}These skills load unconditionally in every project:{C.RESET}\n")
    
    for idx, core in enumerate(MANDATORY_CORE_SUITE, 1):
        path = os.path.join(SKILLS_DIR, core["name"], "SKILL.md")
        icon = core.get("icon", "•")
        if os.path.isfile(path):
            status = f"{C.GREEN}✅ AVAILABLE{C.RESET}"
        else:
            status = f"{C.YELLOW}⚠️  PENDING INGESTION{C.RESET}"
        print(f"    {C.BOLD}{idx:02d}.{C.RESET} {icon} {C.BOLD}{core['name']:<24}{C.RESET} {status}")
        print(f"        {C.GRAY}{core['reason']}{C.RESET}")
    
    print(f"\n  {C.MAGENTA}ℹ️  Core skills are governance-locked and cannot be disabled.{C.RESET}")


def view_category_manager():
    while True:
        print_header("🎛️  CATEGORY MANAGER & INDIVIDUAL TOGGLE")
        
        categories = list(CATEGORY_REGISTRY.keys())
        for idx, cat_key in enumerate(categories, 1):
            cat_data = CATEGORY_REGISTRY[cat_key]
            print(f"  {C.YELLOW}{C.BOLD}[{idx}]{C.RESET} {cat_data['title']} {C.GRAY}({len(cat_data['skills'])} skills){C.RESET}")
        
        print(f"\n  {C.RED}{C.BOLD}[0]{C.RESET} ↩️  Back to main menu\n")
        
        choice = input(f"  {C.CYAN}❯ Select category [1-{len(categories)}]:{C.RESET} ").strip()
        if choice in ('0', 'q', 'b'):
            break
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            manage_single_category(categories[int(choice) - 1])
        else:
            print(f"\n  {C.RED}⚠️ Invalid option.{C.RESET}")


def manage_single_category(cat_key: str):
    cat_data = CATEGORY_REGISTRY[cat_key]
    
    while True:
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        print_header(f"CATEGORY: {cat_data['title']}")
        
        for idx, (sk_name, desc) in enumerate(cat_data["skills"], 1):
            is_active = sk_name in active_names
            if is_active:
                badge = f"{C.GREEN}[ON ]{C.RESET}"
            else:
                badge = f"{C.GRAY}[OFF]{C.RESET}"
            print(f"    {C.BOLD}[{idx:02d}]{C.RESET} {badge} {C.BOLD}{sk_name:<30}{C.RESET} {C.GRAY}{desc}{C.RESET}")
        
        print(f"\n    {C.GREEN}[A]{C.RESET} Enable all  |  {C.YELLOW}[D]{C.RESET} Disable all  |  {C.RED}[0]{C.RESET} Back")
        
        action = input(f"\n  {C.CYAN}❯ Toggle skill # or action:{C.RESET} ").strip().upper()
        
        if action in ('0', 'Q'):
            break
        elif action == 'A':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=True)
            print(f"\n  {C.GREEN}✅ All skills in category activated.{C.RESET}")
        elif action == 'D':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=False)
            print(f"\n  {C.YELLOW}⚠️ All non-core skills in category deactivated.{C.RESET}")
        elif action.isdigit() and 1 <= int(action) <= len(cat_data["skills"]):
            target = cat_data["skills"][int(action) - 1][0]
            _, msg = ManifestController.toggle_skill(target)
            print(f"\n  {msg}")
        else:
            print(f"\n  {C.RED}Command not recognized.{C.RESET}")


def view_vault_search():
    print_header("🔎 LIVE VAULT SEARCH (2,700+ SKILLS)")
    query = input(f"  {C.CYAN}❯ Search term (e.g., nextjs, auth, tdd, react, anim):{C.RESET} ").strip()
    
    if not query:
        return
    
    results = run_with_spinner(f"Searching vault for '{query}'", SkillVaultEngine.search_local, query, 25)
    if results is None:
        results = SkillVaultEngine.search_local(query, 25)
    
    if not results:
        print(f"\n  {C.YELLOW}No skills found matching '{query}'.{C.RESET}")
        return
    
    print(f"\n  {C.GREEN}Found {len(results)} matches:{C.RESET}\n")
    for idx, res in enumerate(results, 1):
        if res["active"]:
            badge = f"{C.GREEN}[ON ]{C.RESET}"
        else:
            badge = f"{C.GRAY}[OFF]{C.RESET}"
        core = f" {C.MAGENTA}[CORE]{C.RESET}" if res["is_core"] else ""
        print(f"    {C.BOLD}[{idx:02d}]{C.RESET} {badge}{core} {C.BOLD}{res['name']:<30}{C.RESET} {C.GRAY}{res['preview'][:60]}{C.RESET}")
    
    ans = input(f"\n  {C.CYAN}❯ Enter skill # to toggle (or 0 to go back):{C.RESET} ").strip()
    if ans.isdigit() and 1 <= int(ans) <= len(results):
        sel = results[int(ans) - 1]
        _, msg = ManifestController.toggle_skill(sel["name"])
        print(f"\n  {msg}")


def view_skill_ingestion():
    print_header("📥 SKILL SEEKERS — INGEST REMOTE SKILL")
    print(f"  {C.GRAY}Import a new skill by providing its GitHub URL or a unique name:{C.RESET}\n")
    print(f"    Example URL:    {C.WHITE}https://github.com/author/my-new-skill{C.RESET}")
    print(f"    Example Name:   {C.WHITE}my-custom-skill{C.RESET}\n")
    
    target = input(f"  {C.CYAN}❯ URL or skill name:{C.RESET} ").strip()
    if not target:
        return
    
    _, msg = SkillVaultEngine.ingest_remote_skill(target)
    print(f"\n  {msg}")


def view_sync_multicli():
    print_header("🔄 MULTI-CLI SYNCHRONIZER")
    
    synced = run_with_spinner("Syncing manifest to agent environments", MultiCLISync.sync_all)
    if synced is None:
        synced = MultiCLISync.sync_all()
    
    for agent_host, path in synced.items():
        print(f"    {C.GREEN}✓{C.RESET} {C.BOLD}{agent_host:<20}{C.RESET} → {C.CYAN}{path}{C.RESET}")
    
    print(f"\n  {C.GREEN}✨ Agent manifests and rules synchronized successfully!{C.RESET}")


def view_compliance_audit():
    print_header("🧪 AGENTIC COMPLIANCE AUDIT")
    
    audit = run_with_spinner("Verifying SKILL.md file integrity", MultiCLISync.audit_compliance)
    if audit is None:
        audit = MultiCLISync.audit_compliance()
    
    print_section("Audit Results")
    print(f"    Total active skills:      {C.WHITE}{audit['total_active']}{C.RESET}")
    print(f"    SKILL.md files found:     {C.GREEN}{audit['found_count']}{C.RESET}")
    print(f"    Missing files:            {C.RED if audit['missing_count'] > 0 else C.GREEN}{audit['missing_count']}{C.RESET}")
    
    if audit['missing_count'] > 0:
        print(f"\n  {C.RED}⚠️ Active skills without physical SKILL.md:{C.RESET}")
        for m in audit['missing_skills']:
            print(f"    {C.RED}•{C.RESET} {m}")
    else:
        print(f"\n  {C.GREEN}✅ 100% compliance — all active skills have SKILL.md files ready for view_file invocation.{C.RESET}")


def view_stats_dashboard():
    """Agent 4: Stats Dashboard command."""
    print_header("📊 STATISTICS & DASHBOARD")
    
    stats = MultiCLISync.get_stats()
    
    print_section("Project Overview")
    print(f"    {C.BOLD}Project:{C.RESET}       {C.WHITE}{stats['project_name']}{C.RESET}")
    print(f"    {C.BOLD}Manifest:{C.RESET}      {C.GRAY}{stats['manifest_path']}{C.RESET}")
    
    print_section("Skill Counts")
    print(f"    {C.BOLD}Total Catalog:{C.RESET}  {C.CYAN}{stats['total_catalog']}{C.RESET} skills on disk")
    print(f"    {C.BOLD}Total Active:{C.RESET}   {C.GREEN}{stats['total_active']}{C.RESET} skills in manifest")
    print(f"    {C.BOLD}Core Skills:{C.RESET}    {C.MAGENTA}{stats['core_count']}{C.RESET} mandatory")
    print(f"    {C.BOLD}Specialized:{C.RESET}    {C.YELLOW}{stats['specialized_count']}{C.RESET} user-selected")
    
    if stats['categories']:
        print_section("Breakdown by Category")
        for cat, count in sorted(stats['categories'].items(), key=lambda x: -x[1]):
            bar = "█" * min(count, 30)
            print(f"    {cat:<20} {C.GREEN}{bar}{C.RESET} {count}")


def view_doctor():
    """Agent 4: Doctor command."""
    print_header("🩺 ENVIRONMENT DOCTOR — HEALTH CHECK")
    
    result = run_with_spinner("Running diagnostics", MultiCLISync.doctor_check)
    if result is None:
        result = MultiCLISync.doctor_check()
    
    print_section("Diagnostic Results")
    
    for check in result['checks']:
        if check['status'] == 'PASS':
            icon = f"{C.GREEN}✓ PASS{C.RESET}"
        elif check['status'] == 'WARN':
            icon = f"{C.YELLOW}⚠ WARN{C.RESET}"
        elif check['status'] == 'FAIL':
            icon = f"{C.RED}✗ FAIL{C.RESET}"
        else:
            icon = f"{C.GRAY}ℹ INFO{C.RESET}"
        
        print(f"    {icon}  {C.BOLD}{check['name']:<20}{C.RESET} {C.GRAY}{check['detail']}{C.RESET}")
    
    print()
    if result['all_pass']:
        print(f"  {C.GREEN}🎉 All checks passed! Environment is healthy.{C.RESET}")
    elif result['has_failures']:
        print(f"  {C.RED}⚠️  Some checks failed. Run 'init' to set up missing components.{C.RESET}")
    else:
        print(f"  {C.YELLOW}ℹ️  Some warnings found but no critical failures.{C.RESET}")


def view_export():
    """Agent 4: Export command."""
    print_header("📤 EXPORT MANIFEST")
    
    manifest = ManifestController.load_active_manifest()
    
    export_format = input(f"  {C.CYAN}❯ Export format — [1] JSON  [2] Markdown  [3] Both:{C.RESET} ").strip()
    
    if export_format in ('1', 'json'):
        path = os.path.join(WORKSPACE_DIR, 'exported-manifest.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"\n  {C.GREEN}✅ Manifest exported to {path}{C.RESET}")
    
    elif export_format in ('2', 'md', 'markdown'):
        path = os.path.join(WORKSPACE_DIR, 'exported-manifest.md')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# SuperDuperSkills Active Manifest\n\n")
            f.write(f"**Project:** `{manifest.get('project_name', 'unknown')}`\n")
            f.write(f"**Phase:** {manifest.get('project_phase', 'N/A')}\n\n")
            f.write(f"## Active Skills\n\n")
            f.write(f"| # | Skill | Category | Reason |\n")
            f.write(f"|---|-------|----------|--------|\n")
            for idx, sk in enumerate(manifest.get('active_skills', []), 1):
                f.write(f"| {idx} | `{sk['name']}` | {sk.get('category', '-')} | {sk.get('reason', '-')} |\n")
        print(f"\n  {C.GREEN}✅ Manifest exported to {path}{C.RESET}")
    
    elif export_format in ('3', 'both'):
        json_path = os.path.join(WORKSPACE_DIR, 'exported-manifest.json')
        md_path = os.path.join(WORKSPACE_DIR, 'exported-manifest.md')
        
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# SuperDuperSkills Active Manifest\n\n")
            f.write(f"**Project:** `{manifest.get('project_name', 'unknown')}`\n\n")
            for idx, sk in enumerate(manifest.get('active_skills', []), 1):
                f.write(f"- `{sk['name']}` [{sk.get('category', '-')}] — {sk.get('reason', '-')}\n")
        
        print(f"\n  {C.GREEN}✅ Exported to:{C.RESET}")
        print(f"    {C.CYAN}•{C.RESET} {json_path}")
        print(f"    {C.CYAN}•{C.RESET} {md_path}")


def view_init_project():
    """Agent 4: Init command."""
    print_header("📦 INITIALIZE PROJECT — .agents/ DIRECTORY")
    
    if os.path.isdir(AGENTS_DIR):
        if not print_confirm(f".agents/ already exists at {AGENTS_DIR}. Reinitialize?", default_yes=False):
            print(f"\n  {C.GRAY}Skipped.{C.RESET}")
            return
    
    # Create directories
    os.makedirs(AGENTS_DIR, exist_ok=True)
    os.makedirs(PROFILES_DIR, exist_ok=True)
    os.makedirs(SKILLS_DIR, exist_ok=True)
    
    # Generate default manifest
    manifest = ManifestController.load_active_manifest()
    ManifestController.save_active_manifest(manifest)
    
    # Generate desktop config
    DesktopIntegration.save_desktop_config()
    
    print(f"\n  {C.GREEN}✅ Project initialized!{C.RESET}")
    print(f"    {C.CYAN}•{C.RESET} .agents/ directory created")
    print(f"    {C.CYAN}•{C.RESET} ACTIVE-SKILLS.json manifest generated with 19 core skills")
    print(f"    {C.CYAN}•{C.RESET} PROJECT-QUALIFICATION.md documentation created")
    print(f"    {C.CYAN}•{C.RESET} .agents/profiles/ directory ready")
    print(f"    {C.CYAN}•{C.RESET} .agents/desktop.json config generated")
    print(f"    {C.CYAN}•{C.RESET} skills/ directory ready")


def view_profile_manager():
    """Agent 4: Profile manager command."""
    print_header("💼 PROFILE MANAGER — SAVE/LOAD SKILL SETS")
    
    os.makedirs(PROFILES_DIR, exist_ok=True)
    
    # List existing profiles
    profiles = []
    if os.path.isdir(PROFILES_DIR):
        for fname in os.listdir(PROFILES_DIR):
            if fname.endswith('.json'):
                profiles.append(fname[:-5])
    
    if profiles:
        print(f"  {C.BOLD}Existing profiles:{C.RESET}\n")
        for idx, p in enumerate(profiles, 1):
            ppath = os.path.join(PROFILES_DIR, f'{p}.json')
            try:
                with open(ppath, 'r', encoding='utf-8') as pf:
                    pdata = json.load(pf)
                count = len(pdata.get('skills', []))
                print(f"    {C.GREEN}[{idx}]{C.RESET} {C.BOLD}{p}{C.RESET} — {count} skills")
            except Exception:
                print(f"    {C.GREEN}[{idx}]{C.RESET} {C.BOLD}{p}{C.RESET}")
    else:
        print(f"  {C.GRAY}No profiles saved yet.{C.RESET}")
    
    print(f"\n  {C.CYAN}[S]{C.RESET} Save current manifest as profile")
    print(f"  {C.CYAN}[L]{C.RESET} Load a profile")
    print(f"  {C.RED}[0]{C.RESET} Back\n")
    
    action = input(f"  {C.CYAN}❯ Select action:{C.RESET} ").strip().upper()
    
    if action == 'S':
        name = input(f"  {C.CYAN}❯ Profile name:{C.RESET} ").strip()
        if not name:
            return
        name = re.sub(r'[^a-zA-Z0-9\-_]', '', name.lower())
        
        manifest = ManifestController.load_active_manifest()
        profile_path = os.path.join(PROFILES_DIR, f'{name}.json')
        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump({
                "name": name,
                "created": time.strftime("%Y-%m-%d %H:%M"),
                "project_name": manifest.get("project_name", "unknown"),
                "skills": [s["name"] for s in manifest.get("active_skills", [])],
                "phase": manifest.get("project_phase", "unknown")
            }, f, indent=2)
        
        print(f"\n  {C.GREEN}✅ Profile '{name}' saved with {len(manifest.get('active_skills', []))} skills.{C.RESET}")
    
    elif action == 'L' and profiles:
        idx = input(f"  {C.CYAN}❯ Profile # to load:{C.RESET} ").strip()
        if idx.isdigit() and 1 <= int(idx) <= len(profiles):
            name = profiles[int(idx) - 1]
            ppath = os.path.join(PROFILES_DIR, f'{name}.json')
            with open(ppath, 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            
            # Rebuild manifest from profile
            manifest = ManifestController.load_active_manifest()
            new_skills = []
            for sk_name in data.get('skills', []):
                is_core = any(c["name"] == sk_name for c in MANDATORY_CORE_SUITE)
                reason = next(
                    (c["reason"] for c in MANDATORY_CORE_SUITE if c["name"] == sk_name),
                    "Loaded from profile"
                ) if is_core else "Loaded from profile"
                
                new_skills.append({
                    "name": sk_name,
                    "category": "CORE" if is_core else "PROFILE_LOADED",
                    "reason": reason,
                    "is_core": is_core,
                    "mandatory_view": True
                })
            
            manifest["active_skills"] = new_skills
            ManifestController.save_active_manifest(manifest)
            
            print(f"\n  {C.GREEN}✅ Profile '{name}' loaded — {len(new_skills)} skills activated.{C.RESET}")


# =============================================================================
# 11. CLI ARGUMENT PARSER (AGENT 2: RICH HELP SYSTEM)
# =============================================================================
def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser with rich help text and examples."""
    
    parser = argparse.ArgumentParser(
        prog='superduperskills',
        description=f"""{C.CYAN}{C.BOLD}SuperDuperSkills Agentic CLI & Discovery Control Center{C.RESET}
  v{__version__} «{__codename__}» — 2,700+ AI Agent Skills for Claude, Gemini, Cursor, Codex""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""{C.GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{C.GREEN}Quick Start:{C.RESET}
  $ sds                        {C.GRAY}# Launch interactive TUI{C.RESET}
  $ sds scan                    {C.GRAY}# Scan project stack & recommend skills{C.RESET}
  $ sds init                    {C.GRAY}# Initialize .agents/ directory{C.RESET}
  $ sds doctor                  {C.GRAY}# Check environment health{C.RESET}

{C.GREEN}Skill Management:{C.RESET}
  $ sds list                    {C.GRAY}# List all active skills{C.RESET}
  $ sds search react            {C.GRAY}# Search 2,700+ skills by name{C.RESET}
  $ sds toggle emil-design-eng  {C.GRAY}# Toggle a skill ON/OFF{C.RESET}
  $ sds ingest <url>            {C.GRAY}# Import a remote skill{C.RESET}

{C.GREEN}Project Lifecycle:{C.RESET}
  $ sds scan --json             {C.GRAY}# Scan with JSON output{C.RESET}
  $ sds export --format json    {C.GRAY}# Export manifest to file{C.RESET}
  $ sds sync                    {C.GRAY}# Sync to all agent environments{C.RESET}
  $ sds audit                   {C.GRAY}# Verify all SKILL.md files exist{C.RESET}
  $ sds profile save frontend   {C.GRAY}# Save current skill set as profile{C.RESET}
  $ sds profile load frontend   {C.GRAY}# Load a saved profile{C.RESET}

{C.GREEN}Desktop Integration:{C.RESET}
  $ sds desktop setup           {C.GRAY}# Generate Electron wrapper config{C.RESET}
  $ sds --version               {C.GRAY}# Show version info{C.RESET}
{C.GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{C.RESET}
  Docs: https://superduperskills.vercel.app
  Repo: https://github.com/camilolealdev/superduperskills{C.RESET}"""
    )
    
    # Global flags
    parser.add_argument('--version', '-V', action='version',
                       version=f'{C.CYAN}SuperDuperSkills{C.RESET} v{__version__} «{__codename__}»')
    parser.add_argument('--json', '-j', action='store_true',
                       help='Output results in JSON format (for scripting)')
    parser.add_argument('--quiet', '-q', action='store_true',
                       help='Suppress banner and decorative output')
    parser.add_argument('--no-color', action='store_true',
                       help='Disable ANSI color output')
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # scan
    sp_scan = subparsers.add_parser("scan", 
        help="Scan project stack and recommend skills",
        description="Deep analysis of project structure, dependencies, and frameworks to recommend the best skills.")
    sp_scan.add_argument("--full", "-f", action="store_true",
        help="Run full recursive scan including subdirectories")
    
    # list
    sp_list = subparsers.add_parser("list",
        help="List all active skills in the project manifest",
        description="Display all skills currently active in .agents/ACTIVE-SKILLS.json")
    sp_list.add_argument("--core-only", "-c", action="store_true",
        help="Show only core (mandatory) skills")
    
    # toggle
    sp_toggle = subparsers.add_parser("toggle",
        help="Toggle a skill ON/OFF in the manifest",
        description="Enable or disable a skill. Core skills cannot be disabled.")
    sp_toggle.add_argument("skill_name", type=str, help="Name of the skill to toggle")
    sp_toggle.add_argument("--on", action="store_true", help="Force enable the skill")
    sp_toggle.add_argument("--off", action="store_true", help="Force disable the skill")
    
    # search
    sp_search = subparsers.add_parser("search",
        help="Search the skill vault (2,700+ skills)",
        description="Search for skills by name in the local skills/ directory.")
    sp_search.add_argument("query", type=str, help="Search term to match against skill names")
    sp_search.add_argument("--limit", "-l", type=int, default=25,
        help="Maximum results to return (default: 25)")
    
    # ingest
    sp_ingest = subparsers.add_parser("ingest",
        help="Import a remote skill or create a custom one",
        description="Create a new skill from a GitHub URL or custom name.")
    sp_ingest.add_argument("source", type=str, help="URL or unique name for the skill")
    sp_ingest.add_argument("--category", "-c", type=str, default="INGESTED",
        help="Category tag for the skill (default: INGESTED)")
    
    # sync
    subparsers.add_parser("sync",
        help="Synchronize active manifest to all agent environments",
        description="Write .cursor/rules and .agents/opencode-active.json for multi-CLI compatibility.")
    
    # audit
    subparsers.add_parser("audit",
        help="Audit compliance — verify SKILL.md files exist",
        description="Check that every active skill has a corresponding SKILL.md file on disk.")
    
    # wizard
    subparsers.add_parser("wizard",
        help="Launch the full Socratic qualification wizard",
        description="Interactive interview wizard that qualifies your project and generates a focused skill manifest.")
    
    # init (Agent 4)
    subparsers.add_parser("init",
        help="Initialize project — create .agents/ directory and default manifest",
        description="Set up the .agents/ infrastructure: ACTIVE-SKILLS.json, profiles/, desktop.json, etc.")
    
    # doctor (Agent 4)
    subparsers.add_parser("doctor",
        help="Run environment diagnostics and health checks",
        description="Check Python version, skills directory, .agents/ structure, Git status, and disk space.")
    
    # export (Agent 4)
    sp_export = subparsers.add_parser("export",
        help="Export the active manifest to JSON or Markdown",
        description="Export .agents/ACTIVE-SKILLS.json to a standalone file for sharing or backup.")
    sp_export.add_argument("--format", "-f", choices=["json", "markdown", "both"], default="both",
        help="Export format (default: both)")
    
    # profile (Agent 4)
    sp_profile = subparsers.add_parser("profile",
        help="Save or load skill profiles (presets)",
        description="Manage named skill presets to quickly switch between project configurations.")
    sp_profile.add_argument("profile_action", choices=["save", "load", "list", "delete"],
        help="Profile action: save, load, list, or delete")
    sp_profile.add_argument("profile_name", nargs="?", type=str,
        help="Profile name (required for save/load/delete)")
    
    # stats (Agent 4)
    subparsers.add_parser("stats",
        help="Show usage statistics and dashboard",
        description="Display catalog size, active counts, category breakdown, and project info.")
    
    # desktop (Agent 5)
    sp_desktop = subparsers.add_parser("desktop",
        help="Desktop app integration commands",
        description="Generate Electron wrapper configuration for desktop app integration.")
    sp_desktop.add_argument("desktop_action", choices=["setup", "config"],
        help="Desktop action: setup generates Electron main.js, config shows current settings")
    
    # completions
    sp_completions = subparsers.add_parser("completions",
        help="Install or uninstall shell completions for bash/zsh/fish",
        description="Generate and install shell completion scripts for bash, zsh, and fish.")
    sp_completions.add_argument("completions_action", choices=["install", "uninstall", "show", "path"],
        help="Action: install writes completions to shell dirs, show prints them, path shows install paths")
    sp_completions.add_argument("--shell", "-s", choices=["bash", "zsh", "fish", "all"], default="all",
        help="Target shell (default: all)")
    
    return parser


# =============================================================================
# 12. MAIN ENTRY POINT
# =============================================================================
def apply_no_color():
    """Strip all ANSI codes when --no-color is passed."""
    for attr in dir(C):
        if attr.isupper() and attr != 'RESET':
            setattr(C, attr, '')
    C.RESET = ''

def main():
    parser = build_parser()
    args = parser.parse_args()
    
    if args.no_color:
        apply_no_color()
    
    if args.command is None:
        # Launch Interactive TUI
        if not args.quiet:
            active_skills = ManifestController.load_active_manifest().get("active_skills", [])
            cat_count = sum(1 for _ in os.scandir(SKILLS_DIR) if _.is_dir()) if os.path.isdir(SKILLS_DIR) else 0
            print(QUICK_STATUS_BAR.format(
                ws=WORKSPACE_DIR,
                active_count=len(active_skills),
                core_count=len(MANDATORY_CORE_SUITE),
                spec_count=max(0, len(active_skills) - len(MANDATORY_CORE_SUITE)),
                catalog_count=cat_count,
                version=__version__,
                codename=__codename__
            ))
        run_interactive_tui()
        return
    
    # --- Non-Interactive Subcommands ---
    
    def out(data):
        """Output helper: JSON if --json, else plain text."""
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            if isinstance(data, dict):
                for k, v in data.items():
                    print(f"{k}: {v}")
            elif isinstance(data, list):
                for item in data:
                    if isinstance(item, dict):
                        print(json.dumps(item, ensure_ascii=False))
                    else:
                        print(item)
            else:
                print(data)
    
    if args.command == "scan":
        r = ProjectDiscovery.inspect()
        out(r)
    
    elif args.command == "list":
        m = ManifestController.load_active_manifest()
        skills = m.get("active_skills", [])
        if args.core_only:
            skills = [s for s in skills if s.get("is_core", False)]
        
        if args.json:
            out([{"name": s["name"], "category": s.get("category", "CUSTOM"), "reason": s.get("reason", "")} for s in skills])
        else:
            print(f"\n  Active Skills ({len(skills)}):\n")
            for s in skills:
                core_tag = " [CORE]" if s.get("is_core") else ""
                print(f"    • {s['name']}{core_tag} [{s.get('category', 'CUSTOM')}]: {s.get('reason', '')}")
    
    elif args.command == "toggle":
        if args.on:
            _, msg = ManifestController.toggle_skill(args.skill_name, force_state=True)
        elif args.off:
            _, msg = ManifestController.toggle_skill(args.skill_name, force_state=False)
        else:
            _, msg = ManifestController.toggle_skill(args.skill_name)
        print(msg)
    
    elif args.command == "search":
        res = SkillVaultEngine.search_local(args.query, args.limit)
        if args.json:
            out(res)
        else:
            if not res:
                print(f"No skills found matching '{args.query}'.")
            else:
                for r in res:
                    status = "[ON ]" if r["active"] else "[OFF]"
                    core = " [CORE]" if r["is_core"] else ""
                    print(f"  {status}{core} {r['name']} — {r['preview'][:80]}")
    
    elif args.command == "ingest":
        ok, msg = SkillVaultEngine.ingest_remote_skill(args.source, args.category)
        print(msg)
    
    elif args.command == "sync":
        synced = MultiCLISync.sync_all()
        for k, v in synced.items():
            print(f"  ✓ {k} → {v}")
    
    elif args.command == "audit":
        audit = MultiCLISync.audit_compliance()
        out(audit)
    
    elif args.command == "wizard":
        run_qualification_wizard()
    
    elif args.command == "init":
        os.makedirs(AGENTS_DIR, exist_ok=True)
        os.makedirs(PROFILES_DIR, exist_ok=True)
        os.makedirs(SKILLS_DIR, exist_ok=True)
        manifest = ManifestController.load_active_manifest()
        ManifestController.save_active_manifest(manifest)
        DesktopIntegration.save_desktop_config()
        print(f"✅ Project initialized at {AGENTS_DIR}")
    
    elif args.command == "doctor":
        result = MultiCLISync.doctor_check()
        if args.json:
            out(result)
        else:
            for check in result['checks']:
                icon = "✓" if check['status'] == 'PASS' else "⚠" if check['status'] == 'WARN' else "✗"
                print(f"  {icon} {check['name']}: {check['detail']}")
            if result['all_pass']:
                print(f"\n  🎉 All checks passed!")
            elif result.get('has_failures'):
                print(f"\n  ❌ Critical failures detected.")
                sys.exit(1)
            else:
                print(f"\n  ⚠️  Some warnings detected.")
    
    elif args.command == "export":
        manifest = ManifestController.load_active_manifest()
        fmt = args.format
        
        if fmt in ('json', 'both'):
            path = os.path.join(WORKSPACE_DIR, 'exported-manifest.json')
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            print(f"  ✓ Exported JSON → {path}")
        
        if fmt in ('markdown', 'both'):
            path = os.path.join(WORKSPACE_DIR, 'exported-manifest.md')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(f"# SuperDuperSkills Active Manifest\n\n")
                f.write(f"**Project:** `{manifest.get('project_name', 'unknown')}`\n\n")
                for idx, sk in enumerate(manifest.get('active_skills', []), 1):
                    f.write(f"- `{sk['name']}` [{sk.get('category', '-')}] — {sk.get('reason', '-')}\n")
            print(f"  ✓ Exported Markdown → {path}")
    
    elif args.command == "profile":
        os.makedirs(PROFILES_DIR, exist_ok=True)
        
        if args.profile_action == "list":
            for fname in os.listdir(PROFILES_DIR):
                if fname.endswith('.json'):
                    print(f"  • {fname[:-5]}")
        
        elif args.profile_action == "save":
            if not args.profile_name:
                print("  Error: profile name required for 'save'")
                return
            name = re.sub(r'[^a-zA-Z0-9\-_]', '', args.profile_name.lower())
            manifest = ManifestController.load_active_manifest()
            ppath = os.path.join(PROFILES_DIR, f'{name}.json')
            with open(ppath, 'w', encoding='utf-8') as f:
                json.dump({
                    "name": name,
                    "created": time.strftime("%Y-%m-%d %H:%M"),
                    "skills": [s["name"] for s in manifest.get("active_skills", [])]
                }, f, indent=2)
            print(f"  ✓ Profile '{name}' saved with {len(manifest.get('active_skills', []))} skills")
        
        elif args.profile_action == "load":
            if not args.profile_name:
                print("  Error: profile name required for 'load'")
                return
            name = args.profile_name
            ppath = os.path.join(PROFILES_DIR, f'{name}.json')
            if not os.path.isfile(ppath):
                print(f"  ✗ Profile '{name}' not found")
                return
            with open(ppath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            manifest = ManifestController.load_active_manifest()
            new_skills = []
            for sk_name in data.get('skills', []):
                is_core = any(c["name"] == sk_name for c in MANDATORY_CORE_SUITE)
                new_skills.append({
                    "name": sk_name,
                    "category": "CORE" if is_core else "PROFILE_LOADED",
                    "reason": "Core mandatory" if is_core else "Loaded from profile",
                    "is_core": is_core,
                    "mandatory_view": True
                })
            manifest["active_skills"] = new_skills
            ManifestController.save_active_manifest(manifest)
            print(f"  ✓ Profile '{name}' loaded — {len(new_skills)} skills activated")
        
        elif args.profile_action == "delete":
            if not args.profile_name:
                print("  Error: profile name required for 'delete'")
                return
            ppath = os.path.join(PROFILES_DIR, f'{args.profile_name}.json')
            if os.path.isfile(ppath):
                os.remove(ppath)
                print(f"  ✓ Profile '{args.profile_name}' deleted")
            else:
                print(f"  ✗ Profile '{args.profile_name}' not found")
    
    elif args.command == "stats":
        stats = MultiCLISync.get_stats()
        out(stats)
    
    elif args.command == "desktop":
        if args.desktop_action == "setup":
            config_path = DesktopIntegration.save_desktop_config()
            main_path = os.path.join(AGENTS_DIR, 'main.js')
            with open(main_path, 'w', encoding='utf-8') as f:
                f.write(DesktopIntegration.generate_electron_main())
            print(f"  ✓ Desktop config → {config_path}")
            print(f"  ✓ Electron main.js → {main_path}")
        elif args.desktop_action == "config":
            if os.path.isfile(DESKTOP_CONFIG):
                with open(DESKTOP_CONFIG, 'r', encoding='utf-8') as f:
                    print(f.read())
            else:
                print("  Run 'sds desktop setup' first to generate config.")
    
    elif args.command == "completions":
        shell_target = args.shell
        action = args.completions_action
        completions_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'completions')
        
        if action == "path":
            # Show where completions would be installed
            home = os.path.expanduser("~")
            paths = {
                "bash": [
                    os.path.join(home, ".bashrc"),
                    "/etc/bash_completion.d/sds",
                    "/usr/local/etc/bash_completion.d/sds",
                ],
                "zsh": [
                    os.path.join(home, ".zsh", "completions", "_sds"),
                    os.path.join(home, ".zshrc"),
                ],
                "fish": [
                    os.path.join(home, ".config", "fish", "completions", "sds.fish"),
                ],
            }
            print(f"\n  {C.CYAN}Shell completion install paths:{C.RESET}\n")
            for sh, pts in paths.items():
                if shell_target in (sh, 'all'):
                    print(f"  {C.BOLD}{sh}:{C.RESET}")
                    for p in pts:
                        exists = os.path.isfile(p)
                        icon = "✓" if exists else "○"
                        color = C.GREEN if exists else C.GRAY
                        print(f"    {color}{icon} {p}{C.RESET}")
                    print()
            print(f"  {C.DIM}Source file: {os.path.abspath(completions_dir)}{C.RESET}")
        
        elif action == "show":
            # Print the completion script content
            shells = ["bash", "zsh", "fish"] if shell_target == "all" else [shell_target]
            for sh in shells:
                script = os.path.join(completions_dir, f"sds.{sh}")
                if os.path.isfile(script):
                    print(f"\n  {C.BOLD}{C.CYAN}# {sh.upper()} completion — {script}{C.RESET}")
                    print(f"  {C.GRAY}{'─' * 60}{C.RESET}")
                    with open(script, 'r', encoding='utf-8') as f:
                        for line in f:
                            print(f"  {line}", end="")
                    print(f"\n  {C.GRAY}{'─' * 60}{C.RESET}")
                else:
                    print(f"  {C.RED}✗ {sh} completion not found: {script}{C.RESET}")
        
        elif action == "install":
            home = os.path.expanduser("~")
            installed = []
            shells = ["bash", "zsh", "fish"] if shell_target == "all" else [shell_target]
            
            for sh in shells:
                script = os.path.join(completions_dir, f"sds.{sh}")
                if not os.path.isfile(script):
                    print(f"  {C.RED}✗ Source not found: {script}{C.RESET}")
                    continue
                
                if sh == "bash":
                    dest_dir = os.path.join(home, ".config", "bash_completion.d")
                    if not os.path.isdir(dest_dir):
                        dest_dir = "/etc/bash_completion.d"
                    if not os.path.isdir(dest_dir):
                        dest_dir = os.path.join(home, ".local", "share", "bash-completion", "completions")
                    os.makedirs(dest_dir, exist_ok=True)
                    dest = os.path.join(dest_dir, "sds")
                    shutil.copy2(script, dest)
                    installed.append(("bash", dest))
                    
                elif sh == "zsh":
                    dest_dir = os.path.join(home, ".zsh", "completions")
                    os.makedirs(dest_dir, exist_ok=True)
                    dest = os.path.join(dest_dir, "_sds")
                    shutil.copy2(script, dest)
                    # Add fpath to .zshrc if not present
                    zshrc = os.path.join(home, ".zshrc")
                    fpath_line = f'fpath=({dest_dir} $fpath)'
                    autoload_line = 'autoload -Uz compinit && compinit'
                    if os.path.isfile(zshrc):
                        with open(zshrc, 'r', encoding='utf-8') as f:
                            content = f.read()
                        additions = []
                        if fpath_line not in content:
                            additions.append(fpath_line)
                        if autoload_line not in content:
                            additions.append(autoload_line)
                        if additions:
                            with open(zshrc, 'a', encoding='utf-8') as f:
                                f.write(f"\n# SuperDuperSkills completions\n")
                                f.write("\n".join(additions) + "\n")
                    installed.append(("zsh", dest))
                    
                elif sh == "fish":
                    dest_dir = os.path.join(home, ".config", "fish", "completions")
                    os.makedirs(dest_dir, exist_ok=True)
                    dest = os.path.join(dest_dir, "sds.fish")
                    shutil.copy2(script, dest)
                    installed.append(("fish", dest))
            
            if installed:
                print(f"\n  {C.GREEN}✓ Completions installed:{C.RESET}")
                for sh, path in installed:
                    print(f"    {C.CYAN}{sh}{C.RESET} → {path}")
                print(f"\n  {C.DIM}Restart your shell or run: source <path>{C.RESET}")
            else:
                print(f"\n  {C.RED}No completions installed.{C.RESET}")
        
        elif action == "uninstall":
            home = os.path.expanduser("~")
            removed = []
            shells = ["bash", "zsh", "fish"] if shell_target == "all" else [shell_target]
            
            for sh in shells:
                targets = []
                if sh == "bash":
                    for d in ["~/.config/bash_completion.d", "/etc/bash_completion.d"]:
                        targets.append(os.path.join(d, "sds"))
                elif sh == "zsh":
                    targets.append(os.path.join(home, ".zsh", "completions", "_sds"))
                elif sh == "fish":
                    targets.append(os.path.join(home, ".config", "fish", "completions", "sds.fish"))
                
                for t in targets:
                    if os.path.isfile(t):
                        os.remove(t)
                        removed.append((sh, t))
            
            if removed:
                print(f"\n  {C.GREEN}✓ Completions removed:{C.RESET}")
                for sh, path in removed:
                    print(f"    {C.RED}{sh}{C.RESET} ← {path}")
            else:
                print(f"\n  {C.GRAY}No completions found to remove.{C.RESET}")


def run_qualification_wizard():
    """Launch the Socratic qualification wizard."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import qualify_project as qp
    qp.run_interactive_wizard()


if __name__ == '__main__':
    main()
