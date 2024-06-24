from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.Vote import VoteCreate, VoteUpdate, VoteRead
from app.services.Vote import VoteService as Service
from app.config.database import Session, get_session

vote_router = APIRouter()

tags = {'vote'}

@vote_router.post('/votar', tags=tags, response_model=dict, status_code=201)
def vote(vote: VoteCreate, db: Session = Depends(get_session)) -> dict:
    vote = Service(db).create(vote)
    return JSONResponse(status_code=201, content={'message': "se registró el voto"})

@vote_router.put('/update/', tags=tags, response_model=dict, status_code=200)
def update_vote(user_id: str, voting_id: str, new_vote: VoteUpdate, db: Session = Depends(get_session)) -> dict:
    Service(db).update(user_id, voting_id, new_vote)
    return JSONResponse(status_code=200, content={"message": "se cambió el voto"})

@vote_router.get('/get_vote/{user_id}/{voting_id}', tags=tags, response_model=VoteRead, status_code=200)
def get_vote(user_id: str, voting_id: str, db: Session = Depends(get_session)) -> VoteRead:
    vote = Service(db).get_by_id(user_id, voting_id)
    return vote

@vote_router.get('/get_votes/{voting_id}', tags=tags, response_model=list[VoteRead], status_code=200)
def get_votes(voting_id: str, db: Session = Depends(get_session)) -> list[VoteRead]:
    votes = Service(db).get_by_voting_id(voting_id)
    return votes
