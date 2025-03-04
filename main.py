from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from sqlmodel import create_engine, Session
from sqlalchemy import select

from contextlib import asynccontextmanager
from decouple import config
import random

from src.db import create_db_and_tables
from src import tts

from src.models.flashcard import Flashcard, ShowFlashcard
from src.models.verb import FrenchVerb, ShowFrenchVerb, create_and_get_verb_conjugations

from src.utils import lookup_french_verbs_from_bescherelle

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

@app.post("/flashcards", response_model=ShowFlashcard, status_code=status.HTTP_201_CREATED)
def create_flashcard(flashcard: Flashcard, session: Session = Depends(get_session)):
    session.add(flashcard)
    session.commit()
    session.refresh(flashcard)
    return flashcard

@app.get("/flashcards", response_model=list[ShowFlashcard])
def read_flashcards(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    statement = select(Flashcard).offset(skip).limit(limit)
    flashcards = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    flashcards = [flashcard[0] for flashcard in flashcards]
    return flashcards

@app.get("/flashcards/{flashcard_id}", response_model=ShowFlashcard)
def read_flashcard(flashcard_id: int, session: Session = Depends(get_session)):
    flashcard = session.get(Flashcard, flashcard_id)
    if not flashcard:
        raise HTTPException(status_code=404, detail="Flashcard not found")
    return flashcard

@app.get("/api/speak")
async def api_speak(text: str, lang: str = "fr-FR"):
    if not text:
        raise HTTPException(status_code=400, detail="Missing text parameter")
    await tts.async_speak_text(text, lang)
    return {"status": "success"}

# TODO: create a route for creating and accessing verbs

@app.post("/verbs", response_model=ShowFrenchVerb, status_code=status.HTTP_201_CREATED)
def create_verb(verb: str, session: Session = Depends(get_session)):
    # First check if verb exists in database
    existing_verb = session.exec(
        select(FrenchVerb).where(FrenchVerb.infinitif == verb)
    ).first()

    if existing_verb:
        return existing_verb

    # If not in database, lookup in Bescherelle
    verb_dict = lookup_french_verbs_from_bescherelle(verb)
    if verb_dict is None:
        raise HTTPException(status_code=404, detail="Verb not found in Bescherelle.")

    # create verb conjugations objects
    verb_conj_objects = create_and_get_verb_conjugations(verb_dict)
    
    # Add the verb conjugations to the database
    for key, new_obj in verb_conj_objects.items():
        session.add(new_obj)

    new_verb = FrenchVerb(
        infinitif=verb_dict["temps_simples"]["infinitif"],
        groupe=verb_dict["groupe"],
        auxiliaire=verb_dict["auxiliaire"],
        participe_present=verb_dict["temps_simples"]["participe"],
        participe_passe=verb_dict["temps_composes"]["participe"],
        indicatif_present=verb_conj_objects["indicatif_present"],
        indicatif_imparfait=verb_conj_objects["indicatif_imparfait"],
        indicatif_passe_simple=verb_conj_objects["indicatif_passe_simple"],
        indicatif_futur_simple=verb_conj_objects["indicatif_futur_simple"],
        conditionnel_present=verb_conj_objects["conditionnel_present"],
        subjonctif_present=verb_conj_objects["subjonctif_present"],
        subjonctif_imparfait=verb_conj_objects["subjonctif_imparfait"],
        imperatif_present=verb_conj_objects["imperatif_present"],
        indicatif_passe_compose=verb_conj_objects["indicatif_passe_compose"],
        indicatif_plus_que_parfait=verb_conj_objects["indicatif_plus_que_parfait"],
        indicatif_passe_anterieur=verb_conj_objects["indicatif_passe_anterieur"],
        indicatif_futur_anterieur=verb_conj_objects["indicatif_futur_anterieur"],
        conditionnel_passe=verb_conj_objects["conditionnel_passe"],
        subjonctif_passe=verb_conj_objects["subjonctif_passe"],
        subjonctif_plus_que_parfait=verb_conj_objects["subjonctif_plus_que_parfait"],
        imperatif_passe=verb_conj_objects["imperatif_passe"],
    )

    session.add(new_verb)
    session.commit()

    for key, new_obj in verb_conj_objects.items():
        session.refresh(new_obj)
    session.refresh(new_verb)
    
    return new_verb

@app.get("/verbs", response_model=list[ShowFrenchVerb])
def read_verbs(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    statement = select(FrenchVerb).offset(skip).limit(limit)
    verbs = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    verbs = [verb[0] for verb in verbs]
    return verbs

@app.get("/verbs/{verb_id}", response_model=ShowFrenchVerb)
def read_verb(verb_id: int, session: Session = Depends(get_session)):
    verb = session.get(FrenchVerb, verb_id)
    if not verb:
        raise HTTPException(status_code=404, detail="Verb not found")
    return verb