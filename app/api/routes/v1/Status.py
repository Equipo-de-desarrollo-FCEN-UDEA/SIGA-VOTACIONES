from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.Status import StatusCreate
from app.services.Status import StatusService as Service

from app.config.database import Session



status_router = APIRouter()

tags = {'status'}

@status_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(status: StatusCreate) -> dict:
    db = Session
    vote = Service(db).create(status)
    return JSONResponse(status_code=201, content={'message': "se registro el nuevo estado"})