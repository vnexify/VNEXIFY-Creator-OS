<#
.SYNOPSIS
    VNEXIFY Creator OS System Health Diagnostics Script

.DESCRIPTION
    Performs comprehensive diagnostic health checks across 13 core environment
    and workspace components, displaying a formatted health table.

.EXAMPLE
    .\scripts\health.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Continue"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "     VNEXIFY Creator OS - System Health Diagnostics  " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

$healthResults = [System.Collections.Generic.List[PSObject]]::new()
$allHealthy = $true

function Add-HealthCheck {
    param (
        [string]$Component,
        [bool]$Passed,
        [string]$Details
    )
    
    $statusStr = if ($Passed) { "PASS" } else { "FAIL" }
    
    $script:healthResults.Add([PSCustomObject]@{
        Component = $Component
        Status    = $statusStr
        Details   = $Details
    })

    if (-not $Passed) {
        $script:allHealthy = $false
    }
}

# 1. Git repository (Safe command discovery)
$gitExe = Get-Command "git" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
if (-not $gitExe -and (Test-Path "C:\Program Files\Git\cmd\git.exe")) {
    $gitExe = "C:\Program Files\Git\cmd\git.exe"
}

$gitCheck = [bool](Test-Path ".git")
if ($gitExe) {
    try {
        $res = & $gitExe rev-parse --is-inside-work-tree 2>$null
        if ($res -eq "true") { $gitCheck = $true }
    } catch {}
}
Add-HealthCheck -Component "Git Repository" -Passed $gitCheck -Details $(if ($gitCheck) { "Git repository detected" } else { "Missing .git repository" })

# 2. Python
$pyPath = ".\.venv\Scripts\python.exe"
$pyCheck = Test-Path $pyPath
$pyVer = if ($pyCheck) { (& $pyPath --version 2>&1).Trim() } else { "N/A" }
Add-HealthCheck -Component "Python Venv" -Passed $pyCheck -Details $(if ($pyCheck) { $pyVer } else { "Virtualenv missing at .venv" })

# 3. Node.js
$nodeVer = node --version 2>$null
$nodeCheck = $LASTEXITCODE -eq 0 -and (-not [string]::IsNullOrWhiteSpace($nodeVer))
Add-HealthCheck -Component "Node.js Tooling" -Passed $nodeCheck -Details $(if ($nodeCheck) { $nodeVer.Trim() } else { "Node.js not found" })

# 4. npm
$npmVer = npm --version 2>$null
$npmCheck = $LASTEXITCODE -eq 0 -and (-not [string]::IsNullOrWhiteSpace($npmVer))
Add-HealthCheck -Component "npm Package Mgr" -Passed $npmCheck -Details $(if ($npmCheck) { "v" + $npmVer.Trim() } else { "npm not found" })

# 5. Frontend & Workspace Dependencies (Dynamic Detection)
$rootModules = Test-Path "node_modules"
$frontendModules = Test-Path "frontend/node_modules"
$reactInstalled = (Test-Path "node_modules/react") -or (Test-Path "frontend/node_modules/react")
$feCheck = $rootModules -or $frontendModules -or $reactInstalled

$feDetails = if ($feCheck) {
    if ($rootModules -and $frontendModules) { "Root & Frontend Workspaces present" }
    elseif ($rootModules) { "Root Workspace (Hoisted) present" }
    else { "Frontend Workspace present" }
} else {
    "npm node_modules missing (Run 'npm install')"
}
Add-HealthCheck -Component "Frontend Modules" -Passed $feCheck -Details $feDetails

# 6. Backend Dependencies
$beCheck = $pyCheck -and (& $pyPath -c "import fastapi, sqlalchemy, pydantic; print('ok')" 2>$null) -eq "ok"
Add-HealthCheck -Component "Backend Modules" -Passed $beCheck -Details $(if ($beCheck) { "FastAPI, SQLAlchemy, Pydantic verified" } else { "Backend dependencies missing" })

# 7. Electron Config & Modules
$elModules = (Test-Path "node_modules/electron") -or (Test-Path "electron/node_modules") -or (Test-Path "node_modules/electron-builder")
$elCheck = (Test-Path "electron/tsconfig.json") -and ($rootModules -or $elModules)
Add-HealthCheck -Component "Electron Config" -Passed $elCheck -Details $(if ($elCheck) { "Electron shell & tsconfig present" } else { "Electron tsconfig/modules missing" })

# 8. SQLite Folder
$sqliteCheck = Test-Path "backend/db"
Add-HealthCheck -Component "SQLite Directory" -Passed $sqliteCheck -Details $(if ($sqliteCheck) { "backend/db exists" } else { "backend/db missing" })

# 9. Logs Folder
$logsCheck = Test-Path "logs"
Add-HealthCheck -Component "Logs Directory" -Passed $logsCheck -Details $(if ($logsCheck) { "logs folder exists" } else { "logs folder missing" })

# 10. Exports Folder
$exportsCheck = Test-Path "exports"
Add-HealthCheck -Component "Exports Directory" -Passed $exportsCheck -Details $(if ($exportsCheck) { "exports folder exists" } else { "exports folder missing" })

# 11. Docs Folder
$docsCheck = Test-Path "docs"
Add-HealthCheck -Component "Docs Directory" -Passed $docsCheck -Details $(if ($docsCheck) { "docs folder exists" } else { "docs folder missing" })

# 12. Frontend Dist
$distCheck = Test-Path "frontend/dist"
Add-HealthCheck -Component "Frontend Dist" -Passed $distCheck -Details $(if ($distCheck) { "frontend/dist bundle exists" } else { "frontend/dist not built yet" })

# 13. Backend DB Path
$dbCheck = Test-Path "backend/db"
Add-HealthCheck -Component "Backend DB Path" -Passed $dbCheck -Details $(if ($dbCheck) { "backend/db path verified" } else { "backend/db path missing" })

# Display Health Table
Write-Host "`nSystem Diagnostics Table:" -ForegroundColor Yellow
$healthResults | Format-Table -AutoSize

# Overall System Health Result
Write-Host "====================================================" -ForegroundColor Cyan
if ($allHealthy) {
    Write-Host "                System Healthy                      " -ForegroundColor Green
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 0
} else {
    Write-Host "            System Issues Detected                  " -ForegroundColor Red
    Write-Host "====================================================" -ForegroundColor Cyan
    exit 1
}
