from fastapi import APIRouter
from backend.routers import verbs, flashcards

api_router = APIRouter()
api_router.include_router(verbs.router, prefix="/verbs", tags=["verbs"])
api_router.include_router(flashcards.router, prefix="/flashcards", tags=["flashcards"])