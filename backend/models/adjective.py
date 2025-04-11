import datetime
from sqlmodel import Field, SQLModel, Relationship

from pydantic import ConfigDict

class Adjective(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    masc_french_singular: str = Field(default=None)
    fem_french_singular: str = Field(default=None)
    masc_french_plural: str = Field(default=None)
    fem_french_plural: str = Field(default=None)
    english_text: str = Field(default=None)
    # default_factory so it will be set to the current time when the object is created, not on module load
    created_on: datetime.datetime = Field(default_factory=datetime.datetime.now)

class ShowAdjective(SQLModel):
    model_config = ConfigDict(from_attributes = True) #tells pydantic to convert even non dict obj to json

    masc_french_singular: str
    fem_french_singular: str
    masc_french_plural: str
    fem_french_plural: str
    english_text: str
