<#
.SYNOPSIS
    VNEXIFY Creator OS Release Automation Script

.DESCRIPTION
    Automates local Git release workflows for VNEXIFY Creator OS:
    Verifies Git repo state, displays status, stages files, commits with
    user-defined message, pushes to origin main, and prints release summary.

.PARAMETER CommitMessage
    The message for the Git commit. Prompted interactively if omitted.

.EXAMPLE
    .\scripts\release.ps1 -CommitMessage "Sprint 9: Database foundation"
#>

[CmdletBinding()]
param (
    [Parameter(Mandatory = $false, Position = 0)]
    [string]$CommitMessage
)

$ErrorActionPreference = "Stop"

Write-Host "====================================================" -ForegroundColor Cyan
Write-Host "    VNEXIFY Creator OS - Git Release Automation    " -ForegroundColor Cyan
Write-Host "====================================================" -ForegroundColor Cyan

# 1. Verify current directory is a Git repository
$isGitRepo = git rev-parse --is-inside-work-tree 2>$null
if ($LASTEXITCODE -ne 0 -or $isGitRepo -ne "true") {
    Write-Host "[ERROR] Current directory is not a valid Git repository." -ForegroundColor Red
    exit 1
}

# 2. Display Git Status
Write-Host "`n[1/5] Checking Git repository status..." -ForegroundColor Yellow
git status

# 3. Check for staged or unstaged changes
$statusOutput = git status --porcelain
if ([string]::IsNullOrWhiteSpace($statusOutput)) {
    Write-Host "`n[INFO] Nothing to commit. Workspace is clean." -ForegroundColor Green
    exit 0
}

# 4. Handle Commit Message parameter
if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
    Write-Host "`n[ATTENTION] No commit message provided." -ForegroundColor Yellow
    $CommitMessage = Read-Host "Enter release commit message"
    if ([string]::IsNullOrWhiteSpace($CommitMessage)) {
        Write-Host "[ERROR] Commit message cannot be empty. Release cancelled." -ForegroundColor Red
        exit 1
    }
}

# 5. Stage Changes
Write-Host "`n[2/5] Staging workspace changes (git add .)..." -ForegroundColor Yellow
git add .
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Failed to stage changes." -ForegroundColor Red
    exit $LASTEXITCODE
}

# 6. Create Commit
Write-Host "`n[3/5] Creating Git commit: '$CommitMessage'..." -ForegroundColor Yellow
git commit -m "$CommitMessage"
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Git commit failed." -ForegroundColor Red
    exit $LASTEXITCODE
}

# 7. Push to Remote Main
Write-Host "`n[4/5] Pushing changes to origin main..." -ForegroundColor Yellow
git push origin main
if ($LASTEXITCODE -ne 0) {
    Write-Host "[ERROR] Git push to origin main failed." -ForegroundColor Red
    exit $LASTEXITCODE
}

# 8. Display Success Summary
Write-Host "`n====================================================" -ForegroundColor Green
Write-Host "        Release completed successfully!             " -ForegroundColor Green
Write-Host "====================================================" -ForegroundColor Green

$currentBranch = (git branch --show-current).Trim()
$latestHash = (git log -1 --format="%H").Trim()
$latestMsg = (git log -1 --format="%s").Trim()

Write-Host "Current Branch: $currentBranch" -ForegroundColor White
Write-Host "Latest Hash:    $latestHash" -ForegroundColor White
Write-Host "Latest Message: $latestMsg" -ForegroundColor White
