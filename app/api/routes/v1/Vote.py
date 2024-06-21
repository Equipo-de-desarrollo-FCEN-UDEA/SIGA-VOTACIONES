from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from app.models.Vote import VoteCreate, VoteUpdate, VoteRead
from app.services.Vote import VoteService as Service

from app.config.database import session



vote_router = APIRouter()

tags = {'vote'}

@vote_router.post('/votar', tags=tags, response_model=dict, status_code=201)
def vote(vote: VoteCreate) -> dict:
    db = session
    #Service(db).validate_max_votes(vote.voting_id)
    vote = Service(db).create(vote)
    return JSONResponse(status_code=201, content={'message': "se registro el voto"})

@vote_router.put('/update/', tags=tags, response_model=dict, status_code=200)
def update_vote(user_id: str, voting_id: str, new_vote: VoteUpdate) -> dict:
    db = session
    Service(db).update(user_id, voting_id, new_vote)
    return JSONResponse(status_code=200, content={"message": "se cambio el voto"})

@vote_router.get('/get_vote/{user_id}/{voting_id}', tags=tags, response_model=VoteRead, status_code=200)
def get_vote(user_id: str, voting_id: str) -> VoteRead:
    db = session
    vote = Service(db).get_by_id(user_id, voting_id)
    return vote

@vote_router.get('/get_votes/{voting_id}', tags=tags, response_model=list[VoteRead], status_code=200)
def get_votes(voting_id: str) -> list[VoteRead]:
    db = session
    votes = Service(db).get_by_voting_id(voting_id)
    return votes