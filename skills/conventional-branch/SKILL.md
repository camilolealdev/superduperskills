---
name: conventional-branch
description: >
  Create Git branches following the Conventional Branch specification (feature/, bugfix/, hotfix/, release/, chore/).
  Use when creating a new branch, naming a branch, or when user mentions "conventional-branch", "branch naming", or "git branch convention".
argument-hint: "[feature|bugfix|hotfix|release|chore]"
license: MIT
---

# Conventional Branch — Standardized Git Branch Naming

Based on [github/conventional-branch](https://skillrepo.dev/skills/github/conventional-branch) (v1.0A), this skill enforces conventional branch names.

## Branch Naming Syntax

```
<type>/<issue-number>-<short-description>
```

### Types
- `feature/`: New user-facing capabilities (`feature/102-user-auth`).
- `bugfix/`: Defect fixes (`bugfix/204-fix-header-overflow`).
- `hotfix/`: Emergency production patches (`hotfix/301-patch-jwt-secret`).
- `chore/`: Dependency updates, tooling changes (`chore/deps-update-vite`).
