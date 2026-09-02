---
name: gsap-framer-scroll-animation
description: >-
  Use this skill whenever the user wants to build scroll animations, scroll effects,
  parallax, scroll-triggered reveals, pinned sections, horizontal scroll, text animations,
  or any motion tied to scroll position — in vanilla JS, React, or Next.js.
  Covers GSAP ScrollTrigger (pinning, scrubbing, snapping, timelines, horizontal scroll,
  ScrollSmoother, matchMedia) and Framer Motion / Motion v12 (useScroll, useTransform,
  useSpring, whileInView, variants). Use this skill even if the user just says
  "animate on scroll", "fade in as I scroll", "make it scroll like Apple",
  "parallax effect", "sticky section", "scroll progress bar", or "entrance animation".
  Also triggers for Copilot prompt patterns for GSAP or Framer Motion code generation.
  Pairs with the premium-frontend-ui skill for creative philosophy and design-level polish.
metadata:
  author: 'Utkarsh Patrikar'
  author_url: 'https://github.com/utkarsh232005'
---

# GSAP & Framer Motion — Scroll Animations Skill

Production-grade scroll animations with GitHub Copilot prompts, ready-to-use code recipes, and deep API references.

> **Design Companion:** This skill provides the *technical implementation* for scroll-driven motion.
> For the *creative philosophy*, design principles, and premium aesthetics that should guide **how**
> and **when** to animate, always cross-reference the **premium-frontend-ui** skill.
> Together they form a complete approach: premium-frontend-ui decides the **what** and **why**;
> this skill delivers the **how**.

## Quick Library Selector

| Need | Use |
|---|---|
| Vanilla JS, Webflow, Vue | **GSAP** |
| Pinning, horizontal scroll, complex timelines | **GSAP** |
| React / Next.js, declarative style | **Framer Motion** |
| whileInView entrance animations | **Framer Motion** |
| Both in same Next.js app | See notes in references |

Read the relevant reference file for full recipes and Copilot prompts:

- **GSAP** → `references/gsap.md` — ScrollTrigger API, all recipes, React integration
- **Framer Motion** → `references/framer.md` — useScroll, useTransform, all recipes

## Setup (Always Do First)

### GSAP
```bash
npm install gsap
```
```js
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger); // MUST call before any ScrollTrigger usage
```

### Framer Motion (Motion v12)
```bash
npm install motion   # package name
```
```js
import { motion, useScroll, useTransform, useSpring } from 'motion/react';
```

## Workflow

1. Interpret the user's intent to identify if GSAP or Framer Motion fits best.
2. Ensure plugins/modules are correctly imported and registered.
3. Apply responsive animations with `matchMedia` or CSS container queries.
4. Verify performance (will-change, transform3d, passive listeners).
