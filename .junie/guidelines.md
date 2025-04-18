# Project Guidelines

## Project Outline
A fullstack python and Typescript project consisting of:
- FastAPI backend (in ./backend/)
- SQLite database (SQLAlchemy 2.0 or greater)
- Alembic for database migrations
- React frontend using Vite and TailwindCSS (in ./frontend/)

## Test Commands For the Backend
- Run all tests: `pytest backend/tests`
- Run specific test: `pytest backend/tests/test_routes/test_flashcards.py::test_create_flashcard`
- Run with coverage: `pytest --cov=backend`
* Whether Junie should build the project before submitting the result

## Code Style Guidelines
- Line length: 120 characters max
- Use FastAPI dependency injection pattern
- Follow SQLModel patterns for database models
- Error handling: Use FastAPI HTTPException with appropriate status codes
- Organization: Keep routers, models, and database code separate
- Testing: Write unit tests for all new functionality
- Import order: stdlib → third-party → local modules

## General Instructions
- check the correctness of the proposed solution when possible

