from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.Voting import VotingCreate, VotingReadWithInfo, VotingRead, Voting

from app.config.database import Session

from app.services.Voting import VotingService as Service


voting_router = APIRouter()

tags = {'voting'}

@voting_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(voting: VotingCreate) -> dict:
    db = Session
    voting_db = Service(db).create(voting)
    return JSONResponse(status_code=201, content={'message': "se registró una nueva votación"})

@voting_router.get('/info', tags=tags, response_model=VotingReadWithInfo, status_code=200)
def get_voting_info(voting_id: str) -> dict:
    db = Session
    voting_db = Service(db).get_by_id(voting_id)
    return (voting_db)