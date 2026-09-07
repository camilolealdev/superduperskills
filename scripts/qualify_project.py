#!/usr/bin/env python3
"""
Qualify Project & Skill Selector for SuperDuperSkills (Gemini & Claude Edition)
Interactive Socratic CLI Wizard that qualifies project requirements, selects exact skills,
and generates .agents/ACTIVE-SKILLS.json with mandatory SKILL.md reading directives.
"""

import os
import sys
import json
import glob
import re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# TrueColor / ANSI Styling
class C:
    RESET       = "\033[0m"
    BOLD        = "\033[1m"
    DIM         = "\033[2m"
    CYAN        = "\033[38;2;34;211;238m"
    BLUE        = "\033[38;2;96;165;250m"
    INDIGO      = "\033[38;2;129;140;248m"
    VIOLET      = "\033[38;2;168;85;247m"
    GOLD        = "\033[38;2;251;191;36m"
    EMERALD     = "\033[38;2;52;211;153m"
    SLATE_LIGHT = "\033[38;2;226;232;240m"
    SLATE_MUTED = "\033[38;2;148;163;184m"
    SLATE_DARK  = "\033[38;2;100;116;139m"
    ROSE        = "\033[38;2;248;113;113m"

WORKSPACE_DIR = os.getcwd()
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if os.path.isdir(os.path.join(REPO_ROOT, 'skills')):
    SKILLS_DIR = os.path.join(REPO_ROOT, 'skills')
elif os.path.isdir(os.path.join(WORKSPACE_DIR, 'skills')):
    SKILLS_DIR = os.path.join(WORKSPACE_DIR, 'skills')
else:
    SKILLS_DIR = os.path.join(os.path.expanduser('~'), '.claude', 'skills')

AGENTS_DIR = os.path.join(WORKSPACE_DIR, '.agents')
ACTIVE_MANIFEST = os.path.join(AGENTS_DIR, 'ACTIVE-SKILLS.json')
QUALIFICATION_DOC = os.path.join(AGENTS_DIR, 'PROJECT-QUALIFICATION.md')

CORE_SUITE = [
    {"name": "caveman", "reason": "Output Compression (-75% token reduction)"},
    {"name": "ponytail", "reason": "YAGNI & Simplicity Architecture"},
    {"name": "spec-kit", "reason": "Spec-Driven Development & Task Breakdown"},
    {"name": "token-savings", "reason": "Context Budget & Skill Filtering"},
    {"name": "harness", "reason": "Automated Verification & Test Harness"},
    {"name": "claude-mem", "reason": "Persistent Session Memory"},
    {"name": "rtk", "reason": "Terminal Log Compression (Rust Token Killer)"},
    {"name": "graphify", "reason": "Codebase Knowledge Graph Indexing"},
    {"name": "archify", "reason": "Interactive System Diagrams (Trigger: 3 Commits)"},
    {"name": "skill-seekers", "reason": "Ingesta & Búsqueda Activa de Skills"},
    {"name": "skill-vault", "reason": "Bóveda Persistente de Skills"},
    {"name": "all-deploy", "reason": "Despliegues Universales Multicloud"},
    {"name": "context-mode", "reason": "Gestión & Compresión de Ventana de Contexto"},
    {"name": "aprende-skill", "reason": "Aprendizaje Acelerado Agentico"},
    {"name": "agentshield", "reason": "Escudo de Seguridad & Prompt Sanitization"},
    {"name": "modo-tdah", "reason": "Ejecución Ultra-Focalizada sin Explicaciones Infladas"},
    {"name": "agentic-awesome-skills", "reason": "Catálogo de Patrones Agenticos Autónomos"},
    {"name": "gsd-core", "reason": "Get Shit Done (GSD) Execution Framework"},
    {"name": "i-have-adhd", "reason": "Formateo de Salida Amigable ADHD (Acciones Primero)"}
]

def render_box(title: str, lines: list, width: int = 72) -> str:
    top = f"  {C.SLATE_DARK}╭─{C.RESET} {C.BOLD}{C.CYAN}✦ {title}{C.RESET} {C.SLATE_DARK}{'─' * max(2, width - len(title) - 8)}╮{C.RESET}"
    bot = f"  {C.SLATE_DARK}╰{'─' * (width - 2)}╯{C.RESET}"
    body = [f"  {C.SLATE_DARK}│{C.RESET}  {line}" for line in lines]
    return "\n".join([top] + body + [bot])

def detect_stack():
    detected = {
        'frontend': [],
        'backend': [],
        'mobile': [],
        'devops': [],
        'database': [],
        'security': []
    }
    
    pkg_path = os.path.join(WORKSPACE_DIR, 'package.json')
    if os.path.isfile(pkg_path):
        try:
            with open(pkg_path, 'r', encoding='utf-8') as f:
                pkg = json.load(f)
                deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
                if 'react' in deps:
                    detected['frontend'].append('react-patterns')
                    detected['frontend'].append('react-performance')
                if 'next' in deps:
                    detected['frontend'].append('nextjs-developer')
                if 'vue' in deps:
                    detected['frontend'].append('vue-patterns')
                if 'tailwindcss' in deps or '@tailwindcss/vite' in deps:
                    detected['frontend'].append('tailwind-theme-builder')
                if 'express' in deps or 'fastify' in deps:
                    detected['backend'].append('nodejs-backend-patterns')
        except Exception:
            pass

    if any(os.path.isfile(os.path.join(WORKSPACE_DIR, f)) for f in ['requirements.txt', 'pyproject.toml', 'Pipfile', 'setup.py']):
        detected['backend'].append('python-patterns')
        detected['backend'].append('python-testing')

    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'go.mod')):
        detected['backend'].append('golang-patterns')
        detected['backend'].append('golang-testing')

    if glob.glob(os.path.join(WORKSPACE_DIR, '*.csproj')) or glob.glob(os.path.join(WORKSPACE_DIR, '*.sln')):
        detected['backend'].append('dotnet-patterns')
        detected['backend'].append('dotnet-best-practices')

    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'pubspec.yaml')):
        detected['mobile'].append('flutter-apply-architecture-best-practices')
        detected['mobile'].append('flutter-build-responsive-layout')
    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'app.json')):
        detected['mobile'].append('expo-overview')
        detected['mobile'].append('expo-router')

    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'Dockerfile')) or os.path.isfile(os.path.join(WORKSPACE_DIR, 'docker-compose.yml')):
        detected['devops'].append('docker-patterns')

    return detected

def prompt_choice(step: str, question: str, options: list):
    print(f"\n  {C.GOLD}Step {step}:{C.RESET} {C.BOLD}{question}{C.RESET}")
    print(f"  {C.SLATE_DARK}{'─' * 60}{C.RESET}")
    for idx, opt in enumerate(options, 1):
        print(f"    {C.CYAN}[{idx}]{C.RESET} {C.SLATE_LIGHT}{opt}{C.RESET}")
    while True:
        try:
            choice = input(f"\n  {C.CYAN}❯ Selecciona una opción [1-{len(options)}]:{C.RESET} ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return int(choice) - 1
            print(f"  {C.ROSE}⚠ Opción inválida. Intenta nuevamente.{C.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n  {C.SLATE_MUTED}Operación cancelada.{C.RESET}\n")
            sys.exit(0)

def prompt_multiselect(step: str, question: str, options: list):
    print(f"\n  {C.GOLD}Step {step}:{C.RESET} {C.BOLD}{question}{C.RESET} {C.SLATE_MUTED}(separados por coma, ej: 1, 3){C.RESET}")
    print(f"  {C.SLATE_DARK}{'─' * 60}{C.RESET}")
    for idx, opt in enumerate(options, 1):
        print(f"    {C.CYAN}[{idx}]{C.RESET} {C.SLATE_LIGHT}{opt}{C.RESET}")
    while True:
        try:
            choice = input(f"\n  {C.CYAN}❯ Selecciona opciones:{C.RESET} ").strip()
            if not choice:
                return []
            parts = [p.strip() for p in choice.split(',')]
            valid = []
            for p in parts:
                if p.isdigit() and 1 <= int(p) <= len(options):
                    valid.append(int(p) - 1)
            if valid:
                return valid
            print(f"  {C.ROSE}⚠ Selección inválida.{C.RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n  {C.SLATE_MUTED}Operación cancelada.{C.RESET}\n")
            sys.exit(0)

def run_interactive_wizard():
    print(f"""
  {C.CYAN}╭────────────────────────────────────────────────────────────────────────╮{C.RESET}
  {C.CYAN}│{C.RESET}  {C.CYAN}{C.BOLD}✦ SOCRATIC QUALIFICATION WIZARD{C.RESET}                       {C.INDIGO}● SuperDuperSkills{C.RESET} {C.CYAN}│{C.RESET}
  {C.BLUE}│{C.RESET}  {C.SLATE_LIGHT}Entrevista guiada para calibrar el contexto de los agentes AI{C.RESET}         {C.BLUE}│{C.RESET}
  {C.INDIGO}╰────────────────────────────────────────────────────────────────────────╯{C.RESET}
""")
    
    stack = detect_stack()
    detected_items = []
    for category, skills in stack.items():
        if skills:
            detected_items.append(f"{category.upper()}: {', '.join(skills)}")
            
    if detected_items:
        lines = [f"{C.EMERALD}✔ Detectado:{C.RESET} {item}" for item in detected_items]
        print(render_box("Stack Detectado Automáticamente", lines))
    else:
        print(f"  {C.SLATE_MUTED}ℹ No se detectó stack específico en el directorio raíz.{C.RESET}")

    # Step 1: Project Phase
    phases = [
        "0-to-1 MVP / Creación de Nuevo Producto desde Cero",
        "Refactorización / Deuda Técnica / Optimización de Rendimiento",
        "Diseño & Pulido de Interfaz (Anti-Slop / Animaciones / Micro-detalles)",
        "Seguridad / Hardening OWASP / Auditoría de Código",
        "Feature Enterprise / Integración de APIs & Backend"
    ]
    p_idx = prompt_choice("[1/4]", "¿En qué fase se encuentra tu proyecto actualmente?", phases)
    selected_phase = phases[p_idx]

    # Step 2: Key Priorities
    priorities = [
        "Simplicidad y Minimal Diffs (Evitar sobre-ingeniería)",
        "Calidad Visual de Clase Mundial (Emil Kowalski / Micro-interacciones)",
        "Testing Automatizado Riguroso (TDD / Harness Verification)",
        "Protección de Tokens y Contexto (Caveman / RTK)",
        "Arquitectura RAG / IA / Sistemas Multi-Agente",
        "SEO Técnico / Posicionamiento y Copia Persuasiva"
    ]
    p_selected = prompt_multiselect("[2/4]", "¿Cuáles son tus prioridades principales?", priorities)

    # Step 3: Skill Mapping
    selected_skills = []
    
    # Always include core suite
    for c in CORE_SUITE:
        selected_skills.append({
            "name": c["name"],
            "category": "CORE",
            "reason": c["reason"],
            "is_core": True,
            "mandatory_view": True
        })

    # Add stack skills
    for cat, skills in stack.items():
        for sk in skills:
            selected_skills.append({
                "name": sk,
                "category": cat.upper(),
                "reason": f"Detectado automáticamente por stack {cat}",
                "is_core": False,
                "mandatory_view": True
            })

    # Add UI skills if chosen
    if any(p in [1, 2] for p in p_selected) or p_idx == 2:
        for sk, reason in [("emil-design-eng", "Micro-detalles y diseño UI"), ("animate", "Animaciones web fluidas"), ("taste-skill", "Diseño anti-slop")]:
            selected_skills.append({
                "name": sk,
                "category": "DESIGN_UI",
                "reason": reason,
                "is_core": False,
                "mandatory_view": True
            })

    # Deduplicate
    unique_skills = []
    seen = set()
    for s in selected_skills:
        if s["name"] not in seen:
            seen.add(s["name"])
            unique_skills.append(s)

    # Save to manifest
    os.makedirs(AGENTS_DIR, exist_ok=True)
    manifest = {
        "project_name": os.path.basename(WORKSPACE_DIR),
        "project_phase": selected_phase,
        "objectives": [priorities[i] for i in p_selected] if p_selected else ["YAGNI", "UI Polish"],
        "active_skills": unique_skills,
        "mandatory_protocol": "EL AGENTE AI DEBE INVOCAR view_file EN CADA SKILL.md ANTES DE ESCRIBIR CÓDIGO."
    }

    with open(ACTIVE_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    summary_lines = [
        f"Fase Calificada: {C.SLATE_LIGHT}{selected_phase}{C.RESET}",
        f"Skills Activas:   {C.EMERALD}{len(unique_skills)} habilidades calibradas{C.RESET}",
        f"Manifiesto:       {C.CYAN}.agents/ACTIVE-SKILLS.json{C.RESET}"
    ]
    print(f"\n{render_box('Cualificación Completada con Éxito', summary_lines)}")
    print(f"\n  {C.EMERALD}✔ Todo agente AI consultará esta matriz antes de emitir código.{C.RESET}\n")

if __name__ == '__main__':
    run_interactive_wizard()
