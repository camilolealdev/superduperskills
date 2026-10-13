# =============================================================================
# SuperDuperSkills (sds) - PowerShell Tab Completion (Windows PowerShell 5.1 + pwsh 7)
# =============================================================================
# Install:   sds completions install --shell powershell
# Manual:    . path\to\superduperskills\completions\sds.ps1     (add to $PROFILE)
# =============================================================================

$script:SdsCommands = @(
    'scan','list','toggle','search','budget','mode','prompt','watch','preview','ingest',
    'sync','audit','wizard','init','doctor','export','profile','stats','ui','ask','why',
    'graph','auto-branch','benchmark','update','eval','desktop','completions'
)
$script:SdsGlobalFlags = @('--help','--version','--json','--quiet','--no-color','-h','-V','-j','-q')
$script:SdsSubFlags = @{
    'scan'        = @('--full','-f')
    'list'        = @('--core-only','-c')
    'toggle'      = @('--on','--off')
    'search'      = @('--limit','-l')
    'ingest'      = @('--category','-c')
    'export'      = @('--format','-f')
    'ui'          = @('--port','-p','--no-browser')
    'profile'     = @('save','load','list','delete')
    'mode'        = @('mvp','harden','refactor','design','fullstack','ai-agents')
    'desktop'     = @('setup','config')
    'completions' = @('install','uninstall','show','path','--shell','-s')
}
# Commands whose first positional argument is a skill name
$script:SdsSkillCommands = @('toggle','preview','why','eval')

function script:Get-SdsSkillsDir {
    $dir = Split-Path -Parent $PSCommandPath
    $skills = Join-Path (Split-Path -Parent $dir) 'skills'
    if (Test-Path -LiteralPath $skills) { return $skills }
    $local = Join-Path (Get-Location) 'skills'
    if (Test-Path -LiteralPath $local) { return $local }
    return $null
}

Register-ArgumentCompleter -Native -CommandName 'sds','superduperskills' -ScriptBlock {
    param($wordToComplete, $commandAst, $cursorPosition)

    $words = @($commandAst.CommandElements | ForEach-Object { $_.ToString() })
    $sub = if ($words.Count -gt 1 -and $words[1] -notlike '-*') { $words[1] } else { $null }
    $candidates = @()

    if (-not $sub -or ($words.Count -eq 2 -and $wordToComplete -eq $words[1])) {
        $candidates = $script:SdsCommands + $script:SdsGlobalFlags
    }
    else {
        if ($script:SdsSubFlags.ContainsKey($sub)) { $candidates += $script:SdsSubFlags[$sub] }
        $candidates += $script:SdsGlobalFlags
        $prev = if ($wordToComplete -and $words.Count -ge 2) { $words[-2] } else { $words[-1] }
        if ($sub -eq 'completions' -and $prev -in '--shell','-s') {
            $candidates = @('bash','zsh','fish','powershell','all')
        }
        elseif ($script:SdsSkillCommands -contains $sub -and $wordToComplete -notlike '-*') {
            $dir = Get-SdsSkillsDir
            if ($dir) {
                $candidates = @(Get-ChildItem -LiteralPath $dir -Directory -Filter "$wordToComplete*" |
                    Select-Object -First 50 -ExpandProperty Name)
            }
        }
    }

    $candidates | Where-Object { $_ -like "$wordToComplete*" } | Sort-Object -Unique | ForEach-Object {
        [System.Management.Automation.CompletionResult]::new($_, $_, 'ParameterValue', $_)
    }
}
