---
name: android-clean-architecture
description: >
  Clean Architecture patterns for Android and Kotlin Multiplatform (KMP) projects — module structure, dependency rules,
  UseCases, Repositories, Coroutines/Flow, and ViewModel state mapping. Use when building Android apps, structuring KMP code,
  or when user mentions "android clean architecture", "android-clean-architecture", "kmp clean architecture", or "android architecture".
argument-hint: "[usecase|repository|viewmodel|kmp|flow]"
license: MIT
---

# Android Clean Architecture — Kotlin & KMP Architecture

Based on [affaan-m/android-clean-architecture](https://skillrepo.dev/skills/affaan-m/android-clean-architecture) (v1.2A), this skill establishes clean architecture boundaries for Kotlin and Android projects.

## Layer Structure

- **Domain Layer**: Pure Kotlin entities, Repository interfaces, and single-responsibility UseCases.
- **Data Layer**: Repository implementations, Ktor/Retrofit API sources, Room DB DAO, and DTO mappers.
- **UI Layer**: Jetpack Compose screens, ViewModels exposing immutable `StateFlow<UiState>`, and MVI intent handling.
