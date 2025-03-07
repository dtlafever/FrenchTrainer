from typing import Optional
import datetime

from sqlmodel import Field, SQLModel

class Flashcard(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    question: str = Field(max_length=200)
    answer: str = Field(max_length=200)
    last_chosen_date: Optional[datetime.datetime] = Field(default=None)  # Added last chosen date

class ShowFlashcard(SQLModel):
    question: str
    answer: str

    class Config(): #tells pydantic to convert even non dict obj to json
        from_attributes = True
