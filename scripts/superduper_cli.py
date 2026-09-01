#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
 🚀 SUPERDUPERSKILLS AGENTIC CLI & CONTROL CENTER v3.0
================================================================================
 Comprehensive Terminal UI & Discovery Engine for AI Agent Skills Governance.
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
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

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

WORKSPACE_DIR = os.getcwd()
SKILLS_DIR = os.path.join(WORKSPACE_DIR, 'skills')
AGENTS_DIR = os.path.join(WORKSPACE_DIR, '.agents')
ACTIVE_MANIFEST = os.path.join(AGENTS_DIR, 'ACTIVE-SKILLS.json')
QUALIFICATION_DOC = os.path.join(AGENTS_DIR, 'PROJECT-QUALIFICATION.md')

# ==============================================================================
# 🔒 1. MANDATORY INVARIANT CORE SUITE (19 SKILLS)
# ==============================================================================
MANDATORY_CORE_SUITE = [
    {"name": "caveman", "reason": "Output Compression (-75% token reduction)", "category": "CORE"},
    {"name": "ponytail", "reason": "YAGNI & Simplicity Architecture (Minimal Diffs)", "category": "CORE"},
    {"name": "spec-kit", "reason": "Spec-Driven Development & Task Breakdown", "category": "CORE"},
    {"name": "token-savings", "reason": "Context Budget & Skill Filtering", "category": "CORE"},
    {"name": "harness", "reason": "Automated Verification & Test Harness Loop", "category": "CORE"},
    {"name": "claude-mem", "reason": "Persistent Session & Architecture Memory", "category": "CORE"},
    {"name": "rtk", "reason": "Terminal Log Compression (Rust Token Killer)", "category": "CORE"},
    {"name": "graphify", "reason": "Codebase Knowledge Graph Indexing", "category": "CORE"},
    {"name": "archify", "reason": "Interactive System Diagrams (Trigger: 3 Commits)", "category": "CORE"},
    {"name": "skill-seekers", "reason": "Ingesta & Búsqueda Activa de Skills Remotas", "category": "CORE"},
    {"name": "skill-vault", "reason": "Bóveda Persistente de Skills", "category": "CORE"},
    {"name": "all-deploy", "reason": "Despliegues Universales Multicloud", "category": "CORE"},
    {"name": "context-mode", "reason": "Gestión & Compresión de Ventana de Contexto", "category": "CORE"},
    {"name": "aprende-skill", "reason": "Aprendizaje Acelerado Agentico", "category": "CORE"},
    {"name": "agentshield", "reason": "Escudo de Seguridad & Prompt Sanitization", "category": "CORE"},
    {"name": "modo-tdah", "reason": "Ejecución Ultra-Focalizada sin Explicaciones Infladas", "category": "CORE"},
    {"name": "agentic-awesome-skills", "reason": "Catálogo de Patrones Agenticos Autónomos", "category": "CORE"},
    {"name": "gsd-core", "reason": "Get Shit Done (GSD) Execution Framework", "category": "CORE"},
    {"name": "i-have-adhd", "reason": "Formateo de Salida Action-First", "category": "CORE"}
]

# ==============================================================================
# 📂 2. SPECIALIZED CATEGORIES & HIGH-VALUE SKILL MAPPINGS
# ==============================================================================
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
            ("flutter-apply-architecture-best-practices", "Arquitectura en capas para Flutter (UI, Logic, Data)"),
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
            ("claude-seo", "SEO técnico, Schema.org markup y GEO (Generative Engine Optimization)"),
            ("editor-pro-max", "Edición profesional de estilo y copywriting de alta conversión"),
            ("claude-for-legal", "Análisis de contratos y cumplimiento normativo"),
            ("humanizer", "Eliminación de marcas artificiales de escritura de IA (Anti-AI-slop)"),
            ("gtm-0-to-1-launch", "Estrategia Go-To-Market y tracción temprana"),
            ("neuro-persuasion-toolkit", "Neuromarketing y psicología de conversión")
        ]
    }
}

# ==============================================================================
# 🔍 3. DEEP PROJECT DISCOVERY ENGINE
# ==============================================================================
class ProjectDiscovery:
    """Escanea el espacio de trabajo en profundidad y detecta stack, monorepos, microservicios y métricas."""
    
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
        
        # 1. Monorepo Check
        if os.path.isfile(os.path.join(root_path, 'pnpm-workspace.yaml')):
            report["is_monorepo"] = True
            report["monorepo_type"] = "pnpm workspaces"
            report["architecture"] = "Monorepo (pnpm)"
        elif os.path.isfile(os.path.join(root_path, 'turbo.json')):
            report["is_monorepo"] = True
            report["monorepo_type"] = "Turborepo"
            report["architecture"] = "Monorepo (Turbo)"
        elif os.path.isfile(os.path.join(root_path, 'nx.json')):
            report["is_monorepo"] = True
            report["monorepo_type"] = "Nx"
            report["architecture"] = "Monorepo (Nx)"

        # 2. Package.json / Node detection
        pkg_path = os.path.join(root_path, 'package.json')
        if os.path.isfile(pkg_path):
            report["languages"].append("JavaScript / TypeScript")
            try:
                with open(pkg_path, 'r', encoding='utf-8') as f:
                    pkg = json.load(f)
                    deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
                    
                    if 'react' in deps:
                        report["frameworks"].append("React")
                        report["recommended_skills"].extend(["emil-design-eng", "animate", "taste-skill"])
                    if 'next' in deps:
                        report["frameworks"].append("Next.js")
                        report["recommended_skills"].extend(["claude-seo", "high-end-visual-design"])
                    if 'vue' in deps:
                        report["frameworks"].append("Vue.js")
                    if 'svelte' in deps or '@sveltejs/kit' in deps:
                        report["frameworks"].append("Svelte")
                    if 'astro' in deps:
                        report["frameworks"].append("Astro")
                        report["recommended_skills"].append("claude-seo")
                    if 'tailwindcss' in deps or '@tailwindcss/vite' in deps:
                        report["frontend_ui"].append("Tailwind CSS")
                        report["recommended_skills"].append("tailwind-theme-builder")
                    if 'framer-motion' in deps or 'motion' in deps:
                        report["frontend_ui"].append("Framer Motion")
                        report["recommended_skills"].append("animate")
                    if 'gsap' in deps:
                        report["frontend_ui"].append("GSAP")
                        report["recommended_skills"].append("gsap-framer-scroll-animation")
                    if 'sonner' in deps:
                        report["frontend_ui"].append("Sonner Toasts")
                        report["recommended_skills"].append("ask-sonner")
                    if 'express' in deps or 'fastify' in deps or 'koa' in deps:
                        report["backend"].append("Node.js API")
                        report["recommended_skills"].append("nodejs-backend-patterns")
                    if '@nestjs/core' in deps:
                        report["backend"].append("NestJS")
                    if 'prisma' in deps or '@prisma/client' in deps:
                        report["databases"].append("Prisma ORM")
                    if 'drizzle-orm' in deps:
                        report["databases"].append("Drizzle ORM")
                    if 'pg' in deps or 'postgres' in deps:
                        report["databases"].append("PostgreSQL")
                        report["recommended_skills"].append("postgres-patterns")
                    if 'react-native' in deps or 'expo' in deps:
                        report["mobile"].append("Expo / React Native")
                        report["recommended_skills"].extend(["expo-overview", "animate-expo"])
            except Exception:
                pass

        # 3. Python detection
        py_files = ['requirements.txt', 'pyproject.toml', 'Pipfile', 'setup.py', 'poetry.lock']
        if any(os.path.isfile(os.path.join(root_path, f)) for f in py_files):
            report["languages"].append("Python")
            report["recommended_skills"].append("python-patterns")
            
            # Sub-check for FastAPI/Django/Flask
            for req_file in ['requirements.txt', 'pyproject.toml']:
                p = os.path.join(root_path, req_file)
                if os.path.isfile(p):
                    try:
                        content = open(p, 'r', encoding='utf-8', errors='ignore').read().lower()
                        if 'fastapi' in content:
                            report["frameworks"].append("FastAPI")
                        if 'django' in content:
                            report["frameworks"].append("Django")
                        if 'flask' in content:
                            report["frameworks"].append("Flask")
                        if 'sqlalchemy' in content:
                            report["databases"].append("SQLAlchemy")
                    except Exception:
                        pass

        # 4. Go detection
        if os.path.isfile(os.path.join(root_path, 'go.mod')):
            report["languages"].append("Go")
            report["backend"].append("Go Microservices")
            report["recommended_skills"].append("golang-patterns")

        # 5. Rust detection
        if os.path.isfile(os.path.join(root_path, 'Cargo.toml')):
            report["languages"].append("Rust")
            report["backend"].append("Rust Engine")
            report["recommended_skills"].append("rust-patterns")

        # 6. .NET detection
        if glob.glob(os.path.join(root_path, '*.csproj')) or glob.glob(os.path.join(root_path, '*.sln')):
            report["languages"].append("C# / .NET")
            report["backend"].append(".NET Core")
            report["recommended_skills"].append("dotnet-patterns")

        # 7. Flutter / Dart detection
        if os.path.isfile(os.path.join(root_path, 'pubspec.yaml')):
            report["languages"].append("Dart")
            report["mobile"].append("Flutter")
            report["recommended_skills"].extend(["flutter-apply-architecture-best-practices", "flutter-build-responsive-layout"])

        # 8. DevOps / Containers
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

        # Deduplicate recommendations
        report["recommended_skills"] = list(dict.fromkeys(report["recommended_skills"]))
        return report

# ==============================================================================
# 🎛️ 4. ACTIVE SKILL MANIFEST CONTROLLER
# ==============================================================================
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
        
        # Default initialization with Mandatory Core
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
        
        # Ensure mandatory core suite is always present
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
        
        # Write ACTIVE-SKILLS.json
        with open(ACTIVE_MANIFEST, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        # Write PROJECT-QUALIFICATION.md
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
                link_url = f"[`skills/{sk_name}/SKILL.md`](file:///{path_local.replace('\\', '/')})"
                f.write(f"| {idx:02d} | {sk_cat} | `{sk_name}` | {sk_reason} | {exists_icon} | {link_url} |\n")

    @staticmethod
    def toggle_skill(skill_name: str, force_state: Optional[bool] = None) -> Tuple[bool, str]:
        manifest = ManifestController.load_active_manifest()
        skills = manifest.get("active_skills", [])
        
        # Check if skill is in mandatory core (cannot disable)
        if any(c["name"] == skill_name for c in MANDATORY_CORE_SUITE):
            return False, f"⚠️ La skill '{skill_name}' es parte de la Suite Core Mandatoria y NO puede ser desactivada."
            
        found_idx = -1
        for idx, s in enumerate(skills):
            if s["name"] == skill_name:
                found_idx = idx
                break
                
        if found_idx >= 0:
            # Currently active
            if force_state is True:
                return True, f"ℹ️ La skill '{skill_name}' ya se encuentra activa."
            # Remove / disable
            removed = skills.pop(found_idx)
            ManifestController.save_active_manifest(manifest)
            return True, f"🔴 Skill '{skill_name}' desactivada correctamente."
        else:
            # Currently inactive
            if force_state is False:
                return True, f"ℹ️ La skill '{skill_name}' ya se encuentra inactiva."
            # Add / enable
            skills.append({
                "name": skill_name,
                "category": "USER_SELECTED",
                "reason": "Habilitada interactivamente por el usuario.",
                "is_core": False,
                "mandatory_view": True
            })
            ManifestController.save_active_manifest(manifest)
            return True, f"🟢 Skill '{skill_name}' activada e integrada en el manifiesto."

# ==============================================================================
# 🔎 5. SKILL VAULT SEARCH & REMOTE INGESTION ENGINE
# ==============================================================================
class SkillVaultEngine:
    """Busca en el repositorio local de 2,700+ skills o ingesta nuevas habilidades remotas."""
    
    @staticmethod
    def search_local(query: str, limit: int = 30) -> List[Dict[str, str]]:
        query_norm = query.lower().strip()
        results = []
        
        if not os.path.isdir(SKILLS_DIR):
            return results
            
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        # Fast Pass: Match directory names directly (instant <0.01s scan)
        try:
            with os.scandir(SKILLS_DIR) as entries:
                for entry in entries:
                    if entry.is_dir():
                        name = entry.name
                        if query_norm in name.lower():
                            results.append({
                                "name": name,
                                "active": name in active_names,
                                "is_core": any(c["name"] == name for c in MANDATORY_CORE_SUITE),
                                "preview": f"Habilidad '{name}' en la bóveda local de SuperDuperSkills."
                            })
                            if len(results) >= limit:
                                return results
        except Exception:
            pass
        return results

    @staticmethod
    def ingest_remote_skill(name_or_url: str, category: str = "INGESTED") -> Tuple[bool, str]:
        """Crea o descarga una skill hacia skills/<nombre>/SKILL.md."""
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

# {clean_name.capitalize()}

Habilidad creada e integrada por el usuario a través del orquestador.
"""
        with open(sk_path, 'w', encoding='utf-8') as f:
            f.write(content.strip() + "\n")
            
        ManifestController.toggle_skill(clean_name, force_state=True)
        return True, f"✨ Skill '{clean_name}' ingerida con éxito en {sk_path} y activada en el manifiesto."

# ==============================================================================
# 🚀 6. MULTI-CLI AGENT SYNCHRONIZER
# ==============================================================================
class MultiCLISync:
    """Sincroniza las skills activas hacia los entornos de los agentes más populares."""
    
    @staticmethod
    def sync_all() -> Dict[str, str]:
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        results = {}
        
        # 1. Cursor Rules Sync (.cursor/rules/superduperskills.mdc)
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

        # 2. Local OpenCode / Claude compatibility file
        opencode_file = os.path.join(AGENTS_DIR, 'opencode-active.json')
        with open(opencode_file, 'w', encoding='utf-8') as f:
            json.dump({
                "source": "superduperskills",
                "active_count": len(active_skills),
                "skills": [s["name"] for s in active_skills]
            }, f, indent=2)
        results["OpenCode & Claude"] = opencode_file
        
        return results

    @staticmethod
    def audit_compliance() -> Dict[str, Any]:
        """Verifica la existencia física de cada SKILL.md en el disco."""
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

# ==============================================================================
# 🎨 7. INTERACTIVE TUI INTERFACE
# ==============================================================================
def print_header(title: str):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"{C.BG_BLUE}{C.WHITE}{C.BOLD} {'=' * 78} {C.RESET}")
    print(f"{C.BG_BLUE}{C.WHITE}{C.BOLD}  🚀 SUPERDUPERSKILLS — CONTROL CENTER & AGENTIC DISCOVERY CLI          {C.RESET}")
    print(f"{C.BG_BLUE}{C.WHITE}{C.BOLD} {'=' * 78} {C.RESET}")
    print(f"{C.CYAN}{C.BOLD}  ► {title}{C.RESET}\n")

def run_interactive_tui():
    """Bucle principal de la interfaz interactiva con menús y opciones completas."""
    while True:
        print_header("MENÚ PRINCIPAL — CENTRO DE COMANDO")
        
        manifest = ManifestController.load_active_manifest()
        active_skills = manifest.get("active_skills", [])
        active_count = len(active_skills)
        
        print(f" {C.GRAY}Espacio de trabajo:{C.RESET} {C.WHITE}{WORKSPACE_DIR}{C.RESET}")
        print(f" {C.GRAY}Skills Activas:{C.RESET} {C.GREEN}{C.BOLD}{active_count} skills{C.RESET} (19 Core Suite + {active_count - 19 if active_count >= 19 else 0} Especializadas)\n")
        
        print(f" {C.BOLD}{C.YELLOW}[ 1 ]{C.RESET} 🔍 {C.BOLD}Deep Project Discovery{C.RESET} (Escanear Stack, Monorepos & Frameworks)")
        print(f" {C.BOLD}{C.YELLOW}[ 2 ]{C.RESET} 🔒 {C.BOLD}Core Invariant Suite{C.RESET} (Ver y verificar las 19 skills obligatorias)")
        print(f" {C.BOLD}{C.YELLOW}[ 3 ]{C.RESET} 🎛️  {C.BOLD}Gestor de Categorías & Toggle 1-a-1{C.RESET} (Activar / Desactivar)")
        print(f" {C.BOLD}{C.YELLOW}[ 4 ]{C.RESET} 🔎 {C.BOLD}Buscador en Bóveda (2,700+ Skills){C.RESET} (Búsqueda en vivo)")
        print(f" {C.BOLD}{C.YELLOW}[ 5 ]{C.RESET} 📥 {C.BOLD}Skill Seekers — Ingestar Nueva Skill{C.RESET} (URL o Nombre Remoto)")
        print(f" {C.BOLD}{C.YELLOW}[ 6 ]{C.RESET} 🔄 {C.BOLD}Sincronizador Multi-CLI{C.RESET} (Cursor, Claude, Gemini, Codex)")
        print(f" {C.BOLD}{C.YELLOW}[ 7 ]{C.RESET} 🧪 {C.BOLD}Auditoría de Cumplimiento Agentico{C.RESET} (Verificar SKILL.md)")
        print(f" {C.BOLD}{C.YELLOW}[ 8 ]{C.RESET} 🧙 {C.BOLD}Lanzar Wizard de Cualificación Completo{C.RESET} (Entrevista Socrática)")
        print(f" {C.BOLD}{C.RED}[ 0 ]{C.RESET} 🚪 {C.BOLD}Salir{C.RESET}\n")
        
        choice = input(f"{C.CYAN}❯ Selecciona una opción [0-8]: {C.RESET}").strip()
        
        if choice == '1':
            view_project_discovery()
        elif choice == '2':
            view_core_suite()
        elif choice == '3':
            view_category_manager()
        elif choice == '4':
            view_vault_search()
        elif choice == '5':
            view_skill_ingestion()
        elif choice == '6':
            view_sync_multicli()
        elif choice == '7':
            view_compliance_audit()
        elif choice == '8':
            import scripts.qualify_project as qp
            qp.run_interactive_wizard()
            input(f"\n{C.GREEN}Presiona ENTER para volver al menú principal...{C.RESET}")
        elif choice == '0' or choice.lower() in ['q', 'exit']:
            print(f"\n{C.GREEN}✨ ¡Sesión de SuperDuperSkills finalizada con éxito!{C.RESET}\n")
            break
        else:
            input(f"\n{C.RED}⚠️ Opción no reconocida. Presiona ENTER para reintentar...{C.RESET}")

def view_project_discovery():
    print_header("DEEP PROJECT DISCOVERY — ESCANEO DE STACK & ARQUITECTURA")
    print(f"{C.GRAY}Analizando estructura del proyecto en {WORKSPACE_DIR}...{C.RESET}\n")
    
    report = ProjectDiscovery.inspect()
    
    print(f" {C.BOLD}📦 Arquitectura:{C.RESET}  {C.CYAN}{report['architecture']}{C.RESET}")
    print(f" {C.BOLD}💻 Lenguajes:{C.RESET}     {C.WHITE}{', '.join(report['languages']) if report['languages'] else 'Agnóstico'}{C.RESET}")
    print(f" {C.BOLD}⚛️  Frameworks:{C.RESET}    {C.GREEN}{', '.join(report['frameworks']) if report['frameworks'] else 'Ninguno detectado'}{C.RESET}")
    print(f" {C.BOLD}🎨 UI & Motion:{C.RESET}   {C.MAGENTA}{', '.join(report['frontend_ui']) if report['frontend_ui'] else 'CSS Estándar'}{C.RESET}")
    print(f" {C.BOLD}⚡ Backend & DB:{C.RESET}  {C.YELLOW}{', '.join(report['backend'] + report['databases']) if (report['backend'] or report['databases']) else 'N/A'}{C.RESET}")
    print(f" {C.BOLD}🚀 DevOps/Infra:{C.RESET}  {C.BLUE}{', '.join(report['devops']) if report['devops'] else 'Sin Docker/CI'}{C.RESET}\n")
    
    if report["recommended_skills"]:
        print(f"{C.BOLD}{C.GREEN}🎯 Skills Recomendadas para este Stack:{C.RESET}")
        for idx, s in enumerate(report["recommended_skills"], 1):
            print(f"   [{idx:02d}] {s}")
        
        print(f"\n{C.CYAN}¿Deseas activar todas las skills recomendadas automáticamente? (s/n){C.RESET}")
        ans = input("❯ ").strip().lower()
        if ans in ['s', 'si', 'y', 'yes']:
            for s in report["recommended_skills"]:
                ManifestController.toggle_skill(s, force_state=True)
            print(f"\n{C.GREEN}✅ ¡Todas las skills recomendadas han sido activadas!{C.RESET}")
    else:
        print(f"{C.GRAY}No hay sugerencias específicas adicionales para este directorio.{C.RESET}")
        
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

def view_core_suite():
    print_header("🔒 SUITE CORE INVARIANTE — 19 SKILLS OBLIGATORIAS")
    print(f"{C.GRAY}Estas habilidades se cargan de forma obligatoria e incondicional en todo proyecto:{C.RESET}\n")
    
    for idx, core in enumerate(MANDATORY_CORE_SUITE, 1):
        path = os.path.join(SKILLS_DIR, core["name"], "SKILL.md")
        status = f"{C.GREEN}[LOCKED CORE & DISPONIBLE]{C.RESET}" if os.path.isfile(path) else f"{C.YELLOW}[LOCKED CORE - PENDIENTE]{C.RESET}"
        print(f"  {C.BOLD}{idx:02d}. {core['name']:<24}{C.RESET} | {core['reason']:<48} {status}")
        
    print(f"\n{C.MAGENTA}ℹ️  Nota: Las skills de la Suite Core están fijadas por gobernanza y no pueden deshabilitarse.{C.RESET}")
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

def view_category_manager():
    while True:
        print_header("🎛️ GESTOR DE CATEGORÍAS & ACTIVACIÓN INDIVIDUAL")
        
        categories = list(CATEGORY_REGISTRY.keys())
        for idx, cat_key in enumerate(categories, 1):
            cat_data = CATEGORY_REGISTRY[cat_key]
            print(f" {C.BOLD}{C.YELLOW}[ {idx} ]{C.RESET} {cat_data['title']} ({len(cat_data['skills'])} skills)")
            
        print(f"\n {C.BOLD}{C.RED}[ 0 ]{C.RESET} ↩️ Volver al menú principal\n")
        
        choice = input(f"{C.CYAN}❯ Selecciona una categoría para explorar [1-{len(categories)}]: {C.RESET}").strip()
        if choice == '0' or choice.lower() in ['q', 'b']:
            break
            
        if choice.isdigit() and 1 <= int(choice) <= len(categories):
            selected_cat_key = categories[int(choice) - 1]
            manage_single_category(selected_cat_key)
        else:
            input(f"\n{C.RED}⚠️ Opción inválida. Presiona ENTER...{C.RESET}")

def manage_single_category(cat_key: str):
    cat_data = CATEGORY_REGISTRY[cat_key]
    
    while True:
        manifest = ManifestController.load_active_manifest()
        active_names = {s["name"] for s in manifest.get("active_skills", [])}
        
        print_header(f"CATEGORÍA: {cat_data['title']}")
        print(f"{C.GRAY}Ingresa el número para alternar (ON/OFF), 'A' para activar todas, o 'D' para desactivar todas:{C.RESET}\n")
        
        for idx, (sk_name, desc) in enumerate(cat_data["skills"], 1):
            is_active = sk_name in active_names
            status_badge = f"{C.GREEN}[ ACTIVADA  ]{C.RESET}" if is_active else f"{C.GRAY}[ INACTIVA  ]{C.RESET}"
            print(f"  {C.BOLD}[{idx:02d}]{C.RESET} {status_badge} {C.BOLD}{sk_name:<28}{C.RESET} | {desc}")
            
        print(f"\n  {C.CYAN}[ A ] Activar todas{C.RESET}  |  {C.YELLOW}[ D ] Desactivar todas{C.RESET}  |  {C.RED}[ 0 ] Volver a categorías{C.RESET}\n")
        
        action = input(f"{C.CYAN}❯ Opción / Número de skill a alternar: {C.RESET}").strip().upper()
        
        if action == '0' or action == 'Q':
            break
        elif action == 'A':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=True)
            print(f"\n{C.GREEN}✅ Todas las skills de la categoría fueron activadas.{C.RESET}")
        elif action == 'D':
            for sk_name, _ in cat_data["skills"]:
                ManifestController.toggle_skill(sk_name, force_state=False)
            print(f"\n{C.YELLOW}⚠️ Todas las skills no-core de la categoría fueron desactivadas.{C.RESET}")
        elif action.isdigit() and 1 <= int(action) <= len(cat_data["skills"]):
            target_skill = cat_data["skills"][int(action) - 1][0]
            success, msg = ManifestController.toggle_skill(target_skill)
            print(f"\n{msg}")
        else:
            print(f"\n{C.RED}Comando no reconocido.{C.RESET}")

def view_vault_search():
    print_header("🔎 BÚSQUEDA EN VIVO EN LA BÓVEDA (2,700+ SKILLS)")
    query = input(f"{C.CYAN}❯ Ingresa término de búsqueda (ej: nextjs, auth, tdd, react, anim): {C.RESET}").strip()
    
    if not query:
        return
        
    print(f"\n{C.GRAY}Buscando en la bóveda local...{C.RESET}\n")
    results = SkillVaultEngine.search_local(query, limit=25)
    
    if not results:
        print(f"{C.YELLOW}No se encontraron skills locales con el término '{query}'.{C.RESET}")
    else:
        print(f"{C.GREEN}Se encontraron {len(results)} coincidencias:{C.RESET}\n")
        for idx, res in enumerate(results, 1):
            badge = f"{C.GREEN}[ACTIVA]{C.RESET}" if res["active"] else f"{C.GRAY}[OFF]{C.RESET}"
            core_badge = f"{C.MAGENTA}[CORE]{C.RESET} " if res["is_core"] else ""
            print(f"  [{idx:02d}] {badge} {core_badge}{C.BOLD}{res['name']:<28}{C.RESET} - {res['preview']}")
            
        print(f"\n{C.CYAN}Ingresa el número de una skill para alternar su estado (o 0 para salir):{C.RESET}")
        ans = input("❯ ").strip()
        if ans.isdigit() and 1 <= int(ans) <= len(results):
            sel = results[int(ans) - 1]
            success, msg = ManifestController.toggle_skill(sel["name"])
            print(f"\n{msg}")
            
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

def view_skill_ingestion():
    print_header("📥 SKILL SEEKERS — INGESTIÓN DE NUEVAS HABILIDADES")
    print(f"{C.GRAY}Puedes ingestar una nueva skill ingresando su URL de GitHub o un identificador único:{C.RESET}\n")
    print(f"  Ejemplo URL: {C.WHITE}https://github.com/autor/mi-nueva-skill{C.RESET}")
    print(f"  Ejemplo Nombre: {C.WHITE}mi-skill-personalizada{C.RESET}\n")
    
    target = input(f"{C.CYAN}❯ Ingresa URL o Nombre de la skill a ingestar: {C.RESET}").strip()
    if not target:
        return
        
    success, msg = SkillVaultEngine.ingest_remote_skill(target)
    print(f"\n{msg}")
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

def view_sync_multicli():
    print_header("🔄 SINCRONIZADOR MULTI-CLI & CONFIGURACIÓN DE AGENTES")
    print(f"{C.GRAY}Sincronizando manifiesto activo hacia entornos compatibles (Cursor, Claude, Gemini, Codex)...{C.RESET}\n")
    
    synced = MultiCLISync.sync_all()
    for agent_host, path in synced.items():
        print(f"  {C.GREEN}✓{C.RESET} {agent_host:<20} ➔ {C.CYAN}{path}{C.RESET}")
        
    print(f"\n{C.GREEN}✨ ¡Manifiestos y reglas de agentes sincronizados correctamente!{C.RESET}")
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

def view_compliance_audit():
    print_header("🧪 AUDITORÍA DE CUMPLIMIENTO AGENTICO")
    print(f"{C.GRAY}Verificando la integridad física de las skills activadas en .agents/ACTIVE-SKILLS.json...{C.RESET}\n")
    
    audit = MultiCLISync.audit_compliance()
    
    print(f"  • Total de skills activadas: {C.WHITE}{audit['total_active']}{C.RESET}")
    print(f"  • Archivos SKILL.md presentes: {C.GREEN}{audit['found_count']}{C.RESET}")
    print(f"  • Archivos faltantes: {C.RED if audit['missing_count'] > 0 else C.GREEN}{audit['missing_count']}{C.RESET}\n")
    
    if audit['missing_count'] > 0:
        print(f"{C.RED}⚠️ Skills activas sin archivo SKILL.md físico en skills/:{C.RESET}")
        for m in audit['missing_skills']:
            print(f"    - {m}")
    else:
        print(f"{C.GREEN}✅ 100% de las skills activas están presentes y listas para ser invocadas con `view_file`.{C.RESET}")
        
    input(f"\n{C.GREEN}Presiona ENTER para continuar...{C.RESET}")

# ==============================================================================
# 💻 8. CLI ARGUMENT PARSER (NON-INTERACTIVE AUTOMATION)
# ==============================================================================
def main():
    parser = argparse.ArgumentParser(
        description="SuperDuperSkills Agentic CLI & Discovery Control Center",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Comando a ejecutar")
    
    # scan
    subparsers.add_parser("scan", help="Escanear stack del proyecto y recomendar skills")
    
    # list
    subparsers.add_parser("list", help="Listar skills activas del proyecto")
    
    # toggle
    p_toggle = subparsers.add_parser("toggle", help="Alternar estado de una skill (ON/OFF)")
    p_toggle.add_argument("skill_name", type=str, help="Nombre de la skill")
    
    # search
    p_search = subparsers.add_parser("search", help="Buscar en la bóveda de skills")
    p_search.add_argument("query", type=str, help="Término de búsqueda")
    
    # ingest
    p_ingest = subparsers.add_parser("ingest", help="Ingestar skill remota o crearla")
    p_ingest.add_argument("source", type=str, help="URL o Nombre de la skill")
    
    # sync
    subparsers.add_parser("sync", help="Sincronizar configuraciones Multi-CLI")
    
    # audit
    subparsers.add_parser("audit", help="Auditar cumplimiento y presencia de SKILL.md")
    
    # wizard
    subparsers.add_parser("wizard", help="Lanzar wizard socrático de cualificación")
    
    args = parser.parse_args()
    
    if args.command is None:
        # Launch Interactive TUI by default
        run_interactive_tui()
    elif args.command == "scan":
        r = ProjectDiscovery.inspect()
        print(json.dumps(r, indent=2, ensure_ascii=False))
    elif args.command == "list":
        m = ManifestController.load_active_manifest()
        for s in m.get("active_skills", []):
            print(f"- {s['name']} [{s.get('category', 'CUSTOM')}]: {s.get('reason', '')}")
    elif args.command == "toggle":
        ok, msg = ManifestController.toggle_skill(args.skill_name)
        print(msg)
    elif args.command == "search":
        res = SkillVaultEngine.search_local(args.query)
        for r in res:
            status = "[ACTIVA]" if r["active"] else "[INACTIVA]"
            print(f"{status} {r['name']} - {r['preview']}")
    elif args.command == "ingest":
        ok, msg = SkillVaultEngine.ingest_remote_skill(args.source)
        print(msg)
    elif args.command == "sync":
        synced = MultiCLISync.sync_all()
        for k, v in synced.items():
            print(f"Synced {k} -> {v}")
    elif args.command == "audit":
        audit = MultiCLISync.audit_compliance()
        print(json.dumps(audit, indent=2))
    elif args.command == "wizard":
        import scripts.qualify_project as qp
        qp.run_interactive_wizard()

if __name__ == '__main__':
    main()
