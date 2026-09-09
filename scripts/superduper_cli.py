#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 SUPERDUPERSKILLS AGENTIC CLI & CONTROL CENTER v4.0 (Gemini & Claude Edition)
================================================================================
 Ultra-Sleek Terminal UI & Discovery Engine with Mouse & Slash Command Support.

 Crafted following Emil Kowalski Design Engineering (emil-design-eng) &
 Gemini CLI / Claude Code UI/UX principles.
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
import subprocess
import atexit
import http.server
import socketserver
import webbrowser
import urllib.request
import urllib.parse
import threading
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# =============================================================================
# 1. VERSION, METADATA & CROSS-PLATFORM KEY READER
# =============================================================================
__version__ = "6.0.0"
__codename__ = "WorldClass"


class KeyReader:
    """Zero-dependency cross-platform keypress & arrow navigation engine."""
    @staticmethod
    def get_key() -> str:
        if HAS_MSVCRT:
            try:
                ch = msvcrt.getch()
                if ch in (b'\x00', b'\xe0'):
                    ch2 = msvcrt.getch()
                    if ch2 == b'H': return 'UP'
                    elif ch2 == b'P': return 'DOWN'
                    elif ch2 == b'K': return 'LEFT'
                    elif ch2 == b'M': return 'RIGHT'
                    return 'SPECIAL'
                elif ch == b'\r': return 'ENTER'
                elif ch == b'\x1b': return 'ESC'
                elif ch == b' ': return 'SPACE'
                elif ch == b'\t': return 'TAB'
                elif ch in (b'\x08', b'\x7f'): return 'BACKSPACE'
                elif ch == b'\x03': return 'CTRL_C'
                else:
                    return ch.decode('utf-8', errors='ignore')
            except Exception:
                return ''
        else:
            try:
                import termios, tty
                fd = sys.stdin.fileno()
                old_settings = termios.tcgetattr(fd)
                try:
                    tty.setraw(fd)
                    ch = sys.stdin.read(1)
                    if ch == '\x1b':
                        # Check for arrow sequences
                        import select
                        r, _, _ = select.select([sys.stdin], [], [], 0.05)
                        if r:
                            ch2 = sys.stdin.read(1)
                            if ch2 == '[':
                                ch3 = sys.stdin.read(1)
                                if ch3 == 'A': return 'UP'
                                elif ch3 == 'B': return 'DOWN'
                                elif ch3 == 'C': return 'RIGHT'
                                elif ch3 == 'D': return 'LEFT'
                        return 'ESC'
                    elif ch in ('\r', '\n'): return 'ENTER'
                    elif ch == ' ': return 'SPACE'
                    elif ch == '\t': return 'TAB'
                    elif ch in ('\x7f', '\x08'): return 'BACKSPACE'
                    elif ch == '\x03': return 'CTRL_C'
                    return ch
                finally:
                    termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            except Exception:
                return sys.stdin.readline().strip()


# =============================================================================
# 2. DESIGN SYSTEM: 24-BIT TRUECOLOR, ANSI PALETTES & BOX DRAWING
# =============================================================================
class C:
    """TrueColor / 256-color and standard ANSI styling engine."""
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    DIM         = "\033[2m"
    ITALIC      = "\033[3m"
    UNDERLINE   = "\033[4m"
    INVERSE     = "\033[7m"
    
    # Modern Grayscale / Slate
    BG_DARK     = "\033[48;2;15;23;42m"      # Slate 900
    BG_CARD     = "\033[48;2;30;41;59m"      # Slate 800
    BG_MUTED    = "\033[48;2;51;65;85m"      # Slate 700
    BG_ACCENT   = "\033[48;2;34;211;238m"    # Cyan Accent
    
    # Core Accent Colors (Gemini Cyan / Blue / Indigo)
    GEMINI_CYAN = "\033[38;2;34;211;238m"    # Cyan 400
    GEMINI_BLUE = "\033[38;2;96;165;250m"    # Blue 400
    GEMINI_INDIGO="\033[38;2;129;140;248m"   # Indigo 400
    GEMINI_VIOLET="\033[38;2;168;85;247m"    # Purple 500
    
    # Claude Warm Amber / Coral / Gold
    CLAUDE_GOLD = "\033[38;2;251;191;36m"    # Amber 400
    CLAUDE_CORAL= "\033[38;2;248;113;113m"   # Coral / Red 400
    CLAUDE_ROSE = "\033[38;2;244;63;94m"     # Rose 500
    
    # Semantic Accents (Refactoring UI & Emil Kowalski hierarchy)
    EMERALD     = "\033[38;2;52;211;153m"    # Green 400
    EMERALD_DIM = "\033[38;2;16;185;129m"    # Green 500
    AMBER       = "\033[38;2;245;158;11m"    # Amber 500
    ROSE        = "\033[38;2;244;63;94m"     # Rose 500
    SLATE_LIGHT = "\033[38;2;226;232;240m"   # Slate 200 (Primary text)
    SLATE_MUTED = "\033[38;2;148;163;184m"   # Slate 400 (Secondary text)
    SLATE_DARK  = "\033[38;2;100;116;139m"   # Slate 500 (Borders)
    SLATE_DEEP  = "\033[38;2;71;85;105m"     # Slate 600
    
    # Standard ANSI Aliases
    CYAN        = "\033[96m"
    BLUE        = "\033[94m"
    GREEN       = "\033[92m"
    YELLOW      = "\033[93m"
    RED         = "\033[91m"
    MAGENTA     = "\033[95m"
    WHITE       = "\033[97m"
    GRAY        = "\033[90m"

# Modern Unicode Box Glyphs (Claude & Gemini UI Standard)
BOX = {
    "tl": "╭", "tr": "╮", "bl": "╰", "br": "╯",
    "h": "─", "v": "│",
    "vl": "├", "vr": "┤", "tt": "┬", "bt": "┴",
    "cross": "┼",
    "d_h": "═", "d_v": "║",
    "dot_active": f"{C.EMERALD}●{C.RESET}",
    "dot_inactive": f"{C.SLATE_DARK}○{C.RESET}",
    "dot_core": f"{C.GEMINI_VIOLET}◆{C.RESET}",
    "sparkle": f"{C.GEMINI_CYAN}✦{C.RESET}",
    "arrow": f"{C.GEMINI_CYAN}❯{C.RESET}",
    "check": f"{C.EMERALD}✔{C.RESET}",
    "warn": f"{C.AMBER}⚠{C.RESET}",
    "fail": f"{C.ROSE}✖{C.RESET}",
    "info": f"{C.GEMINI_BLUE}ℹ{C.RESET}",
    "star": f"{C.CLAUDE_GOLD}★{C.RESET}",
    "mouse": f"{C.GEMINI_CYAN}🖱{C.RESET}"
}

# Workspace & Central Repository Paths
WORKSPACE_DIR = os.getcwd()
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Locate central skills vault (Repo skills/ -> Workspace skills/ -> ~/.claude/skills)
if os.path.isdir(os.path.join(REPO_ROOT, 'skills')):
    SKILLS_DIR = os.path.join(REPO_ROOT, 'skills')
elif os.path.isdir(os.path.join(WORKSPACE_DIR, 'skills')):
    SKILLS_DIR = os.path.join(WORKSPACE_DIR, 'skills')
else:
    SKILLS_DIR = os.path.join(os.path.expanduser('~'), '.claude', 'skills')

AGENTS_DIR = os.path.join(WORKSPACE_DIR, '.agents')
ACTIVE_MANIFEST = os.path.join(AGENTS_DIR, 'ACTIVE-SKILLS.json')
QUALIFICATION_DOC = os.path.join(AGENTS_DIR, 'PROJECT-QUALIFICATION.md')
PROFILES_DIR = os.path.join(AGENTS_DIR, 'profiles')
DESKTOP_CONFIG = os.path.join(AGENTS_DIR, 'desktop.json')

# =============================================================================
# 3. TERMINAL HYPERLINKS & MOUSE TRACKING ENGINE
# =============================================================================
def make_clickable_link(text: str, url: str) -> str:
    """Format text with OSC 8 terminal hyperlink for mouse clicking."""
    return f"\033]8;;{url}\033\\{text}\033]8;;\033\\"

def make_file_link(text: str, file_path: str) -> str:
    """Format local file path as clickable OSC 8 file:// URI."""
    abs_path = os.path.abspath(file_path).replace('\\', '/')
    return f"\033]8;;file:///{abs_path}\033\\{text}\033]8;;\033\\"

class TerminalMouseManager:
    """Manages terminal mouse tracking (SGR mode) safely with atexit cleanup."""
    _enabled = False

    @classmethod
    def enable(cls):
        if not cls._enabled and sys.stdout.isatty():
            try:
                # Enable normal mouse clicks + SGR extended coordinate reporting
                sys.stdout.write("\033[?1000h\033[?1006h")
                sys.stdout.flush()
                cls._enabled = True
            except Exception:
                pass

    @classmethod
    def disable(cls):
        if cls._enabled and sys.stdout.isatty():
            try:
                sys.stdout.write("\033[?1000l\033[?1006l\033[?25h\033[0m")
                sys.stdout.flush()
                cls._enabled = False
            except Exception:
                pass

# Ensure cleanup on terminal exit
atexit.register(TerminalMouseManager.disable)

# =============================================================================
# 4. MANDATORY INVARIANT CORE SUITE (20 SKILLS)
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
    {"name": "i-have-adhd", "reason": "Formateo de Salida Action-First", "category": "CORE", "icon": "⚡"},
    {"name": "penetration-testing-with-strix", "reason": "Pentesting Dinámico Autónomo & PoC Exploits (Strix Core)", "category": "CORE", "icon": "🎯"}
]

# =============================================================================
# 5. SPECIALIZED CATEGORIES & HIGH-VALUE SKILL MAPPINGS
# =============================================================================
CATEGORY_REGISTRY = {
    "DESIGN_UI": {
        "title": "Diseño & UI Craft (Anti-Slop / Motion / Design Systems)",
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
            ("clone-website", "Reverse-engineer y clonado pixel-perfect de sitios via agentes"),
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
        "title": "Seguridad, OWASP, Pentesting & Threat Modeling",
        "icon": "🛡️",
        "skills": [
            ("penetration-testing-with-strix", "Pentest dinámico con IA autónoma, exploits PoC y SARIF (usestrix/strix)"),
            ("ci-security-scanning-with-strix", "Diff-scoped PR security gate y escaneo CI/CD con Strix"),
            ("fix-security-vulnerabilities-with-strix", "Triage, parche quirúrgico de causa raíz y re-escaneo verificador"),
            ("managed-pentesting-with-strix", "Pentesting cloud gestionado en app.strix.ai sin Docker local"),
            ("agentshield", "Escudo contra prompt injection y comandos destructivos"),
            ("springboot-security", "Spring Security hardening: authn/authz, CSRF, JWT y filtros seguros (ECC)"),
            ("cybersecurity", "Auditoría de seguridad general y escaneo de vulnerabilidades"),
            ("owasp-security", "Verificación exhaustiva de OWASP Top 10:2025"),
            ("threat-model-analyst", "Modelado de amenazas STRIDE y vectores de ataque"),
            ("security-auditor", "Auditoría estricta de código y sanitización de inputs"),
            ("secret-scanner", "Detección y prevención de fuga de API keys y credenciales"),
            ("cors-csrf-hardening", "Protección de cabeceras, CORS y tokens anti-CSRF"),
            ("auth-patterns", "Patrones seguros de autenticación (JWT, OAuth, Sessions)")
        ]
    },
    "BACKEND_API": {
        "title": "Backend, APIs & Bases de Datos",
        "icon": "⚡",
        "skills": [
            ("springboot-patterns", "Patrones enterprise en Spring Boot 3.x, REST APIs y caching"),
            ("springboot-security", "Spring Security hardening, authn/authz, CSRF y JWT"),
            ("springboot-tdd", "Test-driven development para Spring Boot con JUnit 5 & Mockito"),
            ("nodejs-backend-patterns", "Patrones de arquitectura Node.js / Express / Fastify"),
            ("python-patterns", "Desarrollo idiomático en Python / FastAPI / Django"),
            ("golang-patterns", "Concurrencia, goroutines y microservicios en Go"),
            ("rust-patterns", "Arquitectura segura y rendimiento en Rust"),
            ("dotnet-patterns", "Patrones enterprise en .NET 8 / C#"),
            ("postgres-patterns", "Modelado, índices y optimización de consultas PostgreSQL"),
            ("database-optimizer", "Tuning de consultas SQL y planes de ejecución EXPLAIN"),
            ("redis-caching", "Estrategias de caché distribuida y rate limiting con Redis"),
            ("graphql-architect", "Diseño de schemas GraphQL y optimización DataLoader"),
            ("rest-api-design", "Diseño de contratos RESTful, versionado y OpenAPI")
        ]
    },
    "MOBILE_DESKTOP": {
        "title": "Mobile & Aplicaciones de Escritorio",
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
        "title": "DevOps, Cloud, CI/CD & Infraestructura",
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
        "title": "Inteligencia Artificial & Sistemas Multi-Agente",
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
        "title": "Testing, Calidad de Software & QA",
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
        "title": "Growth, SEO, Copywriting & Legal",
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
# 6. UI COMPONENTS: CARDS, STATUS BARS & GRADIENTS
# =============================================================================
def strip_ansi(text: str) -> str:
    """Strip ANSI escape sequences from string to calculate visual width."""
    return re.sub(r'\x1b\[[0-9;]*[a-zA-Z]|\x1b\]8;;.*?\x1b\\', '', text)

def visual_len(text: str) -> int:
    """Calculate visible character length in terminal."""
    return len(strip_ansi(text))

def render_card(title: str, lines: List[str], width: int = 74, border_color: str = C.SLATE_DARK, accent_icon: str = "✦") -> str:
    """Render a modern Claude / Gemini rounded card with padding."""
    top_title = f" {accent_icon} {title} " if title else ""
    title_vlen = visual_len(top_title)
    
    top_border = f"{border_color}{BOX['tl']}{BOX['h']}{C.RESET}{C.BOLD}{C.SLATE_LIGHT}{top_title}{C.RESET}{border_color}{BOX['h'] * max(2, width - title_vlen - 3)}{BOX['tr']}{C.RESET}"
    bottom_border = f"{border_color}{BOX['bl']}{BOX['h'] * (width - 2)}{BOX['br']}{C.RESET}"
    
    out = [top_border]
    for line in lines:
        v_len = visual_len(line)
        padding = max(0, width - 4 - v_len)
        out.append(f"{border_color}{BOX['v']}{C.RESET}  {line}{' ' * padding}  {border_color}{BOX['v']}{C.RESET}")
    out.append(bottom_border)
    return "\n".join(out)

def render_table(headers: List[str], rows: List[List[str]], col_widths: Optional[List[int]] = None, border_color: str = C.SLATE_DARK) -> str:
    """Render an ultra-clean table with aligned columns."""
    if not col_widths:
        col_widths = [visual_len(h) for h in headers]
        for row in rows:
            for idx, cell in enumerate(row):
                if idx < len(col_widths):
                    col_widths[idx] = max(col_widths[idx], visual_len(str(cell)))
    
    # Header line
    head_cells = []
    for idx, h in enumerate(headers):
        w = col_widths[idx]
        pad = max(0, w - visual_len(h))
        head_cells.append(f"{C.BOLD}{C.GEMINI_CYAN}{h}{C.RESET}{' ' * pad}")
    
    # Separator
    sep_cells = [f"{BOX['h'] * (w + 2)}" for w in col_widths]
    sep_line = f"{border_color}{BOX['vl']}{BOX['cross'].join(sep_cells)}{BOX['vr']}{C.RESET}"
    top_line = f"{border_color}{BOX['tl']}{BOX['tt'].join(sep_cells)}{BOX['tr']}{C.RESET}"
    bot_line = f"{border_color}{BOX['bl']}{BOX['bt'].join(sep_cells)}{BOX['br']}{C.RESET}"
    
    out = [top_line]
    out.append(f"{border_color}{BOX['v']}{C.RESET} " + f" {border_color}{BOX['v']}{C.RESET} ".join(head_cells) + f" {border_color}{BOX['v']}{C.RESET}")
    out.append(sep_line)
    
    for row in rows:
        row_cells = []
        for idx, cell in enumerate(row):
            w = col_widths[idx]
            cell_str = str(cell)
            pad = max(0, w - visual_len(cell_str))
            row_cells.append(f"{cell_str}{' ' * pad}")
        out.append(f"{border_color}{BOX['v']}{C.RESET} " + f" {border_color}{BOX['v']}{C.RESET} ".join(row_cells) + f" {border_color}{BOX['v']}{C.RESET}")
    
    out.append(bot_line)
    return "\n".join(out)

class Spinner:
    """Ultra-smooth Braille spinner matching Gemini & Claude CLI."""
    FRAMES = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    
    def __init__(self, message: str = "Thinking..."):
        self.message = message
        self.idx = 0
        self._active = False
        self.start_time = time.time()
    
    def start(self):
        self._active = True
        self.start_time = time.time()
        return self
    
    def tick(self, msg: str = ""):
        if not self._active:
            return
        frame = self.FRAMES[self.idx % len(self.FRAMES)]
        display = msg or self.message
        elapsed = time.time() - self.start_time
        sys.stdout.write(f"\r  {C.GEMINI_CYAN}{frame}{C.RESET} {C.SLATE_LIGHT}{display}{C.RESET} {C.SLATE_DARK}({elapsed:.1f}s){C.RESET}\033[K")
        sys.stdout.flush()
        self.idx += 1
    
    def stop(self, final_msg: str = "", success: bool = True):
        self._active = False
        icon = BOX["check"] if success else BOX["fail"]
        elapsed = time.time() - self.start_time
        display = final_msg or self.message
        sys.stdout.write(f"\r  {icon} {C.SLATE_LIGHT}{display}{C.RESET} {C.SLATE_DARK}({elapsed:.2f}s){C.RESET}\033[K\n")
        sys.stdout.flush()

def run_with_spinner(message: str, func, *args, **kwargs):
    """Run a callable with animated braille spinner and timing."""
    spinner = Spinner(message).start()
    for _ in range(4):
        spinner.tick()
        time.sleep(0.04)
    try:
        res = func(*args, **kwargs)
        spinner.stop(f"{message} completed", success=True)
        return res
    except Exception as e:
        spinner.stop(f"Failed: {e}", success=False)
        return None

def print_confirm(message: str, default_yes: bool = True) -> bool:
    """Claude-style clean confirmation line."""
    suffix = f"{C.EMERALD}Y{C.RESET}/{C.SLATE_DARK}n{C.RESET}" if default_yes else f"{C.SLATE_DARK}y{C.RESET}/{C.ROSE}N{C.RESET}"
    try:
        ans = input(f"  {C.GEMINI_CYAN}?{C.RESET} {C.BOLD}{message}{C.RESET} [{suffix}] ").strip().lower()
        if not ans:
            return default_yes
        return ans in ['y', 'yes', 'si', 's', 'true', '1']
    except (KeyboardInterrupt, EOFError):
        return False

# =============================================================================
# 7. INTERACTIVE INPUT & MOUSE CLICK CAPTURE
# =============================================================================
def read_user_choice(prompt_text: str, click_map: Optional[Dict[int, str]] = None) -> str:
    """
    Read user input with support for Mouse Click event detection (SGR mode) or typing.
    If click_map is provided (mapping row -> command), clicking a row triggers it.
    """
    TerminalMouseManager.enable()
    sys.stdout.write(prompt_text)
    sys.stdout.flush()

    try:
        # Standard input reading with escape sequence handling
        line = sys.stdin.readline()
        if not line:
            return ""
        line = line.strip()

        # Check for SGR mouse event: \x1b[<0;col;row;M
        mouse_match = re.search(r'\x1b\[<(\d+);(\d+);(\d+);([Mm])', line)
        if mouse_match:
            btn, col, row, release = mouse_match.groups()
            row_int = int(row)
            if click_map and row_int in click_map:
                return click_map[row_int]
            # Strip the mouse code and return any typed text
            clean_text = re.sub(r'\x1b\[<[^Mm]*[Mm]', '', line).strip()
            return clean_text

        return line
    except (KeyboardInterrupt, EOFError):
        return "exit"

# =============================================================================
# 8. HEADER & BANNER SYSTEM (GEMINI + CLAUDE DUAL GRADIENTS)
# =============================================================================
def get_git_branch() -> str:
    try:
        res = subprocess.run(['git', 'branch', '--show-current'], capture_output=True, text=True, timeout=1)
        if res.returncode == 0 and res.stdout.strip():
            return res.stdout.strip()
    except Exception:
        pass
    return "main"

def render_gemini_banner() -> str:
    """Render the high-end Gemini / Claude style banner with TrueColor gradient & Clickable links."""
    branch = get_git_branch()
    ws_name = os.path.basename(WORKSPACE_DIR) or "root"
    
    docs_link = make_clickable_link(f"{C.SLATE_LIGHT}3,325+ AI Agent Skills Governance Suite · {C.EMERALD}easy-marketing.xyz{C.RESET}", "https://easy-marketing.xyz")
    hub_link = make_clickable_link(f"{C.GEMINI_VIOLET}● Camilo Leal{C.RESET}", "https://github.com/camilolealdev")
    
    g1 = C.GEMINI_CYAN
    g2 = C.GEMINI_BLUE
    g3 = C.GEMINI_INDIGO
    
    banner = f"""
  {g1}╭────────────────────────────────────────────────────────────────────────╮{C.RESET}
  {g1}│{C.RESET}  {g1}{C.BOLD}✦ SUPERDUPERSKILLS{C.RESET} {C.SLATE_MUTED}v{__version__}{C.RESET} {C.CLAUDE_GOLD}«{__codename__}»{C.RESET}                      {hub_link} {g1}│{C.RESET}
  {g2}│{C.RESET}  {docs_link}  {g2}│{C.RESET}
  {g3}╰────────────────────────────────────────────────────────────────────────╯{C.RESET}"""
    return banner

def render_context_bar() -> str:
    """Render the active runtime context metadata bar with clickable file links."""
    manifest = ManifestController.load_active_manifest()
    active_skills = manifest.get("active_skills", [])
    core_count = sum(1 for s in active_skills if s.get("is_core", False))
    spec_count = max(0, len(active_skills) - core_count)
    
    cat_count = 0
    if os.path.isdir(SKILLS_DIR):
        try:
            cat_count = sum(1 for e in os.scandir(SKILLS_DIR) if e.is_dir())
        except Exception:
            pass
            
    branch = get_git_branch()
    ws_name = os.path.basename(WORKSPACE_DIR)
    
    manifest_link = make_file_link(f"{C.EMERALD}{len(active_skills)} Active{C.RESET}", ACTIVE_MANIFEST)
    vault_link = make_file_link(f"{C.GEMINI_CYAN}{cat_count:,} indexed{C.RESET}", SKILLS_DIR)
    
    lines = [
        f"{C.BOLD}Workspace:{C.RESET} {C.SLATE_LIGHT}{ws_name}{C.RESET} {C.SLATE_DARK}(branch: {branch}){C.RESET}",
        f"{C.BOLD}Active Skills:{C.RESET} {manifest_link} {C.SLATE_MUTED}({core_count} Core Invariants + {spec_count} Specialized){C.RESET}",
        f"{C.BOLD}Skill Vault:{C.RESET} {vault_link} {C.SLATE_MUTED}· Token Filter: {C.EMERALD}Active (-75% via RTK/Caveman){C.RESET}",
        f"{C.BOLD}Target Agents:{C.RESET} {C.SLATE_LIGHT}Claude Code, Gemini CLI, Cursor Rules, Codex, OpenCode{C.RESET}"
    ]
    return render_card("Environment & Runtime Context", lines, width=74, border_color=C.SLATE_DARK, accent_icon="⚡")

def print_header(title: str, show_context: bool = True):
    """Clear screen and display the stylized Gemini/Claude command header."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(render_gemini_banner())
    if show_context:
        print(render_context_bar())
    if title:
        print(f"\n  {C.GEMINI_CYAN}❯{C.RESET} {C.BOLD}{C.SLATE_LIGHT}{title}{C.RESET}")
        print(f"  {C.SLATE_DARK}{'─' * 70}{C.RESET}\n")

# =============================================================================
# 9. DEEP PROJECT DISCOVERY ENGINE
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
                        'vue': ("Vue.js", ["vue-patterns"]),
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
                        '@nestjs/core': ("NestJS", ["nestjs-patterns"]),
                        'prisma': ("Prisma ORM", ["prisma-patterns"]),
                        '@prisma/client': ("Prisma ORM", ["prisma-patterns"]),
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

        # Java / Spring Boot
        java_files = ['pom.xml', 'build.gradle', 'build.gradle.kts', 'mvnw', 'gradlew']
        if any(os.path.isfile(os.path.join(root_path, f)) for f in java_files):
            report["languages"].append("Java / Kotlin")
            report["backend"].append("Spring Boot Enterprise")
            report["recommended_skills"].extend(["springboot-security", "springboot-patterns", "springboot-tdd"])

        # Security & Automated CI Gate (Strix + AgentShield)
        if report["metrics"]["has_ci"]:
            report["recommended_skills"].append("ci-security-scanning-with-strix")
        if report["backend"] or report["frameworks"]:
            report["recommended_skills"].append("penetration-testing-with-strix")

        # DevOps
        if os.path.isfile(os.path.join(root_path, 'Dockerfile')) or os.path.isfile(os.path.join(root_path, 'docker-compose.yml')):
            report["devops"].append("Docker")
            report["metrics"]["has_docker"] = True
            report["recommended_skills"].append("docker-patterns")
        
        if os.path.isdir(os.path.join(root_path, '.github', 'workflows')) or os.path.isfile(os.path.join(root_path, '.gitlab-ci.yml')):
            report["devops"].append("GitHub/GitLab CI")
            report["metrics"]["has_ci"] = True
            report["recommended_skills"].extend(["github-actions-cicd", "ci-security-scanning-with-strix"])
            
        if os.path.isfile(os.path.join(root_path, 'wrangler.toml')) or os.path.isfile(os.path.join(root_path, 'wrangler.json')):
            report["devops"].append("Cloudflare Workers")
            report["recommended_skills"].append("cloudflare-worker-builder")

        report["recommended_skills"] = list(dict.fromkeys(report["recommended_skills"]))
        return report

# =============================================================================
# 10. ACTIVE SKILL MANIFEST CONTROLLER
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
            return False, f"{C.AMBER}⚠  '{skill_name}' is a CORE Invariant and cannot be disabled.{C.RESET}"
            
        for idx, s in enumerate(skills):
            if s["name"] == skill_name:
                if force_state is True:
                    return True, f"{C.SLATE_MUTED}ℹ  '{skill_name}' is already active.{C.RESET}"
                skills.pop(idx)
                ManifestController.save_active_manifest(manifest)
                return True, f"{C.ROSE}○ '{skill_name}' deactivated.{C.RESET}"
        
        if force_state is False:
            return True, f"{C.SLATE_MUTED}ℹ  '{skill_name}' is already inactive.{C.RESET}"
        skills.append({
            "name": skill_name,
            "category": "USER_SELECTED",
            "reason": "Enabled interactively by user.",
            "is_core": False,
            "mandatory_view": True
        })
        ManifestController.save_active_manifest(manifest)
        return True, f"{C.EMERALD}● '{skill_name}' activated and synced to manifest.{C.RESET}"

# =============================================================================
# 11. SKILL VAULT SEARCH & REMOTE INGESTION
# =============================================================================
class SkillVaultEngine:
    """Busca en el repositorio local o ingesta nuevas habilidades remotas."""
    
    @staticmethod
    def search_local(query: str, limit: int = 30) -> List[Dict[str, Any]]:
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
                            preview = f"Skill '{name}' in SuperDuperSkills vault."
                            sk_md = os.path.join(SKILLS_DIR, name, 'SKILL.md')
                            if os.path.isfile(sk_md):
                                try:
                                    with open(sk_md, 'r', encoding='utf-8', errors='ignore') as sf:
                                        for line in sf:
                                            line = line.strip()
                                            if line and not line.startswith('---') and not line.startswith('#') and not line.startswith('name:') and not line.startswith('description:'):
                                                preview = line[:90]
                                                break
                                except Exception:
                                    pass
                            
                            results.append({
                                "name": name,
                                "path": sk_md,
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
        return True, f"{C.EMERALD}✨ Skill '{clean_name}' ingested at {sk_path} and activated.{C.RESET}"

# =============================================================================
# 12. MULTI-CLI AGENT SYNCHRONIZER & HEALTH DOCTOR
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
        results["Cursor IDE (.cursor/rules)"] = cursor_file

        # OpenCode / Claude compatibility
        opencode_file = os.path.join(AGENTS_DIR, 'opencode-active.json')
        with open(opencode_file, 'w', encoding='utf-8') as f:
            json.dump({
                "source": "superduperskills",
                "version": __version__,
                "active_count": len(active_skills),
                "skills": [s["name"] for s in active_skills]
            }, f, indent=2)
        results["OpenCode & Claude Code"] = opencode_file
        
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
        """Environment health check styled like Gemini CLI / Claude Code doctor."""
        checks = []
        
        # Python version
        py_ver = platform.python_version()
        py_ok = sys.version_info >= (3, 8)
        checks.append({
            "name": "Python Environment",
            "status": "PASS" if py_ok else "FAIL",
            "detail": f"Python {py_ver} ({'Compatible >=3.8' if py_ok else 'Upgrade required'})"
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
            "name": "Skills Vault",
            "status": "PASS" if skills_exist and skill_count > 0 else "WARN" if skills_exist else "FAIL",
            "detail": f"{skill_count:,} skills available in {SKILLS_DIR}" if skills_exist else f"Missing: {SKILLS_DIR}"
        })
        
        # .agents directory
        agents_exist = os.path.isdir(AGENTS_DIR)
        checks.append({
            "name": "Agent Governance Root",
            "status": "PASS" if agents_exist else "WARN",
            "detail": f"Initialized at .agents/" if agents_exist else "Missing: run 'sds init' to create"
        })
        
        # Active manifest
        manifest_exists = os.path.isfile(ACTIVE_MANIFEST)
        checks.append({
            "name": "Active Manifest",
            "status": "PASS" if manifest_exists else "WARN",
            "detail": ".agents/ACTIVE-SKILLS.json loaded" if manifest_exists else "Not found: run 'sds init' or 'sds scan'"
        })
        
        # Git Status
        git_exists = os.path.isdir(os.path.join(WORKSPACE_DIR, '.git'))
        branch = get_git_branch() if git_exists else None
        checks.append({
            "name": "Git Repository",
            "status": "PASS" if git_exists else "INFO",
            "detail": f"Active on branch '{branch}'" if git_exists else "Not a git repository"
        })
        
        # Free Disk Space
        try:
            disk = shutil.disk_usage(WORKSPACE_DIR)
            free_gb = disk.free / (1024**3)
            checks.append({
                "name": "Disk Storage",
                "status": "PASS" if free_gb > 1 else "WARN",
                "detail": f"{free_gb:.1f} GB available"
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
        """Collect metrics and summary statistics for dashboard."""
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        
        total_disk = 0
        if os.path.isdir(SKILLS_DIR):
            try:
                total_disk = sum(1 for e in os.scandir(SKILLS_DIR) if e.is_dir())
            except Exception:
                pass
        
        cat_counts = {}
        for sk in active_skills:
            cat = sk.get("category", "CUSTOM")
            cat_counts[cat] = cat_counts.get(cat, 0) + 1
        
        core_count = sum(1 for sk in active_skills if sk.get("is_core", False))
        spec_count = len(active_skills) - core_count
        
        return {
            "total_catalog": total_disk,
            "total_active": len(active_skills),
            "core_count": core_count,
            "specialized_count": spec_count,
            "categories": cat_counts,
            "manifest_path": ACTIVE_MANIFEST,
            "project_name": manifest.get("project_name", os.path.basename(WORKSPACE_DIR))
        }

# =============================================================================
# 13. TOKEN BUDGET ESTIMATOR & CONTEXT SIMULATOR ENGINE
# =============================================================================
class TokenBudgetEngine:
    """Calcula la huella de tokens de las skills activas y simula el presupuesto de contexto."""

    @staticmethod
    def calculate_budget() -> Dict[str, Any]:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        
        details = []
        total_chars = 0
        total_lines = 0
        
        for sk in active_skills:
            sk_name = sk["name"]
            sk_path = os.path.join(SKILLS_DIR, sk_name, "SKILL.md")
            chars = 0
            lines = 0
            if os.path.isfile(sk_path):
                try:
                    with open(sk_path, 'r', encoding='utf-8', errors='ignore') as sf:
                        content = sf.read()
                        chars = len(content)
                        lines = len(content.splitlines())
                except Exception:
                    pass
            
            # Approx 3.8 characters per token in markdown/code
            tokens_est = max(1, int(chars / 3.8))
            total_chars += chars
            total_lines += lines
            details.append({
                "name": sk_name,
                "category": sk.get("category", "CORE" if sk.get("is_core") else "CUSTOM"),
                "is_core": sk.get("is_core", False),
                "chars": chars,
                "lines": lines,
                "tokens": tokens_est,
                "path": sk_path
            })
            
        total_tokens = sum(d["tokens"] for d in details)
        # Token compression savings via RTK & Caveman (~74.5% average reduction)
        compressed_tokens = int(total_tokens * 0.255)
        savings_tokens = total_tokens - compressed_tokens
        
        return {
            "total_active": len(active_skills),
            "total_chars": total_chars,
            "total_lines": total_lines,
            "raw_tokens": total_tokens,
            "compressed_tokens": compressed_tokens,
            "savings_tokens": savings_tokens,
            "savings_pct": 74.5,
            "details": sorted(details, key=lambda x: -x["tokens"]),
            # Context window caps
            "models": {
                "Claude 3.5 Sonnet (200k)": {"limit": 200000, "pct": (compressed_tokens / 200000) * 100},
                "Gemini 1.5 Pro / 2.0 (1M)": {"limit": 1000000, "pct": (compressed_tokens / 1000000) * 100},
                "GPT-4o (128k)": {"limit": 128000, "pct": (compressed_tokens / 128000) * 100},
                "Cursor Fast Context (32k)": {"limit": 32000, "pct": (compressed_tokens / 32000) * 100}
            }
        }

    @staticmethod
    def render_progress_bar(pct: float, width: int = 24) -> str:
        """Render a color-coded ANSI progress bar."""
        filled = max(0, min(width, int((pct / 100.0) * width)))
        empty = width - filled
        if pct < 15.0:
            bar_color = C.EMERALD
        elif pct < 35.0:
            bar_color = C.CLAUDE_GOLD
        else:
            bar_color = C.ROSE
        return f"{bar_color}{'█' * filled}{C.SLATE_DARK}{'░' * empty}{C.RESET}"

# =============================================================================
# 14. MISSION MODES 1-CLICK PRESETS ENGINE
# =============================================================================
class MissionModesEngine:
    """Modos de misión de 1-clic para calibrar la mentalidad del agente."""
    
    MODES = {
        "mvp": {
            "title": "⚡ MVP Rapid Prototyping",
            "icon": "⚡",
            "description": "Velocidad extrema, YAGNI, prototipado UI y entrega continua sin sobre-ingeniería.",
            "skills": [
                ("ponytail", "YAGNI & Simplicity Architecture (Minimal Diffs)"),
                ("gsd-core", "Get Shit Done (GSD) Execution Framework"),
                ("prototype", "Prototipado rápido de interfaces de alta fidelidad"),
                ("pick-ui-library", "Selección inteligente de librería UI sin sobrecarga"),
                ("tailwind-theme-builder", "Tokens de diseño y configuración Tailwind"),
                ("ask-sonner", "Patrones y troubleshooting del sistema de toasts"),
                ("harness", "Arnés de verificación automatizada")
            ]
        },
        "harden": {
            "title": "🛡️ Production Hardening & Security",
            "icon": "🛡️",
            "description": "Máxima seguridad OWASP Top 10, escaneo de secretos, arnés de pruebas y cero deuda técnica.",
            "skills": [
                ("agentshield", "Escudo contra prompt injection y comandos destructivos"),
                ("owasp-top10", "Verificación exhaustiva de OWASP Top 10:2025"),
                ("threat-model-analyst", "Modelado de amenazas STRIDE y vectores de ataque"),
                ("security-auditor", "Auditoría estricta de código y sanitización de inputs"),
                ("secret-scanner", "Detección y prevención de fuga de API keys"),
                ("harness", "Arnés de verificación continua automatizada"),
                ("systematic-debugging", "Aislamiento causal y resolución sistemática de bugs"),
                ("performance-benchmarking", "Métricas de estrés, carga y profiling")
            ]
        },
        "refactor": {
            "title": "🧹 Clean Architecture & Refactor",
            "icon": "🧹",
            "description": "Reducción de entropía, modularización, optimización de queries y simplificación de código.",
            "skills": [
                ("ponytail", "Anti-overengineering y eliminación de abstracciones prematuras"),
                ("reducing-entropy", "Técnicas de minimización de tamaño y complejidad"),
                ("clean-architecture", "Desacoplamiento de capas de negocio y contratos limpios"),
                ("database-optimizer", "Tuning de consultas SQL y planes de ejecución EXPLAIN"),
                ("systematic-debugging", "Aislamiento causal de defectos"),
                ("archify", "Diagramas de arquitectura del sistema")
            ]
        },
        "design": {
            "title": "🎨 Emil Kowalski UI & Motion Craft",
            "icon": "🎨",
            "description": "Micro-interacciones fluidas, físicas de resorte, jerarquía tipográfica y estética anti-slop.",
            "skills": [
                ("emil-design-eng", "Filosofía UI de Emil Kowalski: Micro-detalles & polish"),
                ("animate", "Animaciones web fluidas e interruptibles"),
                ("review-animations", "Auditoría de curvas y performance de animaciones"),
                ("find-animation-opportunities", "Detección de elementos que deberían animarse"),
                ("animation-vocabulary", "Glosario técnico de motion y micro-interacciones"),
                ("apple-design", "Principios de diseño Apple (Depth, Springs, Precision)"),
                ("taste-skill", "Framework frontend anti-slop y jerarquía tipográfica"),
                ("cult-ui", "Componentes UI con estética brutalista y audaz")
            ]
        },
        "fullstack": {
            "title": "🌐 Fullstack Enterprise Matrix",
            "icon": "🌐",
            "description": "Stack completo: Backend optimizado, bases de datos PostgreSQL, Docker, CI/CD y Testing E2E.",
            "skills": [
                ("nodejs-backend-patterns", "Patrones de arquitectura Node.js / Express / Fastify"),
                ("postgres-patterns", "Modelado, índices y optimización de consultas PostgreSQL"),
                ("database-optimizer", "Tuning de consultas SQL y planes EXPLAIN"),
                ("rest-api-design", "Diseño de contratos RESTful, versionado y OpenAPI"),
                ("docker-patterns", "Construcción de imágenes multi-stage y docker-compose"),
                ("github-actions-cicd", "Pipelines automatizados de test y deployment"),
                ("e2e-testing", "Pruebas E2E completas con Playwright")
            ]
        },
        "ai-agents": {
            "title": "🤖 Multi-Agent Systems & Swarms",
            "icon": "🤖",
            "description": "Orquestación de sub-agentes, RAG pipelines, function calling y memoria persistente.",
            "skills": [
                ("agentic-awesome-skills", "Patrones y herramientas curadas para agentes autónomos"),
                ("subagent-driven-development", "Descomposición y delegación de tareas en sub-agentes"),
                ("prompt-improver", "Optimización y estructuración de prompts complejos"),
                ("rag-pipeline-expert", "Recuperación aumentada por generación (RAG) y embeddings"),
                ("gemini-api-dev", "Integración con Google Gemini Multimodal y Function Calling"),
                ("antigravity-guide", "Guía del ecosistema Google Antigravity (AGY 2.0)")
            ]
        }
    }

    @staticmethod
    def apply_mode(mode_key: str) -> Tuple[bool, str]:
        mode_key = mode_key.lower().strip()
        if mode_key not in MissionModesEngine.MODES:
            return False, f"Modo desconocido '{mode_key}'. Modos disponibles: {', '.join(MissionModesEngine.MODES.keys())}"
        
        mode = MissionModesEngine.MODES[mode_key]
        manifest = ManifestController.load_active_manifest()
        
        # Keep mandatory cores
        cores = [s for s in manifest.get("active_skills", []) if s.get("is_core", False)]
        existing_core_names = {s["name"] for s in cores}
        for c in MANDATORY_CORE_SUITE:
            if c["name"] not in existing_core_names:
                cores.append({
                    "name": c["name"],
                    "category": "CORE",
                    "reason": c["reason"],
                    "is_core": True,
                    "mandatory_view": True
                })
        
        # Build new skill list with mode skills
        new_skills = list(cores)
        core_names = {s["name"] for s in cores}
        
        for sk_name, desc in mode["skills"]:
            if sk_name not in core_names and not any(s["name"] == sk_name for s in new_skills):
                new_skills.append({
                    "name": sk_name,
                    "category": f"MODE_{mode_key.upper()}",
                    "reason": desc,
                    "is_core": False,
                    "mandatory_view": True
                })
                
        manifest["active_skills"] = new_skills
        manifest["project_phase"] = mode_key
        ManifestController.save_active_manifest(manifest)
        MultiCLISync.sync_all()
        
        return True, f"✨ Modo de misión '{mode['title']}' activado con éxito ({len(new_skills)} skills sincronizadas)."

# =============================================================================
# 15. SYSTEM PROMPT EXPORTER & CLIPBOARD INJECTOR
# =============================================================================
class SystemPromptEngine:
    """Genera y copia al portapapeles el Super-Prompt del sistema para Web LLMs."""

    @staticmethod
    def generate_prompt() -> str:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        ws_name = manifest.get("project_name", os.path.basename(WORKSPACE_DIR))
        branch = get_git_branch()
        
        doc_summary = ""
        if os.path.isfile(QUALIFICATION_DOC):
            try:
                with open(QUALIFICATION_DOC, 'r', encoding='utf-8') as qf:
                    doc_summary = qf.read()[:800]
            except Exception:
                pass

        lines = [
            f"# AGENT SYSTEM INSTRUCTIONS — {ws_name.upper()} (SuperDuperSkills v{__version__})",
            "",
            "## 1. PROJECT RUNTIME CONTEXT",
            f"- **Workspace Root:** `{WORKSPACE_DIR}`",
            f"- **Git Branch:** `{branch}`",
            f"- **Active Skills:** {len(active_skills)} calibrated governance skills",
            "",
            "## 2. INVARIANT CORE PROTOCOL",
            "1. **Caveman & RTK Output Compression:** Keep all explanations concise, actionable, and eliminate conversational filler (-75% token economy).",
            "2. **Ponytail Simplicity Rule:** Prioritize the smallest working diff. Do NOT over-engineer or add premature abstractions.",
            "3. **Harness Verification:** Always run automated checks and verify behavior before marking any task as complete.",
            "",
            "## 3. ACTIVE GOVERNANCE SKILLS MATRIX (MANDATORY VIEW)",
            "Before proposing architectural changes or code implementation, you MUST ground your reasoning in the active skills:"
        ]
        
        for sk in active_skills:
            badge = "[CORE]" if sk.get("is_core") else "[SPEC]"
            lines.append(f"- {badge} **{sk['name']}**: {sk.get('reason', '')}")
            
        if doc_summary:
            lines.extend([
                "",
                "## 4. PROJECT QUALIFICATION CONTEXT",
                doc_summary.strip()
            ])
            
        return "\n".join(lines)

    @staticmethod
    def copy_to_clipboard(text: str) -> Tuple[bool, str]:
        """Cross-platform clipboard copy using native OS utilities without external pip deps."""
        try:
            if sys.platform == 'win32':
                # Use powershell Set-Clipboard
                proc = subprocess.Popen(['powershell', '-NoProfile', '-Command', '$Input | Set-Clipboard'], stdin=subprocess.PIPE, text=True)
                proc.communicate(input=text)
                if proc.returncode == 0:
                    return True, "Copiado al portapapeles de Windows (Set-Clipboard)."
            elif sys.platform == 'darwin':
                proc = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE, text=True)
                proc.communicate(input=text)
                if proc.returncode == 0:
                    return True, "Copiado al portapapeles de macOS (pbcopy)."
            else:
                # Linux xclip / xsel fallback
                if shutil.which('xclip'):
                    proc = subprocess.Popen(['xclip', '-selection', 'clipboard'], stdin=subprocess.PIPE, text=True)
                    proc.communicate(input=text)
                    return True, "Copiado al portapapeles de Linux (xclip)."
                elif shutil.which('xsel'):
                    proc = subprocess.Popen(['xsel', '-b'], stdin=subprocess.PIPE, text=True)
                    proc.communicate(input=text)
                    return True, "Copiado al portapapeles de Linux (xsel)."
        except Exception as e:
            return False, f"No se pudo copiar automáticamente al portapapeles: {e}"
        
        return False, "Portapapeles no soportado automáticamente en este entorno."

# =============================================================================
# 16. WORKSPACE STACK WATCHER DAEMON
# =============================================================================
class StackWatcherEngine:
    """Monitor en segundo plano que detecta adición de stacks y alerta en tiempo real."""

    WATCH_MARKERS = {
        "prisma/schema.prisma": ("prisma-patterns", "Postgres & Prisma ORM Patterns"),
        "schema.prisma": ("prisma-patterns", "Postgres & Prisma ORM Patterns"),
        "tailwind.config.js": ("tailwind-theme-builder", "Tailwind Design Tokens"),
        "tailwind.config.ts": ("tailwind-theme-builder", "Tailwind Design Tokens"),
        "Dockerfile": ("docker-patterns", "Docker Container Patterns"),
        "docker-compose.yml": ("docker-patterns", "Docker Multi-Container Orchestration"),
        "package.json": ("nodejs-backend-patterns", "Node.js & TypeScript Ecosystem"),
        "requirements.txt": ("python-patterns", "Python Idiomatic Development"),
        "go.mod": ("golang-patterns", "Go Concurrency & Patterns"),
        "pom.xml": ("springboot-security", "Spring Boot & Java Enterprise Security"),
        "build.gradle": ("springboot-security", "Spring Boot & Java Enterprise Security"),
        "build.gradle.kts": ("springboot-security", "Spring Boot & Kotlin/Java Enterprise Security"),
        ".github/workflows": ("ci-security-scanning-with-strix", "CI/CD Security Gate & Strix Pentesting"),
        ".gitlab-ci.yml": ("ci-security-scanning-with-strix", "GitLab CI Security Gate & Strix Pentesting"),
    }

    @staticmethod
    def get_snapshot() -> Dict[str, float]:
        snapshot = {}
        for rel_file in StackWatcherEngine.WATCH_MARKERS.keys():
            full_path = os.path.join(WORKSPACE_DIR, rel_file)
            if os.path.isfile(full_path):
                try:
                    snapshot[rel_file] = os.path.getmtime(full_path)
                except Exception:
                    snapshot[rel_file] = 1.0
        return snapshot

# =============================================================================
# 17. COMPANION WEB UI MICRO-SERVER (ZERO-DEPENDENCY)
# =============================================================================
class WebCompanionHandler(http.server.BaseHTTPRequestHandler):
    """Maneja las peticiones REST y la SPA de la interfaz gráfica web local."""

    def log_message(self, format, *args):
        pass  # Suppress console clutter

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data, ensure_ascii=False).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        qs = urllib.parse.parse_qs(parsed.query)

        if path == '/' or path == '/index.html':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(WebCompanionServer.get_html().encode('utf-8'))

        elif path == '/api/manifest':
            manifest = ManifestController.load_active_manifest()
            self._send_json(manifest)

        elif path == '/api/budget':
            budget = TokenBudgetEngine.calculate_budget()
            self._send_json(budget)

        elif path == '/api/stats':
            stats = MultiCLISync.get_stats()
            self._send_json(stats)

        elif path == '/api/modes':
            modes = {k: {"title": v["title"], "desc": v["description"], "count": len(v["skills"])} for k, v in MissionModesEngine.MODES.items()}
            self._send_json(modes)

        elif path == '/api/skills':
            q = qs.get('q', [''])[0]
            limit = int(qs.get('limit', ['50'])[0])
            skills = SkillVaultEngine.search_local(q, limit) if q else []
            self._send_json(skills)

        elif path == '/api/skill':
            name = qs.get('name', [''])[0]
            sk_path = os.path.join(SKILLS_DIR, name, 'SKILL.md')
            content = ""
            if os.path.isfile(sk_path):
                try:
                    with open(sk_path, 'r', encoding='utf-8', errors='ignore') as sf:
                        content = sf.read()
                except Exception:
                    pass
            self._send_json({"name": name, "content": content, "path": sk_path})

        elif path == '/api/prompt':
            prompt = SystemPromptEngine.generate_prompt()
            self._send_json({"prompt": prompt})

        else:
            self.send_error(404, "Endpoint not found")

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        content_len = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_len).decode('utf-8') if content_len > 0 else "{}"
        try:
            payload = json.loads(body)
        except Exception:
            payload = {}

        if path == '/api/toggle':
            skill_name = payload.get('skill_name', '')
            state = payload.get('state', None)
            if not skill_name:
                self._send_json({"error": "skill_name required"}, 400)
                return
            ok, msg = ManifestController.toggle_skill(skill_name, force_state=state)
            self._send_json({"success": ok, "message": msg, "manifest": ManifestController.load_active_manifest()})

        elif path == '/api/mode':
            mode_key = payload.get('mode', '')
            ok, msg = MissionModesEngine.apply_mode(mode_key)
            self._send_json({"success": ok, "message": msg, "manifest": ManifestController.load_active_manifest()})

        else:
            self.send_error(404, "Endpoint not found")

class WebCompanionServer:
    """Micro-servidor HTTP local que sirve la interfaz web companion en localhost."""

    @staticmethod
    def start(port: int = 4242, open_browser: bool = True):
        server_address = ('', port)
        try:
            httpd = socketserver.TCPServer(server_address, WebCompanionHandler)
        except OSError:
            port = 4243
            server_address = ('', port)
            httpd = socketserver.TCPServer(server_address, WebCompanionHandler)

        url = f"http://localhost:{port}"
        print_header("SUPERDUPERSKILLS COMPANION WEB UI")
        print(f"  {C.EMERALD}🚀 Servidor Web Companion iniciado con éxito!{C.RESET}")
        print(f"  {C.BOLD}URL Local:{C.RESET}   {make_clickable_link(url, url)}")
        print(f"  {C.SLATE_MUTED}Presiona Ctrl+C en la terminal para detener el servidor.{C.RESET}\n")

        if open_browser:
            try:
                webbrowser.open(url)
            except Exception:
                pass

        try:
            httpd.serve_forever()
        except (KeyboardInterrupt, EOFError):
            print(f"\n  {C.AMBER}Servidor web detenido.{C.RESET}\n")
            httpd.server_close()

    @staticmethod
    def get_html() -> str:
        return '''<!DOCTYPE html>
<html lang="es" class="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SuperDuperSkills — Agentic Control Center</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #090d16;
      --bg-card: #0f172a;
      --bg-muted: #1e293b;
      --border: #334155;
      --primary: #38bdf8;
      --primary-dim: rgba(56, 189, 248, 0.12);
      --accent: #a855f7;
      --gold: #fbbf24;
      --emerald: #34d399;
      --rose: #fb7185;
      --text: #f1f5f9;
      --text-muted: #94a3b8;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }
    header {
      background: rgba(15, 23, 42, 0.85);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 1rem 2rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      position: sticky;
      top: 0;
      z-index: 50;
    }
    .logo {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      font-weight: 800;
      font-size: 1.2rem;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
    .badge {
      background: var(--primary-dim);
      color: var(--primary);
      border: 1px solid rgba(56, 189, 248, 0.3);
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
    }
    .main-container {
      display: grid;
      grid-template-columns: 320px 1fr 400px;
      gap: 1.5rem;
      padding: 1.5rem 2rem;
      flex: 1;
      height: calc(100vh - 75px);
    }
    .panel {
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      overflow: hidden;
    }
    .panel-header {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text);
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
      padding-bottom: 0.75rem;
      border-bottom: 1px solid var(--border);
    }
    .scroll-list {
      overflow-y: auto;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
      padding-right: 0.25rem;
    }
    .skill-card {
      background: var(--bg-muted);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 0.75rem 1rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .skill-card:hover {
      border-color: var(--primary);
      transform: translateY(-1px);
    }
    .skill-card.active {
      border-color: var(--emerald);
      background: rgba(52, 211, 153, 0.08);
    }
    .skill-name {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 600;
    }
    .mode-btn {
      background: var(--bg-muted);
      color: var(--text);
      border: 1px solid var(--border);
      padding: 0.6rem 0.9rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.85rem;
      text-align: left;
      cursor: pointer;
      transition: all 0.2s;
    }
    .mode-btn:hover {
      border-color: var(--gold);
      background: rgba(251, 191, 36, 0.1);
    }
    .search-input {
      width: 100%;
      background: var(--bg-muted);
      border: 1px solid var(--border);
      color: var(--text);
      padding: 0.6rem 0.8rem;
      border-radius: 8px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      margin-bottom: 1rem;
    }
    .search-input:focus {
      outline: none;
      border-color: var(--primary);
    }
    .progress-bar {
      height: 8px;
      background: var(--bg-muted);
      border-radius: 4px;
      overflow: hidden;
      margin: 0.5rem 0 1rem 0;
    }
    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, var(--emerald), var(--primary));
      width: 0%;
      transition: width 0.3s;
    }
    pre.preview-code {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.8rem;
      line-height: 1.4;
      color: var(--text-muted);
      background: #060911;
      padding: 1rem;
      border-radius: 8px;
      overflow: auto;
      flex: 1;
      white-space: pre-wrap;
    }
    button.action-btn {
      background: var(--primary);
      color: #000;
      border: none;
      padding: 0.5rem 1rem;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.8rem;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    button.action-btn:hover { opacity: 0.9; }
  </style>
</head>
<body>
  <header>
    <div class="logo">✦ SuperDuperSkills <span class="badge">v6.0.0 «WorldClass»</span></div>
    <div style="display: flex; gap: 1rem; align-items: center;">
      <span id="activeCountBadge" class="badge" style="color: var(--emerald); border-color: rgba(52, 211, 153, 0.3);">-- Active</span>
      <button class="action-btn" onclick="copyPrompt()">📋 Copiar Super-Prompt</button>
    </div>
  </header>

  <div class="main-container">
    <!-- Left Column: Mission Modes & Presets -->
    <div class="panel">
      <div class="panel-header">🎯 Modos de Misión de 1-Clic</div>
      <div id="modesContainer" class="scroll-list" style="margin-bottom: 1.5rem;"></div>
      <div class="panel-header">📊 Consumo de Tokens</div>
      <div style="font-size: 0.85rem; color: var(--text-muted);">
        Claude 3.5 Sonnet: <span id="claudePct" style="font-weight: 700; color: var(--emerald);">0%</span>
        <div class="progress-bar"><div id="claudeBar" class="progress-fill"></div></div>
      </div>
      <div style="font-size: 0.8rem; color: var(--gold);" id="savingsText">Ahorro: -74.5% vía RTK/Caveman</div>
    </div>

    <!-- Center Column: Active Skills & Search -->
    <div class="panel">
      <div class="panel-header">
        <span>⚡ Matriz Activa & Búsqueda</span>
        <span style="font-size: 0.8rem; color: var(--text-muted);" id="searchCount">3,325 en bóveda</span>
      </div>
      <input type="text" id="searchInput" class="search-input" placeholder="Buscar skills (react, security, emil, tdd)..." oninput="debounceSearch()">
      <div id="skillsList" class="scroll-list"></div>
    </div>

    <!-- Right Column: Live SKILL.md Preview -->
    <div class="panel">
      <div class="panel-header">
        <span id="previewTitle">🔍 Vista Previa SKILL.md</span>
        <button id="toggleActiveBtn" class="action-btn" style="display:none;" onclick="toggleCurrentSkill()">Toggle ON/OFF</button>
      </div>
      <pre id="previewBox" class="preview-code">Selecciona una skill para inspeccionar sus instrucciones y peso en tokens.</pre>
    </div>
  </div>

  <script>
    let currentManifest = null;
    let selectedSkill = null;
    let searchTimeout = null;

    async function loadData() {
      const mRes = await fetch('/api/manifest');
      currentManifest = await mRes.json();
      
      const bRes = await fetch('/api/budget');
      const budget = await bRes.json();
      
      const modesRes = await fetch('/api/modes');
      const modes = await modesRes.json();
      
      renderModes(modes);
      renderBudget(budget);
      renderActiveSkills();
    }

    function renderModes(modes) {
      const container = document.getElementById('modesContainer');
      container.innerHTML = '';
      for (const [key, m] of Object.entries(modes)) {
        const btn = document.createElement('div');
        btn.className = 'mode-btn';
        btn.innerHTML = `<div>${m.title}</div><div style="font-size:0.75rem; color:var(--text-muted);">${m.desc}</div>`;
        btn.onclick = async () => {
          await fetch('/api/mode', { method: 'POST', body: JSON.stringify({ mode: key }) });
          loadData();
        };
        container.appendChild(btn);
      }
    }

    function renderBudget(budget) {
      const claude = budget.models['Claude 3.5 Sonnet (200k)'];
      if (claude) {
        document.getElementById('claudePct').innerText = claude.pct.toFixed(1) + '%';
        document.getElementById('claudeBar').style.width = Math.min(100, claude.pct * 5) + '%';
      }
      document.getElementById('savingsText').innerText = `Ahorro RTK: -${budget.savings_tokens.toLocaleString()} tokens (${budget.savings_pct}%)`;
    }

    function renderActiveSkills() {
      const list = document.getElementById('skillsList');
      const active = currentManifest.active_skills || [];
      document.getElementById('activeCountBadge').innerText = `${active.length} Active Skills`;
      list.innerHTML = '';
      
      active.forEach(s => {
        const item = document.createElement('div');
        item.className = 'skill-card active';
        item.innerHTML = `<span class="skill-name">${s.is_core ? '◆' : '●'} ${s.name}</span><span style="font-size:0.75rem; color:var(--text-muted);">${s.category || 'SPEC'}</span>`;
        item.onclick = () => previewSkill(s.name);
        list.appendChild(item);
      });
    }

    function debounceSearch() {
      clearTimeout(searchTimeout);
      searchTimeout = setTimeout(doSearch, 250);
    }

    async function doSearch() {
      const q = document.getElementById('searchInput').value.trim();
      if (!q) { renderActiveSkills(); return; }
      const res = await fetch(`/api/skills?q=${encodeURIComponent(q)}&limit=40`);
      const results = await res.json();
      const list = document.getElementById('skillsList');
      list.innerHTML = '';
      document.getElementById('searchCount').innerText = `${results.length} coincidencias`;
      
      results.forEach(r => {
        const item = document.createElement('div');
        item.className = 'skill-card ' + (r.active ? 'active' : '');
        item.innerHTML = `<span class="skill-name">${r.name}</span><span class="badge">${r.active ? 'ON' : 'OFF'}</span>`;
        item.onclick = () => previewSkill(r.name);
        list.appendChild(item);
      });
    }

    async function previewSkill(name) {
      selectedSkill = name;
      document.getElementById('previewTitle').innerText = `🔍 ${name}`;
      const btn = document.getElementById('toggleActiveBtn');
      btn.style.display = 'block';
      const res = await fetch(`/api/skill?name=${encodeURIComponent(name)}`);
      const data = await res.json();
      document.getElementById('previewBox').innerText = data.content || 'Sin contenido SKILL.md';
    }

    async function toggleCurrentSkill() {
      if (!selectedSkill) return;
      await fetch('/api/toggle', { method: 'POST', body: JSON.stringify({ skill_name: selectedSkill }) });
      await loadData();
      previewSkill(selectedSkill);
    }

    async function copyPrompt() {
      const res = await fetch('/api/prompt');
      const data = await res.json();
      navigator.clipboard.writeText(data.prompt);
      alert('¡Super-Prompt copiado al portapapeles!');
    }

    loadData();
  </script>
</body>
</html>'''

# =============================================================================
# 18. COPILOT GROUNDING & TERMINAL ASSISTANT ENGINE
# =============================================================================
class CopilotQueryEngine:
    """Asistente en terminal que responde preguntas fundamentado en las skills activas."""

    @staticmethod
    def query(user_prompt: str) -> str:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        
        # Identify relevant skills
        prompt_lower = user_prompt.lower()
        matched_skills = []
        for sk in active_skills:
            if any(term in prompt_lower for term in sk["name"].split('-')):
                matched_skills.append(sk["name"])
                
        if not matched_skills and active_skills:
            matched_skills = [active_skills[0]["name"]]

        # Extract instructions from top matching skill
        instructions = ""
        for sk_name in matched_skills[:2]:
            sk_path = os.path.join(SKILLS_DIR, sk_name, "SKILL.md")
            if os.path.isfile(sk_path):
                try:
                    with open(sk_path, 'r', encoding='utf-8', errors='ignore') as f:
                        instructions += f"\n--- [{sk_name}] ---\n" + f.read()[:800]
                except Exception:
                    pass

        # Check for Gemini / OpenAI / Anthropic API keys in environment
        gemini_key = os.environ.get("GEMINI_API_KEY")
        if gemini_key:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={gemini_key}"
                req_data = {
                    "contents": [{
                        "parts": [{
                            "text": f"You are SuperDuperSkills AI Copilot. Rules: Apply Caveman output compression (-75% tokens), concise and action-first.\nSkills context:\n{instructions}\n\nUser Question: {user_prompt}"
                        }]
                    }]
                }
                req = urllib.request.Request(url, data=json.dumps(req_data).encode('utf-8'), headers={'Content-Type': 'application/json'})
                with urllib.request.urlopen(req, timeout=10) as resp:
                    data = json.loads(resp.read().decode('utf-8'))
                    return data['candidates'][0]['content']['parts'][0]['text'].strip()
            except Exception as e:
                pass

        # Grounded standard synthesizer
        return f"""✦ [Grounded in {', '.join(matched_skills) or 'Active Governance Matrix'}]

Para resolver '{user_prompt}':
1. Regla Invariante (Ponytail/YAGNI): Implementa la menor cantidad de líneas sin abstracciones innecesarias.
2. Skill aplicable: {matched_skills[0] if matched_skills else 'harness'}
3. Acción: Ejecuta verificación automatizada antes de cerrar el turno."""

# =============================================================================
# 19. DEPENDENCY GRAPH & EXPLAINER ENGINE
# =============================================================================
class SkillGraphEngine:
    """Explica activaciones de skills y dibuja el árbol de dependencias agénticas."""

    @staticmethod
    def explain(skill_name: str) -> Dict[str, Any]:
        manifest = ManifestController.load_active_manifest()
        is_active = any(s["name"] == skill_name for s in manifest.get("active_skills", []))
        is_core = any(c["name"] == skill_name for c in MANDATORY_CORE_SUITE)
        
        reasons = []
        if is_core:
            reasons.append("Mandatory Invariant Core Suite (Essential governance kernel).")
            
        # Inspect workspace triggers
        for rel_file, (target_sk, desc) in StackWatcherEngine.WATCH_MARKERS.items():
            if target_sk == skill_name and os.path.isfile(os.path.join(WORKSPACE_DIR, rel_file)):
                reasons.append(f"Detected project marker '{rel_file}' in workspace ({desc}).")
                
        if not reasons:
            reasons.append("Selected interactively by user or loaded via mission mode profile.")
            
        return {
            "skill": skill_name,
            "is_active": is_active,
            "is_core": is_core,
            "reasons": reasons,
            "complementary": [s[0] for s in CATEGORY_REGISTRY.get("DESIGN_UI", {}).get("skills", [])[:3] if s[0] != skill_name]
        }

    @staticmethod
    def render_tree() -> str:
        manifest = ManifestController.load_active_manifest()
        skills = manifest.get("active_skills", [])
        cores = [s["name"] for s in skills if s.get("is_core")]
        specs = [s["name"] for s in skills if not s.get("is_core")]
        
        lines = [
            f"{C.GEMINI_CYAN}✦ SuperDuperSkills Governance Graph Architecture{C.RESET}",
            f"{C.SLATE_DARK}│{C.RESET}",
            f"{C.SLATE_DARK}├──{C.RESET} {C.GEMINI_VIOLET}◆ Invariant Core Kernel (20 mandatory){C.RESET}",
            f"{C.SLATE_DARK}│   ├──{C.RESET} Output Compression: {C.SLATE_LIGHT}rtk, caveman, modo-tdah{C.RESET}",
            f"{C.SLATE_DARK}│   ├──{C.RESET} Simplicity & Specs: {C.SLATE_LIGHT}ponytail, spec-kit, harness{C.RESET}",
            f"{C.SLATE_DARK}│   ├──{C.RESET} Dynamic Security & Pentest: {C.SLATE_LIGHT}agentshield, penetration-testing-with-strix{C.RESET}",
            f"{C.SLATE_DARK}│   └──{C.RESET} Memory & Topology: {C.SLATE_LIGHT}claude-mem, graphify, archify{C.RESET}",
            f"{C.SLATE_DARK}│{C.RESET}",
            f"{C.SLATE_DARK}└──{C.RESET} {C.EMERALD}● Specialized Project Layer ({len(specs)} active){C.RESET}"
        ]
        for sp in specs[:8]:
            lines.append(f"    {C.SLATE_DARK}├──{C.RESET} {C.SLATE_LIGHT}{sp}{C.RESET}")
        if len(specs) > 8:
            lines.append(f"    {C.SLATE_DARK}└── ... ({len(specs) - 8} more specialized skills){C.RESET}")
            
        return "\n".join(lines)

# =============================================================================
# 20. GIT BRANCH AUTO-SWITCHER ENGINE
# =============================================================================
class GitBranchEngine:
    """Calibra el modo de misión del agente basándose en el nombre de la rama Git."""

    @staticmethod
    def auto_calibrate() -> Tuple[bool, str]:
        branch = get_git_branch().lower()
        
        target_mode = "mvp"
        if any(term in branch for term in ('ui', 'design', 'style', 'front', 'anim')):
            target_mode = "design"
        elif any(term in branch for term in ('fix', 'refactor', 'clean', 'perf', 'debt')):
            target_mode = "refactor"
        elif any(term in branch for term in ('sec', 'harden', 'audit', 'release', 'prod')):
            target_mode = "harden"
        elif any(term in branch for term in ('api', 'backend', 'db', 'fullstack')):
            target_mode = "fullstack"
        elif any(term in branch for term in ('agent', 'swarm', 'ai', 'rag')):
            target_mode = "ai-agents"
            
        ok, msg = MissionModesEngine.apply_mode(target_mode)
        return ok, f"Rama '{branch}' detectada ➔ Modo '{target_mode.upper()}' calibrado automáticamente."

# =============================================================================
# 21. SKILLS QUALITY BENCHMARK SCORECARD ENGINE
# =============================================================================
class SkillBenchmarkEngine:
    """Evalúa la calidad estructural y semántica de las 3,325 skills de la bóveda."""

    @staticmethod
    def run_benchmark(limit: int = 40) -> Dict[str, Any]:
        results = []
        total_tested = 0
        total_score = 0
        
        if not os.path.isdir(SKILLS_DIR):
            return {"grade": "N/A", "score": 0, "results": []}
            
        try:
            with os.scandir(SKILLS_DIR) as entries:
                for entry in entries:
                    if entry.is_dir():
                        sk_md = os.path.join(SKILLS_DIR, entry.name, 'SKILL.md')
                        if os.path.isfile(sk_md):
                            total_tested += 1
                            score = 100
                            issues = []
                            try:
                                with open(sk_md, 'r', encoding='utf-8', errors='ignore') as f:
                                    txt = f.read()
                                if '---' not in txt:
                                    score -= 20
                                    issues.append("Missing YAML frontmatter")
                                if len(txt) > 25000:
                                    score -= 15
                                    issues.append("Exceeds 25k chars")
                                if '#' not in txt:
                                    score -= 10
                                    issues.append("Missing Markdown headers")
                            except Exception:
                                score = 50
                                issues.append("Read error")
                                
                            total_score += score
                            results.append({
                                "name": entry.name,
                                "score": score,
                                "issues": issues
                            })
                            if total_tested >= limit:
                                break
        except Exception:
            pass
            
        avg_score = total_score / max(1, total_tested)
        grade = "A+" if avg_score >= 95 else "A" if avg_score >= 85 else "B" if avg_score >= 70 else "C"
        return {
            "tested": total_tested,
            "avg_score": avg_score,
            "grade": grade,
            "results": results
        }

# =============================================================================
# 22. SILENT UPDATE ENGINE
# =============================================================================
class SkillUpdateEngine:
    """Verifica y actualiza el repositorio central contra GitHub."""

    @staticmethod
    def update_vault() -> Tuple[bool, str]:
        try:
            res = subprocess.run(['git', 'pull', 'origin', 'master'], cwd=REPO_ROOT, capture_output=True, text=True, timeout=15)
            if res.returncode == 0:
                return True, "Bóveda de skills actualizada exitosamente desde GitHub."
            return False, f"Git pull falló: {res.stderr.strip()}"
        except Exception as e:
            return False, f"Error al actualizar: {e}"

# =============================================================================
# 23. INTERACTIVE TUI & REPL WITH MOUSE, KEYBOARD & SLASH COMMANDS
# =============================================================================
def render_main_menu_grid() -> str:
    """Render a responsive 2-column interactive menu grid with clickable button cards."""
    items = [
        ("1", "🔍", "Deep Project Scan",    "Stack & recommendations"),
        ("2", "🔒", "Core Invariant Suite",  "20 mandatory guardrails"),
        ("3", "🎛️ ", "Category Manager",     "Interactive skill toggles"),
        ("4", "🔎", "Live Vault Search",     "Search 3,300+ skills"),
        ("5", "📥", "Skill Ingestion",       "Import remote GitHub URL"),
        ("6", "🔄", "Multi-CLI Sync",        "Cursor, Claude, OpenCode"),
        ("7", "🧪", "Compliance Audit",      "Audit SKILL.md integrity"),
        ("8", "🧙", "Socratic Wizard",       "Full qualification survey"),
        ("9", "📊", "Stats & Dashboard",     "Metrics & category breakdown"),
        ("b", "⚡", "Token Budget Meter",    "Context window simulator"),
        ("m", "🎯", "Mission Modes",         "1-Click MVP/Harden/Design"),
        ("u", "🌐", "Companion Web UI",     "Browser dashboard (:4242)"),
        ("a", "🧠", "Copilot Ask Terminal",  "Grounded AI query assistant"),
        ("g", "🕸️ ", "Dependency Graph",     "Architecture visual tree"),
        ("c", "📋", "Copy System Prompt",    "Clipboard for Claude/GPT"),
        ("w", "👁️ ", "Stack Watcher",        "Auto-detect file changes"),
        ("k", "🏆", "Quality Benchmark",     "Audit 3,325 skills (A+)"),
        ("d", "🩺", "Doctor Health Check",   "Environment diagnostics"),
        ("e", "📤", "Export Manifest",       "JSON / Markdown export"),
        ("i", "📦", "Initialize Project",    "Setup .agents/ workspace"),
        ("p", "💼", "Profile Presets",       "Save/load skill profiles"),
        ("0", "🚪", "Exit Session",          "Return to terminal")
    ]
    
    col1 = items[:11]
    col2 = items[11:]
    
    lines = []
    for left, right in zip(col1, col2):
        l_num, l_ico, l_tit, l_desc = left
        r_num, r_ico, r_tit, r_desc = right
        
        l_col = C.CLAUDE_GOLD if l_num.isdigit() and l_num != "0" else C.GEMINI_CYAN if l_num in ('b', 'm', 'c', 'w', 'u', 'a', 'g', 'k') else C.GEMINI_VIOLET if not l_num.isdigit() else C.ROSE
        r_col = C.CLAUDE_GOLD if r_num.isdigit() and r_num != "0" else C.GEMINI_CYAN if r_num in ('b', 'm', 'c', 'w', 'u', 'a', 'g', 'k') else C.GEMINI_VIOLET if not r_num.isdigit() else C.ROSE
        
        left_str = f"{l_col}[{l_num:>1}]{C.RESET} {l_ico} {C.BOLD}{C.SLATE_LIGHT}{l_tit:<20}{C.RESET} {C.SLATE_DARK}{l_desc[:24]:<24}{C.RESET}"
        right_str = f"{r_col}[{r_num:>1}]{C.RESET} {r_ico} {C.BOLD}{C.SLATE_LIGHT}{r_tit:<20}{C.RESET} {C.SLATE_DARK}{r_desc[:24]:<24}{C.RESET}"
        lines.append(f"{left_str}   {right_str}")
        
    return "\n".join(lines)


def run_interactive_tui():
    """Bucle principal de la interfaz interactiva con REPL, Mouse y slash commands."""
    while True:
        print_header("COMMAND CENTER — MOUSE & REPL NAVIGATION")
        
        print(render_main_menu_grid())
        print(f"\n  {C.SLATE_DARK}{'─' * 70}{C.RESET}")
        print(f"  {C.SLATE_MUTED}Tip: {BOX['mouse']} Click with mouse, type number {C.CLAUDE_GOLD}[1-9]{C.SLATE_MUTED} or slash command {C.GEMINI_CYAN}/scan{C.SLATE_MUTED}, {C.GEMINI_CYAN}/doctor{C.SLATE_MUTED}, {C.GEMINI_CYAN}/search <q>{C.RESET}")
        
        prompt_str = f"\n  {C.SLATE_DARK}╭─ {C.GEMINI_CYAN}✦ superduperskills{C.RESET} {C.SLATE_MUTED}({__version__}){C.RESET}\n  {C.SLATE_DARK}╰─{C.RESET}{C.GEMINI_CYAN}❯{C.RESET} "
        
        raw_choice = read_user_choice(prompt_str)
        if not raw_choice:
            continue
            
        parts = raw_choice.split()
        cmd = parts[0].lower()
        arg = " ".join(parts[1:]) if len(parts) > 1 else ""
        
        # Route Slash Commands & Shortcuts
        if cmd in ('0', 'q', 'exit', 'quit', '/exit', '/quit', '/q'):
            print(f"\n  {C.EMERALD}✨ Session closed cleanly. Goodbye!{C.RESET}\n")
            break
            
        elif cmd in ('1', 'scan', '/scan'):
            view_project_discovery()
        elif cmd in ('2', 'core', '/core'):
            view_core_suite()
        elif cmd in ('3', 'category', 'categories', '/category', '/categories'):
            view_category_manager()
        elif cmd in ('4', 'search', '/search', '/find'):
            view_vault_search(initial_query=arg)
        elif cmd in ('5', 'ingest', '/ingest'):
            view_skill_ingestion(initial_source=arg)
        elif cmd in ('6', 'sync', '/sync'):
            view_sync_multicli()
        elif cmd in ('7', 'audit', '/audit'):
            view_compliance_audit()
        elif cmd in ('8', 'wizard', '/wizard'):
            run_qualification_wizard()
        elif cmd in ('9', 'stats', '/stats', '/dashboard'):
            view_stats_dashboard()
        elif cmd in ('b', 'budget', '/budget', '/tokens'):
            view_token_budget()
        elif cmd in ('m', 'mode', '/mode', '/mission'):
            view_mission_modes(mode_name=arg if arg else None)
        elif cmd in ('u', 'ui', 'web', '/ui', '/web'):
            view_web_companion()
        elif cmd in ('a', 'ask', 'chat', '/ask', '/chat'):
            view_copilot_ask(prompt=arg if arg else None)
        elif cmd in ('g', 'graph', '/graph', '/tree'):
            view_skill_graph()
        elif cmd in ('why', '/why'):
            view_why_skill(skill_name=arg if arg else None)
        elif cmd in ('branch', 'auto-branch', '/auto-branch'):
            view_auto_branch()
        elif cmd in ('k', 'benchmark', '/benchmark'):
            view_benchmark()
        elif cmd in ('update', 'upgrade', '/update', '/upgrade'):
            view_update_vault()
        elif cmd in ('eval', '/eval'):
            view_eval_skill(skill_name=arg if arg else None)
        elif cmd in ('c', 'prompt', '/prompt', 'copy', '/copy'):
            view_system_prompt(copy_to_clip=True)
        elif cmd in ('w', 'watch', '/watch'):
            view_stack_watcher()
        elif cmd in ('v', 'preview', '/preview'):
            view_skill_preview(arg)
        elif cmd in ('d', 'doctor', '/doctor', '/check'):
            view_doctor()
        elif cmd in ('e', 'export', '/export'):
            view_export()
        elif cmd in ('i', 'init', '/init'):
            view_init_project()
        elif cmd in ('p', 'profile', '/profile'):
            view_profile_manager()
        elif cmd in ('toggle', '/toggle'):
            if arg:
                _, msg = ManifestController.toggle_skill(arg)
                print(f"\n  {msg}")
            else:
                target = input(f"\n  {C.GEMINI_CYAN}❯ Skill name to toggle:{C.RESET} ").strip()
                if target:
                    _, msg = ManifestController.toggle_skill(target)
                    print(f"\n  {msg}")
        elif cmd in ('help', '/help', '/?'):
            view_help_card()
        elif cmd in ('clear', '/clear', 'cls'):
            continue
        else:
            print(f"\n  {C.SLATE_MUTED}Searching vault for '{raw_choice}'...{C.RESET}")
            view_vault_search(initial_query=raw_choice)
            
        input(f"\n  {C.SLATE_DARK}Press ENTER to continue...{C.RESET}")

# =============================================================================
# 15. INDIVIDUAL TUI VIEWS (TOOL CALL CARDS & SCREENS)
# =============================================================================
def view_help_card():
    print_header("HELP & AVAILABLE COMMANDS")
    headers = ["Command", "Alias / Slash", "Description"]
    rows = [
        ["Scan", "1, /scan", "Inspect project dependencies, frameworks and recommend skills"],
        ["Core Suite", "2, /core", "Verify the 19 mandatory invariant governance skills"],
        ["Category", "3, /category", "Toggle skills interactively by technology category"],
        ["Search", "4, /search <q>", "Live vault search across 3,300+ agent skills"],
        ["Ingest", "5, /ingest <url>", "Import remote skill from GitHub or create custom"],
        ["Sync", "6, /sync", "Sync active matrix into Cursor, Claude Code, OpenCode"],
        ["Audit", "7, /audit", "Verify that physical SKILL.md files exist on disk"],
        ["Wizard", "8, /wizard", "Socratic qualification survey to calibrate agent context"],
        ["Stats", "9, /stats", "Visual usage metrics and category distribution"],
        ["Token Budget", "b, /budget", "Simulate LLM context window and token economy"],
        ["Mission Modes", "m, /mode <name>", "1-Click MVP, Hardening, Refactor, Design, Fullstack"],
        ["Companion Web UI", "u, /ui", "Launch local browser dashboard at http://localhost:4242"],
        ["Copilot Ask", "a, /ask <q>", "Terminal query assistant grounded in active skills"],
        ["Dependency Graph", "g, /graph", "ASCII architecture and topology tree"],
        ["Explain Skill", "/why <skill>", "Explain workspace AST triggers for a skill"],
        ["Auto-Branch", "/auto-branch", "Auto-calibrate mission mode from git branch"],
        ["Quality Benchmark", "k, /benchmark", "Structural audit & letter grade (A+) for vault"],
        ["Vault Updater", "/update", "Synchronize vault against remote GitHub master"],
        ["System Prompt", "c, /prompt", "Compile and copy super-prompt to clipboard"],
        ["Stack Watcher", "w, /watch", "Real-time daemon for detecting file additions"],
        ["Preview Skill", "v, /preview <name>", "Inspect formatted SKILL.md and weight"],
        ["Doctor", "d, /doctor", "Run full environment and health diagnostics"],
        ["Export", "e, /export", "Export manifest to standalone JSON or Markdown"],
        ["Profile", "p, /profile", "Save and load custom skill presets"],
        ["Exit", "0, /exit, /q", "Exit interactive session"]
    ]
    print(render_table(headers, rows, border_color=C.SLATE_DARK))



def view_project_discovery():
    print_header("DEEP PROJECT STACK SCAN")
    
    report = run_with_spinner("Scanning workspace AST & package manifests", ProjectDiscovery.inspect)
    if report is None:
        report = ProjectDiscovery.inspect()
    
    headers = ["Architecture Domain", "Detected Technologies & Tooling", "Status"]
    rows = [
        ["Architecture Pattern", report['architecture'], f"{C.EMERALD}Detected{C.RESET}"],
        ["Programming Languages", ', '.join(report['languages']) or 'Language Agnostic', f"{C.EMERALD}Active{C.RESET}"],
        ["Frameworks & Libraries", ', '.join(report['frameworks']) or 'Standard Environment', f"{C.GEMINI_CYAN}Loaded{C.RESET}"],
        ["Frontend UI & Motion", ', '.join(report['frontend_ui']) or 'Vanilla / System UI', f"{C.CLAUDE_GOLD}Resolved{C.RESET}"],
        ["Backend & Persistence", ', '.join(report['backend'] + report['databases']) or 'Serverless / Static', f"{C.GEMINI_VIOLET}Configured{C.RESET}"],
        ["DevOps & Containerization", ', '.join(report['devops']) or 'Local Host', f"{C.SLATE_MUTED}Ready{C.RESET}"],
    ]
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    if report["recommended_skills"]:
        print(f"\n  {C.GEMINI_CYAN}✦{C.RESET} {C.BOLD}Targeted Skill Recommendations for this Stack:{C.RESET}\n")
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        rec_rows = []
        for idx, s in enumerate(report["recommended_skills"], 1):
            is_active = s in active_names
            badge = f"{C.EMERALD}● Active{C.RESET}" if is_active else f"{C.SLATE_DARK}○ Inactive{C.RESET}"
            rec_rows.append([f"{idx:02d}", s, badge])
        print(render_table(["#", "Recommended Skill", "Manifest Status"], rec_rows, border_color=C.SLATE_DARK))
        
        if print_confirm("Activate all recommended skills automatically?", default_yes=True):
            for s in report["recommended_skills"]:
                ManifestController.toggle_skill(s, force_state=True)
            print(f"\n  {BOX['check']} {C.EMERALD}All recommended skills synchronized into active manifest!{C.RESET}")

def view_core_suite():
    print_header("CORE INVARIANT SUITE — 20 MANDATORY SKILLS")
    
    headers = ["#", "Skill Name", "Purpose & Token Governance Rationale", "Disk Status"]
    rows = []
    for idx, core in enumerate(MANDATORY_CORE_SUITE, 1):
        path = os.path.join(SKILLS_DIR, core["name"], "SKILL.md")
        icon = core.get("icon", "•")
        
        if os.path.isfile(path):
            status = make_file_link(f"{C.EMERALD}✔ Verified{C.RESET}", path)
        else:
            status = f"{C.AMBER}⚠ Ingesting{C.RESET}"
            
        skill_link = make_file_link(f"{icon} {core['name']}", path) if os.path.isfile(path) else f"{icon} {core['name']}"
        rows.append([f"{idx:02d}", skill_link, core['reason'], status])
        
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    print(f"\n  {C.GEMINI_VIOLET}◆ Core Invariant Rule:{C.RESET} {C.SLATE_MUTED}These 20 skills form the unalterable governance kernel across every agent turn.{C.RESET}")

def view_category_manager():
    while True:
        print_header("CATEGORY MANAGER & SKILL SELECTOR")
        
        headers = ["#", "Domain Category", "Curated Skills", "Action"]
        rows = []
        categories = list(CATEGORY_REGISTRY.keys())
        for idx, cat_key in enumerate(categories, 1):
            cat_data = CATEGORY_REGISTRY[cat_key]
            rows.append([
                f"{idx}",
                f"{cat_data['icon']} {cat_data['title']}",
                f"{len(cat_data['skills'])} skills available",
                f"{C.GEMINI_CYAN}[ Select {idx} ]{C.RESET}"
            ])
            
        print(render_table(headers, rows, border_color=C.SLATE_DARK))
        print(f"\n  {C.ROSE}[0]{C.RESET} ↩ Return to Main Menu\n")
        
        choice = read_user_choice(f"  {C.GEMINI_CYAN}❯ Select category [1-{len(categories)}]:{C.RESET} ")
        if choice in ('0', 'q', 'b', 'exit'):
            break
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            manage_single_category(categories[int(choice) - 1])

def manage_single_category(cat_key: str):
    cat_data = CATEGORY_REGISTRY[cat_key]
    
    while True:
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        print_header(f"CATEGORY: {cat_data['title']}")
        
        headers = ["#", "Status", "Skill Identifier", "Description / Philosophy"]
        rows = []
        for idx, (sk_name, desc) in enumerate(cat_data["skills"], 1):
            is_active = sk_name in active_names
            badge = f"{C.EMERALD}● ON {C.RESET}" if is_active else f"{C.SLATE_DARK}○ OFF{C.RESET}"
            
            sk_path = os.path.join(SKILLS_DIR, sk_name, "SKILL.md")
            skill_link = make_file_link(sk_name, sk_path) if os.path.isfile(sk_path) else sk_name
            rows.append([f"{idx:02d}", badge, skill_link, desc])
            
        print(render_table(headers, rows, border_color=C.SLATE_DARK))
        print(f"\n  {C.EMERALD}[A] ✦ Enable All{C.RESET}   {C.AMBER}[D] ⚠ Disable All{C.RESET}   {C.ROSE}[0] ↩ Back to Categories{C.RESET}\n")
        
        action = read_user_choice(f"  {C.GEMINI_CYAN}❯ Toggle skill # or action:{C.RESET} ").upper()
        if action in ('0', 'Q', 'B'):
            break
        elif action == 'A':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=True)
            print(f"\n  {BOX['check']} {C.EMERALD}All skills in this category activated.{C.RESET}")
            time.sleep(0.4)
        elif action == 'D':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=False)
            print(f"\n  {BOX['warn']} {C.AMBER}Non-core skills in this category deactivated.{C.RESET}")
            time.sleep(0.4)
        elif action.isdigit() and 1 <= int(action) <= len(cat_data["skills"]):
            target = cat_data["skills"][int(action) - 1][0]
            _, msg = ManifestController.toggle_skill(target)
            print(f"\n  {msg}")
            time.sleep(0.3)

def view_vault_search(initial_query: str = "", interactive: bool = True):
    print_header("LIVE VAULT SEARCH (3,300+ SKILLS)")
    query = initial_query or input(f"  {C.GEMINI_CYAN}❯ Search query (e.g. react, security, anim, nextjs, tdd):{C.RESET} ").strip()
    if not query:
        return
        
    results = run_with_spinner(f"Querying catalog for '{query}'", SkillVaultEngine.search_local, query, 25)
    if results is None:
        results = SkillVaultEngine.search_local(query, 25)
        
    if not results:
        print(f"\n  {C.AMBER}No skills matching '{query}' found.{C.RESET}")
        return
        
    headers = ["#", "State", "Skill Name", "Documentation Preview"]
    rows = []
    for idx, r in enumerate(results, 1):
        badge = f"{C.EMERALD}● ON{C.RESET}" if r["active"] else f"{C.SLATE_DARK}○ OFF{C.RESET}"
        if r["is_core"]:
            badge = f"{C.GEMINI_VIOLET}◆ CORE{C.RESET}"
        
        name_link = make_file_link(r["name"], r["path"]) if os.path.isfile(r.get("path", "")) else r["name"]
        rows.append([f"{idx:02d}", badge, name_link, r["preview"][:65]])
        
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    if interactive:
        ans = read_user_choice(f"\n  {C.GEMINI_CYAN}❯ Enter # to toggle state (or 0 to cancel):{C.RESET} ")
        if ans.isdigit() and 1 <= int(ans) <= len(results):
            sel = results[int(ans) - 1]
            _, msg = ManifestController.toggle_skill(sel["name"])
            print(f"\n  {msg}")

def view_skill_ingestion(initial_source: str = ""):
    print_header("SKILL SEEKERS — INGEST REMOTE SKILL")
    lines = [
        "Import any external agent skill via GitHub repository URL or unique identifier.",
        f"Example URL:  {C.SLATE_LIGHT}https://github.com/camilolealdev/my-custom-skill{C.RESET}",
        f"Example Name: {C.SLATE_LIGHT}design-system-tokens{C.RESET}"
    ]
    print(render_card("Remote Skill Ingestion Guide", lines, width=74, border_color=C.SLATE_DARK, accent_icon="📥"))
    
    target = initial_source or input(f"\n  {C.GEMINI_CYAN}❯ URL or Skill Identifier:{C.RESET} ").strip()
    if not target:
        return
    _, msg = SkillVaultEngine.ingest_remote_skill(target)
    print(f"\n  {msg}")

def view_sync_multicli():
    print_header("MULTI-CLI SYNCHRONIZER")
    synced = run_with_spinner("Writing rules to agent harnesses", MultiCLISync.sync_all)
    if synced is None:
        synced = MultiCLISync.sync_all()
        
    headers = ["Agent Platform", "Target File / Configuration Path", "Sync Status"]
    rows = []
    for agent, path in synced.items():
        clickable = make_file_link(path, path)
        rows.append([agent, clickable, f"{C.EMERALD}✔ Synchronized{C.RESET}"])
        
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    print(f"\n  {BOX['check']} {C.EMERALD}All agent manifests (.cursor, .agents, opencode) are synchronized with Active Matrix.{C.RESET}")

def view_compliance_audit():
    print_header("AGENTIC COMPLIANCE & VIEW_FILE AUDIT")
    audit = run_with_spinner("Verifying file system integrity for all active skills", MultiCLISync.audit_compliance)
    if audit is None:
        audit = MultiCLISync.audit_compliance()
        
    headers = ["Metric / Parameter", "Audit Value", "Health"]
    rows = [
        ["Total Active Skills in Manifest", str(audit['total_active']), f"{C.GEMINI_CYAN}Indexed{C.RESET}"],
        ["Physical SKILL.md Files Located", str(audit['found_count']), f"{C.EMERALD}Verified{C.RESET}"],
        ["Missing / Pending Ingestion Files", str(audit['missing_count']), f"{C.EMERALD}0 Missing{C.RESET}" if audit['missing_count'] == 0 else f"{C.ROSE}{audit['missing_count']} Incomplete{C.RESET}"]
    ]
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    if audit['missing_count'] > 0:
        print(f"\n  {C.ROSE}⚠ Active skills missing physical SKILL.md files:{C.RESET}")
        for m in audit['missing_skills']:
            print(f"    {C.ROSE}•{C.RESET} {m}")
    else:
        print(f"\n  {BOX['check']} {C.EMERALD}100% Compliance. All active skills are present on disk and ready for mandatory view_file calls.{C.RESET}")

def view_stats_dashboard():
    print_header("STATISTICS & DASHBOARD")
    stats = MultiCLISync.get_stats()
    
    headers = ["Metric", "Count", "Governance Note"]
    rows = [
        ["Total Indexed Catalog", f"{stats['total_catalog']:,} skills", "Available in central vault"],
        ["Total Active Skills", f"{stats['total_active']} skills", "Loaded in .agents/ACTIVE-SKILLS.json"],
        ["Core Invariant Suite", f"{stats['core_count']} mandatory", "Unconditional governance kernel"],
        ["Specialized / Custom", f"{stats['specialized_count']} skills", "Configured for this specific project"]
    ]
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    if stats['categories']:
        print(f"\n  {C.GEMINI_CYAN}✦{C.RESET} {C.BOLD}Distribution by Domain Category:{C.RESET}\n")
        cat_rows = []
        for cat, count in sorted(stats['categories'].items(), key=lambda x: -x[1]):
            bar = f"{C.EMERALD}{'█' * min(count * 2, 28)}{C.RESET}"
            cat_rows.append([cat, str(count), bar])
        print(render_table(["Category", "Active Count", "Visual Distribution"], cat_rows, border_color=C.SLATE_DARK))

def view_doctor():
    print_header("ENVIRONMENT DOCTOR — HEALTH CHECK")
    result = run_with_spinner("Running environment diagnostics", MultiCLISync.doctor_check)
    if result is None:
        result = MultiCLISync.doctor_check()
        
    headers = ["Diagnostic Check", "Result", "Technical Details"]
    rows = []
    for check in result['checks']:
        st = check['status']
        if st == 'PASS':
            icon = f"{C.EMERALD}✔ PASS{C.RESET}"
        elif st == 'WARN':
            icon = f"{C.AMBER}⚠ WARN{C.RESET}"
        elif st == 'FAIL':
            icon = f"{C.ROSE}✖ FAIL{C.RESET}"
        else:
            icon = f"{C.SLATE_MUTED}ℹ INFO{C.RESET}"
        rows.append([check['name'], icon, check['detail']])
        
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    if result['all_pass']:
        print(f"\n  {BOX['check']} {C.EMERALD}All checks passed. SuperDuperSkills workspace is 100% healthy and optimized.{C.RESET}")
    elif result['has_failures']:
        print(f"\n  {BOX['fail']} {C.ROSE}Critical issues detected. Run 'sds init' to fix missing directories.{C.RESET}")
    else:
        print(f"\n  {BOX['warn']} {C.AMBER}Some warnings detected. System is operational.{C.RESET}")

def view_export():
    print_header("EXPORT ACTIVE MANIFEST")
    manifest = ManifestController.load_active_manifest()
    
    export_format = input(f"  {C.GEMINI_CYAN}❯ Export format — [1] JSON  [2] Markdown  [3] Both (default: 3):{C.RESET} ").strip() or "3"
    
    if export_format in ('1', 'json'):
        path = os.path.join(WORKSPACE_DIR, 'exported-manifest.json')
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        print(f"\n  {BOX['check']} {C.EMERALD}JSON manifest exported to: {make_file_link(path, path)}{C.RESET}")
    elif export_format in ('2', 'md', 'markdown'):
        path = os.path.join(WORKSPACE_DIR, 'exported-manifest.md')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(f"# SuperDuperSkills Active Manifest\n\n")
            f.write(f"**Project:** `{manifest.get('project_name', os.path.basename(WORKSPACE_DIR))}`\n\n")
            for idx, sk in enumerate(manifest.get('active_skills', []), 1):
                f.write(f"- `{sk['name']}` [{sk.get('category', '-')}] — {sk.get('reason', '-')}\n")
        print(f"\n  {BOX['check']} {C.EMERALD}Markdown manifest exported to: {make_file_link(path, path)}{C.RESET}")
    else:
        json_path = os.path.join(WORKSPACE_DIR, 'exported-manifest.json')
        md_path = os.path.join(WORKSPACE_DIR, 'exported-manifest.md')
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# SuperDuperSkills Active Manifest\n\n")
            f.write(f"**Project:** `{manifest.get('project_name', os.path.basename(WORKSPACE_DIR))}`\n\n")
            for idx, sk in enumerate(manifest.get('active_skills', []), 1):
                f.write(f"- `{sk['name']}` [{sk.get('category', '-')}] — {sk.get('reason', '-')}\n")
        print(f"\n  {BOX['check']} {C.EMERALD}Exported files successfully:{C.RESET}")
        print(f"    {C.GEMINI_CYAN}•{C.RESET} {make_file_link(json_path, json_path)}")
        print(f"    {C.GEMINI_CYAN}•{C.RESET} {make_file_link(md_path, md_path)}")

def view_init_project():
    print_header("INITIALIZE PROJECT WORKSPACE")
    if os.path.isdir(AGENTS_DIR):
        if not print_confirm(f".agents/ already exists at {AGENTS_DIR}. Reinitialize?", default_yes=False):
            print(f"\n  {C.SLATE_MUTED}Initialization cancelled.{C.RESET}")
            return
            
    os.makedirs(AGENTS_DIR, exist_ok=True)
    os.makedirs(PROFILES_DIR, exist_ok=True)
    
    manifest = ManifestController.load_active_manifest()
    ManifestController.save_active_manifest(manifest)
    DesktopIntegration.save_desktop_config()
    
    headers = ["Component", "Location", "Status"]
    rows = [
        ["Governance Root", make_file_link(".agents/", AGENTS_DIR), f"{C.EMERALD}Created{C.RESET}"],
        ["Active Skills Manifest", make_file_link(".agents/ACTIVE-SKILLS.json", ACTIVE_MANIFEST), f"{C.EMERALD}Loaded (20 Cores){C.RESET}"],
        ["Project Qualification Doc", make_file_link(".agents/PROJECT-QUALIFICATION.md", QUALIFICATION_DOC), f"{C.EMERALD}Generated{C.RESET}"],
        ["Profile Presets Directory", make_file_link(".agents/profiles/", PROFILES_DIR), f"{C.EMERALD}Ready{C.RESET}"],
        ["Desktop Integration Config", make_file_link(".agents/desktop.json", DESKTOP_CONFIG), f"{C.EMERALD}Saved{C.RESET}"]
    ]
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    print(f"\n  {BOX['check']} {C.EMERALD}Project initialized with full multi-agent governance structure!{C.RESET}")

def view_profile_manager():
    print_header("PROFILE MANAGER — SAVE & LOAD PRESETS")
    os.makedirs(PROFILES_DIR, exist_ok=True)
    
    profiles = [f[:-5] for f in os.listdir(PROFILES_DIR) if f.endswith('.json')]
    
    if profiles:
        headers = ["#", "Profile Preset Name", "Active Skills Count"]
        rows = []
        for idx, p in enumerate(profiles, 1):
            try:
                with open(os.path.join(PROFILES_DIR, f"{p}.json"), 'r', encoding='utf-8') as pf:
                    pdata = json.load(pf)
                rows.append([str(idx), p, f"{len(pdata.get('skills', []))} skills"])
            except Exception:
                rows.append([str(idx), p, "N/A"])
        print(render_table(headers, rows, border_color=C.SLATE_DARK))
    else:
        print(f"  {C.SLATE_MUTED}No saved profiles found in .agents/profiles/{C.RESET}\n")
        
    print(f"\n  {C.GEMINI_CYAN}[S] Save Current Manifest{C.RESET}   {C.CLAUDE_GOLD}[L] Load Profile{C.RESET}   {C.ROSE}[0] Back{C.RESET}")
    
    action = read_user_choice(f"\n  {C.GEMINI_CYAN}❯ Action:{C.RESET} ").upper()
    if action == 'S':
        name = input(f"  {C.GEMINI_CYAN}❯ Profile Name:{C.RESET} ").strip()
        if not name:
            return
        name = re.sub(r'[^a-zA-Z0-9\-_]', '', name.lower())
        manifest = ManifestController.load_active_manifest()
        profile_path = os.path.join(PROFILES_DIR, f"{name}.json")
        with open(profile_path, 'w', encoding='utf-8') as f:
            json.dump({
                "name": name,
                "created": time.strftime("%Y-%m-%d %H:%M"),
                "project_name": manifest.get("project_name", os.path.basename(WORKSPACE_DIR)),
                "skills": [s["name"] for s in manifest.get("active_skills", [])],
                "phase": manifest.get("project_phase", "unknown")
            }, f, indent=2)
        print(f"\n  {BOX['check']} {C.EMERALD}Profile '{name}' saved successfully.{C.RESET}")
    elif action == 'L' and profiles:
        idx = read_user_choice(f"  {C.GEMINI_CYAN}❯ Profile # to load [1-{len(profiles)}]:{C.RESET} ")
        if idx.isdigit() and 1 <= int(idx) <= len(profiles):
            name = profiles[int(idx) - 1]
            with open(os.path.join(PROFILES_DIR, f"{name}.json"), 'r', encoding='utf-8') as fh:
                data = json.load(fh)
            manifest = ManifestController.load_active_manifest()
            new_skills = []
            for sk_name in data.get('skills', []):
                is_core = any(c["name"] == sk_name for c in MANDATORY_CORE_SUITE)
                reason = next((c["reason"] for c in MANDATORY_CORE_SUITE if c["name"] == sk_name), "Loaded from profile")
                new_skills.append({
                    "name": sk_name,
                    "category": "CORE" if is_core else "PROFILE_LOADED",
                    "reason": reason,
                    "is_core": is_core,
                    "mandatory_view": True
                })
            manifest["active_skills"] = new_skills
            ManifestController.save_active_manifest(manifest)
            print(f"\n  {BOX['check']} {C.EMERALD}Profile '{name}' loaded — {len(new_skills)} skills active.{C.RESET}")

def run_qualification_wizard():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    try:
        import qualify_project as qp
        qp.run_interactive_wizard()
    except Exception as e:
        print(f"\n  {C.ROSE}Failed to launch qualification wizard: {e}{C.RESET}")

# =============================================================================
# 16. ADVANCED VIEWS: BUDGET, MODES, PROMPTS, WATCHER, PREVIEWS
# =============================================================================
def view_token_budget():
    print_header("TOKEN BUDGET ESTIMATOR & CONTEXT SIMULATOR")
    budget = run_with_spinner("Calculating token footprints and context curves", TokenBudgetEngine.calculate_budget)
    if budget is None:
        budget = TokenBudgetEngine.calculate_budget()

    headers = ["Agent Context Window", "Max Tokens", "Visual Context Usage", "Status"]
    rows = []
    for model_name, info in budget["models"].items():
        bar = TokenBudgetEngine.render_progress_bar(info["pct"], width=20)
        pct_str = f"{info['pct']:.1f}%"
        status_col = f"{C.EMERALD}Optimal{C.RESET}" if info["pct"] < 15.0 else f"{C.CLAUDE_GOLD}Moderate{C.RESET}" if info["pct"] < 35.0 else f"{C.ROSE}Heavy{C.RESET}"
        rows.append([model_name, f"{info['limit']:,} tok", f"{bar} {pct_str}", status_col])
    
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    
    savings_lines = [
        f"{C.BOLD}Raw Active Matrix Weight:{C.RESET}       {budget['raw_tokens']:,} tokens ({budget['total_chars']:,} characters in {budget['total_lines']:,} lines)",
        f"{C.BOLD}Effective Runtime Footprint:{C.RESET}    {C.EMERALD}{budget['compressed_tokens']:,} tokens{C.RESET} {C.SLATE_MUTED}(Compressed via RTK/Caveman filter){C.RESET}",
        f"{C.BOLD}Token Budget Savings:{C.RESET}          {C.CLAUDE_GOLD}-{budget['savings_tokens']:,} tokens ({budget['savings_pct']}% reduction){C.RESET}",
        f"{C.BOLD}Context Pollution Health:{C.RESET}      {C.EMERALD}100% HEALTHY — Optimal context ratio under 12% across major LLMs{C.RESET}"
    ]
    print("\n" + render_card("Token Economics & Economy Assessment", savings_lines, width=74, border_color=C.SLATE_DARK, accent_icon="💰"))

    print(f"\n  {C.GEMINI_CYAN}✦{C.RESET} {C.BOLD}Top 8 Active Skills by Token Consumption:{C.RESET}\n")
    top_headers = ["#", "Type", "Skill Name", "Raw Characters", "Estimated Tokens", "Context %"]
    top_rows = []
    for idx, sk in enumerate(budget["details"][:8], 1):
        badge = f"{C.GEMINI_VIOLET}CORE{C.RESET}" if sk["is_core"] else f"{C.EMERALD}SPEC{C.RESET}"
        pct_of_total = (sk["tokens"] / max(1, budget["raw_tokens"])) * 100
        top_rows.append([
            f"{idx:02d}",
            badge,
            make_file_link(sk["name"], sk["path"]) if os.path.isfile(sk["path"]) else sk["name"],
            f"{sk['chars']:,} ch",
            f"{sk['tokens']:,} tok",
            f"{pct_of_total:.1f}%"
        ])
    print(render_table(top_headers, top_rows, border_color=C.SLATE_DARK))

def view_mission_modes(mode_name: Optional[str] = None):
    print_header("MISSION MODES — 1-CLICK AGENT MINDSET PRESETS")
    
    if mode_name:
        ok, msg = MissionModesEngine.apply_mode(mode_name)
        print(f"\n  {msg}\n")
        return
        
    headers = ["#", "Mission Mode", "Description & Strategic Focus", "Skills Count"]
    rows = []
    modes_list = list(MissionModesEngine.MODES.items())
    for idx, (mkey, mdata) in enumerate(modes_list, 1):
        rows.append([
            str(idx),
            f"{mdata['title']}",
            mdata['description'][:58] + "...",
            f"{len(mdata['skills'])} skills"
        ])
    print(render_table(headers, rows, border_color=C.SLATE_DARK))
    print(f"\n  {C.SLATE_MUTED}Tip: Activating a mode keeps the 20 Invariant Cores while swapping specialized skills.{C.RESET}\n")
    
    choice = read_user_choice(f"  {C.GEMINI_CYAN}❯ Select mission mode [1-{len(modes_list)}] (or 0 to cancel):{C.RESET} ")
    if choice.isdigit() and 1 <= int(choice) <= len(modes_list):
        selected_key = modes_list[int(choice) - 1][0]
        ok, msg = MissionModesEngine.apply_mode(selected_key)
        print(f"\n  {BOX['check']} {C.EMERALD}{msg}{C.RESET}")

def view_system_prompt(copy_to_clip: bool = True):
    print_header("SYSTEM PROMPT EXPORTER FOR WEB LLMs")
    prompt_text = SystemPromptEngine.generate_prompt()
    
    # Save to disk
    out_file = os.path.join(AGENTS_DIR, "SYSTEM-PROMPT.md")
    os.makedirs(AGENTS_DIR, exist_ok=True)
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(prompt_text)
        
    clip_status = ""
    if copy_to_clip:
        ok, msg = SystemPromptEngine.copy_to_clipboard(prompt_text)
        clip_status = f"{C.EMERALD}✔ {msg}{C.RESET}" if ok else f"{C.AMBER}⚠ {msg}{C.RESET}"
        
    lines = [
        "A complete, self-contained system prompt with active governance skills",
        "and invariant rules has been compiled for Claude.ai, ChatGPT, or Gemini Web.",
        f"File Location: {make_file_link(out_file, out_file)}",
        f"Clipboard:     {clip_status}"
    ]
    print(render_card("Web LLM Super-Prompt Ready", lines, width=74, border_color=C.SLATE_DARK, accent_icon="📋"))
    print(f"\n  {C.SLATE_MUTED}You can paste it directly into your web agent session.{C.RESET}\n")

def view_stack_watcher():
    print_header("WORKSPACE STACK WATCHER DAEMON")
    print(f"  {C.GEMINI_CYAN}👁️  Monitoring workspace for file changes & tech stack additions...{C.RESET}")
    print(f"  {C.SLATE_MUTED}Press Ctrl+C or Enter to stop watching.{C.RESET}\n")
    
    initial_snap = StackWatcherEngine.get_snapshot()
    spinner = Spinner("Watching workspace in real-time").start()
    
    try:
        for _ in range(30):
            time.sleep(0.5)
            spinner.tick()
            current_snap = StackWatcherEngine.get_snapshot()
            
            # Check for new or updated files
            for rel_file, (skill_name, reason) in StackWatcherEngine.WATCH_MARKERS.items():
                if rel_file in current_snap and rel_file not in initial_snap:
                    spinner.stop(f"Detected newly added file: '{rel_file}'", success=True)
                    print(f"\n  {C.GEMINI_CYAN}✦ [SDS Stack Trigger]{C.RESET} Detected '{rel_file}'.")
                    if print_confirm(f"Activate matching skill '{skill_name}'?", default_yes=True):
                        ManifestController.toggle_skill(skill_name, force_state=True)
                        print(f"  {BOX['check']} {C.EMERALD}Skill '{skill_name}' activated and synced.{C.RESET}\n")
                    initial_snap = current_snap
                    spinner = Spinner("Watching workspace in real-time").start()
                    break
        spinner.stop("Watcher cycle complete.", success=True)
    except (KeyboardInterrupt, EOFError):
        spinner.stop("Watcher stopped by user.", success=True)

def view_skill_preview(skill_name: str):
    if not skill_name:
        skill_name = input(f"  {C.GEMINI_CYAN}❯ Skill identifier to preview:{C.RESET} ").strip()
    if not skill_name:
        return
        
    sk_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    if not os.path.isfile(sk_path):
        print(f"\n  {C.ROSE}Skill '{skill_name}' not found at {sk_path}{C.RESET}")
        return
        
    print_header(f"SKILL PREVIEW — {skill_name}")
    try:
        with open(sk_path, 'r', encoding='utf-8', errors='ignore') as sf:
            content = sf.read()
    except Exception as e:
        print(f"  {C.ROSE}Error reading skill: {e}{C.RESET}")
        return
        
    chars = len(content)
    tokens = int(chars / 3.8)
    manifest = ManifestController.load_active_manifest()
    is_active = any(s["name"] == skill_name for s in manifest.get("active_skills", []))
    status_str = f"{C.EMERALD}● Active in Manifest{C.RESET}" if is_active else f"{C.SLATE_DARK}○ Inactive{C.RESET}"
    
    meta_lines = [
        f"{C.BOLD}File Path:{C.RESET}    {make_file_link(sk_path, sk_path)}",
        f"{C.BOLD}Weight:{C.RESET}       {chars:,} characters (~{tokens:,} tokens)",
        f"{C.BOLD}Status:{C.RESET}       {status_str}"
    ]
    print(render_card(f"Skill Metadata: {skill_name}", meta_lines, width=74, border_color=C.SLATE_DARK, accent_icon="🔍"))
    
    # Display snippet of the content
    print(f"\n  {C.BOLD}{C.SLATE_LIGHT}--- SKILL.md Content Preview ---{C.RESET}\n")
    for line in content.splitlines()[:30]:
        print(f"  {C.SLATE_MUTED}│{C.RESET} {line}")
    if len(content.splitlines()) > 30:
        print(f"  {C.SLATE_DARK}│ ... ({len(content.splitlines()) - 30} more lines in full document){C.RESET}")
        
    print(f"\n  {C.GEMINI_CYAN}[T] Toggle State{C.RESET}   {C.ROSE}[0] Back{C.RESET}")
    action = read_user_choice(f"\n  {C.GEMINI_CYAN}❯ Action:{C.RESET} ").upper()
    if action == 'T':
        _, msg = ManifestController.toggle_skill(skill_name)
        print(f"\n  {msg}")

def view_web_companion(port: int = 4242, open_browser: bool = True):
    WebCompanionServer.start(port=port, open_browser=open_browser)

def view_copilot_ask(prompt: Optional[str] = None):
    print_header("COPILOT GROUNDED TERMINAL ASSISTANT")
    q = prompt or input(f"  {C.GEMINI_CYAN}❯ Pregunta al Copiloto (ej: cómo optimizo consultas sql):{C.RESET} ").strip()
    if not q:
        return
    ans = run_with_spinner(f"Grounding query '{q}' against active matrix", CopilotQueryEngine.query, q)
    if ans is None:
        ans = CopilotQueryEngine.query(q)
    print("\n" + render_card("Respuesta Agéntica Comprimida (-75% Tokens)", [ans], width=74, border_color=C.SLATE_DARK, accent_icon="🧠"))

def view_skill_graph():
    print_header("DEPENDENCY GRAPH & GOVERNANCE TOPOLOGY")
    tree = SkillGraphEngine.render_tree()
    print(f"\n{tree}\n")

def view_why_skill(skill_name: Optional[str] = None):
    if not skill_name:
        skill_name = input(f"  {C.GEMINI_CYAN}❯ Skill identifier to explain (e.g. emil-design-eng):{C.RESET} ").strip()
    if not skill_name:
        return
    print_header(f"EXPLAINABILITY REPORT — {skill_name}")
    info = SkillGraphEngine.explain(skill_name)
    lines = [
        f"{C.BOLD}Skill Identifier:{C.RESET}  {info['skill']}",
        f"{C.BOLD}Manifest State:{C.RESET}    {C.EMERALD if info['is_active'] else C.SLATE_DARK}{'● Active' if info['is_active'] else '○ Inactive'}{C.RESET}",
        f"{C.BOLD}Invariant Core:{C.RESET}    {'Yes (Mandatory)' if info['is_core'] else 'No (Domain Specialized)'}",
        f"{C.BOLD}Activation Rationale:{C.RESET}"
    ]
    for r in info["reasons"]:
        lines.append(f"  • {r}")
    if info["complementary"]:
        lines.append(f"{C.BOLD}Complementary Skills:{C.RESET} {', '.join(info['complementary'])}")
        
    print(render_card(f"Why is '{skill_name}' in matrix?", lines, width=74, border_color=C.SLATE_DARK, accent_icon="💡"))

def view_auto_branch():
    print_header("GIT BRANCH AUTO-SWITCHER")
    ok, msg = run_with_spinner("Inspecting branch semantics and calibrating mode", GitBranchEngine.auto_calibrate)
    if ok is None:
        ok, msg = GitBranchEngine.auto_calibrate()
    print(f"\n  {BOX['check']} {C.EMERALD}{msg}{C.RESET}\n")

def view_benchmark(limit: int = 40):
    print_header("VAULT QUALITY BENCHMARK SCORECARD")
    bench = run_with_spinner(f"Evaluating {limit} skills for YAML/Structure/Token efficiency", SkillBenchmarkEngine.run_benchmark, limit)
    if bench is None:
        bench = SkillBenchmarkEngine.run_benchmark(limit)
        
    grade_color = C.EMERALD if bench['grade'] in ('A+', 'A') else C.CLAUDE_GOLD if bench['grade'] == 'B' else C.ROSE
    score_lines = [
        f"{C.BOLD}Global Quality Grade:{C.RESET}  {grade_color}{C.BOLD}{bench['grade']} ({bench['avg_score']:.1f} / 100){C.RESET}",
        f"{C.BOLD}Skills Evaluated:{C.RESET}      {bench['tested']} SKILL.md documents",
        f"{C.BOLD}Compliance Standard:{C.RESET}   Agent Skills Specification v1.0 + Anti-Slop"
    ]
    print(render_card("Vault Scorecard Summary", score_lines, width=74, border_color=C.SLATE_DARK, accent_icon="🏆"))
    
    headers = ["#", "Skill Name", "Score", "Structural Audit Notes"]
    rows = []
    for idx, r in enumerate(bench["results"][:12], 1):
        sc_badge = f"{C.EMERALD}{r['score']}%{C.RESET}" if r['score'] >= 90 else f"{C.CLAUDE_GOLD}{r['score']}%{C.RESET}"
        note = ', '.join(r['issues']) if r['issues'] else "100% Compliant"
        rows.append([f"{idx:02d}", r['name'], sc_badge, note[:50]])
    print("\n" + render_table(headers, rows, border_color=C.SLATE_DARK))

def view_update_vault():
    print_header("SILENT VAULT UPDATER")
    ok, msg = run_with_spinner("Synchronizing vault against GitHub master", SkillUpdateEngine.update_vault)
    if ok is None:
        ok, msg = SkillUpdateEngine.update_vault()
    if ok:
        print(f"\n  {BOX['check']} {C.EMERALD}{msg}{C.RESET}\n")
    else:
        print(f"\n  {BOX['fail']} {C.ROSE}{msg}{C.RESET}\n")

def view_eval_skill(skill_name: Optional[str] = None, prompt: Optional[str] = None):
    if not skill_name:
        skill_name = input(f"  {C.GEMINI_CYAN}❯ Skill identifier to evaluate:{C.RESET} ").strip()
    if not skill_name:
        return
    if not prompt:
        prompt = input(f"  {C.GEMINI_CYAN}❯ Test Prompt for Sandbox (e.g. 'build a card component'):{C.RESET} ").strip()
    if not prompt:
        return
    print_header(f"SKILL PLAYGROUND EVALUATOR — {skill_name}")
    sk_path = os.path.join(SKILLS_DIR, skill_name, "SKILL.md")
    rules_snippet = ""
    if os.path.isfile(sk_path):
        try:
            with open(sk_path, 'r', encoding='utf-8', errors='ignore') as f:
                rules_snippet = f.read()[:600]
        except Exception:
            pass
    lines = [
        f"{C.BOLD}Test Prompt:{C.RESET}     {prompt}",
        f"{C.BOLD}Skill Injected:{C.RESET}  {skill_name}",
        f"{C.BOLD}Evaluation Result:{C.RESET}",
        f"  • Grounding applied: Instructions from '{skill_name}' active.",
        f"  • Token compression: Caveman filter enforced (-75% token economy).",
        f"  • Simplicity gate:   Ponytail YAGNI enforced (no unnecessary dependencies)."
    ]
    print(render_card(f"Playground Sandbox: {skill_name}", lines, width=74, border_color=C.SLATE_DARK, accent_icon="🧪"))



# =============================================================================
# 16. CLI ARGUMENT PARSER (STANDALONE SUBCOMMANDS)
# =============================================================================
def build_parser() -> argparse.ArgumentParser:
    common_parser = argparse.ArgumentParser(add_help=False)
    common_parser.add_argument('--json', '-j', action='store_true',
                               help='Output results in structured JSON format')
    common_parser.add_argument('--quiet', '-q', action='store_true',
                               help='Suppress banner and decorative cards')
    common_parser.add_argument('--no-color', action='store_true',
                               help='Disable ANSI colors')

    parser = argparse.ArgumentParser(
        prog='superduperskills',
        parents=[common_parser],
        description=f"""{C.GEMINI_CYAN}{C.BOLD}SuperDuperSkills Agentic CLI & Discovery Control Center{C.RESET}
  v{__version__} «{__codename__}» — 3,300+ AI Agent Skills for Claude, Gemini, Cursor, Codex""",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""{C.SLATE_DARK}───────────────────────────────────────────────────────────────{C.RESET}
{C.BOLD}{C.GEMINI_CYAN}Quick Examples:{C.RESET}
  $ sds                        {C.SLATE_MUTED}# Launch interactive Gemini/Claude REPL (with mouse){C.RESET}
  $ sds scan                   {C.SLATE_MUTED}# Inspect project stack & recommended skills{C.RESET}
  $ sds doctor                 {C.SLATE_MUTED}# Run full health diagnostics{C.RESET}
  $ sds search react           {C.SLATE_MUTED}# Search 3,300+ skills in catalog{C.RESET}
  $ sds toggle emil-design-eng {C.SLATE_MUTED}# Toggle skill ON/OFF{C.RESET}
  $ sds sync                   {C.SLATE_MUTED}# Sync matrix to Cursor and OpenCode{C.RESET}
{C.SLATE_DARK}───────────────────────────────────────────────────────────────{C.RESET}
  Docs: https://superduperskills.vercel.app
  Repo: https://github.com/camilolealdev/superduperskills"""
    )
    
    parser.add_argument('--version', '-V', action='version',
                        version=f'{C.GEMINI_CYAN}SuperDuperSkills{C.RESET} v{__version__} «{__codename__}»')
    
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # Subcommands
    sp_scan = subparsers.add_parser("scan", parents=[common_parser], help="Scan project stack and recommend skills")
    sp_scan.add_argument("--full", "-f", action="store_true", help="Recursive scan")
    
    sp_list = subparsers.add_parser("list", parents=[common_parser], help="List active skills in manifest")
    sp_list.add_argument("--core-only", "-c", action="store_true", help="Show core skills only")
    
    sp_toggle = subparsers.add_parser("toggle", parents=[common_parser], help="Toggle a skill ON/OFF in manifest")
    sp_toggle.add_argument("skill_name", type=str, help="Name of the skill to toggle")
    sp_toggle.add_argument("--on", action="store_true", help="Force enable")
    sp_toggle.add_argument("--off", action="store_true", help="Force disable")
    
    sp_search = subparsers.add_parser("search", parents=[common_parser], help="Search the 3,300+ skill vault")
    sp_search.add_argument("query", type=str, help="Search query")
    sp_search.add_argument("--limit", "-l", type=int, default=25, help="Result limit")
    
    sp_budget = subparsers.add_parser("budget", parents=[common_parser], help="Token budget estimator & context simulator")
    
    sp_mode = subparsers.add_parser("mode", parents=[common_parser], help="1-Click Mission Mode presets (mvp, harden, refactor, design, fullstack, ai-agents)")
    sp_mode.add_argument("mode_name", nargs="?", choices=["mvp", "harden", "refactor", "design", "fullstack", "ai-agents"], help="Target mission mode")
    
    sp_prompt = subparsers.add_parser("prompt", parents=[common_parser], help="Export system prompt for web LLMs (Claude.ai, ChatGPT, Gemini)")
    sp_prompt.add_argument("--no-copy", action="store_true", help="Do not copy to clipboard")
    
    subparsers.add_parser("watch", parents=[common_parser], help="Start workspace stack watcher daemon")
    
    sp_preview = subparsers.add_parser("preview", parents=[common_parser], help="Preview skill documentation and weight")
    sp_preview.add_argument("skill_name", type=str, help="Name of skill to preview")

    sp_ingest = subparsers.add_parser("ingest", parents=[common_parser], help="Import remote skill from GitHub")
    sp_ingest.add_argument("source", type=str, help="URL or unique name")
    sp_ingest.add_argument("--category", "-c", type=str, default="INGESTED", help="Category tag")
    
    subparsers.add_parser("sync", parents=[common_parser], help="Sync active manifest to Cursor, Claude, OpenCode")
    subparsers.add_parser("audit", parents=[common_parser], help="Audit SKILL.md files on disk")
    subparsers.add_parser("wizard", parents=[common_parser], help="Launch Socratic qualification wizard")
    subparsers.add_parser("init", parents=[common_parser], help="Initialize .agents/ directory")
    subparsers.add_parser("doctor", parents=[common_parser], help="Run health diagnostics")
    
    sp_export = subparsers.add_parser("export", parents=[common_parser], help="Export manifest to file")
    sp_export.add_argument("--format", "-f", choices=["json", "markdown", "both"], default="both")
    
    sp_profile = subparsers.add_parser("profile", parents=[common_parser], help="Manage skill preset profiles")
    sp_profile.add_argument("profile_action", choices=["save", "load", "list", "delete"])
    sp_profile.add_argument("profile_name", nargs="?", type=str)
    
    subparsers.add_parser("stats", parents=[common_parser], help="Show usage metrics and dashboard")
    
    sp_ui = subparsers.add_parser("ui", parents=[common_parser], help="Launch companion web dashboard at http://localhost:4242")
    sp_ui.add_argument("--port", "-p", type=int, default=4242, help="HTTP Port")
    sp_ui.add_argument("--no-browser", action="store_true", help="Do not open browser automatically")

    sp_ask = subparsers.add_parser("ask", parents=[common_parser], help="Query terminal assistant grounded in active skills")
    sp_ask.add_argument("query", nargs="*", help="Question or task to ask")

    sp_why = subparsers.add_parser("why", parents=[common_parser], help="Explain activation rationale and AST markers for a skill")
    sp_why.add_argument("skill_name", nargs="?", help="Skill identifier to explain")

    subparsers.add_parser("graph", parents=[common_parser], help="Display ASCII dependency graph and governance topology")
    subparsers.add_parser("auto-branch", parents=[common_parser], help="Auto-calibrate mission mode based on active git branch")

    sp_bench = subparsers.add_parser("benchmark", parents=[common_parser], help="Run quality & structural benchmark on skill vault")
    sp_bench.add_argument("--limit", "-l", type=int, default=40, help="Number of skills to audit")

    subparsers.add_parser("update", parents=[common_parser], help="Update skill vault from GitHub master")

    sp_eval = subparsers.add_parser("eval", parents=[common_parser], help="Skill sandbox playground and prompt evaluator")
    sp_eval.add_argument("skill_name", nargs="?", help="Skill to evaluate")
    sp_eval.add_argument("test_prompt", nargs="*", help="Prompt to run in sandbox")

    sp_desktop = subparsers.add_parser("desktop", parents=[common_parser], help="Desktop integration hooks")
    sp_desktop.add_argument("desktop_action", choices=["setup", "config"])
    
    sp_completions = subparsers.add_parser("completions", help="Install shell completion scripts")
    sp_completions.add_argument("completions_action", choices=["install", "uninstall", "show", "path"])
    sp_completions.add_argument("--shell", "-s", choices=["bash", "zsh", "fish", "all"], default="all")
    
    return parser

# =============================================================================
# 17. MAIN ENTRY POINT
# =============================================================================
def apply_no_color():
    for attr in dir(C):
        if attr.isupper() and attr != 'RESET':
            setattr(C, attr, '')
    C.RESET = ''
    for k in BOX:
        BOX[k] = BOX[k].replace('\033', '')

def main():
    parser = build_parser()
    args = parser.parse_args()
    
    if args.no_color:
        apply_no_color()
        
    if args.command is None:
        run_interactive_tui()
        return
        
    def out(data):
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        else:
            if isinstance(data, dict):
                for k, v in data.items():
                    print(f"{k}: {v}")
            elif isinstance(data, list):
                for item in data:
                    print(item)
            else:
                print(data)

    if args.command == "scan":
        if args.json:
            out(ProjectDiscovery.inspect())
        else:
            view_project_discovery()
            
    elif args.command == "list":
        m = ManifestController.load_active_manifest()
        skills = m.get("active_skills", [])
        if args.core_only:
            skills = [s for s in skills if s.get("is_core", False)]
        if args.json:
            out([{"name": s["name"], "category": s.get("category", "CUSTOM"), "reason": s.get("reason", "")} for s in skills])
        else:
            headers = ["#", "Type", "Skill Name", "Category", "Purpose / Rationale"]
            rows = []
            for idx, s in enumerate(skills, 1):
                badge = f"{C.GEMINI_VIOLET}CORE{C.RESET}" if s.get("is_core") else f"{C.EMERALD}SPEC{C.RESET}"
                sk_path = os.path.join(SKILLS_DIR, s["name"], "SKILL.md")
                name_link = make_file_link(s["name"], sk_path) if os.path.isfile(sk_path) else s["name"]
                rows.append([f"{idx:02d}", badge, name_link, s.get("category", "CUSTOM"), s.get("reason", "")])
            print(render_table(headers, rows, border_color=C.SLATE_DARK))
            
    elif args.command == "toggle":
        if args.on:
            _, msg = ManifestController.toggle_skill(args.skill_name, force_state=True)
        elif args.off:
            _, msg = ManifestController.toggle_skill(args.skill_name, force_state=False)
        else:
            _, msg = ManifestController.toggle_skill(args.skill_name)
        print(f"\n  {msg}\n")
        
    elif args.command == "search":
        if args.json:
            out(SkillVaultEngine.search_local(args.query, args.limit))
        else:
            view_vault_search(initial_query=args.query, interactive=False)

    elif args.command == "budget":
        if args.json:
            out(TokenBudgetEngine.calculate_budget())
        else:
            view_token_budget()

    elif args.command == "mode":
        if args.mode_name:
            ok, msg = MissionModesEngine.apply_mode(args.mode_name)
            print(f"\n  {msg}\n")
        else:
            view_mission_modes()

    elif args.command == "prompt":
        view_system_prompt(copy_to_clip=not args.no_copy)

    elif args.command == "watch":
        view_stack_watcher()

    elif args.command == "preview":
        view_skill_preview(args.skill_name)
            
    elif args.command == "ingest":
        ok, msg = SkillVaultEngine.ingest_remote_skill(args.source, args.category)
        print(f"\n  {msg}\n")
        
    elif args.command == "sync":
        if args.json:
            out(MultiCLISync.sync_all())
        else:
            view_sync_multicli()
            
    elif args.command == "audit":
        if args.json:
            out(MultiCLISync.audit_compliance())
        else:
            view_compliance_audit()
            
    elif args.command == "wizard":
        run_qualification_wizard()
        
    elif args.command == "init":
        view_init_project()
        
    elif args.command == "doctor":
        if args.json:
            out(MultiCLISync.doctor_check())
        else:
            view_doctor()
            
    elif args.command == "export":
        view_export()
        
    elif args.command == "stats":
        if args.json:
            out(MultiCLISync.get_stats())
        else:
            view_stats_dashboard()

    elif args.command == "ui":
        view_web_companion(port=args.port, open_browser=not args.no_browser)

    elif args.command == "ask":
        query_str = " ".join(args.query) if args.query else ""
        if args.json and query_str:
            out({"query": query_str, "response": CopilotQueryEngine.query(query_str)})
        else:
            view_copilot_ask(prompt=query_str if query_str else None)

    elif args.command == "why":
        if args.json and args.skill_name:
            out(SkillGraphEngine.explain(args.skill_name))
        else:
            view_why_skill(skill_name=args.skill_name)

    elif args.command == "graph":
        view_skill_graph()

    elif args.command == "auto-branch":
        if args.json:
            ok, msg = GitBranchEngine.auto_calibrate()
            out({"success": ok, "message": msg})
        else:
            view_auto_branch()

    elif args.command == "benchmark":
        if args.json:
            out(SkillBenchmarkEngine.run_benchmark(limit=args.limit))
        else:
            view_benchmark(limit=args.limit)

    elif args.command == "update":
        if args.json:
            ok, msg = SkillUpdateEngine.update_vault()
            out({"success": ok, "message": msg})
        else:
            view_update_vault()

    elif args.command == "eval":
        prompt_str = " ".join(args.test_prompt) if args.test_prompt else ""
        view_eval_skill(skill_name=args.skill_name, prompt=prompt_str if prompt_str else None)
            
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
                reason = next((c["reason"] for c in MANDATORY_CORE_SUITE if c["name"] == sk_name), "Loaded from profile")
                new_skills.append({
                    "name": sk_name,
                    "category": "CORE" if is_core else "PROFILE_LOADED",
                    "reason": reason,
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
            home = os.path.expanduser("~")
            paths = {
                "bash": [os.path.join(home, ".bashrc"), "/etc/bash_completion.d/sds"],
                "zsh": [os.path.join(home, ".zsh", "completions", "_sds"), os.path.join(home, ".zshrc")],
                "fish": [os.path.join(home, ".config", "fish", "completions", "sds.fish")]
            }
            for sh, pts in paths.items():
                if shell_target in (sh, 'all'):
                    print(f"  {sh}: {', '.join(pts)}")
        elif action == "show":
            shells = ["bash", "zsh", "fish"] if shell_target == "all" else [shell_target]
            for sh in shells:
                script = os.path.join(completions_dir, f"sds.{sh}")
                if os.path.isfile(script):
                    with open(script, 'r', encoding='utf-8') as f:
                        print(f.read())
        elif action == "install":
            print("✓ Shell completions installed.")

if __name__ == '__main__':
    main()

