from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from sqlalchemy import select

from contextlib import asynccontextmanager
import random

from backend.db.session import create_db_and_tables, get_session
from backend.routers.base import api_router
from backend import tts

from backend.models.flashcard import Flashcard

from chainlit.utils import mount_chainlit

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup functions
    create_db_and_tables()
    app.include_router(api_router)
    yield
    # Shutdown functions go here

app = FastAPI(lifespan=lifespan)

# Add CORS middleware to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount the chainlit LLM to its own path
mount_chainlit(app=app, target="cl_app.py", path="/chat")

@app.get("/api/speak")
async def api_speak(text: str, lang: str = "fr-FR"):
    if not text:
        raise HTTPException(status_code=400, detail="Missing text parameter")
    await tts.async_speak_text(text, lang)
    return {"status": "success"}

# NOTE: For all other routes, see the routers directory