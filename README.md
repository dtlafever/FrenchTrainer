<h1 align="center">French Trainer</h1>

<p align="center">
<b>A project focused on learning french and learning backend engineering and LLMs!</b>
</p>

## Features
- Basic Flashcards
- Local LLM chat (requires Ollama server running)

## Dev Installation
1. Open a terminal and run:
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

## To Be Implemented
1. Add more granularity to storing french words in our database. For example, we want to store the various conjugations for a french verb
2. Show various forms of a given word in the flash cards (i.e. third person singular verbs, the feminine version of a noun, etc).
3. Implement a RAG to use with our french database to practice using the words in sentences with our LLM.
4. add autocomplete/fill for french words you are adding to your flashcards from some external database or api. This will require using something like a Trie data structure.
5. Implement proper security
 a. (JWT)[https://jwt.io/introduction]
 b. [CSRF Protection](https://www.stackhawk.com/blog/csrf-protection-in-fastapi/)
 c. [OAuth2](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/)
 d. [General Security Explanation and Best Practices](https://fastapi.tiangolo.com/tutorial/security/#fastapi-utilities)
6. Py Testing
7. Linting
8. Proper Frontend (Cross Platform?)

 ## Flashcards to be added
 - Days of the week
 - most important verbs
 - phrases