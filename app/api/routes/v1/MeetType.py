from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.models.MeetType import MeetTypeCreate
from app.services.MeetType import MeetTypeService as Service

from app.config.database import session

meet_type_router = APIRouter()

tags = {'meet_type'}

@meet_type_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(meet_type: MeetTypeCreate) -> dict:
    db = session
    meet_type_db = Service(db).create(meet_type)
    return JSONResponse(status_code=201, content={'message': "se registró el nuevo tipo de votación"})