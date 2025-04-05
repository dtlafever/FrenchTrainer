from fastapi import Depends
from sqlmodel import Session
from sqlalchemy import select, or_, text

from backend.models.verb import FrenchVerb
from backend.db.session import get_session

#TODO: update and delete functions

# TODO: should we add a function for each sub table in the db? Or just French Verb?

def create_verb_with_dict_in_db(verb_dict, verb_english_dict, verb_conj_objects, session) -> FrenchVerb | None:
    """
    Create a new verb with all of its conjugations in the database.
    
    Args:
        verb_dict: Dictionary containing basic verb information from Bescherelle
        verb_english_dict: Dictionary containing English translation
        verb_conj_objects: Dictionary containing conjugation objects
        session: SQLAlchemy session
    
    Returns:
        FrenchVerb: The created verb with all relations populated
    """
    # Add the verb conjugations to the database
    for _, new_obj in verb_conj_objects.items():
        session.add(new_obj)
    
    # Create the main verb object
    new_verb = FrenchVerb(
        english_text=verb_english_dict["english_text"],
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
    
    # Add, commit and refresh
    session.add(new_verb)
    session.commit()
    
    # Refresh all objects to ensure they have their database-generated IDs
    for _, new_obj in verb_conj_objects.items():
        session.refresh(new_obj)
    session.refresh(new_verb)
    
    return new_verb

def create_verb_in_db(verb: FrenchVerb, session: Session = Depends(get_session)) -> FrenchVerb | None:
    session.add(verb)
    session.commit()
    session.refresh(verb)
    return verb

def retrieve_verb_from_db(id: int, session: Session = Depends(get_session)) -> FrenchVerb | None:
    verb = session.get(FrenchVerb, id)
    return verb

def retrieve_all_verbs_from_db(skip: int = 0, limit: int = 10, session: Session = Depends(get_session)) -> list[FrenchVerb]:
    statement = select(FrenchVerb).offset(skip).limit(limit)
    verbs = session.exec(statement).all()
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    verbs = [verb[0] for verb in verbs]
    return verbs

def retrieve_verb_from_db_by_verb(verb_form: str, session: Session = Depends(get_session)) -> FrenchVerb | None:
    """
    Find a verb by any of its conjugated forms using SQL JOINs for efficient searching.
    
    This function searches through all verb forms (infinitif, participe present, participe passe,
    etc) to find a match.
    
    Args:
        verb_form (str): The verb form to search for
        session (Session, optional): Database session. Defaults to Depends(get_session).
        
    Returns:
        Optional[FrenchVerb]: The matching verb or None if not found
    """
    # First check the main verb table (infinitif, participe_present, participe_passe)
    statement = select(FrenchVerb).where(
        or_(
            FrenchVerb.infinitif == verb_form,
            FrenchVerb.participe_present == verb_form,
            FrenchVerb.participe_passe == verb_form
        )
    )
    
    result = session.exec(statement).first()
    if result:
        return result[0]
    
    # Build a complex query with all tenses joined
    from backend.models.verb import (
        FrenchIndicatifPresent, FrenchIndicatifImparfait, FrenchIndicatifPasseSimple,
        FrenchIndicatifFuturSimple, FrenchConditionnelPresent, FrenchSubjonctifPresent,
        FrenchSubjonctifImparfait, FrenchImperatifPresent, FrenchIndicatifPasseCompose,
        FrenchIndicatifPlusQueParfait, FrenchIndicatifPasseAnterieur, FrenchIndicatifFuturAnterieur,
        FrenchConditionnelPasse, FrenchSubjonctifPasse, FrenchSubjonctifPlusQueParfait,
        FrenchImperatifPasse
    )
    
    # Create a query that joins all the conjugation tables
    query = select(FrenchVerb)
    
    # Add all the left joins
    query = (query
        .outerjoin(FrenchIndicatifPresent)
        .outerjoin(FrenchIndicatifImparfait)
        .outerjoin(FrenchIndicatifPasseSimple)
        .outerjoin(FrenchIndicatifFuturSimple)
        .outerjoin(FrenchConditionnelPresent)
        .outerjoin(FrenchSubjonctifPresent)
        .outerjoin(FrenchSubjonctifImparfait)
        .outerjoin(FrenchImperatifPresent)
        .outerjoin(FrenchIndicatifPasseCompose)
        .outerjoin(FrenchIndicatifPlusQueParfait)
        .outerjoin(FrenchIndicatifPasseAnterieur)
        .outerjoin(FrenchIndicatifFuturAnterieur)
        .outerjoin(FrenchConditionnelPasse)
        .outerjoin(FrenchSubjonctifPasse)
        .outerjoin(FrenchSubjonctifPlusQueParfait)
        .outerjoin(FrenchImperatifPasse)
    )
    
    # We'll construct a complex OR condition for all the conjugated forms
    conditions = []
    
    # Indicatif present
    conditions.extend([
        FrenchIndicatifPresent.je == verb_form,
        FrenchIndicatifPresent.tu == verb_form,
        FrenchIndicatifPresent.il_elle == verb_form,
        FrenchIndicatifPresent.nous == verb_form,
        FrenchIndicatifPresent.vous == verb_form,
        FrenchIndicatifPresent.ils_elles == verb_form
    ])
    
    # Indicatif imparfait
    conditions.extend([
        FrenchIndicatifImparfait.je == verb_form,
        FrenchIndicatifImparfait.tu == verb_form,
        FrenchIndicatifImparfait.il_elle == verb_form,
        FrenchIndicatifImparfait.nous == verb_form,
        FrenchIndicatifImparfait.vous == verb_form,
        FrenchIndicatifImparfait.ils_elles == verb_form
    ])
    
    # Indicatif passe simple
    conditions.extend([
        FrenchIndicatifPasseSimple.je == verb_form,
        FrenchIndicatifPasseSimple.tu == verb_form,
        FrenchIndicatifPasseSimple.il_elle == verb_form,
        FrenchIndicatifPasseSimple.nous == verb_form,
        FrenchIndicatifPasseSimple.vous == verb_form,
        FrenchIndicatifPasseSimple.ils_elles == verb_form
    ])
    
    # Indicatif futur simple
    conditions.extend([
        FrenchIndicatifFuturSimple.je == verb_form,
        FrenchIndicatifFuturSimple.tu == verb_form,
        FrenchIndicatifFuturSimple.il_elle == verb_form,
        FrenchIndicatifFuturSimple.nous == verb_form,
        FrenchIndicatifFuturSimple.vous == verb_form,
        FrenchIndicatifFuturSimple.ils_elles == verb_form
    ])
    
    # Conditionnel present
    conditions.extend([
        FrenchConditionnelPresent.je == verb_form,
        FrenchConditionnelPresent.tu == verb_form,
        FrenchConditionnelPresent.il_elle == verb_form,
        FrenchConditionnelPresent.nous == verb_form,
        FrenchConditionnelPresent.vous == verb_form,
        FrenchConditionnelPresent.ils_elles == verb_form
    ])
    
    # Subjonctif present
    conditions.extend([
        FrenchSubjonctifPresent.je == verb_form,
        FrenchSubjonctifPresent.tu == verb_form,
        FrenchSubjonctifPresent.il_elle == verb_form,
        FrenchSubjonctifPresent.nous == verb_form,
        FrenchSubjonctifPresent.vous == verb_form,
        FrenchSubjonctifPresent.ils_elles == verb_form
    ])
    
    # Subjonctif imparfait
    conditions.extend([
        FrenchSubjonctifImparfait.je == verb_form,
        FrenchSubjonctifImparfait.tu == verb_form,
        FrenchSubjonctifImparfait.il_elle == verb_form,
        FrenchSubjonctifImparfait.nous == verb_form,
        FrenchSubjonctifImparfait.vous == verb_form,
        FrenchSubjonctifImparfait.ils_elles == verb_form
    ])
    
    # Imperatif present
    conditions.extend([
        FrenchImperatifPresent.tu == verb_form,
        FrenchImperatifPresent.nous == verb_form,
        FrenchImperatifPresent.vous == verb_form
    ])
    
    # Indicatif passe compose
    conditions.extend([
        FrenchIndicatifPasseCompose.je == verb_form,
        FrenchIndicatifPasseCompose.tu == verb_form,
        FrenchIndicatifPasseCompose.il_elle == verb_form,
        FrenchIndicatifPasseCompose.nous == verb_form,
        FrenchIndicatifPasseCompose.vous == verb_form,
        FrenchIndicatifPasseCompose.ils_elles == verb_form
    ])
    
    # Indicatif plus que parfait
    conditions.extend([
        FrenchIndicatifPlusQueParfait.je == verb_form,
        FrenchIndicatifPlusQueParfait.tu == verb_form,
        FrenchIndicatifPlusQueParfait.il_elle == verb_form,
        FrenchIndicatifPlusQueParfait.nous == verb_form,
        FrenchIndicatifPlusQueParfait.vous == verb_form,
        FrenchIndicatifPlusQueParfait.ils_elles == verb_form
    ])
    
    # Indicatif passe anterieur
    conditions.extend([
        FrenchIndicatifPasseAnterieur.je == verb_form,
        FrenchIndicatifPasseAnterieur.tu == verb_form,
        FrenchIndicatifPasseAnterieur.il_elle == verb_form,
        FrenchIndicatifPasseAnterieur.nous == verb_form,
        FrenchIndicatifPasseAnterieur.vous == verb_form,
        FrenchIndicatifPasseAnterieur.ils_elles == verb_form
    ])
    
    # Indicatif futur anterieur
    conditions.extend([
        FrenchIndicatifFuturAnterieur.je == verb_form,
        FrenchIndicatifFuturAnterieur.tu == verb_form,
        FrenchIndicatifFuturAnterieur.il_elle == verb_form,
        FrenchIndicatifFuturAnterieur.nous == verb_form,
        FrenchIndicatifFuturAnterieur.vous == verb_form,
        FrenchIndicatifFuturAnterieur.ils_elles == verb_form
    ])
    
    # Conditionnel passe
    conditions.extend([
        FrenchConditionnelPasse.je == verb_form,
        FrenchConditionnelPasse.tu == verb_form,
        FrenchConditionnelPasse.il_elle == verb_form,
        FrenchConditionnelPasse.nous == verb_form,
        FrenchConditionnelPasse.vous == verb_form,
        FrenchConditionnelPasse.ils_elles == verb_form
    ])
    
    # Subjonctif passe
    conditions.extend([
        FrenchSubjonctifPasse.je == verb_form,
        FrenchSubjonctifPasse.tu == verb_form,
        FrenchSubjonctifPasse.il_elle == verb_form,
        FrenchSubjonctifPasse.nous == verb_form,
        FrenchSubjonctifPasse.vous == verb_form,
        FrenchSubjonctifPasse.ils_elles == verb_form
    ])
    
    # Subjonctif plus que parfait
    conditions.extend([
        FrenchSubjonctifPlusQueParfait.je == verb_form,
        FrenchSubjonctifPlusQueParfait.tu == verb_form,
        FrenchSubjonctifPlusQueParfait.il_elle == verb_form,
        FrenchSubjonctifPlusQueParfait.nous == verb_form,
        FrenchSubjonctifPlusQueParfait.vous == verb_form,
        FrenchSubjonctifPlusQueParfait.ils_elles == verb_form
    ])
    
    # Imperatif passe
    conditions.extend([
        FrenchImperatifPasse.nous == verb_form,
        FrenchImperatifPasse.vous == verb_form
    ])
    
    # Add the WHERE clause with all our OR conditions
    query = query.where(or_(*conditions))
    
    # Execute the query, limiting to 1 result
    verb = session.exec(query).first()

    if verb is not None:
        verb = verb[0]
    return verb

def retrieve_random_verb_flashcard_from_db(session: Session = Depends(get_session)) -> FrenchVerb | None:
    statement = select(FrenchVerb).order_by(text('RANDOM()')).limit(1)
    results = session.exec(statement)
    # TODO: figure out how to use session.exec properly. Currently it is returning a tuple
    random_verb = results.first()
    if random_verb is not None:
        random_verb = random_verb[0]
    return random_verb
