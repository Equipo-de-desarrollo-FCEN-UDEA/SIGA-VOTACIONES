from app.models.Voting import Voting
from app.services.BaseService import BaseService


class VotingService(BaseService):
    def __init__(self, db):
        super().__init__(db, Voting)