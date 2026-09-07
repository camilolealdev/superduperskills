// SuperDuperSkills Desktop — Electron Main Process
const { app, BrowserWindow, Tray, Menu, shell } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let tray;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1200,
    height: 800,
    title: 'SuperDuperSkills Desktop',
    icon: path.join(__dirname, '..', 'icon-512.png'),
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    },
    backgroundColor: '#0c0e13'
  });

  mainWindow.loadURL('data:text/html,<html><body style="background:#0c0e13;color:#e8e6e1;font-family:monospace;display:flex;align-items:center;justify-content:center;height:100vh;"><h1>🚀 SuperDuperSkills Desktop</h1><p>Terminal launching...</p></body></html>');
  
  // Open external links in browser
  mainWindow.webContents.setWindowOpenHandler(({ url }) => {
    shell.openExternal(url);
    return { action: 'deny' };
  });
}

function createTray() {
  tray = new Tray(path.join(__dirname, '..', 'icon-192.png'));
  tray.setToolTip('SuperDuperSkills v4.0');
  
  const contextMenu = Menu.buildFromTemplate([
    { label: 'Open CLI', click: () => mainWindow?.show() },
    { label: 'Scan Project', click: () => { /* trigger scan */ } },
    { type: 'separator' },
    { label: 'Quit', click: () => app.quit() }
  ]);
  
  tray.setContextMenu(contextMenu);
  tray.on('double-click', () => mainWindow?.show());
}

app.whenReady().then(() => {
  createWindow();
  createTray();
});

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') app.quit();
});
