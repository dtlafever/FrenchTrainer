from fastapi import APIRouter
from backend.routers import verbs, flashcards

api_router = APIRouter()
api_router.include_router(verbs.router)
api_router.include_router(flashcards.router)
