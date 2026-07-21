from dataclasses import dataclass

from app.models.enums import CopyStatus

@dataclass
class BookCopy:
    id:int
    book_id:int
    status:CopyStatus