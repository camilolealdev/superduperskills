#!/usr/bin/env zsh
# =============================================================================
# SuperDuperSkills (sds) — Zsh Tab Completion
# =============================================================================
# Install:
#   source completions/sds.zsh                  # temporary
#   cp completions/sds.zsh ~/.zsh/completions/_sds  # persistent
#
# Or add to ~/.zshrc:
#   fpath=(/path/to/superduperskills/completions $fpath)
#   autoload -Uz compinit && compinit
# =============================================================================

compdef _sds sds
compdef _sds superduperskills

_sds() {
    local -a commands
    commands=(
        'init:Initialize project — create .agents/ directory and default manifest'
        'scan:Scan project stack and recommend skills'
        'list:List all active skills in the project manifest'
        'toggle:Toggle a skill ON/OFF in the manifest'
        'search:Search the skill vault (2,700+ skills)'
        'ingest:Import a remote skill or create a custom one'
        'sync:Synchronize active manifest to all agent environments'
        'audit:Audit compliance — verify SKILL.md files exist'
        'wizard:Launch the full Socratic qualification wizard'
        'doctor:Run environment diagnostics and health checks'
        'export:Export the active manifest to JSON or Markdown'
        'stats:Show usage statistics and dashboard'
        'profile:Save or load skill profiles (presets)'
        'desktop:Desktop app integration commands'
        'completions:Install or uninstall shell completions'
    )

    local -a global_flags
    global_flags=(
        '--help[Show help message and exit]'
        '--version[Show version and exit]'
        '--json[Output results in JSON format]'
        '--quiet[Suppress banner and decorative output]'
        '--no-color[Disable ANSI color output]'
        '-V[Show version]'
        '-j[JSON output shorthand]'
        '-q[Quiet shorthand]'
    )

    _arguments -C \
        '1:command:->command' \
        '*::arg:->args' \
        ${global_flags[@]}

    case $state in
        command)
            _describe -t commands 'sds command' commands
            ;;
        args)
            case ${words[1]} in
                scan)
                    _arguments \
                        '--full[Run full recursive scan]' \
                        '-f[Full scan shorthand]'
                    ;;
                list)
                    _arguments \
                        '--core-only[Show only core mandatory skills]' \
                        '-c[Core-only shorthand]' \
                        '--json[JSON output]' \
                        '-j[JSON output shorthand]'
                    ;;
                toggle)
                    _arguments \
                        '1:skill name:->skill_name' \
                        '--on[Force enable the skill]' \
                        '--off[Force disable the skill]'
                    case $state in
                        skill_name)
                            _sds_complete_skills
                            ;;
                    esac
                    ;;
                search)
                    _arguments \
                        '1:query:' \
                        '--limit[Maximum results to return]' \
                        '-l[Limit shorthand]' \
                        '--json[JSON output]' \
                        '-j[JSON output shorthand]'
                    ;;
                ingest)
                    _arguments \
                        '1:source: ' \
                        '--category[Category tag]' \
                        '-c[Category shorthand]'
                    ;;
                export)
                    _arguments \
                        '--format[Export format]:format:(json markdown both)' \
                        '-f[Format shorthand]' \
                        '--json[JSON output]'
                    ;;
                profile)
                    _arguments \
                        '1:action:(save load list delete)' \
                        '2:profile name:->profile_name'
                    case $state in
                        profile_name)
                            _sds_complete_profiles
                            ;;
                    esac
                    ;;
                desktop)
                    _arguments \
                        '1:action:(setup config)'
                    ;;
                completions)
                    _arguments \
                        '1:action:(install uninstall show path)' \
                        '--shell[Target shell]:shell:(bash zsh fish)' \
                        '-s[Shell shorthand]'
                    ;;
            esac
            ;;
    esac
}

# Complete skill names from skills/ directory
_sds_complete_skills() {
    local -a skills
    if [[ -d "skills" ]]; then
        skills=(${(f)"$(find skills -mindepth 1 -maxdepth 1 -type d -printf '%f\n' 2>/dev/null | sort)"})
    fi
    _describe -t skills 'skill name' skills
}

# Complete profile names from .agents/profiles/
_sds_complete_profiles() {
    local -a profiles
    if [[ -d ".agents/profiles" ]]; then
        profiles=(${(f)"$(find .agents/profiles -name '*.json' -printf '%f\n' 2>/dev/null | sed 's/\.json$//' | sort)"})
    fi
    _describe -t profiles 'profile name' profiles
}
