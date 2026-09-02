---
name: c4-architecture
description: >
  Generates software architecture documentation using C4 model Mermaid diagrams (Context, Container, Component, Code).
  Use when asked to create architecture diagrams, document system boundaries, visualize software components, or when user
  mentions "c4 architecture", "c4 model", or "c4 mermaid diagram".
argument-hint: "[context|container|component|mermaid]"
license: MIT
---

# C4 Architecture — C4 Model Diagram Generator

Based on [softaworks/c4-architecture](https://skillrepo.dev/skills/softaworks/c4-architecture) (v1.1A), this skill creates C4 model architectural diagrams in Mermaid format.

## C4 Abstraction Levels

1. **System Context**: High-level users, software systems, and external integrations.
2. **Container Diagram**: Applications, databases, microservices, and protocols (`https`, `gRPC`, `AMQP`).
3. **Component Diagram**: Internal building blocks within a single container.
4. **Code Diagram**: Class or entity relationship diagrams for critical modules.
