from typing import Any, Generator
from sqlmodel import SQLModel, create_engine, Session
from backend.config import settings

DB_URL = settings.DATABASE_URL
engine = create_engine(DB_URL, echo=False)

def create_db_and_tables() -> None:
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, Any, None]:
    """
    Provides a session generator for database operations.
    
    Yields:
        Session: A SQLAlchemy Session object.
    """
    with Session(engine) as session:
        yield session