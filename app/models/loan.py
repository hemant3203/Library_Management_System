from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Loan:
    id:int
    student_id:int
    copy_id:int
    issue_date:date
    due_date:date
    return_date:Optional[date]= None

    def is_overdue(self)->bool:
        if self.return_date is not None:
            return False
        return date.today()>self.due_date