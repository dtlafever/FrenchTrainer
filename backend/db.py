from sqlmodel import SQLModel
from sqlalchemy import Engine

def create_db_and_tables(engine: Engine) -> None:
    SQLModel.metadata.create_all(engine)
