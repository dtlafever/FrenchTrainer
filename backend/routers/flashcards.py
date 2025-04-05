from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session

from backend.models.flashcard import Flashcard, ShowFlashcard
from backend.db.session import get_session
from backend.db.flashcard import retrieve_flashcard_from_db, retrieve_all_flashcards_from_db, create_flashcard_in_db, retrieve_random_flashcard_from_db

router = APIRouter(
    prefix="/flashcards",
    tags=["flashcards"],
    dependencies=[], # TODO: add any tokens are security we might need
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ShowFlashcard, status_code=status.HTTP_201_CREATED)
def create_flashcard(flashcard: Flashcard, session: Session = Depends(get_session)):
    new_flashcard = create_flashcard_in_db(flashcard, session)
    return new_flashcard

@router.get("/", response_model=list[ShowFlashcard])
def read_flashcards(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    flashcards = retrieve_all_flashcards_from_db(skip, limit, session)
    return flashcards

@router.get("/random", response_model=ShowFlashcard)
def read_random_flashcard(session: Session = Depends(get_session)):
    flashcard = retrieve_random_flashcard_from_db(session)
    # TODO: double check if this is the right way to handle this. Maybe it should always return a flashcard?
    if flashcard is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No flashcards found")
    return flashcard

@router.get("/{flashcard_id}", response_model=ShowFlashcard)
def read_flashcard(flashcard_id: int, session: Session = Depends(get_session)):
    flashcard = retrieve_flashcard_from_db(flashcard_id, session)
    if flashcard is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Flashcard not found")
    return flashcard
