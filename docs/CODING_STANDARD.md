# VNEXIFY Creator OS Coding Standards

- Version: v0.1
- Creation Date: 2026-08-06

## Table of Contents

- [Introduction](#introduction)
- [General Principles](#general-principles)
- [JavaScript / TypeScript Standards](#javascript--typescript-standards)
- [Python Standards](#python-standards)
- [Documentation Standards](#documentation-standards)
- [Code Review Guidelines](#code-review-guidelines)
- [Related Documents](#related-documents)
- [Future Updates](#future-updates)

## Introduction

This document defines code style, naming, and quality expectations for the VNEXIFY Creator OS project.

## General Principles

- Write readable, maintainable code.
- Prefer explicit over implicit behavior.
- Keep functions small and focused.
- Document assumptions and non-obvious decisions.

## JavaScript / TypeScript Standards

- Use TypeScript for all frontend and Electron code.
- Prefer strict typing and avoid `any` when possible.
- Organize imports alphabetically.
- Keep files small and logically grouped.

## Python Standards

- Use clear module and function names.
- Prefer type annotations for public APIs.
- Keep backend modules small and isolated.
- Use `snake_case` for functions and variables.

## Documentation Standards

- Document public modules and API endpoints.
- Keep README and docs up to date.
- Reference related docs in headers and cross-links.

## Code Review Guidelines

- Verify architecture and scope before approving changes.
- Ensure no application features are added during environment-only phases unless explicitly requested.
- Use this document to validate style consistency.

## Related Documents

- [DEVELOPMENT_WORKFLOW.md](DEVELOPMENT_WORKFLOW.md)
- [GIT_WORKFLOW.md](GIT_WORKFLOW.md)
- [TESTING_STRATEGY.md](TESTING_STRATEGY.md)

## Future Updates

- Add linting rules and examples.
- Add formatting guidelines for Markdown and config files.
- Add best practices for AI-assisted code generation.
