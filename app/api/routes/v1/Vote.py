from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

from sqlmodel import select
from app.models.Vote import VoteCreate, VoteUpdate, VoteRead, Vote
from app.services.Vote import VoteService as Service

from app.config.database import Session



vote_router = APIRouter()

tags = {'vote'}

@vote_router.post('/votar', tags=tags, response_model=dict, status_code=201)
def vote(vote: VoteCreate) -> dict:
    db = Session
    #Service(db).validate_max_votes(vote.voting_id)
    vote = Service(db).create(vote)
    return JSONResponse(status_code=201, content={'message': "se registro el voto"})

@vote_router.put('/cambiar_voto/', tags=tags, response_model=dict, status_code=200)
def update_adelanto(user_id: str, voting_id: str, new_vote: VoteUpdate) -> dict:
    db = Session
    Service(db).update_vote(user_id, voting_id, new_vote)
    return JSONResponse(status_code=200, content={"message": "se cambio el voto"})

@vote_router.get('/all', tags=tags, response_model=list[VoteRead], status_code=200)
def get_all() -> dict:
    db = Session
    votes = Service(db).get_all()
    return votes


@vote_router.get('/votos/{voting_id}', tags=tags, response_model=list[VoteRead], status_code=200)
def get_vote_by_voting(voting_id: str) -> dict:
    db = Session
    votes = Service(db).get_votes_by_voting(voting_id)
    print(votes)
    return votes.all()