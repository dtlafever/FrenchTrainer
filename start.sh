#!/bin/bash

echo "Starting French Trainer application..."

# Make sure we have a database directory
mkdir -p backend/instance

# Build and start the containers
docker-compose build
docker-compose up -d

# Wait for backend to be ready
echo "Waiting for backend to be ready..."
sleep 5

# Migrate existing database if needed
echo "Checking for existing database to migrate..."
docker-compose exec backend bash -c "if [ -f /app/backend/db.sqlite3 ] && [ ! -f /app/backend/instance/db.sqlite3 ]; then
  echo 'Moving existing database to volume...'
  cp /app/backend/db.sqlite3 /app/backend/instance/
  echo 'Database moved successfully'
fi"

# Run database migrations with error handling
echo "Running database migrations..."
docker-compose exec backend bash -c "cd /app/backend && alembic upgrade head || true"

# Pull the LLM model
echo "Pulling the LLM model (deepseek-r1:8b)..."
docker-compose exec ollama ollama pull deepseek-r1:8b

echo "Application is running!"
echo "Frontend: http://localhost"
echo "Backend API: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"