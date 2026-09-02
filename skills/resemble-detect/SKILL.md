---
name: resemble-detect
description: >
  Detects AI-generated or synthetic audio, image, and video content using Resemble AI detection models.
  Use when analyzing media authenticity, content moderation pipelines, or when user mentions "resemble detect",
  "ai detection", "synthetic audio", "deepfake detection", or "media verification".
argument-hint: "[audio|image|video|detect]"
license: MIT
---

# Resemble Detect — AI Media & Deepfake Detection

Based on [resemble-ai/detect-skill](https://github.com/resemble-ai/detect-skill) (61 ★), **Resemble Detect** analyzes audio, image, and video files to identify synthetic or AI-manipulated content.

## Usage

```bash
npx skills add resemble-ai/detect-skill
```

---

## Guidelines

- **Probability Score**: Treats detection metrics as probabilistic signals rather than definitive proof.
- **Multimodal**: Supports spectral analysis of audio streams, image artifacts, and video frame inconsistencies.
