from sqlmodel import select
from fastapi import HTTPException
from datetime import datetime
from .BasePolicy import BasePolicy
from app.models.Voting import Voting
from app.models.Vote import Vote
from app.models.Status import Status
from typing import Type
from sqlalchemy.orm import joinedload

class VotingPolicy(BasePolicy):
    def __init__(self, db, model: Type[Voting]):
        self.db = db
        self.model = model

    def count_votes(self, session, voting_id: str) -> int:
        query = select(Vote).where(Vote.voting_id == voting_id)
        votes = session.exec(query).all()
        return len(votes)
        
    def close_voting(self, voting_id: str) -> dict:
        with self.db as session:
            query = select(Voting).options(joinedload(Voting.votes)).where(Voting.id == voting_id)
            voting = session.exec(query).first()

            if not voting:
                raise HTTPException(status_code=404, detail="Voting not found")
            
            total_votes = self.count_votes(session, voting_id)
            if total_votes == voting.maxVotes:
                query = select(Vote).where(Vote.voting_id == voting_id, Vote.vote_type == "meet")
                meet_vote = session.exec(query).first()
                
                positive_votes = session.exec(select(Vote).where(Vote.voting_id == voting_id, Vote.vote_type == "positive")).all()
                negative_votes = session.exec(select(Vote).where(Vote.voting_id == voting_id, Vote.vote_type == "negative")).all()

                if not meet_vote:
                    positive_votes_count = len(positive_votes)
                    negative_votes_count = len(negative_votes)
                    
                    if positive_votes_count > negative_votes_count:
                        voting.status_id = session.exec(select(Status).where(Status.name == "approved")).first().id
                    else:
                        voting.status_id = session.exec(select(Status).where(Status.name == "declined")).first().id

                    voting.updated_at = datetime.now()
                    session.add(voting)
                    session.commit()
                    session.refresh(voting)
                    
                    return {"status": voting.status_id}
                            
            return {"status": "open"}
