from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
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
templates = Jinja2Templates(directory="templates")

# mount the chainlit LLM to its own path
mount_chainlit(app=app, target="cl_app.py", path="/chat")

@app.get("/")
async def index(request: Request, session: Session = Depends(get_session)):
    flashcards = session.exec(select(Flashcard)).all()
    flashcard = random.choice(flashcards)[0] if flashcards else None
    context = {"request": request, "flashcard": flashcard}
    return templates.TemplateResponse("flashcards/index.html", context)

@app.post("/create_flashcard")
async def create_flashcard_from_form(request: Request, session: Session = Depends(get_session)):
    form = await request.form()
    question = form.get("question")
    answer = form.get("answer")
    new_flashcard = Flashcard(question=question, answer=answer)
    session.add(new_flashcard)
    session.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/api/speak")
async def api_speak(text: str, lang: str = "fr-FR"):
    if not text:
        raise HTTPException(status_code=400, detail="Missing text parameter")
    await tts.async_speak_text(text, lang)
    return {"status": "success"}

# NOTE: For all other routes, see the routers directory