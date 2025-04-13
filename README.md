<h1 align="center">French Trainer</h1>

<p align="center">
<b>A project focused on learning french and learning fullstack engineering and LLMs!</b>
</p>

## Features
- Basic Flashcards
- Local LLM chat (requires Ollama server running)
- French Verb lookup and conjugations (passive voice only for the moment)

### Backend
- FastAPI: our backend API
- SQLModel: how we define our Database Models
- Alembic: handles Database migrations
- Beautiful Soup: web scrapping for looking up verb tenses
- Ollama and Chainlit: LLM library and LLM UI, as well as Model Context Protocol (MCP) for read only access to our database using and LLM.

### Frontend
- React: UI library
- TypeScript: type safety
- Tailwind CSS: styling
- React Router: navigation
- Axios: API requests

### Does this project use any AI Code Generation?
Yes it does. I know that code generation is contentious for some, and potentially dangerous for a developer's learning, but I firmly believe that is not only the future of development, I also believe if it is used correctly can be an aide to learning new frameworks and reducing tedium. I use Github Copilot for some auto complete and for receiving advice on changes to make to the project. I attempt to back that up by reading documentation on specific frameworks and doing my own research on the internet as well. I am also experimenting with tools such as Claude Code, but I think agentic coding has some polishing before it is ready for more complex projects.

Ultimately, I see LLM Code Generation as another tool under my belt to help me develop and learn the large breadth of concepts needed to be a good developer.

## Installation

### Option 1: Docker Deployment (Recommended)

1. Install [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)

2. Run the start script:
```bash
./start.sh
```

This will:
- Start all services (frontend, backend, and Ollama)
- Run database migrations
- Pull the LLM model (deepseek-r1:8b)

The application will be available at:
- Frontend: [http://localhost](http://localhost)
- Backend API: [http://localhost:8000](http://localhost:8000)
- API Documentation: [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: Manual Development Setup

The easiest way is to run the script `setup_local.sh`. Alternatively, you can execute the steps below.

#### Backend
1. Open a terminal and run:
`cd backend`
`mkdir instances`
`uv run -- fastapi dev main.py --host 0.0.0.0 --port 8000`

This will install all the packages required and start up the fastapi server. You should be able to access the fastapi server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

#### Frontend
1. Open a new terminal window and run:
```bash
cd frontend
npm install
nvm install 22.14.0
nvm use 22.14.0
npm run dev
```

This will start the React development server. You can access the frontend at [http://localhost:5173](http://localhost:5173).

2. Install Ollama (if you want LLMs)
- [Ollama](https://ollama.com/download) should be installed. If you run ollama using Docker, it should be started and running on port `11434`.

3. Create a `.env` file in the `backend` folder and fill out the following fields:
```
LLM_MODEL="phi4-mini"
SYSTEM_PROMPT_FILE="basic_prompt.txt"
DATABASE_URL="sqlite:///flashcards.db"
```
Feel free to change to whatever llm model you want from [ollama](https://ollama.com/search). For system prompt, this is the prompt you will use to define how you want your chatbot to behave. for now we just have a placeholder one. Finally, the database_url is can be left alone for the moment since the only database we are using is a sqlite database with basic flashcards.

## Model Context Protocol
### Clients
- Option 1: [Claude Desktop](https://claude.ai/download)
  - Go to Settings->Developer->Edit Config:
```json
{
    "mcpServers": {
        "frenchtrainer-mcp-proxy": {
            "command": "uv",
            "args": [
            "tool",
            "run",
            "mcp-proxy",
            "http://127.0.0.1:8000/mcp"
            ]
        }
    }
}
  - restart the client and you should see a little hammer icon and a number.
```
- Option 2: Use the built in Chainlit client built into the app. Go to http://127.0.0.1:8000/chat
  - Click on the adaptor icon and Fill in the name field with `frenchtrainer_mcp`, type with `SSE`, and Server URL with `http://localhost:8000/mcp`.
  - NOTE: the first time you run this LLM, it might take a few minutes to be ready as it is downloading the LLM from Ollama Servers.

## Migrations
### Just Starting
If for some reason alembic (our lib for database migrations) is not created, we can recreate it using `alembic init migrations` inside `backend`. Assuming it is created, we can create our first migration (if not already created) by calling:

`alembic revision --autogenerate -m "initial"`

This will create our first migration to create our tables. Once we have that migration created, we can run our migration using the following command:

`alembic upgrade head`

We now have successfully completed our first migration!

### Adding new migrations
1. Create new migration file:
`alembic revision --autogenerate -m "INSERT TASK HERE"`
2. Make any changes needed for your database in your revision file stored in `backend/alembic/versions` folder. It should be named a revision number + the text your wrote when creating the revision. This should be done automatically using `-autogenerate`.
3. Run the latest migration:
`alembic upgrade head`

### Getting Information
1. Get our current revision:
`alembic current`
2. Get history:
`alembic history --verbose`

### Downgrade
1. Downgrade to our base migration (nothing)
`alembic downgrade base`
 a. (optional) We can then build our migrations back up again from nothing
 `alembic upgrade head`

 ### Resources
 - [SQLModel + Alembic Setup](https://arunanshub.hashnode.dev/using-sqlmodel-with-alembic)

## PyTesting
`pytest`

## Linting
`uv run ruff check   # Lint all files in the current directory.`
`uv run ruff check --fix # Lint all files in the current directory and fix what we can.`
`uv run ruff format  # Format all files in the current directory.`

## To Be Implemented
1. ~~Add more granularity to storing french words in our database. For example, we want to store the various conjugations for a french verb~~
 a. Update Verb Models to support passive voice instead of only active.
2. ~~Add migrations to our app to ensure smooth updates to our database.~~
3. Show various forms of a given word in the flash cards (i.e. third person singular verbs, the feminine version of a noun, etc).
4. ~Implement a RAG to use with our french database to practice using the words in sentences with our LLM.~
 a. fix MCP connection to local LLM chainlit server. It currently only works for external servers like Claude Desktop.
5. add autocomplete/fill for french words you are adding to your flashcards from some external database or api. This will require using something like a Trie data structure.
6. ~~Be able to add or search a verb using  tense. That way I dont need to know the infinitive.~~
7. Implement proper security
 a. (JWT)[https://jwt.io/introduction]
 b. [CSRF Protection](https://www.stackhawk.com/blog/csrf-protection-in-fastapi/)
 c. [OAuth2](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
 d. [General Security Explanation and Best Practices](https://fastapi.tiangolo.com/tutorial/security/#fastapi-utilities)
8. ~~Py Testing~~
  a. ~~Test Utils~~
  b. ~~Test Flashcards~~
  c. Test Verbs
  d. Test Adjs
9. Linting
10. ~~Proper Frontend (React with Vite)~~
11. React Testing
12. Combine all types of words into a singular Flashcard Stack instead of seperate stacks.
13. Be able to search all words at the same time instead of just one type at a time (i.e. only verbs, or only adjs, etc)

 ## Flashcards to be added
 - Days of the week
 - most important verbs
 - phrases