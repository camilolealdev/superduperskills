#!/usr/bin/env bash
set -euo pipefail

# ─── superduperskills installer ──────────────────────────────────────────────
# Installs skills into agent skill directories.
# Usage:
#   ./install.sh                    # Install to all detected agents
#   ./install.sh --target claude    # Claude Code only
#   ./install.sh --target gemini    # Gemini CLI only
#   ./install.sh --target codex     # Codex CLI only
#   ./install.sh --mode symlink     # Symlink instead of copy
#   ./install.sh --dry-run          # Show what would be done
# ──────────────────────────────────────────────────────────────────────────────

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$REPO_DIR/skills"
MODE="copy"
TARGET="all"
DRY_RUN=false

usage() {
    sed -n '3,10p' "$0" | sed 's/^#//'
    exit 1
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        --target) TARGET="$2"; shift 2 ;;
        --mode) MODE="$2"; shift 2 ;;
        --dry-run) DRY_RUN=true; shift ;;
        -h|--help) usage ;;
        *) echo "Unknown: $1"; usage ;;
    esac
done

if [[ ! -d "$SKILLS_DIR" ]]; then
    echo "Error: Skills directory not found at $SKILLS_DIR"
    echo "Run build_index.py first or check the repo path."
    exit 1
fi

SKILL_NAMES=()
while IFS= read -r dir; do
    name=$(basename "$dir")
    if [[ -f "$dir/SKILL.md" ]]; then
        SKILL_NAMES+=("$name")
    fi
done < <(find "$SKILLS_DIR" -mindepth 1 -maxdepth 1 -type d | sort)

echo "Found ${#SKILL_NAMES[@]} skills in repo."

# Agent target directories
declare -A AGENTS
AGENTS[claude]="$HOME/.claude/skills"
AGENTS[gemini]="$HOME/.gemini/skills"
AGENTS[codex]="$HOME/.codex/skills"

# Select targets
if [[ "$TARGET" == "all" ]]; then
    SELECTED=("${!AGENTS[@]}")
else
    SELECTED=("$TARGET")
fi

echo "Target agents: ${SELECTED[*]}"
echo "Mode: $MODE"
echo ""

if $DRY_RUN; then
    echo "[DRY RUN] Would install ${#SKILL_NAMES[@]} skills to:"
    for agent in "${SELECTED[@]}"; do
        echo "  $agent → ${AGENTS[$agent]}"
    done
    exit 0
fi

# Confirm
read -rp "Continue? (y/N) " confirm
if [[ "$confirm" != "y" ]]; then
    echo "Aborted."
    exit 0
fi

copied=0
skipped=0
errors=0

for agent in "${SELECTED[@]}"; do
    target="${AGENTS[$agent]}"
    mkdir -p "$target"

    for name in "${SKILL_NAMES[@]}"; do
        src="$SKILLS_DIR/$name/SKILL.md"
        dst_dir="$target/$name"
        dst="$dst_dir/SKILL.md"

        if [[ -f "$dst" ]]; then
            ((skipped++)) || true
            continue
        fi

        mkdir -p "$dst_dir"

        if [[ "$MODE" == "symlink" ]]; then
            ln -sf "$src" "$dst" 2>/dev/null && ((copied++)) || { ((errors++)); echo "  FAIL: $name → $dst"; }
        else
            cp "$src" "$dst" && ((copied++)) || { ((errors++)); echo "  FAIL: $name → $dst"; }
        fi
    done
done

echo ""
echo "=== Install Summary ==="
echo "  Installed: $copied"
echo "  Skipped (exists): $skipped"
echo "  Errors: $errors"
echo ""
echo "Done!"
