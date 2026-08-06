# VNEXIFY Creator OS Official Project Constitution & Rules

- **Version**: v1.0
- **Status**: Official & Binding Architecture Constitution
- **Creation Date**: 2026-08-06
- **Scope**: Mandatory for all Developers, AI Agents, Product Owners, and DevOps Engineers

---

## Table of Contents

- [1. Purpose](#1-purpose)
- [2. Scope & Applicability](#2-scope--applicability)
- [3. AI Responsibilities](#3-ai-responsibilities)
- [4. Developer Responsibilities](#4-developer-responsibilities)
- [5. Project Standards](#5-project-standards)
- [6. Development Rules](#6-development-rules)
- [7. Architecture Rules](#7-architecture-rules)
- [8. Coding Rules](#8-coding-rules)
- [9. Documentation Rules](#9-documentation-rules)
- [10. Git Rules](#10-git-rules)
- [11. DevOps Rules](#11-devops-rules)
- [12. UI & Frontend Rules](#12-ui--frontend-rules)
- [13. Backend Rules](#13-backend-rules)
- [14. Database Rules](#14-database-rules)
- [15. Security Rules](#15-security-rules)
- [16. Testing Rules](#16-testing-rules)
- [17. Release Rules](#17-release-rules)
- [18. Sprint Rules](#18-sprint-rules)
- [19. Definition of Done](#19-definition-of-done)
- [20. Forbidden Actions](#20-forbidden-actions)
- [21. AI Safety Rules](#21-ai-safety-rules)
- [22. Future Expansion Rules](#22-future-expansion-rules)

---

# 1. Purpose

This document serves as the **Official Constitution of VNEXIFY Creator OS**. It establishes non-negotiable architectural constraints, coding standards, workflow procedures, security policies, and AI safety protocols. Every future sprint, pull request, code modification, and automated tool invocation MUST adhere strictly to these rules without exception.

---

# 2. Scope & Applicability

These rules apply to all workspace directories and technology layers within the project repository:
- `frontend/` (React, TypeScript, Vite)
- `electron/` (Electron Desktop Shell, TypeScript)
- `backend/` (Python, FastAPI, SQLAlchemy, Pydantic, Alembic)
- `scripts/` (PowerShell Automation Systems)
- `docs/` (System Architecture & Sprint Documentation)
- `tests/` (Unit, Integration, and End-to-End Test Suites)

---

# 3. AI Responsibilities

AI tools and agents operating within the VNEXIFY Creator OS ecosystem have specialized, non-overlapping roles:

| AI Agent / Tool | Assigned Specialty & Responsibility | Forbidden Actions |
| :--- | :--- | :--- |
| **ChatGPT** | System Architecture Design, Sprint Planning, Code Review | Direct code refactoring or execution without user prompt |
| **Google Antigravity** | Codebase Implementation, Refactoring, Multi-file Edits, Verification | Redesigning architecture without explicit user approval |
| **Google AI Studio** | Prototyping UI Component Layouts & Design References | Direct overwriting of core architecture or backend logic |
| **Stitch** | UI/UX Visual Specs, Color Tokens & Aesthetic Wireframes | Generating production backend logic or DB schemas |
| **Ollama** | Local Offline Coding Assistant & Snippet Completion | Modifying project configuration or executing system build tools |

---

# 4. Developer Responsibilities

1. **Architecture Governance**: Verify that every proposed modification complies with `ARCHITECTURE.md` and `PROJECT_RULES.md`.
2. **Code Ownership**: Audit all AI-generated code prior to merging into production branches.
3. **Build & Health Verification**: Execute `scripts/health.ps1` and `scripts/build.ps1` to confirm zero regressions.
4. **Documentation Discipline**: Update `CHANGELOG.md`, `PROGRESS.md`, `BACKLOG.md`, and Sprint Reports during every sprint.

---

# 5. Project Standards

- **Language Standards**: TypeScript strict mode (`tsconfig.json`), Python 3.10+ with type hints (PEP 484).
- **Encoding & Line Endings**: UTF-8 encoding across all text files.
- **Design Token Integrity**: Use designated theme constants (`#0f172a`, `#1e293b`, `#3b82f6`) without hardcoding arbitrary inline pixel values.

---

# 6. Development Rules

1. **Never Overwrite Stable Modules**: Existing, verified, and tested modules must never be blindly replaced.
2. **Never Redesign Architecture Without Approval**: Architectural changes require formal approval and an updated `ARCHITECTURE.md`.
3. **Never Delete Files Unless Explicitly Instructed**: Deleting source files, assets, or documentation is strictly prohibited unless requested by the user.
4. **Always Preserve Backward Compatibility**: Public interfaces, API schemas, and data contracts must maintain compatibility.
5. **Always Follow Existing Folder Hierarchy**: Respect established top-level directories (`frontend/`, `electron/`, `backend/`, `scripts/`, `docs/`).
6. **Always Review Existing Code Before Writing New Code**: Inspect authoritative files to prevent code duplication.
7. **Never Duplicate Functionality**: Reuse pre-existing utilities, components, and helper modules.

---

# 7. Architecture Rules

- **Clean Architecture & Separation of Concerns**: Maintain strict layer separation between UI Presentation, Application Logic, Domain Services, and Data Repositories.
- **Repository Pattern**: All database interactions MUST be encapsulated inside repository classes (`backend/app/repositories/`).
- **Service Layer Pattern**: All business logic MUST reside in service classes (`backend/app/services/`).
- **Dependency Injection**: Use FastAPI `Depends()` for database sessions, authentication, and core dependencies.
- **No Circular Dependencies**: Dependencies must flow strictly inward from outer layers to inner domain logic.
- **No Business Logic in UI**: React components must consume state and services, never executing direct data validation or SQL queries.
- **No Database Logic in UI Components**: Direct database connections from React or Electron are strictly forbidden.

---

# 8. Coding Rules

- **TypeScript Strict Mode**: No implicit `any` types; all interfaces, props, and functions must be fully typed.
- **Python Type Hints**: Function signatures in Python must specify parameter and return types.
- **No Dead Code**: Remove unused imports, commented-out debug code, and unreachable functions.
- **No Duplicated Code**: Abstract repeating logic into utility functions (`frontend/src/utils/` or `backend/app/core/`).
- **Self-Documenting Code**: Use descriptive function and variable names with clear, concise docstrings.

---

# 9. Documentation Rules

Every sprint MUST update the mandatory documentation suite:
1. `docs/CHANGELOG.md`: Record all added, changed, fixed, and removed items under the current version.
2. `docs/PROGRESS.md`: Update completed work, active work in progress, and next steps.
3. `docs/BACKLOG.md`: Update sprint backlog task items, priorities, and completion status.
4. `docs/SPRINT_X_REPORT.md`: Generate a comprehensive summary report detailing sprint goals, deliverables, build results, and verification metrics.

---

# 10. Git Rules

- **Branch Hygiene**: Work must be conducted on feature branches or version branches matching release targets.
- **Working Tree Verification**: Always inspect `git status` before starting work and prior to committing.
- **Commit Message Convention**: Follow conventional commits (e.g., `feat: ...`, `fix: ...`, `docs: ...`, `refactor: ...`).
- **No Broken Commits**: Code committed to Git must compile and pass static analysis checks.

---

# 11. DevOps Rules

- **Pre-Sprint Health Check**: Run `scripts/health.ps1` before starting work on a new sprint to confirm baseline health.
- **Pre-Release Build Check**: Run `scripts/build.ps1` before executing release scripts.
- **Controlled Release**: Use `scripts/release.ps1` only after `scripts/build.ps1` returns exit code 0.
- **Never Push Broken Builds**: Pushing uncompiled or failing code to remote branches is strictly forbidden.
- **Script Verification**: Inspect automation scripts using `Get-Content` before running them.

---

# 12. UI & Frontend Rules

- **React + TypeScript Strict Mode**: Component trees must strictly adhere to typed props and hooks.
- **Component Reusability**: Store layout components under `frontend/src/components/layout/`, dashboard cards under `components/cards/`, and generic widgets under `components/common/`.
- **No Inline Business Logic**: Decouple state management into custom hooks or Context stores (`frontend/src/store/`).
- **Responsive Layout**: Adhere to the 12-column grid and 4px spacing rhythm specified in `DASHBOARD_UX.md`.
- **Dark Theme Consistency**: Enforce slate dark background tones (`#0f172a`, `#1e293b`) with smooth transitions.

---

# 13. Backend Rules

- **FastAPI Framework**: Use FastAPI for all REST API endpoints.
- **Versioned API Routing**: Mount versioned routers under `/api/v1/`.
- **Pydantic Schemas**: Enforce strong input validation and typed responses using Pydantic schema models (`backend/app/schemas/`).
- **Global Exception Handling**: Throw custom `AppException` subclasses caught by centralized exception handlers returning standardized JSON envelopes.
- **Structured Logging**: Log events through `backend/app/logging/logger.py` with dual-sink logging (`sys.stdout` and `logs/backend.log`).
- **Middleware Usage**: Enforce `CORSMiddleware` and `RequestLoggingMiddleware`.

---

# 14. Database Rules

- **SQLite for Development**: Maintain local-first persistence via SQLite stored at `backend/db/vnexify.db`.
- **Alembic Migration Discipline**: Database schema updates MUST be managed exclusively via Alembic migration scripts.
- **ORM Encapsulation**: Use SQLAlchemy ORM models (`backend/app/models/`); direct execution of raw SQL strings inside service methods is forbidden.
- **No Manual Table Creation**: Do not execute raw SQL `CREATE TABLE` commands outside versioned Alembic migrations.

---

# 15. Security Rules

- **GitHub Security Policy Compliance**: All code, configuration, and documentation MUST comply strictly with [GITHUB_SECURITY_POLICY.md](GITHUB_SECURITY_POLICY.md).
- **No Secrets in Source Code**: Secrets, tokens, API keys, passwords, and private certificates must NEVER be committed or hardcoded into source files, markdown, or logs.
- **Environment Configuration**: Load runtime settings dynamically using `pydantic-settings` from `.env` files. Maintain `.env.example` with ONLY clean placeholder strings.
- **Git Ignore Protection**: `.gitignore` MUST protect `.env`, `.env.*`, `*.pem`, `*.key`, `credentials.json`, `service-account.json`, etc.
- **Automated Stop Gate**: If a secret is detected, HALT execution immediately, output a Security Warning, and DO NOT commit or push to Git.
- **Input Validation & Sanitization**: Sanitize and validate every incoming API request parameter via Pydantic models.
- **Output Sanitization**: Filter sensitive fields out of response schemas and never log secrets in stdout or log files.


---

# 16. Testing Rules

- **Automated Verification**: Run frontend build (`npm run build:frontend`), Electron compilation (`npx tsc`), and backend module checks (`python -c "from backend.app.main import app"`).
- **Unit & Integration Coverage**: Ensure business logic services have associated tests under `tests/`.
- **Zero Regression Tolerance**: A sprint is not complete if existing working features or endpoints are broken.

---

# 17. Release Rules

- **Automated Build Gate**: Releases require successful execution of `scripts/build.ps1`.
- **Health Gate**: System health check (`scripts/health.ps1`) must report `System Healthy`.
- **Documentation Gate**: `CHANGELOG.md`, `PROGRESS.md`, `BACKLOG.md`, and the Sprint Report must be fully updated.
- **Explicit Approval**: Releases must be approved by the Product Owner or Lead Architect.

---

# 18. Sprint Rules

Every sprint workflow MUST strictly follow these 9 execution steps:
1. **Review Existing Architecture**: Inspect `ARCHITECTURE.md` and existing code before editing.
2. **Build Only Requested Features**: Do not add unrequested features or undertake out-of-scope refactoring.
3. **Avoid Unrelated Refactoring**: Focus exclusively on the assigned sprint goal.
4. **Avoid Breaking Changes**: Maintain API and component backward compatibility.
5. **Pass Health Verification**: Confirm `scripts/health.ps1` passes.
6. **Pass Build Verification**: Confirm `scripts/build.ps1` passes.
7. **Generate Sprint Report**: Document outcomes in `docs/SPRINT_X_REPORT.md`.
8. **Update System Docs**: Update `CHANGELOG.md`, `PROGRESS.md`, and `BACKLOG.md`.
9. **Wait for User Approval**: Stop and wait for explicit user approval before starting the next sprint.

---

# 19. Definition of Done

A sprint or task is officially **DONE** only when:
- All functional requirements specified in the prompt are fulfilled.
- `scripts/build.ps1` completes with exit code 0 (`Build Successful!`).
- `scripts/health.ps1` completes with exit code 0 (`System Healthy`).
- Zero syntax, lint, or TypeScript compilation errors exist.
- Documentation suite (`CHANGELOG.md`, `PROGRESS.md`, `BACKLOG.md`, and Sprint Report) is updated.
- Explicit approval is obtained from the user.

---

# 20. Forbidden Actions

The following actions are strictly **FORBIDDEN**:

> [!CAUTION]
> 1. NEVER overwrite or replace working application code with dummy placeholders.
> 2. NEVER delete project directories (`frontend/`, `electron/`, `backend/`, `docs/`, `scripts/`).
> 3. NEVER alter folder hierarchy or move files without prior architectural approval.
> 4. NEVER introduce duplicate modules or utility classes when pre-existing solutions exist.
> 5. NEVER ignore build or static analysis errors.
> 6. NEVER skip updating documentation logs during a sprint.
> 7. NEVER bypass Git working tree checks or commit broken code.
> 8. NEVER hardcode API tokens, credentials, or production secrets into source files.

---

# 21. AI Safety Rules

1. **Consent Before Destructive Commands**: Before running commands that delete files, drop database tables, or destroy resources, obtain explicit user confirmation.
2. **Log Inspection First**: When diagnosing errors, fetch and read the exact error traceback before forming diagnostic hypotheses.
3. **No Symptom Masking**: Never suppress errors by wrapping broken logic in silent `try/except` blocks or commenting out assertions.
4. **Script Verification**: Inspect PowerShell scripts via `Get-Content` before suggesting or running them.

---

# 22. Future Expansion Rules

1. **PostgreSQL Migration Strategy**: Design SQLAlchemy ORM models and Alembic migrations to allow seamless migration from SQLite to PostgreSQL without refactoring business service logic.
2. **AI Provider Abstraction Layer**: Implement provider-agnostic router interfaces for local (Ollama) and cloud (Gemini/OpenAI) LLM services.
3. **Plugin Architecture Scaling**: Enforce strict isolation for third-party extensions in `plugins/` via defined hook APIs.
