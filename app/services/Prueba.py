from datetime import datetime
from app.models.Prueba import Prueba
from app.services.BaseService import BaseService

class PruebaService(BaseService):
    def __init__(self, db):
        super().__init__(db, Prueba)


    def create(self, create_schema):
        with self.db as session:
            entity = self.model.model_validate(create_schema)
            entity.created_at = datetime.now()
            entity.updated_at = datetime.now()
            session.add(entity)
            session.commit()
            session.refresh(entity)
            return entity