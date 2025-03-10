from sqlmodel import SQLModel
from backend.models.flashcard import Flashcard
from backend.models.verb import FrenchVerb

# see documentation for why this is needed: https://alembic.sqlalchemy.org/en/latest/naming.html
NAMING_CONVENTION = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}

# needed for getting all the metadata of the models so we can use this for migrations
metadata = SQLModel.metadata
metadata.naming_convention = NAMING_CONVENTION