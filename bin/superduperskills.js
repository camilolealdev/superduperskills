#!/usr/bin/env node

/**
 * SuperDuperSkills — Node.js CLI Binary Launcher
 * Bridges npx / pnpm dlx executions directly into the Agentic Control Center.
 */

const { spawn } = require('child_process');
const path = require('path');
const fs = require('fs');

const rootDir = path.resolve(__dirname, '..');
const pythonScript = path.join(rootDir, 'scripts', 'superduper_cli.py');

// Pick available python command (python3 or python)
const pythonCmd = process.platform === 'win32' ? 'python' : 'python3';

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
    console.error('\x1b[31m[ERROR] Python 3 no fue detectado en tu PATH.\x1b[0m');
    console.error('Por favor instala Python 3 (https://www.python.org/downloads/) para ejecutar SuperDuperSkills CLI.');
  } else {
    console.error('\x1b[31m[ERROR] Fallo al iniciar el proceso:\x1b[0m', err.message);
  }
  process.exit(1);
});

child.on('close', (code) => {
  process.exit(code ?? 0);
});
