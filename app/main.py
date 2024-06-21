import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.models.Status import Status
from app.models.Vote import Vote
from app.models.MeetType import MeetType
from app.models.Voting import Voting
from app.models.enums import VoteType, StatusName

from app.api.router import api_router
#from app.infraestructure.db.config import init_db
from app.config.database import create_db_and_tables, engine


def create_app() -> FastAPI:
    """Create the application."""
    app = FastAPI()
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.include_router(api_router)
    return app


app = create_app()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.on_event("startup")
def startup_event():
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)
    logger.debug("Event start up")
    create_db_and_tables()