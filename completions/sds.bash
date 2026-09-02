#!/usr/bin/env bash
# =============================================================================
# SuperDuperSkills (sds) — Bash Tab Completion
# =============================================================================
# Install:
#   source completions/sds.bash          # temporary
#   cp completions/sds.bash /etc/bash_completion.d/sds  # system-wide
#
# Or add to ~/.bashrc:
#   source /path/to/superduperskills/completions/sds.bash
# =============================================================================

_sds_completions() {
    local cur prev opts skills_dir
    COMPREPLY=()
    cur="${COMP_WORDS[COMP_CWORD]}"
    prev="${COMP_WORDS[COMP_CWORD-1]}"

    # All subcommands
    local commands="init scan list toggle search ingest sync audit wizard doctor export stats profile desktop completions"

    # Global flags
    local global_flags="--help --version --json --quiet --no-color -V -j -q -h"

    # Subcommand-specific flags
    local scan_flags="--full -f --help"
    local list_flags="--core-only -c --json -j --help"
    local toggle_flags="--on --off --help"
    local search_flags="--limit -l --json -j --help"
    local ingest_flags="--category -c --help"
    local export_flags="--format -f --json -j --help"
    local profile_flags="save load list delete"
    local desktop_flags="setup config"
    local completions_flags="install uninstall show path --shell -s --help"

    # If we're at position 1 (the subcommand)
    if [[ ${COMP_CWORD} -eq 1 ]]; then
        COMPREPLY=( $(compgen -W "${commands} ${global_flags}" -- "${cur}") )
        return 0
    fi

    local subcmd="${COMP_WORDS[1]}"

    # Subcommand-specific completions
    case "${subcmd}" in
        scan)
            COMPREPLY=( $(compgen -W "${scan_flags}" -- "${cur}") )
            ;;
        list)
            COMPREPLY=( $(compgen -W "${list_flags}" -- "${cur}") )
            ;;
        toggle)
            # Complete skill names for toggle
            if [[ "${cur}" == -* ]]; then
                COMPREPLY=( $(compgen -W "${toggle_flags}" -- "${cur}") )
            else
                _sds_complete_skill_names
            fi
            ;;
        search)
            COMPREPLY=( $(compgen -W "${search_flags}" -- "${cur}") )
            ;;
        ingest)
            COMPREPLY=( $(compgen -W "${ingest_flags}" -- "${cur}") )
            ;;
        export)
            if [[ "${cur}" == -* ]]; then
                COMPREPLY=( $(compgen -W "${export_flags}" -- "${cur}") )
            else
                COMPREPLY=( $(compgen -W "json markdown both" -- "${cur}") )
            fi
            ;;
        profile)
            if [[ ${COMP_CWORD} -eq 2 ]]; then
                COMPREPLY=( $(compgen -W "${profile_flags}" -- "${cur}") )
            elif [[ "${prev}" == "save" || "${prev}" == "load" || "${prev}" == "delete" ]]; then
                _sds_complete_profile_names
            fi
            ;;
        desktop)
            COMPREPLY=( $(compgen -W "${desktop_flags}" -- "${cur}") )
            ;;
        completions)
            if [[ "${cur}" == -* ]]; then
                COMPREPLY=( $(compgen -W "${completions_flags}" -- "${cur}") )
            else
                COMPREPLY=( $(compgen -W "install uninstall show path" -- "${cur}") )
            fi
            ;;
        *)
            # Fallback: complete global flags
            COMPREPLY=( $(compgen -W "${global_flags}" -- "${cur}") )
            ;;
    esac
}

# Complete skill names from the skills/ directory
_sds_complete_skill_names() {
    local skills_dir="skills"
    local names=""

    if [[ -d "${skills_dir}" ]]; then
        names=$(find "${skills_dir}" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' 2>/dev/null | sort)
    fi

    COMPREPLY=( $(compgen -W "${names}" -- "${cur}") )
}

# Complete profile names from .agents/profiles/
_sds_complete_profile_names() {
    local profiles_dir=".agents/profiles"
    local names=""

    if [[ -d "${profiles_dir}" ]]; then
        names=$(find "${profiles_dir}" -name '*.json' -printf '%f\n' 2>/dev/null | sed 's/\.json$//' | sort)
    fi

    COMPREPLY=( $(compgen -W "${names}" -- "${cur}") )
}

complete -F _sds_completions sds
complete -F _sds_completions superduperskills
