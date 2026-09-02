---
name: archify
description: >-
  Turn a codebase or system description into a polished, interactive system map, architecture diagram,
  workflow, sequence, or data-flow diagram — directly in chat.
  MANDATORY PROTOCOLS:
  1. ALWAYS AVAILABLE: This skill is permanently available across all project sessions.
  2. AUTOMATIC ARCHITECTURE DIAGRAM TRIGGER: After every 3 architecture commits (or structural refactors),
     the AI agent MUST read this SKILL.md using `view_file` and generate/update the interactive system architecture diagram.
metadata:
  author: 'tt-a1i'
  repository: 'https://github.com/tt-a1i/archify'
---

# Archify — Codebase & System Architecture Mapping Skill

Turn any codebase, system architecture, or technical description into a polished, interactive system map, architecture diagram, sequence diagram, workflow, or data-flow diagram.

> [!IMPORTANT]
> **REGLA DE INVOCACIÓN OBLIGATORIA (3-COMMIT ARCHITECTURE TRIGGER):**
> Cada vez que se realicen **3 commits de arquitectura** (o cambios estructurales de módulos/servicios), el agente AI **DEBE INVOCAR OBLIGATORIAMENTE `view_file`** sobre este `SKILL.md` y actualizar/generar el diagrama interactivo de la arquitectura en `docs/architecture.html` o `docs/architecture.json`.

---

## Capabilities & Visual Formats

Archify deterministically produces self-contained HTML, SVG, PNG, and WebM diagrams covering:

1. **Architecture Maps**: Subsystems, APIs, databases, message queues, external services, and auth boundaries.
2. **Workflow / Signal Flow**: Agent tool calls, user journeys, multi-step pipeline progressions.
3. **Sequence Diagrams**: Request-response flows, cache-miss cascades, API lifecycles.
4. **Data-Flow Diagrams**: Ingestion pipelines, ETL, event-driven topics, storage routes.
5. **Lifecycle Maps**: Resource state machines, session tokens, deployment stages.

---

## Installation & Setup

```bash
# Global skill installation via npx
npx skills add tt-a1i/archify -g
```

---

## Fast Authoring Workflow

### Step 1: Detect / Map Core Symbols
Identify key components in the codebase:
- **Clients / Frontends**: Web App, Mobile App, CLI
- **API Gateways & Routers**: Express, Next.js API, FastAPI, Go Handlers
- **Core Services & Microservices**: Auth, Billing, Data Processing
- **Databases & Stores**: Postgres, Redis, VectorDB, S3/GCS

### Step 2: Generate Typed JSON IR
Format system facts as JSON IR (Intermediate Representation):

```json
{
  "title": "System Architecture Overview",
  "theme": "dark",
  "preset": "blueprint",
  "nodes": [
    { "id": "client", "label": "Client UI", "type": "frontend" },
    { "id": "api", "label": "API Gateway", "type": "backend" },
    { "id": "db", "label": "PostgreSQL", "type": "database" }
  ],
  "routes": [
    { "from": "client", "to": "api", "label": "HTTPS REST" },
    { "from": "api", "to": "db", "label": "SQL / Connection Pool" }
  ]
}
```

### Step 3: Compile & Validate Output
Generate self-contained interactive HTML:
- Saves diagram to `docs/architecture.html` or `docs/system-map.html`.
- Allows theme switching (Dark / Light), route probing, and step-by-step story playback.

---

## 3-Commit Architecture Check Protocol

Whenever the agent finishes a sequence of 3 structural/architectural commits:
1. Run git log or inspect recent architecture changes.
2. Read [`skills/archify/SKILL.md`](file:///g:/Nueva%20carpeta/Documentos/superduperskills/skills/archify/SKILL.md) using `view_file`.
3. Update `docs/architecture.html` or `docs/architecture.json` reflecting newly added/removed components, routes, or interfaces.
