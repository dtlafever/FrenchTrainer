# create .env file
echo "Creating .env file..."
echo "DATABASE_URL=sqlite:///instance/db.sqlite3" > .env
echo "LLM_MODEL=deepseek-r1:8b" >> .env
echo "SYSTEM_PROMPT_FILE=basic_prompt.txt" >> .env

# create instance directory
echo "Creating instance directory..."
mkdir -p instance

# install dependencies from pyproject.toml
echo "Installing dependencies..."
uv sync

# install frontend
npm install
nvm install 22.14.0
nvm use 22.14.0