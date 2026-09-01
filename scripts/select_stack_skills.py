#!/usr/bin/env python3
"""
Stack-Based Skill Selector for SuperDuperSkills
Analyzes project stack and maps recommended skills with clear rationale:
- WHAT the skill does
- WHY it fits this specific technology stack
"""

import os
import json
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def detect_stack(workspace_dir):
    stack = {
        'core': ['caveman', 'ponytail', 'spec-kit', 'token-savings', 'harness', 'claude-mem', 'rtk', 'graphify'],
        'frontend': [],
        'backend': [],
        'database': [],
        'devops': [],
        'security': [],
        'growth': []
    }
    
    # Check for frontend
    pkg_path = os.path.join(workspace_dir, 'package.json')
    if os.path.isfile(pkg_path):
        try:
            with open(pkg_path, 'r', encoding='utf-8') as f:
                pkg = json.load(f)
                deps = {**pkg.get('dependencies', {}), **pkg.get('devDependencies', {})}
                if 'react' in deps:
                    stack['frontend'].append('react-patterns')
                if 'next' in deps:
                    stack['frontend'].append('nextjs-developer')
                if 'tailwindcss' in deps or '@tailwindcss/vite' in deps:
                    stack['frontend'].append('tailwind-theme-builder')
                if 'express' in deps or 'fastify' in deps:
                    stack['backend'].append('nodejs-backend-patterns')
        except Exception:
            pass

    # Check for Python / Backend
    req_path = os.path.join(workspace_dir, 'requirements.txt')
    pyproject_path = os.path.join(workspace_dir, 'pyproject.toml')
    if os.path.isfile(req_path) or os.path.isfile(pyproject_path):
        stack['backend'].append('python-expert')

    # Check for Go
    if os.path.isfile(os.path.join(workspace_dir, 'go.mod')):
        stack['backend'].append('golang-pro')

    # Check for DevOps / Docker / Cloudflare
    if os.path.isfile(os.path.join(workspace_dir, 'Dockerfile')) or os.path.isfile(os.path.join(workspace_dir, 'docker-compose.yml')):
        stack['devops'].append('docker-patterns')
    if os.path.isfile(os.path.join(workspace_dir, 'wrangler.toml')) or os.path.isfile(os.path.join(workspace_dir, 'wrangler.json')):
        stack['devops'].append('cloudflare-worker-builder')

    # Always add quality & security defaults
    stack['security'].append('cybersecurity')
    stack['growth'].append('humanizer')
    
    return stack

def print_stack_matrix(stack):
    print("=" * 80)
    print(" 🛠️  SUPERDUPERSKILLS — STACK-BASED SKILL SELECTION MATRIX")
    print("=" * 80)
    
    SKILL_EXPLANATIONS = {
        'caveman': ('Output Compression (-75%)', 'Reduces verbose agent responses while keeping technical precision.'),
        'ponytail': ('YAGNI & Simplicity', 'Enforces minimal code diffs and stdlib-first solutions.'),
        'spec-kit': ('Spec-Driven Dev', 'Structures specifications, PRDs, and task breakdowns before coding.'),
        'token-savings': ('Context Saver', 'Confirms explicit skills per project to keep prompt metadata lean.'),
        'harness': ('Test Harness', 'Ensures automated test verification loops before completion.'),
        'claude-mem': ('Persistent Memory', 'Remembers architectural decisions across turns and sessions.'),
        'rtk': ('Terminal Log Filter', 'Compresses git diff, test, and build outputs by 60-90%.'),
        'graphify': ('Codebase Knowledge Graph', 'Indexes symbols & callers to answer dependency queries without reloading 40+ files.'),
        'react-patterns': ('React 19 & Component Architecture', 'Optimizes re-renders and component composition.'),
        'nextjs-developer': ('Next.js App Router', 'Handles Server Components, Server Actions, and SSR patterns.'),
        'tailwind-theme-builder': ('Tailwind Styling', 'Configures accessible design tokens and utility classes.'),
        'nodejs-backend-patterns': ('Node.js Server Design', 'Implements resilient REST/GraphQL APIs and middleware.'),
        'python-expert': ('Pythonic Architecture', 'Enforces type hints, async patterns, and clean code.'),
        'golang-pro': ('Go Microservices', 'High-concurrency, idiomatic Go routines and interfaces.'),
        'docker-patterns': ('Containerization', 'Optimizes multi-stage Docker builds and security layers.'),
        'cloudflare-worker-builder': ('Edge Computing', 'Deploys Workers, D1 DB, R2 storage, and Durable Objects.'),
        'cybersecurity': ('Threat Auditing', 'Scans for OWASP, secrets, and security vulnerabilities.'),
        'humanizer': ('AI Tone De-Slop', 'Rewrites prose to eliminate artificial AI writing markers.'),
        'agentic-os': ('Multi-Agent OS Architecture', 'Structures persistent kernel, subagents, and slash commands.'),
        'ai-ready': ('Repo AI Onboarding', 'Generates AGENTS.md, copilot instructions, and CI templates.'),
        'agent-watchdog': ('Agent Transcript Audit', 'Audits and corrects background subagent runs.'),
        'ai-slop-cleaner': ('Deletion-First Refactoring', 'Removes AI-generated code slop and dead fallbacks.'),
        'ai-sdk': ('Vercel AI SDK', 'Generates generateText, streamText, and useChat hooks.'),
        'animate': ('Web Motion Framework', 'Decides UI spring physics, Framer Motion, and timing.'),
        'apple-design': ('Apple HIG Fluid Motion', 'Translates Apple HIG fluid spring physics for web.'),
        'anti-ui-slop': ('Anti-Generic UI', 'Prevents AI from shipping generic Tailwind/Bootstrap UI.'),
        'api-design': ('REST API Design Standards', 'Enforces cursor pagination, error envelopes, and HTTP specs.'),
        'architecture-decision-records': ('ADR Generator', 'Records architectural decisions into doc/adr/.'),
        'autoplan': ('Multi-Perspective Auto Review', 'Sequential CEO/Design/Eng/DX review pipeline.'),
        'c4-architecture': ('C4 Model Diagrams', 'Generates C4 Context/Container/Component Mermaid diagrams.'),
        'bun-runtime': ('Bun Toolkit', 'High-performance runtime, test runner, and package manager.'),
        'clickhouse-io': ('ClickHouse Analytics', 'OLAP column-oriented database patterns & MergeTree optimization.'),
        'baoyu-diagram': ('Dark Vector Diagrams', 'Renders dark-themed SVG architecture & flowchart diagrams.')
    }

    for category, skills in stack.items():
        if not skills:
            continue
        print(f"\n📂 CATEGORY: {category.upper()}")
        print("-" * 80)
        for skill in skills:
            title, reason = SKILL_EXPLANATIONS.get(skill, ('General Skill', 'Recomendado para la arquitectura.'))
            print(f"  • {skill:<25} | {title:<32} | Why: {reason}")
    print("\n" + "=" * 80)

if __name__ == '__main__':
    target_dir = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    stack = detect_stack(target_dir)
    print_stack_matrix(stack)
