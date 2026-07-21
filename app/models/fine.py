from dataclasses import dataclass
from app.models.enums import FineReason,FineStatus

@dataclass
class Fine:
    id:int
    loan_id:int
    amount:float
    reason:FineReason
    status:FineStatus