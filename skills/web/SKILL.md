---
name: web
description: >
  Builds a complete website using visual assets generated with Forkads
  (saved in assets/) and a brief written in content/brief.md. Use when the
  user writes "/web" or says "read the web skill and build the site with
  my assets". Produces a mobile-first, animation-polished static site
  (plain HTML/CSS/JS, no framework) with GSAP/ScrollTrigger, Lenis smooth
  scroll, and Swiper galleries loaded via CDN.
---

# /web — Forkads asset-to-website builder

## Regla de idioma

Responde siempre en el mismo idioma en el que escribe el usuario.

## Pasos a seguir

### 1. LEER CONTEXTO

- Lee `content/brief.md`: de qué trata el sitio, secciones y tono.
- Lista todos los archivos en `assets/` y clasifícalos: video/imagen hero,
  fotos de producto, logo, extras.

### 2. PLANEAR

- Propón la estructura sección por sección (hero, beneficios, galería,
  prueba social, CTA final, footer).
- Espera el OK del usuario antes de escribir código.

### 3. CONSTRUIR

- Crea el sitio dentro de `site/` (`index.html` + `styles.css` + `main.js`).
- El hero usa el asset principal de Forkads: video → muted, loop,
  playsinline / imagen → fondo a todo el ancho.
- Mobile-first y rápido — HTML/CSS/JS plano, sin frameworks pesados.
- Anima con librerías best-in-class, cargadas vía CDN:
  - **GSAP + ScrollTrigger** → reveals al hacer scroll, pinning, parallax.
  - **Lenis** → scroll suave.
  - **Swiper** → sliders y galerías cuando el brief lo pida.
- Mantén el movimiento premium y sutil: reveals de fade + translate,
  parallax ligero en el hero, respeta `prefers-reduced-motion`.

### 4. VERIFICAR

- Explica cómo abrir el sitio localmente para previsualizarlo.
- Lista todos los archivos creados con su ruta.
- Sugiere 2-3 ideas concretas para la siguiente iteración.
