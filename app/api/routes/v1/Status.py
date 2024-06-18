from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.Status import StatusCreate, StatusRead
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

@status_router.get('/all', tags=tags, response_model=List[StatusRead], status_code=200)
def get_all() -> List[dict]:
    db = Session
    status_list = Service(db).get_all()
    return JSONResponse(status_code=200, content=jsonable_encoder(status_list))
    #return [StatusRead.model_validate({"name": status.name, "id": status.id}) for status in status_list]