<h1 align="center">French Trainer</h1>

<p align="center">
<b>A project focused on learning french and learning fullstack engineering and LLMs!</b>
</p>

## Features
- Basic Flashcards
- Local LLM chat (requires Ollama server running)
- French Verb lookup and conjugations (passive voice only for the moment)

## Libraries Used
- FastAPI: our backend api
- SQLModel: how we define our Database Models
- Alembic: handles Database migrations
- Beautiful Soup: web scrapping for looking up verb tenses
- Ollama and Chainlit: LLM library and LLM UI

## Dev Installation
1. Open a terminal and run:
`cd backend`
`uv run -- fastapi dev main.py`

This will install all the packages required and start up the fastapi server. You should be able to access the fastapi server at [http://127.0.0.1:8000](http://127.0.0.1:8000).

2. Install Ollama (if you want LLMs)
- [Ollama](https://ollama.com/download) should be installed and running

3. Create a `.env` file in the `backend` folder and fill out the following fields:
```
LLM_MODEL="deepseek-r1:8b"
SYSTEM_PROMPT_FILE="basic_prompt.txt"
DATABASE_URL="sqlite:///flashcards.db"
```
Feel free to change to whatever llm model you want from [ollama](https://ollama.com/search). For system prompt, this is the prompt you will use to define how you want your chatbot to behave. for now we just have a placeholder one. Finally, the database_url is can be left alone for the moment since the only database we are using is a sqlite database with basic flashcards.

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

## Linting
`uv run ruff check   # Lint all files in the current directory.`
`uv run ruff check --fix # Lint all files in the current directory and fix what we can.`
`uv run ruff format  # Format all files in the current directory.`

## To Be Implemented
1. ~~Add more granularity to storing french words in our database. For example, we want to store the various conjugations for a french verb~~
 a. Update Verb Models to support passive voice instead of only active.
2. ~~Add migrations to our app to ensure smooth updates to our database.~~
3. Show various forms of a given word in the flash cards (i.e. third person singular verbs, the feminine version of a noun, etc).
4. Implement a RAG to use with our french database to practice using the words in sentences with our LLM.
5. add autocomplete/fill for french words you are adding to your flashcards from some external database or api. This will require using something like a Trie data structure.
6. Implement proper security
 a. (JWT)[https://jwt.io/introduction]
 b. [CSRF Protection](https://www.stackhawk.com/blog/csrf-protection-in-fastapi/)
 c. [OAuth2](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
 d. [General Security Explanation and Best Practices](https://fastapi.tiangolo.com/tutorial/security/#fastapi-utilities)
7. ~~Py Testing~~
  a. ~~Test Utils~~
  b. ~~Test Flashcards~~
  c. Test Verbs
8. Linting
9. Proper Frontend (React with Vite)

 ## Flashcards to be added
 - Days of the week
 - most important verbs
 - phrases