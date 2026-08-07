<#
.SYNOPSIS
    VNEXIFY Creator OS DevSecOps Security & Staged File Scanner

.DESCRIPTION
    Performs comprehensive static security auditing across both Git staged files 
    (git diff --cached) and working tree files to detect hardcoded credentials and secret values.
    Allows documentation placeholder examples while stopping actual secrets.

.EXAMPLE
    .\scripts\security_scan.ps1
#>

[CmdletBinding()]
param ()

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host " VNEXIFY Creator OS - Enterprise DevSecOps Scan     " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# Safe Git Command Discovery
$gitExe = Get-Command "git" -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
if (-not $gitExe -and (Test-Path "C:\Program Files\Git\cmd\git.exe")) {
    $gitExe = "C:\Program Files\Git\cmd\git.exe"
}

# Documentation and Policy Specification files allowed to contain regex rule descriptions
$whitelistedDocFiles = @(
    "security_scan.ps1",
    "rotate_secret_check.ps1",
    "github_security_check.ps1",
    "security_report.ps1",
    "run_gitleaks.ps1",
    "install_gitleaks.ps1",
    "GITHUB_SECURITY_POLICY.md",
    "SECURITY_AUTOMATION.md",
    "SECURITY_AUTOMATION_REPORT.md",
    "SECURITY_POLICY_REPORT.md",
    "ENTERPRISE_SECURITY.md",
    "ENTERPRISE_SECURITY_REPORT.md",
    "SECURITY_HARDENING_REPORT.md",
    "SECURITY_VALIDATION_REPORT.md",
    "SECURITY_BUG_FIX_REPORT.md",
    "SECURITY.md",
    "GIT_HOOKS.md",
    "GITLEAKS.md",
    "CHANGELOG.md",
    "PROGRESS.md",
    "BACKLOG.md",
    "README.md",
    "AI_INSTRUCTIONS.md",
    "PROJECT_RULES.md"
)

# Placeholder values permitted in documentation & source code defaults (e.g. SQLite URLs, type annotations)
$placeholderValuesRegex = '(?i)^(your_.*|<.*>|change_this|placeholder|example|sqlite:.*|your_jwt_secret.*|xxx+|\.\.\.|sk-\.\.\.|"sqlite:.*"|''sqlite:.*'')$'

# Sensitive Variable Names Matching (handles optional type annotations like : str = or : string =)
$varAssignmentRegex = '(?i)(OPENAI_API_KEY|GEMINI_API_KEY|CLAUDE_API_KEY|ANTHROPIC_API_KEY|AWS_SECRET_ACCESS_KEY|AWS_ACCESS_KEY_ID|GITHUB_TOKEN|GITHUB_PAT|JWT_SECRET|DATABASE_URL|SMTP_PASSWORD|BEARER_TOKEN|API_KEY|SECRET_KEY|ACCESS_TOKEN|CLIENT_SECRET|PRIVATE_KEY)\s*(?::\s*[a-zA-Z0-9_\[\]]+)?\s*[:=]\s*["'']?([^\s"'']*)'

# Secret Pattern Signatures
$secretPatterns = @(
    @{ Name = "OpenAI Key Pattern"; Pattern = 'sk-[a-zA-Z0-9_-]{10,}' },
    @{ Name = "Gemini / Google AI Key Pattern"; Pattern = 'AIzaSy[a-zA-Z0-9_-]{33}' },
    @{ Name = "Claude / Anthropic Key Pattern"; Pattern = 'sk-ant-[a-zA-Z0-9_-]{10,}' },
    @{ Name = "HuggingFace Token Pattern"; Pattern = 'hf_[a-zA-Z0-9]{34}' },
    @{ Name = "AWS Access Key Pattern"; Pattern = 'AKIA[0-9A-Z]{16}' },
    @{ Name = "Azure Key Pattern"; Pattern = 'AccountKey=[a-zA-Z0-9+/=]{88}' },
    @{ Name = "GitHub PAT Pattern"; Pattern = '(ghp_[a-zA-Z0-9]{36}|github_pat_[a-zA-Z0-9_-]{22,})' },
    @{ Name = "JWT Secret Token Pattern"; Pattern = 'eyJ[a-zA-Z0-9_-]{10,}\.eyJ[a-zA-Z0-9_-]{10,}\.' },
    @{ Name = "Private Key Header Pattern"; Pattern = '-----BEGIN (RSA|EC|OPENSSH|DSA|PRIVATE) KEY-----' }
)

function Test-LineSecurity {
    param (
        [string]$FilePath,
        [int]$LineNumber,
        [string]$LineContent
    )

    $fileName = Split-Path $FilePath -Leaf
    $isDocFile = ($FilePath -match '\.md$' -or $fileName -eq ".env.example" -or $FilePath -match 'docs[/\\]' -or $whitelistedDocFiles -contains $fileName)

    # 1. Check Secret Pattern Signatures
    foreach ($p in $secretPatterns) {
        if ($LineContent -match $p.Pattern) {
            # Skip pattern matches in whitelisted doc files or markdown doc files
            if ($isDocFile -or $whitelistedDocFiles -contains $fileName) { continue }

            Write-Host "`n====================================================" -ForegroundColor Red
            Write-Host "                SECURITY SCAN FAILED                " -ForegroundColor Red
            Write-Host "====================================================" -ForegroundColor Red
            Write-Host "Secret Signature Detected ($($p.Name)):" -ForegroundColor Red
            Write-Host "File: $FilePath" -ForegroundColor Red
            Write-Host "Line: $LineNumber" -ForegroundColor Red
            Write-Host "Content: $($LineContent.Trim())" -ForegroundColor Red
            return $false
        }
    }

    # 2. Check Variable Assignment Pattern
    if ($LineContent -match $varAssignmentRegex) {
        $assignedVal = $matches[2].Trim()
        
        # If value is empty or matches known placeholder patterns / sqlite URLs
        if ([string]::IsNullOrWhiteSpace($assignedVal) -or $assignedVal -match $placeholderValuesRegex -or $assignedVal.StartsWith("sqlite:")) {
            return $true
        }

        # If inside doc file and assigned value looks like placeholder or generic text
        if ($isDocFile) {
            return $true
        }

        Write-Host "`n====================================================" -ForegroundColor Red
        Write-Host "                SECURITY SCAN FAILED                " -ForegroundColor Red
        Write-Host "====================================================" -ForegroundColor Red
        Write-Host "Sensitive Variable Assignment Detected:" -ForegroundColor Red
        Write-Host "File: $FilePath" -ForegroundColor Red
        Write-Host "Line: $LineNumber" -ForegroundColor Red
        Write-Host "Content: $($LineContent.Trim())" -ForegroundColor Red
        return $false
    }

    return $true
}

# Stage 1: Audit Staged Files in Git Index (git diff --cached)
Write-Host "`n[1/4] Auditing Git staged index (git diff --cached)..." -ForegroundColor Yellow
if ($gitExe -and (Test-Path ".git")) {
    $stagedFiles = (& $gitExe diff --cached --name-only 2>$null)
    foreach ($stagedFile in $stagedFiles) {
        if ([string]::IsNullOrWhiteSpace($stagedFile)) { continue }
        if ($stagedFile -match 'scripts[/\\]bin') { continue }

        $stagedContent = (& $gitExe show ":$stagedFile" 2>$null)
        if ([string]::IsNullOrWhiteSpace($stagedContent)) { continue }

        $lineNum = 0
        $lines = $stagedContent -split "\r?\n"
        foreach ($line in $lines) {
            $lineNum++
            $passed = Test-LineSecurity -FilePath $stagedFile -LineNumber $lineNum -LineContent $line
            if (-not $passed) { exit 1 }
        }
    }
}
Write-Host "  [OK] Git staged index scan clean." -ForegroundColor Green

# Stage 2: Audit tracked .env files in Git
Write-Host "[2/4] Auditing Git working tree for tracked secret files..." -ForegroundColor Yellow
if (Test-Path ".env") {
    if ($gitExe) {
        $isEnvTracked = (& $gitExe ls-files .env 2>$null)
        if (-not [string]::IsNullOrWhiteSpace($isEnvTracked)) {
            Write-Host "`n[FAIL] SECURITY SCAN FAILED" -ForegroundColor Red
            Write-Host "Detected tracked .env file in Git repository: .env" -ForegroundColor Red
            exit 1
        }
    }
}

# Stage 3: Audit restricted file patterns in workspace
Write-Host "[3/4] Checking workspace for forbidden credential files..." -ForegroundColor Yellow
$forbiddenFiles = @(
    "credentials.json",
    "service-account.json",
    "firebase-adminsdk.json",
    "secret.json",
    "secrets.json",
    "token.json",
    "oauth.json"
)

foreach ($f in $forbiddenFiles) {
    $found = Get-ChildItem -Path . -Recurse -Filter $f -ErrorAction SilentlyContinue | 
        Where-Object { $_.FullName -notmatch '\\(node_modules|dist|\.venv|\.git|scripts\\bin)\\' }
    
    if ($found) {
        Write-Host "`n[FAIL] SECURITY SCAN FAILED" -ForegroundColor Red
        Write-Host "Forbidden credential file detected: $($found[0].FullName)" -ForegroundColor Red
        exit 1
    }
}

# Stage 4: Audit root environment files & workspace directories
Write-Host "[4/4] Performing workspace scan for variables & secrets..." -ForegroundColor Yellow

$rootEnvFiles = Get-ChildItem -Path . -File -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -match '^\.env' -and $_.Name -ne '.env.example' }

foreach ($envFile in $rootEnvFiles) {
    $lines = Get-Content -Path $envFile.FullName -ErrorAction SilentlyContinue
    $lineNum = 0
    foreach ($line in $lines) {
        $lineNum++
        $passed = Test-LineSecurity -FilePath $envFile.FullName -LineNumber $lineNum -LineContent $line
        if (-not $passed) { exit 1 }
    }
}

$targetDirs = @("frontend", "backend", "electron", "scripts", "docs")

foreach ($dir in $targetDirs) {
    if (-not (Test-Path $dir)) { continue }
    
    $files = Get-ChildItem -Path $dir -Recurse -File -ErrorAction SilentlyContinue |
        Where-Object { 
            $_.FullName -notmatch '\\(node_modules|dist|\.venv|\.git|build|\.vite|scripts\\bin)\\' -and
            $_.Extension -notmatch '\.(png|jpg|jpeg|ico|gif|woff|woff2|ttf|eot|sqlite3|db)$'
        }

    foreach ($file in $files) {
        try {
            $lines = Get-Content -Path $file.FullName -ErrorAction SilentlyContinue
            if (-not $lines) { continue }

            $lineNum = 0
            foreach ($line in $lines) {
                $lineNum++
                $passed = Test-LineSecurity -FilePath $file.FullName -LineNumber $lineNum -LineContent $line
                if (-not $passed) { exit 1 }
            }
        } catch {}
    }
}

Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "                SECURITY SCAN PASSED                " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green
exit 0
