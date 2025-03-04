from typing import Optional, List
import datetime

from sqlmodel import Field, SQLModel, Relationship

# =============
# Temps Simples
# =============

# Indicatif

class FrenchIndicatifPresent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_present")


class FrenchIndicatifImparfait(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_imparfait")


class FrenchIndicatifPasseSimple(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_passe_simple")


class FrenchIndicatifFuturSimple(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_futur_simple")


# Conditionnel

class FrenchConditionnelPresent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="conditionnel_present")


# Subjonctif

class FrenchSubjonctifPresent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="subjonctif_present")


class FrenchSubjonctifImparfait(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="subjonctif_imparfait")


# Extra

class FrenchImperatifPresent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    tu: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="imperatif_present")


# ==============
# Temps Composes
# ==============

# Indicatif

class FrenchIndicatifPasseCompose(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_passe_compose")


class FrenchIndicatifPlusQueParfait(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_plus_que_parfait")


class FrenchIndicatifPasseAnterieur(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_passe_anterieur")


class FrenchIndicatifFuturAnterieur(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="indicatif_futur_anterieur")


# Conditionnel

class FrenchConditionnelPasse(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="conditionnel_passe")


# Subjonctif

class FrenchSubjonctifPasse(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="subjonctif_passe")


class FrenchSubjonctifPlusQueParfait(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    je: str = Field(max_length=50)
    tu: str = Field(max_length=50)
    il_elle: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    ils_elles: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="subjonctif_plus_que_parfait")


# Imperatif

class FrenchImperatifPasse(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    tu: str = Field(max_length=50)
    nous: str = Field(max_length=50)
    vous: str = Field(max_length=50)
    
    # Relationship back to verb
    verb: Optional["FrenchVerb"] = Relationship(back_populates="imperatif_passe")


class FrenchVerb(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    infinitif: str = Field(max_length=50)
    groupe: int = Field()  # TODO: only allow for values 1,2, or 3
    auxiliaire: str = Field(max_length=50)

    # =============
    # Temps Simples
    # =============

    # indicatif
    indicatif_present_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifpresent.id")
    indicatif_present: Optional[FrenchIndicatifPresent] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    indicatif_imparfait_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifimparfait.id")
    indicatif_imparfait: Optional[FrenchIndicatifImparfait] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    indicatif_passe_simple_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifpassesimple.id")
    indicatif_passe_simple: Optional[FrenchIndicatifPasseSimple] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    indicatif_futur_simple_id: Optional[int] = Field(default=None, foreign_key="frenchindicatiffutursimple.id")
    indicatif_futur_simple: Optional[FrenchIndicatifFuturSimple] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # conditionnel
    conditionnel_present_id: Optional[int] = Field(default=None, foreign_key="frenchconditionnelpresent.id")
    conditionnel_present: Optional[FrenchConditionnelPresent] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # subjonctif
    subjonctif_present_id: Optional[int] = Field(default=None, foreign_key="frenchsubjonctifpresent.id")
    subjonctif_present: Optional[FrenchSubjonctifPresent] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    subjonctif_imparfait_id: Optional[int] = Field(default=None, foreign_key="frenchsubjonctifimparfait.id")
    subjonctif_imparfait: Optional[FrenchSubjonctifImparfait] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # imperative
    imperatif_present_id: Optional[int] = Field(default=None, foreign_key="frenchimperatifpresent.id")
    imperatif_present: Optional[FrenchImperatifPresent] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # participe
    participe_present: str

    # ==============
    # Temps Composes
    # ==============
    # indicatif
    indicatif_passe_compose_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifpassecompose.id")
    indicatif_passe_compose: Optional[FrenchIndicatifPasseCompose] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    indicatif_plus_que_parfait_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifplusqueparfait.id")
    indicatif_plus_que_parfait: Optional[FrenchIndicatifPlusQueParfait] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    indicatif_passe_anterieur_id: Optional[int] = Field(default=None, foreign_key="frenchindicatifpasseanterieur.id")
    indicatif_passe_anterieur: Optional[FrenchIndicatifPasseAnterieur] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    indicatif_futur_anterieur_id: Optional[int] = Field(default=None, foreign_key="frenchindicatiffuturanterieur.id")
    indicatif_futur_anterieur: Optional[FrenchIndicatifFuturAnterieur] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # conditionnel
    conditionnel_passe_id: Optional[int] = Field(default=None, foreign_key="frenchconditionnelpasse.id")
    conditionnel_passe: Optional[FrenchConditionnelPasse] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # subjonctif
    subjonctif_passe_id: Optional[int] = Field(default=None, foreign_key="frenchsubjonctifpasse.id")
    subjonctif_passe: Optional[FrenchSubjonctifPasse] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )
    
    subjonctif_plus_que_parfait_id: Optional[int] = Field(default=None, foreign_key="frenchsubjonctifplusqueparfait.id")
    subjonctif_plus_que_parfait: Optional[FrenchSubjonctifPlusQueParfait] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # imperative
    imperatif_passe_id: Optional[int] = Field(default=None, foreign_key="frenchimperatifpasse.id")
    imperatif_passe: Optional[FrenchImperatifPasse] = Relationship(
        sa_relationship_kwargs={"uselist": False},
        back_populates="verb"
    )

    # participe
    participe_passe: str

class ShowFrenchVerb(SQLModel):
    infinitif: str
    groupe: int
    auxiliaire: str
    participe_present: str
    participe_passe: str
    indicatif_present: FrenchIndicatifPresent
    indicatif_imparfait: FrenchIndicatifImparfait
    indicatif_passe_simple: FrenchIndicatifPasseSimple
    indicatif_futur_simple: FrenchIndicatifFuturSimple
    conditionnel_present: FrenchConditionnelPresent
    subjonctif_present: FrenchSubjonctifPresent
    subjonctif_imparfait: FrenchSubjonctifImparfait
    imperatif_present: FrenchImperatifPresent
    indicatif_passe_compose: FrenchIndicatifPasseCompose
    indicatif_plus_que_parfait: FrenchIndicatifPlusQueParfait
    indicatif_passe_anterieur: FrenchIndicatifPasseAnterieur
    indicatif_futur_anterieur: FrenchIndicatifFuturAnterieur
    conditionnel_passe: FrenchConditionnelPasse
    subjonctif_passe: FrenchSubjonctifPasse
    subjonctif_plus_que_parfait: FrenchSubjonctifPlusQueParfait
    imperatif_passe: FrenchImperatifPasse

    class Config(): #tells pydantic to convert even non dict obj to json
        from_attributes = True


def create_and_get_verb_conjugations(verb_dict: dict) -> dict:
    """Create and return a dictionary of French verb conjugations Objects.

    Args:
        verb_dict (dict): Created from `lookup_french_verbs_from_bescherelle`

    Returns:
        dict: A dictionary of French verb conjugations Objects. These have not been committed to the database yet
    """
    temps_simples = verb_dict["temps_simples"]
    temps_composes = verb_dict["temps_composes"]

    new_indicatif_present = FrenchIndicatifPresent(
        je=temps_simples["indicatif"]["Présent"][0],
        tu=temps_simples["indicatif"]["Présent"][1],
        il_elle=temps_simples["indicatif"]["Présent"][2],
        nous=temps_simples["indicatif"]["Présent"][3],
        vous=temps_simples["indicatif"]["Présent"][4],
        ils_elles=temps_simples["indicatif"]["Présent"][5]
    )

    new_indicatif_imparfait = FrenchIndicatifImparfait(
        je=temps_simples["indicatif"]["Imparfait"][0],
        tu=temps_simples["indicatif"]["Imparfait"][1],
        il_elle=temps_simples["indicatif"]["Imparfait"][2],
        nous=temps_simples["indicatif"]["Imparfait"][3],
        vous=temps_simples["indicatif"]["Imparfait"][4],
        ils_elles=temps_simples["indicatif"]["Imparfait"][5]
    )

    new_indicatif_passe_simple = FrenchIndicatifPasseSimple(
        je=temps_simples["indicatif"]["Passé simple"][0],
        tu=temps_simples["indicatif"]["Passé simple"][1],
        il_elle=temps_simples["indicatif"]["Passé simple"][2],
        nous=temps_simples["indicatif"]["Passé simple"][3],
        vous=temps_simples["indicatif"]["Passé simple"][4],
        ils_elles=temps_simples["indicatif"]["Passé simple"][5]
    )

    new_indicatif_futur_simple = FrenchIndicatifFuturSimple(
        je=temps_simples["indicatif"]["Futur simple"][0],
        tu=temps_simples["indicatif"]["Futur simple"][1],
        il_elle=temps_simples["indicatif"]["Futur simple"][2],
        nous=temps_simples["indicatif"]["Futur simple"][3],
        vous=temps_simples["indicatif"]["Futur simple"][4],
        ils_elles=temps_simples["indicatif"]["Futur simple"][5]
    )

    new_conditionnel_present = FrenchConditionnelPresent(
        je=temps_simples["conditionnel"]["Présent"][0],
        tu=temps_simples["conditionnel"]["Présent"][1],
        il_elle=temps_simples["conditionnel"]["Présent"][2],
        nous=temps_simples["conditionnel"]["Présent"][3],
        vous=temps_simples["conditionnel"]["Présent"][4],
        ils_elles=temps_simples["conditionnel"]["Présent"][5]
    )

    new_subjonctif_present = FrenchSubjonctifPresent(
        je=temps_simples["subjonctif"]["Présent"][0],
        tu=temps_simples["subjonctif"]["Présent"][1],
        il_elle=temps_simples["subjonctif"]["Présent"][2],
        nous=temps_simples["subjonctif"]["Présent"][3],
        vous=temps_simples["subjonctif"]["Présent"][4],
        ils_elles=temps_simples["subjonctif"]["Présent"][5]
    )

    new_subjonctif_imparfait = FrenchSubjonctifImparfait(
        je=temps_simples["subjonctif"]["Imparfait"][0],
        tu=temps_simples["subjonctif"]["Imparfait"][1],
        il_elle=temps_simples["subjonctif"]["Imparfait"][2],
        nous=temps_simples["subjonctif"]["Imparfait"][3],
        vous=temps_simples["subjonctif"]["Imparfait"][4],
        ils_elles=temps_simples["subjonctif"]["Imparfait"][5]
    )

    new_imperatif_present = FrenchImperatifPresent(
        tu=temps_simples["imperatif"]["Présent"][0],
        nous=temps_simples["imperatif"]["Présent"][1],
        vous=temps_simples["imperatif"]["Présent"][2]
    )

    new_indicatif_passe_compose = FrenchIndicatifPasseCompose(
        je=temps_composes["indicatif"]["Passé composé"][0],
        tu=temps_composes["indicatif"]["Passé composé"][1],
        il_elle=temps_composes["indicatif"]["Passé composé"][2],
        nous=temps_composes["indicatif"]["Passé composé"][3],
        vous=temps_composes["indicatif"]["Passé composé"][4],
        ils_elles=temps_composes["indicatif"]["Passé composé"][5]
    )

    new_indicatif_plus_que_parfait = FrenchIndicatifPlusQueParfait(
        je=temps_composes["indicatif"]["Plus-que-parfait"][0],
        tu=temps_composes["indicatif"]["Plus-que-parfait"][1],
        il_elle=temps_composes["indicatif"]["Plus-que-parfait"][2],
        nous=temps_composes["indicatif"]["Plus-que-parfait"][3],
        vous=temps_composes["indicatif"]["Plus-que-parfait"][4],
        ils_elles=temps_composes["indicatif"]["Plus-que-parfait"][5]
    )

    new_indicatif_passe_anterieur = FrenchIndicatifPasseAnterieur(
        je=temps_composes["indicatif"]["Passé antérieur"][0],
        tu=temps_composes["indicatif"]["Passé antérieur"][1],
        il_elle=temps_composes["indicatif"]["Passé antérieur"][2],
        nous=temps_composes["indicatif"]["Passé antérieur"][3],
        vous=temps_composes["indicatif"]["Passé antérieur"][4],
        ils_elles=temps_composes["indicatif"]["Passé antérieur"][5]
    )

    new_indicatif_futur_anterieur = FrenchIndicatifFuturAnterieur(
        je=temps_composes["indicatif"]["Futur antérieur"][0],
        tu=temps_composes["indicatif"]["Futur antérieur"][1],
        il_elle=temps_composes["indicatif"]["Futur antérieur"][2],
        nous=temps_composes["indicatif"]["Futur antérieur"][3],
        vous=temps_composes["indicatif"]["Futur antérieur"][4],
        ils_elles=temps_composes["indicatif"]["Futur antérieur"][5]
    )

    new_conditionnel_passe = FrenchConditionnelPasse(
        je=temps_composes["conditionnel"]["Passé"][0],
        tu=temps_composes["conditionnel"]["Passé"][1],
        il_elle=temps_composes["conditionnel"]["Passé"][2],
        nous=temps_composes["conditionnel"]["Passé"][3],
        vous=temps_composes["conditionnel"]["Passé"][4],
        ils_elles=temps_composes["conditionnel"]["Passé"][5]
    )

    new_subjonctif_passe = FrenchSubjonctifPasse(
        je=temps_composes["subjonctif"]["Passé"][0],
        tu=temps_composes["subjonctif"]["Passé"][1],
        il_elle=temps_composes["subjonctif"]["Passé"][2],
        nous=temps_composes["subjonctif"]["Passé"][3],
        vous=temps_composes["subjonctif"]["Passé"][4],
        ils_elles=temps_composes["subjonctif"]["Passé"][5]
    )

    new_subjonctif_plus_que_parfait = FrenchSubjonctifPlusQueParfait(
        je=temps_composes["subjonctif"]["Plus-que-parfait"][0],
        tu=temps_composes["subjonctif"]["Plus-que-parfait"][1],
        il_elle=temps_composes["subjonctif"]["Plus-que-parfait"][2],
        nous=temps_composes["subjonctif"]["Plus-que-parfait"][3],
        vous=temps_composes["subjonctif"]["Plus-que-parfait"][4],
        ils_elles=temps_composes["subjonctif"]["Plus-que-parfait"][5]
    )

    # TODO: handle when there is only two tenses instead of 3 (for example, "etre").
    # This seems to occur when you have active voice. Passive voice has 3.
    new_imperatif_passe = FrenchImperatifPasse(
        tu=temps_composes["imperatif"]["Passé"][0],
        nous=temps_composes["imperatif"]["Passé"][1],
        # vous=temps_composes["imperatif"]["Passé"][2],
        vous="FIXME"
    )

    return {
        "indicatif_present": new_indicatif_present,
        "indicatif_imparfait": new_indicatif_imparfait,
        "indicatif_passe_simple": new_indicatif_passe_simple,
        "indicatif_futur_simple": new_indicatif_futur_simple,
        "conditionnel_present": new_conditionnel_present,
        "subjonctif_present": new_subjonctif_present,
        "subjonctif_imparfait": new_subjonctif_imparfait,
        "imperatif_present": new_imperatif_present,
        "indicatif_passe_compose": new_indicatif_passe_compose,
        "indicatif_plus_que_parfait": new_indicatif_plus_que_parfait,
        "indicatif_passe_anterieur": new_indicatif_passe_anterieur,
        "indicatif_futur_anterieur": new_indicatif_futur_anterieur,
        "conditionnel_passe": new_conditionnel_passe,
        "subjonctif_passe": new_subjonctif_passe,
        "subjonctif_plus_que_parfait": new_subjonctif_plus_que_parfait,
        "imperatif_passe": new_imperatif_passe
    }