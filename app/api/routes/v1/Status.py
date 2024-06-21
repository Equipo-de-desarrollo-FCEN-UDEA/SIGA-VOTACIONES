from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlmodel import Session

from app.models.Status import StatusCreate, StatusReadWithVotings, StatusRead
from app.services.Status import StatusService as Service

from app.config.database import get_session
from fastapi.encoders import jsonable_encoder

status_router = APIRouter()

tags = {'status'}

@status_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(status: StatusCreate, db: Session = Depends(get_session)) -> dict:
    status_db = Service(db).create(status)
    return JSONResponse(status_code=201, content= jsonable_encoder(status_db))

@status_router.get('/all', tags=tags, response_model=list[StatusRead], status_code=200)
def get_all(db: Session = Depends(get_session)) -> dict:
    status = Service(db).get_all()
    status = [StatusRead.model_validate(stat).model_dump() for stat in status]
    return JSONResponse(status_code=200, content=status)

@status_router.get('/{status_id}', tags=tags, response_model=StatusReadWithVotings, status_code=200)
def get_status(status_id: str, db: Session = Depends(get_session)) -> dict:
    status = Service(db).get_by_id(status_id)
    return status
