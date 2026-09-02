# =============================================================================
# SuperDuperSkills (sds) — Fish Tab Completion
# =============================================================================
# Install:
#   source completions/sds.fish                  # temporary
#   cp completions/sds.fish ~/.config/fish/completions/sds.fish  # persistent
#
# Fish auto-loads completions from ~/.config/fish/completions/
# =============================================================================

# Global flags
complete -c sds -l help    -s h -d 'Show help message and exit'
complete -c sds -l version -s V -d 'Show version and exit'
complete -c sds -l json    -s j -d 'Output results in JSON format'
complete -c sds -l quiet   -s q -d 'Suppress banner and decorative output'
complete -c sds -l no-color     -d 'Disable ANSI color output'

# Subcommands
complete -c sds -n '__fish_use_subcommand' -a init        -d 'Initialize project — create .agents/ directory'
complete -c sds -n '__fish_use_subcommand' -a scan        -d 'Scan project stack and recommend skills'
complete -c sds -n '__fish_use_subcommand' -a list        -d 'List all active skills in manifest'
complete -c sds -n '__fish_use_subcommand' -a toggle      -d 'Toggle a skill ON/OFF in manifest'
complete -c sds -n '__fish_use_subcommand' -a search      -d 'Search the skill vault (2,700+ skills)'
complete -c sds -n '__fish_use_subcommand' -a ingest      -d 'Import a remote skill or create custom one'
complete -c sds -n '__fish_use_subcommand' -a sync        -d 'Sync manifest to all agent environments'
complete -c sds -n '__fish_use_subcommand' -a audit       -d 'Verify SKILL.md files exist'
complete -c sds -n '__fish_use_subcommand' -a wizard      -d 'Launch qualification wizard'
complete -c sds -n '__fish_use_subcommand' -a doctor      -d 'Run environment health checks'
complete -c sds -n '__fish_use_subcommand' -a export      -d 'Export manifest to JSON or Markdown'
complete -c sds -n '__fish_use_subcommand' -a stats       -d 'Show usage statistics'
complete -c sds -n '__fish_use_subcommand' -a profile     -d 'Save or load skill profiles'
complete -c sds -n '__fish_use_subcommand' -a desktop     -d 'Desktop app integration'
complete -c sds -n '__fish_use_subcommand' -a completions -d 'Install or uninstall shell completions'

# scan flags
complete -c sds -n '__fish_seen_subcommand_from scan' -l full -s f -d 'Run full recursive scan'

# list flags
complete -c sds -n '__fish_seen_subcommand_from list' -l core-only -s c -d 'Show only core skills'

# toggle: skill names + flags
complete -c sds -n '__fish_seen_subcommand_from toggle' -l on  -d 'Force enable the skill'
complete -c sds -n '__fish_seen_subcommand_from toggle' -l off -d 'Force disable the skill'
complete -c sds -n '__fish_seen_subcommand_from toggle' -a '(ls skills/ 2>/dev/null)' -d 'Skill name'

# search flags
complete -c sds -n '__fish_seen_subcommand_from search' -l limit -s l -r -d 'Max results (default: 25)'

# ingest flags
complete -c sds -n '__fish_seen_subcommand_from ingest' -l category -s c -r -d 'Category tag'

# export flags
complete -c sds -n '__fish_seen_subcommand_from export' -l format -s f -r -a 'json markdown both' -d 'Export format'

# profile: action + names
complete -c sds -n '__fish_seen_subcommand_from profile' -a 'save load list delete' -d 'Profile action'
complete -c sds -n '__fish_seen_subcommand_from profile' -a '(ls .agents/profiles/*.json 2>/dev/null | xargs -I{} basename {} .json)' -d 'Profile name'

# desktop flags
complete -c sds -n '__fish_seen_subcommand_from desktop' -a 'setup config' -d 'Desktop action'

# completions flags
complete -c sds -n '__fish_seen_subcommand_from completions' -a 'install uninstall show path' -d 'Completions action'
complete -c sds -n '__fish_seen_subcommand_from completions' -l shell -s s -r -a 'bash zsh fish' -d 'Target shell'
