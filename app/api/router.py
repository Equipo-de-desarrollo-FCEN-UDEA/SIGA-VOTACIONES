from fastapi import APIRouter

from app.api.routes import ping
from app.api.routes.v1.Prueba import prueba_router
from app.api.routes.v1.Vote import vote_router
from app.api.routes.v1.Status import status_router
from app.api.routes.v1.VotingType import voting_type_router
from app.api.routes.v1.Voting import voting_router

api_router = APIRouter()

api_router.include_router(prueba_router, prefix="/prueba", tags=["prueba"])
api_router.include_router(vote_router, prefix="/vote", tags=["vote"])
api_router.include_router(status_router, prefix="/status", tags=["status"])
api_router.include_router(voting_type_router, prefix="/type", tags=["type"])
api_router.include_router(voting_router, prefix="/voting", tags=["voting"])