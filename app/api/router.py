from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1.Vote import vote_router

api_router = APIRouter()

api_router.include_router(ping.router, tags=["ping"])
api_router.include_router(vote_router, prefix="/vote", tags=["vote"])