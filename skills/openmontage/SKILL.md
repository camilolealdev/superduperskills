---
name: openmontage
description: >
  Autonomous video production team skill for AI agents. Converts script & asset inputs into
  assembled video cuts, auto-subtitles, scene transitions, TTS audio generation, and media exports.
  Use when building video generation workflows, social media clips, video tutorials, or when user
  mentions "openmontage", "open montage", "video production", "auto edit video", or "video pipeline".
argument-hint: "[script|edit|subtitles|tts|export]"
license: MIT
---

# OpenMontage — Autonomous Video Production Pipeline

Based on [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage) (50k+ ★), this skill turns an AI agent into an automated video production studio capable of writing scripts, generating voiceovers, rendering subtitles, cutting scenes, and exporting final video formats.

## Production Pipeline

1. **Scripting & Storyboarding**: Generates timed voiceover scripts and visual scene cues.
2. **Audio & TTS Synthesis**: Generates voiceover audio using neural TTS models (e.g. Piper TTS, ElevenLabs).
3. **Automated Editing & Cutting**: Uses FFmpeg and Python scripts to trim, sync, and transition media clips.
4. **Caption & Subtitle Generation**: Renders animated, burned-in subtitles with word-level timing.
5. **Final Render & Export**: Produces 1080p / 4K MP4 exports formatted for YouTube, TikTok, or Instagram.

---

## Prerequisites & Tools

- Requires `ffmpeg`, `python (venv)`, and audio tools (`piper-tts` or equivalent).
- Integrates with `ai-image-generator` or stock media assets for visual B-roll.
