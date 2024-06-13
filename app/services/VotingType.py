from fastapi import HTTPException
from sqlmodel import select
from app.models.VotingType import *


class VotingTypeService:
    def __init__(self, db) -> None:
        self.db = db

    def create_voting_type(self, type: VotingTypeCreate):
        with self.db:
            db_voting_type = VotingType.model_validate(type)
            db_voting_type.createdAt = datetime.now()
            db_voting_type.updatedAt = datetime.now()
            self.db.add(db_voting_type)
            self.db.commit()
            self.db.refresh(db_voting_type)
            return db_voting_type
        
    def get_voting_types(self):
        with self.db:
            voting_types = self.db.exec(select(VotingType)).all()
            return voting_types
        
        
    def get_voting_type_by_ID(self, voting_type_id: str):
        with self.db:
            voting_type: VotingTypeRead = self.db.get(VotingType, voting_type_id)
            if not voting_type:
                raise HTTPException(status_code=404, detail="voting type not found")
            return voting_type
        
    def update_voting_type(self, voting_type_id: str, voting_type: VotingTypeUpdate):
        with self.db as session:
            db_voting_type = session.get(VotingType, voting_type_id)
            if not db_voting_type:
                raise HTTPException(status_code=404, detail="VotingType not found")
            voting_type_data = voting_type.model_dump(exclude_unset=True)
            db_voting_type.sqlmodel_update(voting_type_data)
            db_voting_type.updatedAt = datetime.now()
            session.add(db_voting_type)
            session.commit()
            session.refresh(db_voting_type)
            return db_voting_type
    
    def delete_voting_type(self, voting_type_id: str):
        with self.db as session:
            voting_type = session.get(VotingType, voting_type_id)
            if not voting_type:
                raise HTTPException(status_code=404, detail="VotingType not found")
            session.delete(voting_type)
            self.db.commit()
            return {"ok": True}