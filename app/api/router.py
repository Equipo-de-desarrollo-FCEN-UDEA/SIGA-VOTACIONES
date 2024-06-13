from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1.Vote import vote_router
from app.api.routes.v1.Status import status_router

api_router = APIRouter()

api_router.include_router(ping.router, tags=["ping"])
api_router.include_router(vote_router, prefix="/vote", tags=["vote"])
api_router.include_router(status_router, prefix="/status", tags=["status"])