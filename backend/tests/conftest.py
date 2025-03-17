import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlalchemy.pool import StaticPool

from backend.routers.base import api_router
from backend.db.session import get_session

# Create an in-memory SQLite database for testing
@pytest.fixture(name="engine")
def engine_fixture():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine
    SQLModel.metadata.drop_all(engine)

@pytest.fixture(name="session")
def session_fixture(engine):
    with Session(engine) as session:
        yield session

@pytest.fixture(name="client")
def client_fixture(session):
    def get_test_session():
        yield session

    app = FastAPI()
    app.include_router(api_router)
    
    # Override the get_session dependency
    app.dependency_overrides[get_session] = get_test_session
    
    return TestClient(app)
