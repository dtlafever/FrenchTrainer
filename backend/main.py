from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_mcp import FastApiMCP

from contextlib import asynccontextmanager

from backend.db.session import create_db_and_tables
from backend.routers.base import api_router

from chainlit.utils import mount_chainlit

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup functions
    create_db_and_tables()
    app.include_router(api_router)
    # init MCP server
    mcp = FastApiMCP(
        app,
        # Optional parameters
        name="frenchtrainer_MCP",
        description="French Trainer MCP",
        base_url="http://localhost:8000",
        exclude_operations=[
            "create_adjective",
            "create_verb",
            "create_flashcard"
        ]
    )

    # mount the MCP server to http://server_url/mcp
    mcp.mount(api_router)
    yield
    # Shutdown functions go here

app = FastAPI(lifespan=lifespan)

# Add CORS middleware to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:80", "http://localhost:5173"],  # http port, and Vite default dev port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# mount the chainlit LLM to its own path
mount_chainlit(app=app, target="cl_app.py", path="/chat")

# NOTE: For all other routes, see the routers directory
