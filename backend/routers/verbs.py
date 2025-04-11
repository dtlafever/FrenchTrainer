from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session

from backend.models.verb import ShowFrenchVerb, create_and_get_verb_conjugations
from backend.db.session import get_session
from backend.utils import lookup_french_verbs_from_bescherelle, lookup_french_verbs_from_lefigaro
from backend.db.verb import retrieve_verb_from_db, retrieve_all_verbs_from_db, retrieve_random_verb_flashcard_from_db, retrieve_verb_from_db_by_verb, create_verb_with_dict_in_db

router = APIRouter(
    prefix="/verbs",
    tags=["verbs"],
    dependencies=[], # TODO: add any tokens are security we might need
    responses={404: {"description": "Not found"}},
)

# =============================
# API Routes (returning JSON)
# =============================

@router.post("/", response_model=ShowFrenchVerb, status_code=status.HTTP_201_CREATED)
def create_verb(verb: str, session: Session = Depends(get_session)):
    # First check if verb exists in database
    existing_verb = retrieve_verb_from_db_by_verb(verb, session)

    if existing_verb:
        return existing_verb

    # If not in database, lookup in Bescherelle
    verb_dict = lookup_french_verbs_from_bescherelle(verb)
    if verb_dict["error"] is True:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Verb not found in Bescherelle.")

    # lookup verb on le figaro for english translation
    verb_english_dict = lookup_french_verbs_from_lefigaro(verb)
    if verb_english_dict["error"] is True:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Verb not found in Le Figaro.")
    
    # create verb conjugations objects
    verb_conj_objects = create_and_get_verb_conjugations(verb_dict)
    
    # Create the verb in the database with all its conjugations
    new_verb = create_verb_with_dict_in_db(verb_dict, verb_english_dict, verb_conj_objects, session)
    if new_verb is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Verb not created.")
    
    return new_verb

@router.get("/", response_model=list[ShowFrenchVerb])
def read_verbs(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    verbs = retrieve_all_verbs_from_db(skip, limit, session)
    return verbs

@router.get("/search", response_model=ShowFrenchVerb)
def search_verbs(verb: str, session: Session = Depends(get_session)):
    """Search for a verb using any form"""
    verb = retrieve_verb_from_db_by_verb(verb, session)

    if verb is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Verb not found")

    return verb

# =============================
# Web Routes (returning HTML)
# =============================

@router.get("/random", response_model=ShowFrenchVerb)
def read_random_flashcard(session: Session = Depends(get_session)):
    flashcard = retrieve_random_verb_flashcard_from_db(session)
    # TODO: double check if this is the right way to handle this. Maybe it should always return a flashcard?
    if flashcard is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No flashcards found")
    return flashcard

@router.get("/{verb_id}", response_model=ShowFrenchVerb)
def read_verb(verb_id: int, session: Session = Depends(get_session)):
    verb = retrieve_verb_from_db(verb_id, session)
    if verb is None:
        raise HTTPException(status_code=404, detail="Verb not found")
    return verb
