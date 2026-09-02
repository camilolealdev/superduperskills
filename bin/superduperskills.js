#!/usr/bin/env node

/**
 * SuperDuperSkills — Node.js CLI Binary Launcher v4.0
 * Bridges npx / pnpm dlx executions directly into the Agentic Control Center.
 * 
 * Agent 5: Desktop integration stubs + Electron wrapper detection
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const rootDir = path.resolve(__dirname, '..');
const pythonScript = path.join(rootDir, 'scripts', 'superduper_cli.py');

const VERSION = '4.0.0';
const CODENAME = 'HyperDrive';  // synced with scripts/superduper_cli.py

// Pick available python command
const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';

// Handle --version flag directly in Node (no Python needed)
if (process.argv.includes('--version') || process.argv.includes('-V')) {
  console.log(`\x1b[36m\x1b[1mSuperDuperSkills\x1b[0m v${VERSION} \x1b[33m\u00ab${CODENAME}\u00bb\x1b[0m`);
  process.exit(0);
}

// Handle --help without Python
if (process.argv.includes('--help') && process.argv.length <= 3) {
  console.log(`
\x1b[36m\x1b[1m SuperDuperSkills Agentic CLI v${VERSION}\x1b[0m
\x1b[37m 2,700+ AI Agent Skills for Claude, Gemini, Cursor, Codex\x1b[0m

\x1b[32mUsage:\x1b[0m
  $ sds                  Launch interactive TUI
  $ sds <command>        Run a specific command
  $ sds --help           Show this help
  $ sds --version        Show version

\x1b[33mCommands:\x1b[0m
  init        Initialize project (.agents/ directory)
  scan        Scan project stack & recommend skills
  list        List active skills in manifest
  toggle      Toggle a skill ON/OFF
  search      Search the 2,700+ skill vault
  ingest      Import a remote skill
  sync        Sync manifest to all agent environments
  audit       Verify SKILL.md files exist
  wizard      Launch qualification wizard
  doctor      Run environment health checks
  export      Export manifest to JSON/Markdown
  stats       Show usage statistics
  profile     Save/load skill profiles
  desktop     Desktop app integration
  completions Install shell completions

\x1b[36mDocs:\x1b[0m  https://superduperskills.vercel.app
\x1b[36mRepo:\x1b[0m  https://github.com/camilolealdev/superduperskills
`);
  process.exit(0);
}

// Desktop mode detection
if (process.argv.includes('--desktop')) {
  // Check if Electron is available
  try {
    require('electron');
    console.log('\x1b[32mElectron detected! Launching desktop mode...\x1b[0m');
    // In a real implementation, this would spawn Electron
    // For now, fall through to Python CLI
  } catch (e) {
    console.log('\x1b[33mDesktop mode requires Electron. Install with: npm install electron\x1b[0m');
    console.log('\x1b[37mFalling back to terminal mode...\x1b[0m');
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
    console.error('\x1b[31m[ERROR] Python 3 not found on PATH.\x1b[0m');
    console.error('Install Python 3 (https://www.python.org/downloads/) to run SuperDuperSkills CLI.');
    console.error('');
    console.error('\x1b[37mTip: You can still use basic commands like --version and --help\x1b[0m');
    console.error('\x1b[37m     without Python installed.\x1b[0m');
  } else {
    console.error('\x1b[31m[ERROR] Failed to start process:\x1b[0m', err.message);
  }
  process.exit(1);
});

child.on('close', (code) => {
  process.exit(code ?? 0);
});
