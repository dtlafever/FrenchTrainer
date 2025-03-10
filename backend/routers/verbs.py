from fastapi import APIRouter, status, Depends, HTTPException
from sqlmodel import Session
from sqlalchemy import select

from backend.models.verb import FrenchVerb, ShowFrenchVerb, create_and_get_verb_conjugations
from backend.db.session import get_session
from backend.utils import lookup_french_verbs_from_bescherelle
from backend.db.verb import retrieve_verb_from_db, retrieve_all_verbs_from_db

router = APIRouter(
    prefix="/verbs",
    tags=["verbs"],
    dependencies=[], # TODO: add any tokens are security we might need
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=ShowFrenchVerb, status_code=status.HTTP_201_CREATED)
def create_verb(verb: str, session: Session = Depends(get_session)):
    # First check if verb exists in database
    existing_verb = session.exec(
        select(FrenchVerb).where(FrenchVerb.infinitif == verb)
    ).first()

    if existing_verb:
        return existing_verb

    # If not in database, lookup in Bescherelle
    verb_dict = lookup_french_verbs_from_bescherelle(verb)
    if verb_dict["error"] is True:
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

@router.get("/", response_model=list[ShowFrenchVerb])
def read_verbs(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)):
    verbs = retrieve_all_verbs_from_db(skip, limit, session)
    return verbs

@router.get("/{verb_id}", response_model=ShowFrenchVerb)
def read_verb(verb_id: int, session: Session = Depends(get_session)):
    verb = retrieve_verb_from_db(verb_id, session)
    if verb is None:
        raise HTTPException(status_code=404, detail="Verb not found")
    return verb
