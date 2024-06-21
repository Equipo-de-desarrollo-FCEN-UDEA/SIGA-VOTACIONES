from app.models.Voting import Voting
from app.services.BaseService import BaseService
from app.policies.VotingPolicy import VotingPolicy

class VotingService(BaseService, VotingPolicy):
    def __init__(self, db):
        super().__init__(db, Voting)