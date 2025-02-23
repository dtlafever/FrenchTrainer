from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlmodel import create_engine, Session
from sqlalchemy import select

from contextlib import asynccontextmanager
from decouple import config
import random

from src.db import create_db_and_tables
from src.models.flashcard import Flashcard, ShowFlashcard

from chainlit.utils import mount_chainlit

DB_URL = config('DATABASE_URL')
engine = create_engine(DB_URL, echo=False)

# Dependency: Get the session
def get_session():
    with Session(engine) as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup functions
    create_db_and_tables(engine)
    # include_router(app)
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

@app.post("/flashcards", response_model=ShowFlashcard)
def create_flashcard(flashcard: Flashcard, session: Session = Depends(get_session)):
    session.add(flashcard)
    session.commit()
    session.refresh(flashcard)
    return flashcard

@app.get("/flashcards", response_model=list[ShowFlashcard])
def read_flashcards(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    flashcards = session.exec(select(Flashcard).offset(skip).limit(limit)).all()
    return flashcards

@app.get("/flashcards/{flashcard_id}", response_model=ShowFlashcard)
def read_flashcard(flashcard_id: int, session: Session = Depends(get_session)):
    flashcard = session.get(Flashcard, flashcard_id)
    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return flashcard
