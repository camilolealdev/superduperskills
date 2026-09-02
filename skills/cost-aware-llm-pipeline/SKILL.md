---
name: cost-aware-llm-pipeline
description: >
  Cost optimization patterns for LLM API usage — model routing by task complexity, budget tracking, retry logic,
  and prompt caching. Use when building production LLM apps, reducing token costs, configuring prompt caching,
  or when user mentions "cost-aware-llm-pipeline", "llm cost optimization", or "prompt caching".
argument-hint: "[routing|caching|budget|retry|prompt-caching]"
license: MIT
---

# Cost-Aware LLM Pipeline — Token & Cost Optimization Patterns

Based on [affaan-m/cost-aware-llm-pipeline](https://skillrepo.dev/skills/affaan-m/cost-aware-llm-pipeline) (v1.2A), this skill minimizes API spending in LLM applications.

## Strategies

1. **Prompt Caching**: Move fixed system instructions and large context documents into Anthropic/OpenAI prompt cache blocks (`cache_control`).
2. **Tiered Model Routing**: Use fast models (Haiku / Mini) for classification and routing, reserving high-tier models for final generation.
3. **Structured Compression**: Apply `caveman` token compression on intermediate subagent outputs.
