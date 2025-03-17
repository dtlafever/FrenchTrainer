from fastapi.testclient import TestClient
from sqlmodel import Session

from backend.models.flashcard import Flashcard

def test_create_flashcard(client: TestClient, session: Session):
    # Test data
    flashcard_data = {
        "question": "Bonjour",
        "answer": "Hello",
    }
    
    # Send POST request to create a flashcard
    response = client.post("/flashcards/", json=flashcard_data)
    
    # Assert response
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["question"] == flashcard_data["question"]
    assert data["answer"] == flashcard_data["answer"]
    
    # Verify the flashcard was added to the database
    db_flashcard = session.get(Flashcard, 1)
    assert db_flashcard is not None
    assert db_flashcard.question == flashcard_data["question"]
    assert db_flashcard.answer == flashcard_data["answer"]

def test_get_flashcard(client: TestClient, session: Session):
    # Create a flashcard in the database
    flashcard = Flashcard(
        question="Merci",
        answer="Thank you",
    )
    session.add(flashcard)
    session.commit()
    session.refresh(flashcard)
    
    # Send GET request to retrieve the flashcard
    response = client.get(f"/flashcards/{flashcard.id}")
    
    # Assert response
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["question"] == flashcard.question
    assert data["answer"] == flashcard.answer

def test_get_all_flashcards(client: TestClient, session: Session):
    # Create multiple flashcards
    flashcards = [
        Flashcard(
            question="Comment ça va?",
            answer="How are you?",
        ),
        Flashcard(
            question="Je m'appelle",
            answer="My name is",
        )
    ]
    
    for flashcard in flashcards:
        session.add(flashcard)
    
    session.commit()
    
    # Send GET request to retrieve all flashcards
    response = client.get("/flashcards/")
    
    # Assert response
    assert response.status_code == 200, response.text
    data = response.json()
    assert len(data) == 2
