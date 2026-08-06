# VNEXIFY Creator OS

VNEXIFY Creator OS is a desktop application scaffold designed to support a React + TypeScript + Vite frontend, an Electron desktop shell, and a Python FastAPI backend.

## Project Structure

- `frontend/` - React + TypeScript + Vite application
- `electron/` - Electron shell and desktop application bootstrap
- `backend/` - Python FastAPI backend with SQLite support
- `docs/` - Project documentation and roadmap
- `assets/` - Shared media, icons, and design assets
- `exports/` - Exported data and build artifacts
- `logs/` - Runtime and developer log output
- `config/` - Configuration templates and environment examples
- `scripts/` - Project automation and bootstrap scripts
- `plugins/` - Plugin architecture and extension points
- `tests/` - Test scaffolding and fixtures

## Getting Started

1. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Install Electron dependencies:
   ```bash
   cd electron
   npm install
   ```

3. Install backend dependencies:
   ```bash
   python -m pip install -r backend/requirements.txt
   ```

4. Start the backend:
   ```bash
   npm run dev:backend
   ```

5. Start the frontend:
   ```bash
   npm run dev:frontend
   ```

6. Start Electron:
   ```bash
   npm run dev:electron
   ```

## Roadmap

See `docs/roadmap.md` for an early development roadmap and priorities.
