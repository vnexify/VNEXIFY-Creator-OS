# VNEXIFY Creator OS Official AI Operating Manual & Instructions

- **Version**: v1.0
- **Status**: Official & Binding AI Operating Manual
- **Creation Date**: 2026-08-06
- **Scope**: Mandatory for all AI Assistants, AI Agents, Prompt Engineers, and Human Developers

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Scope & Applicability](#2-scope--applicability)
- [3. General AI Principles](#3-general-ai-principles)
- [4. AI Communication Rules](#4-ai-communication-rules)
- [5. Decision Making Rules](#5-decision-making-rules)
- [6. Architecture Authority](#6-architecture-authority)
- [7. Implementation Rules](#7-implementation-rules)
- [8. Review Process](#8-review-process)
- [9. Escalation Rules](#9-escalation-rules)
- [10. Code Generation Rules](#10-code-generation-rules)
- [11. Documentation Rules](#11-documentation-rules)
- [12. Git Workflow Rules](#12-git-workflow-rules)
- [13. DevOps Rules](#13-devops-rules)
- [14. Security Rules](#14-security-rules)
- [15. Testing Rules](#15-testing-rules)
- [16. Forbidden Actions](#16-forbidden-actions)
- [17. AI Responsibilities & Role Specializations](#17-ai-responsibilities--role-specializations)
  - [17.1. ChatGPT](#171-chatgpt)
  - [17.2. Antigravity](#172-antigravity)
  - [17.3. Google AI Studio](#173-google-ai-studio)
  - [17.4. Stitch](#174-stitch)
  - [17.5. Ollama](#175-ollama)
  - [17.6. GitHub Copilot (Future)](#176-github-copilot-future)
  - [17.7. Future AI Providers](#177-future-ai-providers)
- [18. AI Collaboration Workflow](#18-ai-collaboration-workflow)
- [19. Decision Authority Matrix](#19-decision-authority-matrix)
- [20. Future AI Expansion Rules](#20-future-ai-expansion-rules)

---

# 1. Purpose

This document serves as the **Official AI Operating Manual for VNEXIFY Creator OS**. It governs how artificial intelligence assistants, multi-agent frameworks, and automated LLM extensions operate within the codebase. Every AI agent interacting with this project MUST comply strictly with these instructions.

---

# 2. Scope & Applicability

These AI instructions apply to all AI models, extensions, local assistants, and cloud generation platforms used in the development lifecycle:
- Architectural planning models (ChatGPT)
- Code implementation and refactoring agents (Google Antigravity)
- Prototyping and UI generation platforms (Google AI Studio, Stitch)
- Local offline coding assistants (Ollama)
- Future inline completions and agents (GitHub Copilot, Claude, Gemini, Cursor, Windsurf, OpenAI Codex)

---

# 3. General AI Principles

1. **Constitution First**: `PROJECT_RULES.md` is the supreme law of the codebase. No AI instruction or generated code may override it.
2. **Context Inspection First**: Prior to editing any file or creating a new module, inspect authoritative codebase files and existing documentation under `docs/`.
3. **No Assumptions or Speculation**: Inspect physical file contents to verify exact imports, signatures, variable names, and schemas.
4. **Zero Code Duplication**: Reuse existing classes, stores, utility functions, and components.
5. **Empirical Verification**: Never claim a task is complete without running verification routines (`npm run build:frontend`, `npx tsc`, `python import check`).

---

# 4. AI Communication Rules

- **Concise & Direct Summaries**: Responses to the user must be clear, structured, and professional. Avoid fluff.
- **Markdown & Hyperlinks**: Use GitHub-style markdown with exact `file://` scheme links when referring to workspace files (e.g., [PROJECT_RULES.md](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/docs/PROJECT_RULES.md)).
- **Transparent Output**: Always clearly outline changes made, files modified, and verification results obtained.

---

# 5. Decision Making Rules

- **Strict Authority Boundaries**: AI agents must only operate within their assigned role boundary (see [Section 19. Decision Authority Matrix](#19-decision-authority-matrix)).
- **Approval Gates**: Major structural changes, database schema modifications, or dependency additions require explicit user approval.
- **No Unilateral Scope Creep**: Implement only requested features for the current sprint. Do not perform out-of-scope refactoring.

---

# 6. Architecture Authority

- **Supreme Architectural Blueprint**: `ARCHITECTURE.md` defines the official multi-tier architecture (React + Electron + FastAPI + SQLite).
- **Sole Architect Role**: ChatGPT holds sole authority over architecture design and sprint roadmap planning.
- **Clean Architecture Enforcer**: All code generated must enforce strict separation between UI, Service, and Repository layers.

---

# 7. Implementation Rules

- **Incremental Edits**: Apply precise code replacements using chunk replace tools rather than replacing entire files unnecessarily.
- **Preserve Docstrings & Comments**: Retain pre-existing documentation, docstrings, and non-obvious code rationale.
- **Strict Typing**: Enforce TypeScript strict mode (`tsconfig.json`) and Python PEP 484 type annotations on all signatures.

---

# 8. Review Process

1. **Self-Audit**: The implementation AI must self-audit generated code against `PROJECT_RULES.md` and static analysis rules.
2. **Architect Review**: ChatGPT or the user reviews proposed pull requests or multi-file diffs.
3. **Automated Verification**: Verification scripts (`scripts/health.ps1` and `scripts/build.ps1`) must pass with exit code 0.

---

# 9. Escalation Rules

- **Build Failures**: If a build fails, immediately fetch un-truncated error logs, identify the exact broken line, apply a root-cause fix, and re-verify.
- **Conflicting Requirements**: If user instructions conflict with `PROJECT_RULES.md`, halt execution, explain the conflict, and request clarification.
- **Irreversible Data Loss Warning**: Never execute commands that delete files, drop tables, or alter git histories without explicit user consent.

---

# 10. Code Generation Rules

- **No Placeholder Code**: Never generate `TODO`, `// implement later`, or stub functions in production files.
- **Strict Component Isolation**: Store layout components under `frontend/src/components/layout/`, cards under `components/cards/`, widgets under `components/common/`, and pages under `pages/`.
- **Backend Standard**: Use FastAPI versioned routers (`/api/v1/`), Pydantic schemas, `AppException` subclasses, and generic repositories.

---

# 11. Documentation Rules

Every AI agent completing an implementation or sprint task MUST update:
1. [docs/CHANGELOG.md](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/docs/CHANGELOG.md): Add concise entries under the current version release.
2. [docs/PROGRESS.md](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/docs/PROGRESS.md): Mark completed items, current status, and in-progress tasks.
3. [docs/BACKLOG.md](file:///c:/Users/viren/OneDrive/Desktop/VNEXIFY/docs/BACKLOG.md): Update task statuses to `Completed` and record dependencies.
4. **Sprint Report**: Generate a dedicated markdown report (`docs/SPRINT_X_REPORT.md` or `docs/FEATURE_REPORT.md`).

---

# 12. Git Workflow Rules

- **Status Check First**: Always run `git status` prior to initiating changes and after completing work.
- **Clean Commits**: Commit messages must follow conventional formatting (`feat:`, `fix:`, `docs:`, `devops:`).
- **Working Tree Integrity**: Never leave untracked temporary scratch files in root directories.

---

# 13. DevOps Rules

- **Pre-Task Health Check**: Run `scripts/health.ps1` to verify baseline environment health before starting major tasks.
- **Pre-Release Build Check**: Run `scripts/build.ps1` to verify frontend build, Electron compilation, and backend imports.
- **Controlled Release Script**: Use `scripts/release.ps1` only after build verification succeeds.
- **No Automatic Script Execution**: Always inspect script contents using `Get-Content` before running automation scripts.

---

# 14. Security Rules

- **GitHub Security Policy Compliance**: Every AI assistant MUST obey the official [GITHUB_SECURITY_POLICY.md](GITHUB_SECURITY_POLICY.md).
- **No Secrets in Source Code or Docs**: Secrets, API keys, tokens, passwords, and private keys MUST NEVER be placed inside source code, configs, markdown, reports, or logs.
- **Dynamic `.env` Runtime Settings**: Secrets MUST be loaded dynamically from `.env`. Maintain `.env.example` with ONLY clean placeholder strings.
- **Git Ignore Protection**: Verify that `.gitignore` excludes `.env`, `.env.*`, `*.pem`, `*.key`, `credentials.json`, `service-account.json`, etc.
- **Automated Stop Gate**: If any secret is detected, HALT execution immediately, output a Security Warning, and DO NOT commit or push to Git.
- **No Secret Printing**: Never print or echo secret values in terminal output, logs (`logs/backend.log`), markdown, or sprint reports.
- **Accidental Exposure Remediation**: If a credential is accidentally pasted, do NOT save it or repeat it; immediately recommend moving it to `.env` and rotating the exposed credential.
- **Input Sanitization**: Validate all inputs using Pydantic models in FastAPI and strict schemas in React.
- **Error Envelope Sanitization**: Never leak raw database tracebacks or internal system paths to frontend clients.


---

# 15. Testing Rules

- **Static Analysis Gate**: Code must compile cleanly via `npm run build:frontend`, `npx tsc --project electron/tsconfig.json`, and Python module check.
- **Regression Prevention**: Maintain pre-existing working API endpoints (such as `GET /health`) and UI state hooks.

---

# 16. Forbidden Actions

No AI assistant operating on VNEXIFY Creator OS may ever:

> [!CAUTION]
> 1. NEVER delete or overwrite stable, working application code.
> 2. NEVER ignore project documentation or bypass `PROJECT_RULES.md`.
> 3. NEVER ignore build failures or health diagnostic errors.
> 4. NEVER modify unrelated files or undertake out-of-scope refactoring.
> 5. NEVER alter established folder structures (`frontend/`, `electron/`, `backend/`, `docs/`, `scripts/`).
> 6. NEVER create duplicate utility classes or redundant state hooks.
> 7. NEVER introduce circular dependencies or inline business logic inside UI components.
> 8. NEVER push unverified or broken builds to remote Git repositories.

---

# 17. AI Responsibilities & Role Specializations

## 17.1. ChatGPT

### Primary Responsibilities
- Product Architecture & System Design
- Sprint Planning & Project Roadmap
- Documentation Review & Consistency Audit
- Code Review & QA Gatekeeping
- Risk Analysis & Architectural Decisions
- Prompt Engineering Governance

### Must Always
- Review existing architecture before suggesting structural changes.
- Protect project standards and enforce `PROJECT_RULES.md`.
- Ensure sprint quality and complete Definition of Done compliance.
- Verify consistency across documentation and codebase.

### Must Never
- Rewrite the entire project unnecessarily.
- Ignore project documentation.
- Break Clean Architecture boundaries.
- Skip architectural code reviews.

---

## 17.2. Antigravity

### Primary Responsibilities
- Code Implementation & Multi-file Edits
- Refactoring & Codebase Organization
- Folder & File Scaffolding
- Component & State Store Creation
- Backend Development (FastAPI, SQLAlchemy, Pydantic, Alembic)
- Frontend Development (React, TypeScript, Vite)
- DevOps Automation Scripts (`build.ps1`, `health.ps1`, `release.ps1`)
- End-to-End Integration & System Verification

### Must Always
- Read project documentation under `docs/` before making changes.
- Follow `PROJECT_RULES.md` strictly without deviation.
- Generate modular, reusable, self-documenting code.
- Update documentation suite (`CHANGELOG.md`, `PROGRESS.md`, `BACKLOG.md`).
- Generate detailed Sprint and Feature Reports.
- Verify frontend build (`npm run build:frontend`) and Electron compilation (`npx tsc`).
- Verify system health via `scripts/health.ps1`.

### Must Never
- Redesign system architecture without explicit approval.
- Delete stable working code or baseline documentation.
- Skip updating system documentation logs.
- Ignore build failures or compiler errors.
- Ignore health diagnostic failures.
- Modify unrelated files outside the prompt scope.

---

## 17.3. Google AI Studio

### Primary Responsibilities
- React UI Layout Prototyping
- Tailwind CSS Component Design
- Visual Dashboard Layout Generation
- UX Micro-interaction Improvements
- Component Styling & Aesthetics

### Must Never
- Generate backend application logic.
- Create database schemas or ORM models.
- Modify REST API router definitions.
- Change project architecture or folder structure.
- Refactor existing core state management.

---

## 17.4. Stitch

### Primary Responsibilities
- UI/UX Design System & Token Generation
- Color Palette & Dark Theme Consistency
- Visual Wireframes & ASCII Component Layouts
- High-Fidelity UI Mockups & Visual Hierarchy
- User Interaction Flow Specifications

### Must Never
- Generate production backend code.
- Alter project folder structure.
- Modify database models or SQL migrations.
- Create architectural specifications outside UI/UX domain.

---

## 17.5. Ollama

### Primary Responsibilities
- Local Offline Coding Assistant
- Code Debugging & Snippet Analysis
- Algorithm Optimization & Math Helpers
- Standalone Utility Function Generation
- Local Stack Trace & Error Diagnostics

### Must Never
- Change system architecture or design patterns.
- Delete codebase modules or project directories.
- Refactor the entire project layout.
- Modify official project documentation automatically.

---

## 17.6. GitHub Copilot (Future)

### Primary Responsibilities
- Real-time Inline Code Completion
- Single-line Syntax & Method Auto-completion
- Local Boilerplate Boilerplate Snippets

### Must Never
- Design system architecture.
- Replace core application modules.
- Create project folder structures.

---

## 17.7. Future AI Providers

The following sections reserve role definitions for future AI integrations:

- **Claude**: Complex multi-file reasoning, deep logic verification, and security auditing. Must never alter core DB schemas without approval.
- **Gemini**: Multimodal vision analysis, data visualization layout generation, and performance optimization. Must never bypass build verification.
- **Cursor**: Inline multi-file refactoring and IDE navigation assistance. Must follow `PROJECT_RULES.md` and Clean Architecture boundaries.
- **Windsurf**: Real-time context awareness and workspace cascade refactoring. Must never delete stable code modules.
- **OpenAI Codex**: Automated test script generation and API client SDK generation. Must never introduce direct DB calls in frontend SDKs.

---

# 18. AI Collaboration Workflow

All development tasks in VNEXIFY Creator OS MUST follow this exact multi-stage workflow:

```
                  ┌───────────────────────────────┐
                  │          USER PROMPT          │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │            CHATGPT            │
                  │   (Planning & Architecture)   │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │          ANTIGRAVITY          │
                  │   (Implementation Agent)      │
                  └───────┬───────────────┬───────┘
                          │               │
            ┌─────────────┴─┐           ┌─┴─────────────┐
            │ AI STUDIO /   │           │    OLLAMA     │
            │    STITCH     │           │  (Debugging)  │
            │(UI Design Specs)          └─┬─────────────┘
            └─────────────┬─┘             │
                          │               │
                          └───────┬───────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │            CHATGPT            │
                  │    (Code & QA Review Gate)    │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │      HEALTH SCRIPT CHECK      │
                  │     (scripts/health.ps1)      │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │       BUILD SCRIPT CHECK      │
                  │      (scripts/build.ps1)      │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │      RELEASE SCRIPT CHECK     │
                  │     (scripts/release.ps1)     │
                  └───────────────┬───────────────┘
                                  │
                                  ▼
                  ┌───────────────────────────────┐
                  │       GITHUB REPOSITORY       │
                  │        (main branch)          │
                  └───────────────────────────────┘
```

---

# 19. Decision Authority Matrix

To prevent role overlap and conflicts, decision authority is strictly assigned as follows:

| Decision Domain | Authorized AI / Tool | Final Approval |
| :--- | :--- | :--- |
| **Architecture & System Design** | **ONLY ChatGPT** | Lead Architect / User |
| **Code Implementation & Refactoring** | **Google Antigravity** | Lead Architect / User |
| **UI Design, Layout & Tokens** | **Google AI Studio + Stitch** | UX Architect / User |
| **Local Debugging & Error Analysis** | **Ollama** | Developer / User |
| **Release & Sprint Approval** | **ONLY ChatGPT** | Product Owner / User |

---

# 20. Future AI Expansion Rules

1. **Role Non-Overlap Principle**: New AI tools added to the project must be assigned a distinct, non-overlapping specialty in Section 17.
2. **Constitution Inheritance**: Any future AI provider added MUST inherit `PROJECT_RULES.md` and `AI_INSTRUCTIONS.md` as prompt constraints.
3. **No Unsanctioned AI Execution**: No automated AI tool may modify project files without explicit prompt delegation by the user.
