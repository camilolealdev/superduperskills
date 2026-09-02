---
name: cpp-coding-standards
description: >
  C++ coding standards based on the C++ Core Guidelines (isocpp.github.io). Enforces modern C++20/23 patterns, RAII,
  smart pointers (`std::unique_ptr`), const-correctness, and memory safety. Use when writing or refactoring C++ code,
  or when user mentions "cpp-coding-standards", "c++ core guidelines", or "modern cpp".
argument-hint: "[raii|smart-pointers|const|concepts|c++20]"
license: MIT
---

# C++ Coding Standards — C++ Core Guidelines Compliance

Based on [affaan-m/cpp-coding-standards](https://skillrepo.dev/skills/affaan-m/cpp-coding-standards) (v1.2A), this skill enforces modern C++ coding guidelines.

## Non-Negotiable Rules

1. **RAII**: Resource management must use RAII wrappers; raw calls to `new` and `delete` are forbidden.
2. **Smart Pointer Ownership**: Use `std::unique_ptr` for exclusive ownership and `std::shared_ptr` only for shared ownership.
3. **Const Correctness**: Mark methods and pass-by-reference parameters `const` by default.
