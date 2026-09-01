#!/usr/bin/env python3
"""
Qualify Project & Skill Selector for SuperDuperSkills
Interactive CLI Wizard that qualifies project requirements, selects exact skills,
and generates .agents/ACTIVE-SKILLS.json with mandatory SKILL.md reading directives.
"""

import os
import sys
import json
import glob
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = os.getcwd()
SKILLS_DIR = os.path.join(WORKSPACE_DIR, 'skills')
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

def detect_stack():
    detected = {
        'frontend': [],
        'backend': [],
        'mobile': [],
        'devops': [],
        'database': [],
        'security': []
    }
    
    # Check Node / JS / TS
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

    # Check Python
    if any(os.path.isfile(os.path.join(WORKSPACE_DIR, f)) for f in ['requirements.txt', 'pyproject.toml', 'Pipfile', 'setup.py']):
        detected['backend'].append('python-patterns')
        detected['backend'].append('python-testing')

    # Check Go
    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'go.mod')):
        detected['backend'].append('golang-patterns')
        detected['backend'].append('golang-testing')

    # Check .NET
    if glob.glob(os.path.join(WORKSPACE_DIR, '*.csproj')) or glob.glob(os.path.join(WORKSPACE_DIR, '*.sln')):
        detected['backend'].append('dotnet-patterns')
        detected['backend'].append('dotnet-best-practices')

    # Check Mobile (Expo / Flutter)
    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'pubspec.yaml')):
        detected['mobile'].append('flutter-apply-architecture-best-practices')
        detected['mobile'].append('flutter-build-responsive-layout')
    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'app.json')):
        detected['mobile'].append('expo-overview')
        detected['mobile'].append('expo-router')

    # Check Docker / Cloud
    if os.path.isfile(os.path.join(WORKSPACE_DIR, 'Dockerfile')) or os.path.isfile(os.path.join(WORKSPACE_DIR, 'docker-compose.yml')):
        detected['devops'].append('docker-patterns')

    return detected

def prompt_choice(question, options):
    print(f"\n❓ {question}")
    for idx, opt in enumerate(options, 1):
        print(f"  [{idx}] {opt}")
    while True:
        try:
            choice = input("\n> Selecciona una opción (número): ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(options):
                return int(choice) - 1
            print("⚠️ Opción inválida. Intenta nuevamente.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            sys.exit(0)

def prompt_multiselect(question, options):
    print(f"\n❓ {question} (Separados por coma, ej: 1, 3)")
    for idx, opt in enumerate(options, 1):
        print(f"  [{idx}] {opt}")
    while True:
        try:
            choice = input("\n> Selecciona una o varias opciones: ").strip()
            if not choice:
                return []
            parts = [p.strip() for p in choice.split(',')]
            valid = []
            for p in parts:
                if p.isdigit() and 1 <= int(p) <= len(options):
                    valid.append(int(p) - 1)
            if valid:
                return valid
            print("⚠️ Selección inválida. Intenta nuevamente.")
        except (KeyboardInterrupt, EOFError):
            print("\nOperación cancelada.")
            sys.exit(0)

def run_interactive_wizard():
    print("=" * 80)
    print(" 🎯 SUPERDUPERSKILLS — SISTEMA INTERACTIVO DE CUALIFICACIÓN DE PROYECTOS")
    print("=" * 80)
    
    stack = detect_stack()
    print("\n🔍 Stack detectado automáticamente en el espacio de trabajo:")
    has_detected = False
    for category, skills in stack.items():
        if skills:
            has_detected = True
            print(f"  • {category.upper()}: {', '.join(skills)}")
    if not has_detected:
        print("  • Proyecto agnóstico o sin dependencias detectadas.")

    # 1. Phase Question
    phases = [
        "0-to-1 MVP / Creación de Proyecto Desde Cero",
        "Refactorización / Deuda Técnica / Limpieza de Código",
        "Diseño Visual & UI Polish (Anti-Slop, Animaciones, Brand)",
        "Auditoría de Seguridad, OWASP & Compliance",
        "Producción, CI/CD, DevOps & Escalabilidad",
        "Investigación Autónoma & Multi-Agent Orchestration"
    ]
    phase_idx = prompt_choice("¿En qué fase se encuentra tu proyecto u objetivo actual?", phases)
    selected_phase = phases[phase_idx]

    # 2. Key Objectives
    objectives = [
        "Garantizar Arquitectura YAGNI & Código Mínimo",
        "Auditar Rendimiento (Core Web Vitals, LCP, Memoria)",
        "Implementar Pruebas Automatizadas (Unit, E2E, TDD)",
        "Diseñar Interfaces Visuales Premium (GSAP, Tailwind, Editorial)",
        "Ajustar Tono & Copywriting (De-Slop Humanizer)",
        "Estrategia GTM, Marketing, Precios & SEO",
        "Integrar Modelos GenAI (Gemini, HuggingFace, Genkit)"
    ]
    obj_indices = prompt_multiselect("¿Cuáles son tus objetivos prioritarios en esta sesión?", objectives)
    selected_objectives = [objectives[i] for i in obj_indices]

    # Map skills based on qualification
    matched_skills = []
    
    # Always Core Suite
    for c in CORE_SUITE:
        matched_skills.append({
            "name": c["name"],
            "category": "CORE (Obligatorio)",
            "reason": c["reason"],
            "mandatory_view": True
        })

    # Stack skills
    for cat, s_list in stack.items():
        for s in s_list:
            matched_skills.append({
                "name": s,
                "category": f"STACK ({cat.upper()})",
                "reason": f"Detectado en el entorno de desarrollo ({cat}).",
                "mandatory_view": True
            })

    # Phase-specific additions
    if "0-to-1 MVP" in selected_phase:
        matched_skills.append({"name": "orch-build-mvp", "category": "FASE", "reason": "Construcción vertical de MVP", "mandatory_view": True})
        matched_skills.append({"name": "spec-driven-development", "category": "FASE", "reason": "Especificación previa", "mandatory_view": True})
    elif "Refactorización" in selected_phase:
        matched_skills.append({"name": "refactor", "category": "FASE", "reason": "Refactorización quirúrgica de código", "mandatory_view": True})
        matched_skills.append({"name": "reducing-entropy", "category": "FASE", "reason": "Reducción de tamaño del codebase", "mandatory_view": True})
    elif "Diseño Visual" in selected_phase:
        matched_skills.append({"name": "design-taste-frontend", "category": "FASE", "reason": "UI Anti-slop landing pages", "mandatory_view": True})
        matched_skills.append({"name": "emil-design-eng", "category": "FASE", "reason": "Filosofía de diseño de Emil Kowalski", "mandatory_view": True})
        matched_skills.append({"name": "animate", "category": "FASE", "reason": "Animaciones web avanzadas (Emil Kowalski)", "mandatory_view": True})
        matched_skills.append({"name": "review-animations", "category": "FASE", "reason": "Auditoría de animaciones UI", "mandatory_view": True})

    # Objective-specific additions
    for obj in selected_objectives:
        if "Diseñar Interfaces" in obj:
            matched_skills.append({"name": "high-end-visual-design", "category": "OBJETIVO", "reason": "Aesthetic agency-grade UI", "mandatory_view": True})
            matched_skills.append({"name": "gsap-framer-scroll-animation", "category": "OBJETIVO", "reason": "Animaciones scroll y reveals", "mandatory_view": True})
            matched_skills.append({"name": "emil-design-eng", "category": "OBJETIVO", "reason": "Emil Kowalski Core UI Craft", "mandatory_view": True})
            matched_skills.append({"name": "apple-design", "category": "OBJETIVO", "reason": "Criterios de diseño al estilo Apple (iOS/macOS)", "mandatory_view": True})
            matched_skills.append({"name": "find-animation-opportunities", "category": "OBJETIVO", "reason": "Detección de puntos de animación", "mandatory_view": True})
            matched_skills.append({"name": "improve-animations", "category": "OBJETIVO", "reason": "Mejora y fix de animaciones", "mandatory_view": True})
        if "Pruebas" in obj:
            matched_skills.append({"name": "tdd-workflow", "category": "OBJETIVO", "reason": "Workflow TDD con 80%+ cobertura", "mandatory_view": True})
            matched_skills.append({"name": "e2e-testing", "category": "OBJETIVO", "reason": "Pruebas E2E con Playwright", "mandatory_view": True})
        if "Copywriting" in obj:
            matched_skills.append({"name": "humanizer", "category": "OBJETIVO", "reason": "Reescritura de tono humano sin IA slop", "mandatory_view": True})
        if "Marketing" in obj:
            matched_skills.append({"name": "gtm-0-to-1-launch", "category": "OBJETIVO", "reason": "Estrategia GTM y captación inicial", "mandatory_view": True})
        if "GenAI" in obj:
            matched_skills.append({"name": "gemini-api-dev", "category": "OBJETIVO", "reason": "Integración Gemini Multimodal", "mandatory_view": True})

    # Deduplicate skills
    unique_skills = []
    seen_names = set()
    for item in matched_skills:
        if item["name"] not in seen_names:
            seen_names.add(item["name"])
            unique_skills.append(item)

    # Output Summary
    print("\n" + "=" * 80)
    print(" 📋 MATRIZ DE SKILLS QUALIFIED & ACTIVADAS PARA TU PROYECTO")
    print("=" * 80)
    for idx, sk in enumerate(unique_skills, 1):
        path = os.path.join(SKILLS_DIR, sk['name'], 'SKILL.md')
        exists_str = "✅ DISPONIBLE" if os.path.exists(path) else "⚠️ NO LOCALIZADO"
        print(f"  {idx:02d}. [{sk['category']}] {sk['name']:<30} | {sk['reason']} ({exists_str})")

    # Generate Manifest
    os.makedirs(AGENTS_DIR, exist_ok=True)
    
    manifest_data = {
        "project_phase": selected_phase,
        "objectives": selected_objectives,
        "active_skills": unique_skills,
        "mandatory_protocol": "EL AGENTE AI DEBE INVOCAR view_file EN CADA SKILL.md ANTES DE ESCRIBIR CÓDIGO."
    }
    
    with open(ACTIVE_MANIFEST, 'w', encoding='utf-8') as f:
        json.dump(manifest_data, f, indent=2, ensure_ascii=False)
        
    print(f"\n💾 Manifiesto guardado en: {ACTIVE_MANIFEST}")

    # Generate Qualification Document
    with open(QUALIFICATION_DOC, 'w', encoding='utf-8') as f:
        f.write(f"# Proyecto Cualificado — Matriz de Skills Activas\n\n")
        f.write(f"**Fase del Proyecto:** {selected_phase}\n")
        f.write(f"**Objetivos Clave:** {', '.join(selected_objectives)}\n\n")
        f.write(f"## Protocolo de Lectura Obligatoria\n")
        f.write(f"> [!IMPORTANT]\n")
        f.write(f"> Todo agente que trabaje en este proyecto **DEBE LEER CADA SKILL.md** usando `view_file` antes de ejecutar código.\n\n")
        f.write(f"| # | Categoría | Skill | Razón de Uso | Ruta Local |\n")
        f.write(f"|---|-----------|-------|--------------|------------|\n")
        for idx, sk in enumerate(unique_skills, 1):
            path_link = f"[`skills/{sk['name']}/SKILL.md`](file:///{os.path.join(SKILLS_DIR, sk['name'], 'SKILL.md').replace('\\', '/')})"
            f.write(f"| {idx} | {sk['category']} | `{sk['name']}` | {sk['reason']} | {path_link} |\n")

    print(f"📄 Reporte de cualificación documentado en: {QUALIFICATION_DOC}\n")
    print("✨ ¡Cualificación completada! Los agentes consultarán este manifiesto activado.")

if __name__ == '__main__':
    run_interactive_wizard()
