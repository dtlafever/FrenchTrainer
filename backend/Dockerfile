FROM python:3.12-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy requirements
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync

# Ensure alembic is available in PATH
RUN ln -s /app/.venv/bin/alembic /usr/local/bin/alembic

# Create backend directory and copy application code
RUN mkdir -p /app/backend
COPY backend/ /app/backend/

# update and install
RUN apt-get update && apt-get install -y sqlite3
RUN mkdir -p /app/backend/instance

# Expose port
EXPOSE 8000

# Command to run the application
WORKDIR /app/backend
CMD ["uv", "run", "--" , "fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]
