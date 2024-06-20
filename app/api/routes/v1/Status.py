from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.Status import StatusCreate, StatusReadWithVotings, StatusRead
from app.services.Status import StatusService as Service

from app.config.database import Session
from fastapi.encoders import jsonable_encoder


status_router = APIRouter()

tags = {'status'}

@status_router.post('/create', tags=tags, response_model=dict, status_code=201)
def create(status: StatusCreate) -> dict:
    db = Session
    status_db = Service(db).create(status)
    return JSONResponse(status_code=201, content={'message': "se registro el nuevo estado"})

@status_router.get('/all', tags=tags, response_model=list[StatusRead], status_code=200)
def get_all() -> dict:
    db = Session
    status = Service(db).get_all()
    return status

@status_router.get('/{status_id}', tags=tags, response_model=StatusReadWithVotings, status_code=200)
def get_status(status_id: str) -> dict:
    db = Session
    status = Service(db).get_by_id(status_id)
    return status
