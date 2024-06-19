from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.VotingType import VotingTypeCreate
from app.services.VotingType import VotingTypeService as Service

from app.config.database import Session

voting_type_router = APIRouter()

tags = {'type'}

@voting_type_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(type: VotingTypeCreate) -> dict:
    db = Session
    type_db = Service(db).create(type)
    return JSONResponse(status_code=201, content={'message': "se registró el nuevo tipo de votación"})