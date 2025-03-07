from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select

from backend.models.verb import FrenchVerb
from backend.db.session import get_session

#TODO: update and delete functions

# TODO: should we add a function for each sub table in the db? Or just French Verb?

# def create_verb_in_db(verb: FrenchVerb, session: Session = Depends(get_session)) -> FrenchVerb:
#     session.add(verb)
#     session.commit()
#     session.refresh(verb)
#     return verb

def retrieve_verb_from_db(id: int, session: Session = Depends(get_session)) -> FrenchVerb:
    verb = session.get(FrenchVerb, id)
    return verb

def retrieve_all_verbs_from_db(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> list[FrenchVerb]:
    statement = select(FrenchVerb).offset(skip).limit(limit)
    verbs = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    verbs = [verb[0] for verb in verbs]
    return verbs