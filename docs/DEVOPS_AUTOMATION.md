# VNEXIFY Creator OS DevOps Automation Guide

- Version: v0.1
- Creation Date: 2026-08-06
- Role: DevOps Automation Engineer
- Target Script: `scripts/release.ps1`

---

## Table of Contents

- [1. Overview](#1-overview)
- [2. Prerequisites](#2-prerequisites)
- [3. Script Workflow](#3-script-workflow)
- [4. Usage & Command Examples](#4-usage--command-examples)
- [5. Expected Console Output](#5-expected-console-output)
- [6. Error Handling & Exit Codes](#6-error-handling--exit-codes)
- [7. Safety & Execution Policy](#7-safety--execution-policy)

---

# 1. Overview

The `scripts/release.ps1` script provides an automated PowerShell workflow for local Git release tasks in **VNEXIFY Creator OS**. It verifies repository state, inspects working tree changes, stages updated files, creates formatted commits, and pushes directly to `origin main`.

---

# 2. Prerequisites

- **PowerShell 5.1** or **PowerShell Core 7+** (Windows 10/11 native).
- **Git** installed and available on system `PATH`.
- Active working tree directory inside the `VNEXIFY` Git repository.

---

# 3. Script Workflow

```
[START] ➔ Verify Git Repo Root (git rev-parse)
          │
          ├── [Not a Git Repo] ➔ Exit with error code 1
          │
          └── [Git Repo Verified] ➔ Display 'git status'
                                    │
                                    ├── [Clean Tree / Nothing to Commit] ➔ Print "Nothing to commit." ➔ Exit 0
                                    │
                                    └── [Unstaged / Staged Changes Found]
                                          │
                                          ├── Check Commit Message Parameter
                                          │     ├── [Missing] ➔ Prompt interactively via Read-Host
                                          │     └── [Provided] ➔ Proceed
                                          │
                                          ├── Stage All Files (git add .)
                                          ├── Create Commit (git commit -m "<message>")
                                          ├── Push to Origin (git push origin main)
                                          │
                                          └── [SUCCESS] ➔ Display Branch, Hash, and Message Summary
```

---

# 4. Usage & Command Examples

### Example 1: Direct Parameter Release (Recommended)
```powershell
.\scripts\release.ps1 "Sprint 9: Database foundation"
```

### Example 2: Interactive Commit Prompt
If executed without arguments:
```powershell
.\scripts\release.ps1
```
The script will prompt:
`Enter release commit message:`

---

# 5. Expected Console Output

### Successful Release Output Example
```text
====================================================
    VNEXIFY Creator OS - Git Release Automation    
====================================================

[1/5] Checking Git repository status...
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  modified:   docs/CHANGELOG.md

[2/5] Staging workspace changes (git add .)...
[3/5] Creating Git commit: 'Sprint 8: Backend foundation'...
[main a1b2c3d] Sprint 8: Backend foundation
 1 file changed, 5 insertions(+)

[4/5] Pushing changes to origin main...
To github.com:vnexify/VNEXIFY-Creator-OS.git
   a1b2c3d..e5f6g7h  main -> main

====================================================
        Release completed successfully!             
====================================================
Current Branch: main
Latest Hash:    e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0
Latest Message: Sprint 8: Backend foundation
```

### Clean Tree Output Example
```text
====================================================
    VNEXIFY Creator OS - Git Release Automation    
====================================================

[1/5] Checking Git repository status...
On branch main
nothing to commit, working tree clean

[INFO] Nothing to commit. Workspace is clean.
```

---

# 6. Error Handling & Exit Codes

| Exit Code | Condition | Behavior |
| :--- | :--- | :--- |
| `0` | Clean workspace or successful push | Displays success metrics and exits cleanly. |
| `1` | Directory is not a Git repository | Prints `[ERROR] Current directory is not a valid Git repository.` |
| `1` | Empty commit message entered | Prints `[ERROR] Commit message cannot be empty. Release cancelled.` |
| `$LASTEXITCODE` | `git add`, `git commit`, or `git push` fails | Displays native Git error traceback and exits immediately. |

---

# 7. Safety & Execution Policy

> [!CAUTION]
> The release automation script MUST NOT be executed automatically during CI/CD or build validation steps without human review. Always verify `git status` prior to triggering release pushes.
