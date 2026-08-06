import { app, BrowserWindow } from 'electron'
import path from 'path'

function createWindow() {
  const mainWindow = new BrowserWindow({
    width: 1280,
    height: 840,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  })

  const indexPath = path.join(__dirname, '..', '..', 'frontend', 'dist', 'index.html')
  
  if (process.env.VITE_DEV_SERVER_URL) {
    mainWindow.loadURL(process.env.VITE_DEV_SERVER_URL).catch(() => {
      mainWindow.loadFile(indexPath).catch(() => {
        mainWindow.loadURL('http://localhost:5173')
      })
    })
  } else {
    mainWindow.loadFile(indexPath).catch(() => {
      mainWindow.loadURL('http://localhost:5173')
    })
  }
}

app.whenReady().then(createWindow)

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit()
  }
})

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow()
  }
})
