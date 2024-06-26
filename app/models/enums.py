from enum import Enum

class VoteType(str, Enum):
    positive = "positive"
    negative = "negative"
    abstain = "abstain"
    meet = "meet"

class StatusName(str, Enum):
    waiting = "waiting"
    approved = "approved"
    declined = "declined"
    
