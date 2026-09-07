#!/usr/bin/env node

/**
 * SuperDuperSkills — Node.js CLI Binary Launcher v4.0 (Gemini & Claude Edition)
 * Bridges npx / pnpm dlx executions directly into the Agentic Control Center.
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const rootDir = path.resolve(__dirname, '..');
const pythonScript = path.join(rootDir, 'scripts', 'superduper_cli.py');

const VERSION = '6.0.0';
const CODENAME = 'WorldClass';

// TrueColor / ANSI Styling
const C = {
  RESET: '\x1b[0m',
  BOLD: '\x1b[1m',
  DIM: '\x1b[2m',
  CYAN: '\x1b[38;2;34;211;238m',
  BLUE: '\x1b[38;2;96;165;250m',
  INDIGO: '\x1b[38;2;129;140;248m',
  GOLD: '\x1b[38;2;251;191;36m',
  EMERALD: '\x1b[38;2;52;211;153m',
  SLATE_LIGHT: '\x1b[38;2;226;232;240m',
  SLATE_MUTED: '\x1b[38;2;148;163;184m',
  SLATE_DARK: '\x1b[38;2;100;116;139m',
  ROSE: '\x1b[38;2;248;113;113m'
};

const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';

// Handle --version flag directly in Node
if (process.argv.includes('--version') || process.argv.includes('-V')) {
  console.log(`\n  ${C.CYAN}${C.BOLD}✦ SuperDuperSkills${C.RESET} ${C.SLATE_LIGHT}v${VERSION}${C.RESET} ${C.GOLD}«${CODENAME}»${C.RESET}\n`);
  process.exit(0);
}

// Handle --help without Python
if (process.argv.includes('--help') && process.argv.length <= 3) {
  console.log(`
  ${C.CYAN}╭────────────────────────────────────────────────────────────────────────╮${C.RESET}
  ${C.CYAN}│${C.RESET}  ${C.CYAN}${C.BOLD}✦ SUPERDUPERSKILLS${C.RESET} ${C.SLATE_MUTED}v${VERSION}${C.RESET} ${C.GOLD}«${CODENAME}»${C.RESET}                       ${C.INDIGO}● Camilo Leal${C.RESET} ${C.CYAN}│${C.RESET}
  ${C.BLUE}│${C.RESET}  ${C.SLATE_LIGHT}3,325+ AI Agent Skills Governance Suite · ${C.EMERALD}easy-marketing.xyz${C.RESET}  ${C.BLUE}│${C.RESET}
  ${C.INDIGO}╰────────────────────────────────────────────────────────────────────────╯${C.RESET}

  ${C.BOLD}${C.CYAN}Usage:${C.RESET}
    ${C.SLATE_LIGHT}$ sds${C.RESET}                   ${C.SLATE_MUTED}Launch interactive Gemini/Claude REPL (with mouse)${C.RESET}
    ${C.SLATE_LIGHT}$ sds <command>${C.RESET}         ${C.SLATE_MUTED}Execute a specific command directly${C.RESET}
    ${C.SLATE_LIGHT}$ sds --help${C.RESET}            ${C.SLATE_MUTED}Show this help screen${C.RESET}
    ${C.SLATE_LIGHT}$ sds --version${C.RESET}         ${C.SLATE_MUTED}Display version information${C.RESET}

  ${C.BOLD}${C.GOLD}World-Class Commands:${C.RESET}
    ${C.EMERALD}ui${C.RESET}          ${C.SLATE_LIGHT}Launch companion web UI dashboard at http://localhost:4242${C.RESET}
    ${C.EMERALD}ask${C.RESET}         ${C.SLATE_LIGHT}Query terminal assistant grounded in active skills (-75% tokens)${C.RESET}
    ${C.EMERALD}why${C.RESET}         ${C.SLATE_LIGHT}Explain why a skill is in matrix & detect AST file markers${C.RESET}
    ${C.EMERALD}graph${C.RESET}       ${C.SLATE_LIGHT}Render ASCII dependency architecture and topology tree${C.RESET}
    ${C.EMERALD}auto-branch${C.RESET} ${C.SLATE_LIGHT}Auto-calibrate mission mode based on active Git branch${C.RESET}
    ${C.EMERALD}benchmark${C.RESET}   ${C.SLATE_LIGHT}Audit structural quality of vault skills with letter grade (A+)${C.RESET}
    ${C.EMERALD}update${C.RESET}      ${C.SLATE_LIGHT}Silent vault synchronization from remote GitHub master${C.RESET}
    ${C.EMERALD}eval${C.RESET}        ${C.SLATE_LIGHT}Run prompt through skill sandbox playground${C.RESET}

  ${C.BOLD}${C.GOLD}Core Commands:${C.RESET}
    ${C.CYAN}scan${C.RESET}        ${C.SLATE_LIGHT}Scan project stack & recommend curated skills${C.RESET}
    ${C.CYAN}budget${C.RESET}      ${C.SLATE_LIGHT}Token budget estimator & LLM context window simulator${C.RESET}
    ${C.CYAN}mode${C.RESET}        ${C.SLATE_LIGHT}1-Click Mission Modes (mvp, harden, refactor, design, fullstack)${C.RESET}
    ${C.CYAN}prompt${C.RESET}      ${C.SLATE_LIGHT}Compile & copy Super-Prompt to clipboard for Web LLMs${C.RESET}
    ${C.CYAN}watch${C.RESET}       ${C.SLATE_LIGHT}Real-time workspace watcher for automatic skill triggers${C.RESET}
    ${C.CYAN}doctor${C.RESET}      ${C.SLATE_LIGHT}Run full health check & environment diagnostics${C.RESET}
    ${C.CYAN}list${C.RESET}        ${C.SLATE_LIGHT}List all active skills in project manifest${C.RESET}
    ${C.CYAN}search${C.RESET}      ${C.SLATE_LIGHT}Search across 3,300+ skills in the local vault${C.RESET}
    ${C.CYAN}preview${C.RESET}     ${C.SLATE_LIGHT}Inspect formatted SKILL.md and calculate token weight${C.RESET}
    ${C.CYAN}toggle${C.RESET}      ${C.SLATE_LIGHT}Toggle a specific skill ON or OFF${C.RESET}
    ${C.CYAN}sync${C.RESET}        ${C.SLATE_LIGHT}Sync manifest to Cursor Rules, Claude, OpenCode${C.RESET}
    ${C.CYAN}audit${C.RESET}       ${C.SLATE_LIGHT}Verify physical SKILL.md compliance on disk${C.RESET}
    ${C.CYAN}wizard${C.RESET}      ${C.SLATE_LIGHT}Launch Socratic qualification interview wizard${C.RESET}
    ${C.CYAN}init${C.RESET}        ${C.SLATE_LIGHT}Initialize .agents/ governance directory${C.RESET}
    ${C.CYAN}stats${C.RESET}       ${C.SLATE_LIGHT}Display telemetry dashboard & category metrics${C.RESET}
    ${C.CYAN}profile${C.RESET}     ${C.SLATE_LIGHT}Save and load custom skill presets${C.RESET}
    ${C.CYAN}export${C.RESET}      ${C.SLATE_LIGHT}Export active manifest to JSON or Markdown${C.RESET}

  ${C.SLATE_DARK}──────────────────────────────────────────────────────────────────────────${C.RESET}
  ${C.SLATE_MUTED}Docs:${C.RESET}  ${C.CYAN}https://superduperskills.vercel.app${C.RESET}
  ${C.SLATE_MUTED}Repo:${C.RESET}  ${C.CYAN}https://github.com/camilolealdev/superduperskills${C.RESET}
`);
  process.exit(0);
}


// Desktop mode detection
if (process.argv.includes('--desktop')) {
  try {
    require('electron');
    console.log(`\n  ${C.EMERALD}✔ Electron runtime found. Launching desktop control center...${C.RESET}\n`);
  } catch (e) {
    console.log(`\n  ${C.GOLD}⚠ Desktop mode requires Electron (npm install electron).${C.RESET}`);
    console.log(`  ${C.SLATE_MUTED}Switching seamlessly to terminal interactive mode...${C.RESET}\n`);
  }
}

const args = [pythonScript, ...process.argv.slice(2)];

const child = spawn(pythonCmd, args, {
  stdio: 'inherit',
  cwd: process.cwd(),
  env: {
    ...process.env,
    PYTHONUNBUFFERED: '1',
    PYTHONIOENCODING: 'utf-8'
  }
});

child.on('error', (err) => {
  if (err.code === 'ENOENT') {
    console.error(`\n  ${C.ROSE}✖ Python 3 was not detected on PATH.${C.RESET}`);
    console.error(`  ${C.SLATE_MUTED}Install Python 3 (https://www.python.org/downloads/) to run SuperDuperSkills CLI.${C.RESET}\n`);
  } else {
    console.error(`\n  ${C.ROSE}✖ Process error:${C.RESET}`, err.message);
  }
  process.exit(1);
});

child.on('close', (code) => {
  process.exit(code ?? 0);
});
