#!/usr/bin/env pwsh
<#
.SYNOPSIS
  Installs superduperskills into agent skill directories.
.DESCRIPTION
  Copies or symlinks all skills from this repo into the target agent's skill directory.
  Supports Claude Code, Gemini CLI, and Codex CLI.
.PARAMETER Target
  Which agent to install for: claude, gemini, codex, or all (default).
.PARAMETER Mode
  copy (default) or symlink. Symlinks require admin on Windows.
.PARAMETER RepoDir
  Path to this repo. Auto-detected if not provided.
.EXAMPLE
  ./install.ps1 -Target claude -Mode copy
  ./install.ps1 -Target all -Mode symlink
#>
param(
    [ValidateSet('claude', 'gemini', 'codex', 'all')]
    [string]$Target = 'all',
    [ValidateSet('copy', 'symlink')]
    [string]$Mode = 'copy',
    [string]$RepoDir = ''
)

if (-not $RepoDir) {
    $RepoDir = Split-Path -Parent $MyInvocation.MyCommand.Path
}
$SkillsDir = Join-Path $RepoDir 'skills'

if (-not (Test-Path $SkillsDir)) {
    Write-Error "Skills directory not found at $SkillsDir. Run build_index.py first or check RepoDir."
    exit 1
}

$SkillNames = Get-ChildItem -Directory $SkillsDir | ForEach-Object { $_.Name }
Write-Host "Found $($SkillNames.Count) skills in repo."

$AgentTargets = @{}
$AgentTargets['claude'] = @{
    Path = [System.IO.Path]::Combine($env:USERPROFILE, '.claude', 'skills')
    Exists = $false
}
$AgentTargets['gemini'] = @{
    Path = [System.IO.Path]::Combine($env:USERPROFILE, '.gemini', 'skills')
    Exists = $false
}
$AgentTargets['codex'] = @{
    Path = [System.IO.Path]::Combine($env:USERPROFILE, '.codex', 'skills')
    Exists = $false
}

# Validate target directories
$selected = if ($Target -eq 'all') { $AgentTargets.Keys } else { @($Target) }
foreach ($name in $selected) {
    $agent = $AgentTargets[$name]
    if (Test-Path $agent.Path) {
        $agent.Exists = $true
        Write-Host "  $name : $($agent.Path) [EXISTS]"
    } else {
        Write-Host "  $name : $($agent.Path) [WILL CREATE]"
    }
}

# Confirm
Write-Host ""
Write-Host "This will install skills using Mode: $Mode"
$confirm = Read-Host "Continue? (y/N)"
if ($confirm -ne 'y') {
    Write-Host "Aborted."
    exit 0
}

$copied = 0
$skipped = 0
$errors = @()

foreach ($agentName in $selected) {
    $agent = $AgentTargets[$agentName]
    $targetDir = $agent.Path
    
    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }
    
    foreach ($skillName in $SkillNames) {
        $sourceSkill = Join-Path $SkillsDir "$skillName\SKILL.md"
        $targetSkillDir = Join-Path $targetDir $skillName
        $targetSkill = Join-Path $targetSkillDir 'SKILL.md'
        
        if (-not (Test-Path $sourceSkill)) {
            continue
        }
        
        if (Test-Path $targetSkill) {
            $skipped++
            continue
        }
        
        try {
            New-Item -ItemType Directory -Path $targetSkillDir -Force | Out-Null
            if ($Mode -eq 'symlink') {
                New-Item -ItemType SymbolicLink -Path $targetSkill -Target $sourceSkill | Out-Null
            } else {
                Copy-Item -Path $sourceSkill -Destination $targetSkill -Force
            }
            $copied++
        } catch {
            $errors += "[$agentName] $skillName : $_"
        }
    }
}

Write-Host ""
Write-Host "=== Install Summary ==="
Write-Host "  Installed: $copied"
Write-Host "  Skipped (already exists): $skipped"
if ($errors.Count -gt 0) {
    Write-Host "  Errors: $($errors.Count)"
    foreach ($e in $errors) {
        Write-Host "    $e"
    }
}
Write-Host ""
Write-Host "Done!"
