# VNEXIFY Creator OS File Structure

- Version: v0.1
- Creation Date: 2026-08-06

## Table of Contents

- [Overview](#overview)
- [Top-level Structure](#top-level-structure)
- [Frontend Structure](#frontend-structure)
- [Electron Structure](#electron-structure)
- [Backend Structure](#backend-structure)
- [Supporting Directories](#supporting-directories)
- [Related Documents](#related-documents)
- [Future Updates](#future-updates)

## Overview

This document describes the folder and file organization for the VNEXIFY Creator OS project.

## Top-level Structure

- `frontend/` - React + TypeScript app
- `electron/` - Electron shell bootstrap
- `backend/` - Python FastAPI service
- `docs/` - Documentation
- `assets/` - Static assets
- `config/` - Configuration templates
- `logs/` - Logging outputs
- `exports/` - Exported build artifacts or data
- `scripts/` - Automation scripts
- `plugins/` - Extension/plugin code
- `tests/` - Test scaffolding

## Frontend Structure

- `frontend/package.json` - frontend dependencies and scripts
- `frontend/tsconfig.json` - TypeScript config
- `frontend/vite.config.ts` - Vite build config
- `frontend/public/` - static HTML and assets
- `frontend/src/` - React application source

## Electron Structure

- `electron/package.json` - Electron dependencies and scripts
- `electron/tsconfig.json` - Electron TypeScript config
- `electron/src/main.ts` - Electron main process
- `electron/src/preload.ts` - Preload script placeholder

## Backend Structure

- `backend/requirements.txt` - Python dependencies
- `backend/app/main.py` - FastAPI app entrypoint
- `backend/app/api/router.py` - API router
- `backend/app/core/` - configuration and DB helpers
- `backend/db/` - SQLite database storage

## Supporting Directories

- `docs/` - Project documentation
- `assets/` - shared design and media assets
- `config/` - environment and runtime config templates
- `logs/` - log files and diagnostic output
- `scripts/` - automation scripts and utilities
- `plugins/` - plugin architecture extensions
- `tests/` - test fixtures and scenarios

## Related Documents

- [PROJECT.md](PROJECT.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [TECH_STACK.md](TECH_STACK.md)

## Future Updates

- Add file-level descriptions for all new modules
- Add naming conventions and placement rules
