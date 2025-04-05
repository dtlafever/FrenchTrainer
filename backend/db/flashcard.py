from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select, text

from backend.models.flashcard import Flashcard
from backend.db.session import get_session

#TODO: update and delete functions

def create_flashcard_in_db(flashcard: Flashcard, session: Session = Depends(get_session)) -> Flashcard:
    session.add(flashcard)
    session.commit()
    session.refresh(flashcard)
    return flashcard


# def create_flashcard_from_form_in_db(form_data: dict[str, str], session: Session = Depends(get_session)) -> Flashcard:
#     """Create a flashcard from form data and save it to the database.

#     Args:
#         form_data (dict[str, str]): question and answer from the form
#         session (Session, optional): session for database operations. Defaults to Depends(get_session).

#     Returns:
#         Flashcard: the created flashcard
#     """
    
#     question = form_data.get("question")
#     answer = form_data.get("answer")
#     if question and answer:
#         new_flashcard = Flashcard(question=question, answer=answer)
#         session.add(new_flashcard)
#         session.commit()
#         session.refresh(new_flashcard)
#         return new_flashcard
#     else:
#         raise ValueError("Question and answer must not be empty.")

def retrieve_flashcard_from_db(id: int, session: Session = Depends(get_session)) -> Flashcard:
    flashcard = session.get(Flashcard, id)
    return flashcard

def retrieve_random_flashcard_from_db(session: Session = Depends(get_session)) -> Flashcard:
    statement = select(Flashcard).order_by(text('RANDOM()')).limit(1)
    results = session.exec(statement)
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    random_flashcard = results.first()
    if random_flashcard is not None:
        random_flashcard = random_flashcard[0]
    return random_flashcard

def retrieve_all_flashcards_from_db(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> list[Flashcard]:
    statement = select(Flashcard).offset(skip).limit(limit)
    flashcards = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    flashcards = [flashcard[0] for flashcard in flashcards]
    return flashcards