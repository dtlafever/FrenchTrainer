# FrenchTrainer Development Guide

## Project Outline
A fullstack python and Typescript project consisting of:
- FastAPI backend
- SQLite database (SQLAlchemy 2.0 or greater)
- Alembic for database migrations
- React frontend using Vite and TailwindCSS

## Python version
3.12

## Build Commands
- Start server: `cd backend && uv run -- fastapi dev main.py`
- Install dependencies: `uv pip install .`

## Database Commands
- Create migration: `alembic revision --autogenerate -m "description"`
- Apply migrations: `alembic upgrade head`
- Check current version: `alembic current`

## Test Commands
- Run all tests: `pytest backend/tests`
- Run specific test: `pytest backend/tests/test_routes/test_flashcards.py::test_create_flashcard`
- Run with coverage: `pytest --cov=backend`

## Lint Commands
- Check code: `uv run ruff check`
- Auto-fix issues: `uv run ruff check --fix`
- Format code: `uv run ruff format`

## Code Style Guidelines
- Line length: 120 characters max
- Use FastAPI dependency injection pattern
- Follow SQLModel patterns for database models
- Error handling: Use FastAPI HTTPException with appropriate status codes
- Organization: Keep routers, models, and database code separate
- Testing: Write unit tests for all new functionality
- Import order: stdlib → third-party → local modules
