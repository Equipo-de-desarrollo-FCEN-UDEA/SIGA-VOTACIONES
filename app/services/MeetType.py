from app.models.MeetType import MeetType
from app.services.BaseService import BaseService


class MeetTypeService(BaseService):
    def __init__(self, db):
        super().__init__(db, MeetType)