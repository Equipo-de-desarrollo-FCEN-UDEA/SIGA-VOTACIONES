from app.models.Status import Status, StatusRead
from app.services.BaseService import BaseService


class StatusService(BaseService):
    def __init__(self, db):
        super().__init__(db, Status)