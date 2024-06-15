from app.models.VotingType import VotingType
from app.services import BaseService


class VotingTypeService(BaseService):
    def __init__(self, db):
        super().__init__(db, VotingType)