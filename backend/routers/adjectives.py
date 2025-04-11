from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session

from backend.models.adjective import Adjective, ShowAdjective
from backend.db.session import get_session
from backend.db.adjective import retrieve_adjective_from_db, retrieve_all_adjectives_from_db, create_adjective_in_db, retrieve_random_adjective_from_db, retrieve_adjective_from_db_by_adjective

router = APIRouter(
    prefix="/adjectives",
    tags=["adjectives"],
    dependencies=[], # TODO: add any tokens are security we might need
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ShowAdjective, status_code=status.HTTP_201_CREATED)
def create_adjective(adjective: Adjective, session: Session = Depends(get_session)):
    new_adjective = create_adjective_in_db(adjective, session)
    return new_adjective

@router.get("/", response_model=list[ShowAdjective])
def read_adjectives(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    adjectives = retrieve_all_adjectives_from_db(skip, limit, session)
    return adjectives

@router.get("/random", response_model=ShowAdjective)
def read_random_adjective(session: Session = Depends(get_session)):
    adjective = retrieve_random_adjective_from_db(session)
    # TODO: double check if this is the right way to handle this. Maybe it should always return an adjective?
    if adjective is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No adjectives found")
    return adjective

# This function needs to be before the read_adjective function
@router.get("/search", response_model=ShowAdjective)
def search_adjective(adj: str, session: Session = Depends(get_session)):
    """Search for an adjective using any form"""
    adjective = retrieve_adjective_from_db_by_adjective(adj, session)

    if adjective is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adjective not found")
    return adjective

@router.get("/{adjective_id}", response_model=ShowAdjective)
def read_adjective(adjective_id: int, session: Session = Depends(get_session)):
    adjective = retrieve_adjective_from_db(adjective_id, session)
    # TODO: double check if this is the right way to handle this.
    if adjective is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Adjective not found")
    return adjective
