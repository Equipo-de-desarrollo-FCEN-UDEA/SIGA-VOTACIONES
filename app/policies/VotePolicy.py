from typing import Type
from fastapi import HTTPException
from app.models.Voting import Voting
from app.policies.BasePolicy import BasePolicy

class VotePolicy(BasePolicy):
    def __init__(self, db, model: Type[Voting]):
        self.db = db
        self.model = model

    def validate_max_votes(self, voting_id: str):
        with self.db as session:
            voting = session.get(Voting, voting_id)
            if not voting:
                raise HTTPException(status_code=404, detail="Voting not found")
            count_votes = len(voting.votes)
            if count_votes >= voting.maxVotes:
                raise HTTPException(status_code=400, detail="Max votes reached, voting is closed")
