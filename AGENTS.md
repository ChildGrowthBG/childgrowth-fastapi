# AGENTS.md

## Setup
- This is a FastAPI backend managed with `uv`; use `uv sync` after dependency changes.
- Python is pinned to `3.14.4` in `.python-version` and `pyproject.toml` requires `>=3.14.4`.
- Required env vars are listed in `.env.example`: `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_NAME`, `DB_PORT`, `JWT_KEY`.
- Settings load `.env` via `python-dotenv` in `app/config.py`; importing DB-dependent modules can fail if env vars are missing.

## Commands
- Install/sync dependencies: `uv sync`.
- Run the dev server: `uv run fastapi dev app/main.py`.
- Alternative server command: `uv run uvicorn app.main:app --reload`.
- Focused syntax check: `uv run python -m py_compile path/to/file.py`.
- Format/lint tool available: `uv run ruff check .`; there is no repo-specific Ruff config yet.
- There is currently no test suite or test command in the repo.

## App Wiring
- FastAPI entrypoint is `app/main.py`; it creates `app`, configures CORS, includes routers, and defines `GET /health`.
- CORS is intentionally limited to the frontend dev port: `http://localhost:5173` and `http://127.0.0.1:5173`.
- Auth routes live in `app/routers/auth_router.py` under `/auth`.
- Request/response models live in `app/schemas/`; keep API response shapes as Pydantic models when adding endpoints.
- Business logic belongs in `app/services/`; database access belongs in function-based repositories under `app/repository/`.
- DB sessions are async SQLAlchemy sessions from `app/db.py`; route handlers should inject `AsyncSession` with `Depends(get_db)` and pass it down.

## Database
- The app uses async PostgreSQL via `postgresql+asyncpg://...` composed in `app/config.py`.
- `app/models/user.py` defines the `users` ORM model; keep it aligned with `migrations/001_create_user_table.sql`.
- There is no Alembic setup; migrations are plain SQL files under `migrations/`.
- Existing repository functions commit inside the repository (`insert_user` commits and refreshes); preserve or deliberately change that transaction boundary.

## Auth Notes
- Password hashing is wrapped in `app/auth/password.py`; use `hash_password` and `check_hashed_password` instead of calling Werkzeug directly.
- JWT creation and verification live in `app/dependancies/token.py`; tokens use `sub` as the user id and expire after 30 days.
- The package directory is spelled `dependancies`, not `dependencies`; use the existing spelling in imports.
