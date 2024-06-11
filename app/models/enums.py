from enum import Enum

class VoteType(str, Enum):
    positive = "positive"
    negative = "negative"
    consensus = "consensus"

class StatusName(str, Enum):
    approved = "approved"
    declined = "declined"
    waiting = "waiting"
