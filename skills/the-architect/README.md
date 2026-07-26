<p align="center">
  <h1 align="center">The Architect</h1>
  <p align="center">
    <strong>A Claude Code meta-agent that designs complete software blueprints.</strong>
  </p>
  <p align="center">
    Describe what you want to build. Get a complete blueprint. Let Claude Code build it for you.
  </p>
  <p align="center">
    <a href="https://tododeia.com">tododeia.com</a> &middot;
    <a href="#english">English</a> &middot;
    <a href="#español">Español</a>
  </p>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Claude_Code-Agent-blueviolet?style=for-the-badge" alt="Claude Code Agent" />
  <img src="https://img.shields.io/badge/Blueprints-Markdown-blue?style=for-the-badge" alt="Markdown Blueprints" />
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="MIT License" />
  <img src="https://img.shields.io/badge/by-tododeia.com-black?style=for-the-badge" alt="by tododeia.com" />
</p>

---

# English

## What is The Architect?

Imagine you want to build a house. Before anyone picks up a hammer, you need a **blueprint** — a detailed plan that shows every room, every wall, every pipe, and every wire. Without it, the builders wouldn't know what to do.

**The Architect does this for software.**

You open this project in [Claude Code](https://claude.com/claude-code), tell it what you want to build (a website, an app, a SaaS, an API — anything), and The Architect:

1. **Asks you smart questions** about your idea
2. **Designs the entire system** — database, API, frontend, auth, payments, everything
3. **Generates a blueprint file** (`.md`) so detailed that another Claude Code instance can build the whole thing — step by step, without asking you anything

Think of it like this:

```
You: "I want to build a project management app like Trello"
         ↓
The Architect: asks questions, designs everything
         ↓
Blueprint.md: complete plan with tech stack, database schema,
              API routes, component hierarchy, build order...
         ↓
Claude Code: reads the blueprint → builds the entire app
```

**You describe the idea. The Architect creates the plan. Claude Code builds it.**

---

## How It Works

The Architect follows a 4-phase workflow:

### Phase 1: Discovery
> "What are you building? Who is it for? How big should it be?"

The Architect asks 2-3 questions to understand your idea. Based on your answers, it classifies your project into one of **6 archetypes** (project types).

### Phase 2: Deep Dive
> "Do you need user accounts? Payments? Real-time features?"

Now it asks questions specific to YOUR type of project. It also researches best practices using skills like `/deep-research`.

### Phase 3: Architecture
> "Here's what I'd build: Next.js + Supabase + Clerk + Stripe on Vercel..."

The Architect presents the complete tech stack and architecture with reasons for every decision. You confirm or adjust. For frontend projects, it designs a full visual system (colors, fonts, spacing) using `/ui-ux-pro-max`.

### Phase 4: Generate
The Architect produces the final blueprint — a single `.md` file with **16 sections** covering everything Claude Code needs to build your project from zero to deployed.

---

## The Blueprint: 16 Sections

Every blueprint The Architect generates includes:

| # | Section | What It Contains |
|---|---------|-----------------|
| 1 | Project Overview | Vision, goals, success metrics |
| 2 | Tech Stack | Every technology with rationale |
| 3 | Directory Structure | Full file tree with explanations |
| 4 | Data Model | Entities, fields, relationships, SQL schema |
| 5 | API Design | Routes, endpoints, request/response shapes |
| 6 | Frontend Architecture | Pages, components, state management |
| 7 | Design System | Colors, fonts, spacing, component style |
| 8 | Auth & Authorization | Login flow, roles, permissions |
| 9 | **Build Order** | Step-by-step: what to build first, second, third... |
| 10 | Environment Setup | Prerequisites, env vars, initial commands |
| 11 | Dependencies | Every package with its purpose |
| 12 | Deployment | Hosting, CI/CD, domains |
| 13 | Testing | What to test, which tools, when |
| 14 | Skills to Use | Which Claude Code skills help during the build |
| 15 | **CLAUDE.md** | Complete instructions for the builder — ready to paste |
| 16 | Rules | Non-negotiable constraints for the build |

**Section 9 (Build Order) is the most important.** It tells Claude Code exactly what to build and in what order — so it can work autonomously without asking you questions.

---

## Supported Project Types

The Architect knows how to design **6 types of projects**, each with its own default stack, directory structure, and build order:

| Type | Examples | Default Stack |
|------|----------|--------------|
| **SaaS / Web App** | Trello, Notion, Slack | Next.js + Supabase + Clerk + Stripe + Vercel |
| **Marketing Site** | Landing pages, portfolios | Astro + Tailwind + Sanity + Vercel |
| **Mobile App** | iOS/Android apps | Expo (React Native) + Supabase + NativeWind |
| **API / Backend** | REST APIs, microservices | Hono + Drizzle + PostgreSQL + Railway |
| **Internal Tool** | Admin panels, dashboards | Next.js + shadcn/ui + Prisma + Recharts |
| **Content Platform** | Blogs, docs, CMS | Next.js + Sanity + Algolia + Vercel |

Don't see your project type? The Architect adapts — these are starting points, not limits.

---

## Quick Start

### Prerequisites

- [Claude Code](https://claude.com/claude-code) installed
- A Claude API subscription

### Installation

```bash
# Clone this repo
git clone https://github.com/Hainrixz/the-architect.git

# Open the project in Claude Code
cd the-architect
claude
```

That's it. Claude Code reads the `CLAUDE.md` file and becomes The Architect.

### Usage

**Step 1:** Tell The Architect what you want to build:

```
You: I want to build a SaaS for managing restaurant reservations
     with team accounts, Stripe payments, and a customer-facing booking page.
```

**Step 2:** Answer the questions (2-3 at a time, conversational).

**Step 3:** Review the proposed architecture. Confirm or adjust.

**Step 4:** The Architect generates your blueprint at `output/<project-name>-blueprint.md`.

**Step 5:** Use the blueprint to build your project:

```bash
# Create your new project
mkdir ~/my-restaurant-saas
cp output/restaurant-saas-blueprint.md ~/my-restaurant-saas/CLAUDE.md

# Open it in Claude Code — it builds everything from the blueprint
cd ~/my-restaurant-saas
claude
```

### Fast-Track Mode

Don't want to answer many questions? Say:

```
You: Build me a SaaS for restaurant reservations. Just build it.
```

The Architect asks only 3 essential questions and uses smart defaults for everything else.

---

## Project Structure

```
the-architect/
├── CLAUDE.md                          # The brain — makes Claude become The Architect
├── knowledge/
│   ├── archetypes/                    # 6 project type templates
│   │   ├── saas-webapp.md             #   SaaS apps
│   │   ├── marketing-site.md          #   Landing pages
│   │   ├── mobile-app.md              #   Mobile apps
│   │   ├── api-backend.md             #   APIs & backends
│   │   ├── internal-tool.md           #   Admin panels
│   │   └── content-platform.md        #   Blogs & CMS
│   ├── building-blocks/               # 8 cross-cutting decision guides
│   │   ├── auth-patterns.md           #   Authentication options
│   │   ├── database-patterns.md       #   Database & ORM choices
│   │   ├── deployment-patterns.md     #   Hosting & CI/CD
│   │   ├── api-design-patterns.md     #   REST vs tRPC vs GraphQL
│   │   ├── frontend-stacks.md         #   Framework comparisons
│   │   ├── testing-patterns.md        #   Testing strategies
│   │   ├── styling-systems.md         #   CSS & design tokens
│   │   └── state-management.md        #   State & real-time patterns
│   ├── skills-registry.md             # Maps Claude Code skills to blueprint sections
│   └── stack-compatibility.md         # What works together (and what doesn't)
├── templates/
│   ├── blueprint-template.md          # The 16-section output skeleton
│   └── claude-md-template.md          # Template for the target project's CLAUDE.md
├── questions/
│   ├── phase-1-discovery.md           # Universal discovery questions
│   ├── phase-2-branches.md            # Archetype-specific deep dives
│   └── phase-3-confirmation.md        # Architecture confirmation
└── output/                            # Generated blueprints go here
```

---

## Skills Integration

The Architect leverages Claude Code skills during the design process:

| Skill | Used For |
|-------|----------|
| `/deep-research` | Researching technologies and best practices |
| `/ui-ux-pro-max` | Designing visual systems (colors, fonts, spacing) |
| `/find-skills` | Discovering skills to recommend for the build phase |
| `/playwright-cli` | Analyzing reference sites |

And recommends skills for the **build phase** in the blueprint:

| Skill | Recommended For |
|-------|----------------|
| `/frontend-design` | Building production-grade UIs |
| `/shadcn-ui` | Setting up component libraries |
| `/seo-audit` | SEO auditing after build |
| `/humanizer` | Making content sound natural |

---

## Contributing

Contributions are welcome! You can help by:

- **Adding new archetypes** — new project types in `knowledge/archetypes/`
- **Improving building blocks** — better decision matrices, newer tech options
- **Enhancing the blueprint template** — more sections, better structure
- **Translating** — help make The Architect accessible in more languages

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

## Built by [tododeia.com](https://tododeia.com)

---
---

# Español

## Que es The Architect?

Imagina que quieres construir una casa. Antes de que alguien agarre un martillo, necesitas un **plano** — un plan detallado que muestre cada cuarto, cada pared, cada tuberia y cada cable. Sin el, los constructores no sabrian que hacer.

**The Architect hace esto para software.**

Abres este proyecto en [Claude Code](https://claude.com/claude-code), le dices que quieres construir (un sitio web, una app, un SaaS, una API — lo que sea), y The Architect:

1. **Te hace preguntas inteligentes** sobre tu idea
2. **Diseña todo el sistema** — base de datos, API, frontend, autenticacion, pagos, todo
3. **Genera un archivo blueprint** (`.md`) tan detallado que otra instancia de Claude Code puede construir todo — paso a paso, sin preguntarte nada

Piensalo asi:

```
Tu: "Quiero construir una app de gestion de proyectos como Trello"
         ↓
The Architect: hace preguntas, diseña todo
         ↓
Blueprint.md: plan completo con tech stack, esquema de base de datos,
              rutas API, jerarquia de componentes, orden de construccion...
         ↓
Claude Code: lee el blueprint → construye toda la app
```

**Tu describes la idea. The Architect crea el plano. Claude Code lo construye.**

---

## Como Funciona

The Architect sigue un flujo de 4 fases:

### Fase 1: Descubrimiento
> "Que estas construyendo? Para quien es? Que tan grande debe ser?"

The Architect hace 2-3 preguntas para entender tu idea. Con tus respuestas, clasifica tu proyecto en uno de **6 arquetipos** (tipos de proyecto).

### Fase 2: Profundizacion
> "Necesitas cuentas de usuario? Pagos? Funciones en tiempo real?"

Ahora hace preguntas especificas para TU tipo de proyecto. Tambien investiga mejores practicas usando skills como `/deep-research`.

### Fase 3: Arquitectura
> "Esto es lo que yo construiria: Next.js + Supabase + Clerk + Stripe en Vercel..."

The Architect presenta el tech stack completo y la arquitectura con razones para cada decision. Tu confirmas o ajustas. Para proyectos con frontend, diseña un sistema visual completo (colores, fuentes, espaciado) usando `/ui-ux-pro-max`.

### Fase 4: Generar
The Architect produce el blueprint final — un solo archivo `.md` con **16 secciones** cubriendo todo lo que Claude Code necesita para construir tu proyecto de cero a desplegado.

---

## El Blueprint: 16 Secciones

Cada blueprint que The Architect genera incluye:

| # | Seccion | Que Contiene |
|---|---------|-------------|
| 1 | Vision del Proyecto | Vision, objetivos, metricas de exito |
| 2 | Tech Stack | Cada tecnologia con su razon |
| 3 | Estructura de Directorios | Arbol completo de archivos con explicaciones |
| 4 | Modelo de Datos | Entidades, campos, relaciones, esquema SQL |
| 5 | Diseño de API | Rutas, endpoints, formas de request/response |
| 6 | Arquitectura Frontend | Paginas, componentes, manejo de estado |
| 7 | Sistema de Diseño | Colores, fuentes, espaciado, estilo de componentes |
| 8 | Auth y Autorizacion | Flujo de login, roles, permisos |
| 9 | **Orden de Construccion** | Paso a paso: que construir primero, segundo, tercero... |
| 10 | Setup del Entorno | Prerequisitos, variables de entorno, comandos iniciales |
| 11 | Dependencias | Cada paquete con su proposito |
| 12 | Despliegue | Hosting, CI/CD, dominios |
| 13 | Testing | Que testear, que herramientas, cuando |
| 14 | Skills a Usar | Que skills de Claude Code ayudan durante la construccion |
| 15 | **CLAUDE.md** | Instrucciones completas para el constructor — listo para pegar |
| 16 | Reglas | Restricciones no negociables para la construccion |

**La Seccion 9 (Orden de Construccion) es la mas importante.** Le dice a Claude Code exactamente que construir y en que orden — para que pueda trabajar autonomamente sin hacerte preguntas.

---

## Tipos de Proyecto Soportados

The Architect sabe diseñar **6 tipos de proyectos**, cada uno con su stack por defecto, estructura de directorios y orden de construccion:

| Tipo | Ejemplos | Stack por Defecto |
|------|----------|------------------|
| **SaaS / Web App** | Trello, Notion, Slack | Next.js + Supabase + Clerk + Stripe + Vercel |
| **Sitio de Marketing** | Landing pages, portafolios | Astro + Tailwind + Sanity + Vercel |
| **App Movil** | Apps iOS/Android | Expo (React Native) + Supabase + NativeWind |
| **API / Backend** | REST APIs, microservicios | Hono + Drizzle + PostgreSQL + Railway |
| **Herramienta Interna** | Paneles admin, dashboards | Next.js + shadcn/ui + Prisma + Recharts |
| **Plataforma de Contenido** | Blogs, docs, CMS | Next.js + Sanity + Algolia + Vercel |

No ves tu tipo de proyecto? The Architect se adapta — estos son puntos de partida, no limites.

---

## Inicio Rapido

### Prerequisitos

- [Claude Code](https://claude.com/claude-code) instalado
- Una suscripcion a la API de Claude

### Instalacion

```bash
# Clona este repo
git clone https://github.com/Hainrixz/the-architect.git

# Abre el proyecto en Claude Code
cd the-architect
claude
```

Eso es todo. Claude Code lee el archivo `CLAUDE.md` y se convierte en The Architect.

### Uso

**Paso 1:** Dile a The Architect que quieres construir:

```
Tu: Quiero construir un SaaS para manejar reservaciones de restaurante
    con cuentas de equipo, pagos con Stripe, y una pagina de reservas para clientes.
```

**Paso 2:** Responde las preguntas (2-3 a la vez, conversacional).

**Paso 3:** Revisa la arquitectura propuesta. Confirma o ajusta.

**Paso 4:** The Architect genera tu blueprint en `output/<nombre-proyecto>-blueprint.md`.

**Paso 5:** Usa el blueprint para construir tu proyecto:

```bash
# Crea tu nuevo proyecto
mkdir ~/mi-saas-restaurante
cp output/restaurant-saas-blueprint.md ~/mi-saas-restaurante/CLAUDE.md

# Abrelo en Claude Code — construye todo desde el blueprint
cd ~/mi-saas-restaurante
claude
```

### Modo Rapido

No quieres responder muchas preguntas? Di:

```
Tu: Hazme un SaaS para reservaciones de restaurante. Solo construyelo.
```

The Architect hace solo 3 preguntas esenciales y usa valores por defecto inteligentes para todo lo demas.

---

## Estructura del Proyecto

```
the-architect/
├── CLAUDE.md                          # El cerebro — hace que Claude se convierta en The Architect
├── knowledge/
│   ├── archetypes/                    # 6 plantillas por tipo de proyecto
│   │   ├── saas-webapp.md             #   Apps SaaS
│   │   ├── marketing-site.md          #   Landing pages
│   │   ├── mobile-app.md              #   Apps moviles
│   │   ├── api-backend.md             #   APIs y backends
│   │   ├── internal-tool.md           #   Paneles admin
│   │   └── content-platform.md        #   Blogs y CMS
│   ├── building-blocks/               # 8 guias de decisiones transversales
│   │   ├── auth-patterns.md           #   Opciones de autenticacion
│   │   ├── database-patterns.md       #   Bases de datos y ORMs
│   │   ├── deployment-patterns.md     #   Hosting y CI/CD
│   │   ├── api-design-patterns.md     #   REST vs tRPC vs GraphQL
│   │   ├── frontend-stacks.md         #   Comparacion de frameworks
│   │   ├── testing-patterns.md        #   Estrategias de testing
│   │   ├── styling-systems.md         #   CSS y design tokens
│   │   └── state-management.md        #   Estado y patrones real-time
│   ├── skills-registry.md             # Mapea skills de Claude Code a secciones del blueprint
│   └── stack-compatibility.md         # Que funciona junto (y que no)
├── templates/
│   ├── blueprint-template.md          # El esqueleto de las 16 secciones
│   └── claude-md-template.md          # Template para el CLAUDE.md del proyecto destino
├── questions/
│   ├── phase-1-discovery.md           # Preguntas universales de descubrimiento
│   ├── phase-2-branches.md            # Profundizacion por arquetipo
│   └── phase-3-confirmation.md        # Confirmacion de arquitectura
└── output/                            # Los blueprints generados van aqui
```

---

## Integracion de Skills

The Architect usa skills de Claude Code durante el proceso de diseño:

| Skill | Se Usa Para |
|-------|-------------|
| `/deep-research` | Investigar tecnologias y mejores practicas |
| `/ui-ux-pro-max` | Diseñar sistemas visuales (colores, fuentes, espaciado) |
| `/find-skills` | Descubrir skills para recomendar en la fase de construccion |
| `/playwright-cli` | Analizar sitios de referencia |

Y recomienda skills para la **fase de construccion** en el blueprint:

| Skill | Recomendado Para |
|-------|-----------------|
| `/frontend-design` | Construir UIs de grado produccion |
| `/shadcn-ui` | Configurar librerias de componentes |
| `/seo-audit` | Auditoria SEO despues de construir |
| `/humanizer` | Hacer que el contenido suene natural |

---

## Contribuir

Las contribuciones son bienvenidas! Puedes ayudar con:

- **Agregar nuevos arquetipos** — nuevos tipos de proyecto en `knowledge/archetypes/`
- **Mejorar building blocks** — mejores matrices de decision, opciones de tech mas nuevas
- **Mejorar el template del blueprint** — mas secciones, mejor estructura
- **Traducir** — ayuda a hacer The Architect accesible en mas idiomas

---

## Licencia

Licencia MIT. Ver [LICENSE](LICENSE) para detalles.

---

## Construido por [tododeia.com](https://tododeia.com)
