from sqlmodel import select
from fastapi import HTTPException
from datetime import datetime
from .BasePolicy import BasePolicy
from app.models.Voting import Voting
from app.models.Vote import Vote
from app.models.Status import Status
from typing import Type

class VotingPolicy(BasePolicy):
    def __init__(self, db, model: Type[Voting]):
        self.db = db
        self.model = model

    def count_votes(self, voting_id: str) -> int:
        with self.db:
            query = select(Vote).where(Vote.voting_id == voting_id)
            votes = self.db.exec(query).all()
            return len(votes)
    
    def close_voting(self, voting_id: str) -> dict:
        with self.db as session:
            voting = session.get(Voting, voting_id)
            if not voting:
                raise HTTPException(status_code=404, detail="Voting not found")
            
            total_votes = self.count_votes(voting_id)
            if total_votes == voting.maxVotes:
                query = select(Vote).where(Vote.voting_id == voting_id, Vote.vote_type == "meet")
                meet_vote = session.exec(query).first()
                
                status_positive = select(Status).where(Status.name == "positive")
                status_negative = select(Status).where(Status.name == "negative")

                if not meet_vote:
                    positive_votes = len([vote for vote in voting.votes if vote.vote_type == "positive"])
                    negative_votes = len([vote for vote in voting.votes if vote.vote_type == "negative"])
                    
                    if positive_votes > negative_votes:
                        voting.status_id = status_positive.id
                    else:
                        voting.status_id = status_negative.id

                    voting.updated_at = datetime.now()
                    session.add(voting)
                    session.commit()
                    session.refresh(voting)
                    
                    return {"status": voting.status_id}
                            
            return {"status": "open"}
