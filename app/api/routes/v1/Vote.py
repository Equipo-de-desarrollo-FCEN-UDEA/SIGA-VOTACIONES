from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.models.Vote import VoteCreate, VoteUpdate
from app.services.Vote import VoteService as Service

from app.config.database import Session



vote_router = APIRouter()

tags = {'vote'}

@vote_router.post('/votar', tags=tags, response_model=dict, status_code=201)
def vote(vote: VoteCreate) -> dict:
    db = Session
    vote = Service(db).create_vote(vote)
    return JSONResponse(status_code=201, content={'message': "se registro el voto"})

@vote_router.put('/cambiar_voto/', tags=tags, response_model=dict, status_code=200)
def update_adelanto(user_id: str, voting_id: str, new_vote: VoteUpdate) -> dict:
    db = Session
    Service(db).update_vote(user_id, voting_id, new_vote)
    return JSONResponse(status_code=200, content={"message": "se cambio el voto"})

@vote_router.get('/votos', tags=tags, response_model=list[VoteCreate], status_code=200)
def get_vote() -> dict:
    db = Session
    votes = Service(db).get_votes()
    return JSONResponse(status_code=200, content=votes)