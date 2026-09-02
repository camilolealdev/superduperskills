---
name: baoyu-compress-image
description: >
  Compresses images to WebP (default) or PNG with automatic tool selection (sharp, cwebp, pngquant).
  Use when optimizing image assets for web performance, converting to webp, or when user mentions
  "baoyu-compress-image", "compress image", "optimize image", or "convert to webp".
argument-hint: "[webp|png|quality|compress]"
license: MIT
---

# Baoyu Compress Image — Web Image Optimizer

Based on [jimliu/baoyu-compress-image](https://skillrepo.dev/skills/jimliu/baoyu-compress-image) (v1.0B), this skill compresses images for maximum web performance.

## Optimization Rules

- **Default Format**: Lossy WebP with quality `82` for photo assets (achieves ~70% size reduction).
- **PNG Optimization**: Lossless compression via `pngquant` for sharp UI screenshots and transparent logos.
- **Dimensional Resizing**: Downscales oversized assets exceeding 2048px width.
