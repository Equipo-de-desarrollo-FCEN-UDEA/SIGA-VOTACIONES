from datetime import datetime
from fastapi import HTTPException
from sqlmodel import select
from sqlalchemy.exc import IntegrityError
from app.models.Vote import Vote


from app.services.BaseService import BaseService


class VoteService(BaseService):
    def __init__(self, db):
        super().__init__(db, Vote)

    def create(self, create_schema):
        with self.db as session:
            try:
                db_vote = self.model.model_validate(create_schema)
                db_vote.created_at = datetime.now()
                db_vote.updated_at = datetime.now()
                session.add(db_vote)
                session.commit()
                session.refresh(db_vote)
                return db_vote
            except IntegrityError as e:
                self.db.rollback()  
                raise HTTPException(status_code=400, detail="Vote already exists. User has already voted in this poll.")
            except Exception as e:
                self.db.rollback()
                raise HTTPException(status_code=500, detail="Internal server error.")

    def get_by_id(self, user_id: str, voting_id: str):
        statement = select(self.model).where(self.model.user_id == user_id, self.model.voting_id == voting_id)
        entity = self.db.exec(statement).first()
        if not entity:
            raise HTTPException(status_code=404, detail="Entity not found")
        return entity
    
    def update(self, user_id: str, voting_id: str, update_schema):
        with self.db as session:
            statement = select(self.model).where(self.model.user_id == user_id, self.model.voting_id == voting_id)
            db_vote = session.exec(statement).first()

            print("objeto encontrad: ", db_vote)

            if not db_vote:
                raise HTTPException(status_code=404, detail="Vote not found")

            update_data = update_schema.model_dump(exclude_unset=True)
            db_vote.sqlmodel_update(update_data)
            db_vote.updated_at = datetime.now()
            session.add(db_vote)
            session.commit()
            session.refresh(db_vote)
            return db_vote
        
    def get_by_voting_id(self, voting_id: str):
        with self.db as session:
            statement = select(self.model).where(self.model.voting_id == voting_id)
            entities = session.exec(statement).all()
            return entities
        
"""     
    def validate_max_votes(self, voting_id: str):
        with self.db as session:
            voting = session.get(Voting, voting_id)
            if not voting:
                raise HTTPException(status_code=404, detail="Voting not found")
            count_votes = len(voting.votes)
            if count_votes == voting.maxVotes:
                raise HTTPException(status_code=400, detail="Max votes reached")
            return
"""