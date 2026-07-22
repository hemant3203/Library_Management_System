from enum import Enum

class CopyStatus(str ,Enum):
    AVAILABLE="available"
    ISSUED="issued"
    DAMAGED="damaged"
    REMOVED="removed"

class FineReason(str , Enum):
    LATE="late"
    DAMAGE="damage"

class FineStatus(str, Enum):
    PENDING="pending"
    PAID="paid"