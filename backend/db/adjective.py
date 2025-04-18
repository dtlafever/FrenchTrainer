from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select, text, or_

from backend.models.adjective import Adjective
from backend.db.session import get_session

#TODO: update and delete functions

def create_adjective_in_db(adjective: Adjective, session: Session = Depends(get_session)) -> Adjective:
    session.add(adjective)
    session.commit()
    session.refresh(adjective)
    return adjective

def retrieve_adjective_from_db(id: int, session: Session = Depends(get_session)) -> Adjective:
    adjective = session.get(Adjective, id)
    return adjective

def retrieve_random_adjective_from_db(session: Session = Depends(get_session)) -> Adjective:
    statement = select(Adjective).order_by(text('RANDOM()')).limit(1)
    results = session.exec(statement)
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    random_adjective = results.first()
    if random_adjective is not None:
        random_adjective = random_adjective[0]
    return random_adjective

def retrieve_all_adjectives_from_db(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> list[Adjective]:
    statement = select(Adjective).offset(skip).limit(limit)
    adjectives = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    adjectives = [adjective[0] for adjective in adjectives]
    return adjectives

def retrieve_adjective_from_db_by_adjective(adj: str, session: Session = Depends(get_session)) -> Adjective | None:
    statement = select(Adjective).where(
        or_(
            Adjective.masc_french_singular == adj,
            Adjective.masc_french_plural == adj,
            Adjective.fem_french_singular == adj,
            Adjective.fem_french_plural == adj,
            Adjective.english_text == adj
        )
    )

    result_adj = session.exec(statement).first()
    if result_adj is not None:
        result_adj = result_adj[0]
    return result_adj
