from fastapi import HTTPException
from sqlmodel import select
from app.models.Vote import *


class VoteService:
    def __init__(self, db) -> None:
        self.db = db

    def create_vote(self, vote: VoteCreate):
        with self.db:
            db_vote = Vote.model_validate(vote)
            db_vote.createdAt = datetime.now()
            db_vote.updatedAt = datetime.now()
            self.db.add(db_vote)
            self.db.commit()
            self.db.refresh(db_vote)
            return db_vote
        
    def get_votes(self):
        with self.db:
            votes = self.db.exec(select(Vote)).all()
            return votes
        
        
    def get_vote_by_ID(self, user_id: str, voting_id: str):
        with self.db:
            vote: VoteRead = self.db.get(Vote, user_id, voting_id)
            if not vote:
                raise HTTPException(status_code=404, detail="vote not found")
            return vote
        
    def update_vote(self, user_id: str, voting_id: str, vote: VoteUpdate):
        with self.db as session:
            db_vote = session.get(Vote, (user_id, voting_id))
            if not db_vote:
                raise HTTPException(status_code=404, detail="Vote not found")
            vote_data = vote.model_dump(exclude_unset=True)
            db_vote.sqlmodel_update(vote_data)
            db_vote.updatedAt = datetime.now()
            session.add(db_vote)
            session.commit()
            session.refresh(db_vote)
            return db_vote
    
    def delete_vote(self, user_id:str, voting_id:str):
        with self.db as session:
            vote = session.get(Vote, (user_id, voting_id))
            if not vote:
                raise HTTPException(status_code=404, detail="Vote not found")
            session.delete(vote)
            self.db.commit()
            return {"ok": True}