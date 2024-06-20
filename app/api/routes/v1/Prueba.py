from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.config.database import Session

from app.models.MeetType import MeetTypeCreate, MeetType
from app.models.Status import StatusCreate, Status
from app.models.Voting import VotingCreate, Voting

from datetime import datetime
from cuid import cuid

prueba_router = APIRouter()
tags = {'prueba'}

@prueba_router.post('/init', tags=tags, response_model=dict, status_code=201)
def init()-> dict:
    db = Session

    type = MeetTypeCreate(rol_id="con_inst", department_id="mat")
    status1 = StatusCreate(name="approved")
    status2 = StatusCreate(name="declined")
    status3 = StatusCreate(name="waiting")

    entity_type = MeetType.model_validate(type)
    entity_type.id = "clxldp8xn00043lpcnl1duhim"
    entity_type.created_at = datetime.now()
    entity_type.updated_at = datetime.now()
    db.add(entity_type)
    db.commit()
    db.refresh(entity_type)

    entity_status = Status.model_validate(status1)
    entity_status.id = "clxldp90m00053lpc3jhcl4yj"
    entity_status.created_at = datetime.now()
    entity_status.updated_at = datetime.now()
    db.add(entity_status)
    db.commit()
    db.refresh(entity_status)

    entity_status = Status.model_validate(status2)
    entity_status.id = "clxldp90u00063lpc9a5jja92"
    entity_status.created_at = datetime.now()
    entity_status.updated_at = datetime.now()
    db.add(entity_status)
    db.commit()
    db.refresh(entity_status)

    entity_status = Status.model_validate(status3)
    entity_status.id = "clxldp91100073lpc4irqc48o"
    entity_status.created_at = datetime.now()
    entity_status.updated_at = datetime.now()
    db.add(entity_status)
    db.commit()
    db.refresh(entity_status)
    
    voting = VotingCreate(maxVotes=3, mongo_id="dedi-1" ,status_id="clxldp91100073lpc4irqc48o", meet_type_id="clxldp8xn00043lpcnl1duhim")

    entity_voting = Voting.model_validate(voting)
    entity_voting.id = cuid()
    entity_voting.created_at = datetime.now()
    entity_voting.updated_at = datetime.now()
    db.add(entity_voting)
    db.commit()
    db.refresh(entity_voting)



    return JSONResponse(status_code=201, content={'message': "se registraron los elementos de prueba para db"})