from abc import ABC, abstractmethod
from typing import Optional

from app.models.loan import Loan


class LoanRepository(ABC):

    @abstractmethod
    def add(self, loan: Loan) -> Loan:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, loan_id: int) -> Optional[Loan]:
        raise NotImplementedError

    @abstractmethod
    def list_active_by_student(self, student_id: int) -> list[Loan]:
        raise NotImplementedError

    @abstractmethod
    def find_active_by_copy(self, copy_id: int) -> Optional[Loan]:
        raise NotImplementedError
   


class InMemoryLoanRepository(LoanRepository):

    def __init__(self):
        self._loans = {}
        self._next_id = 1

    def add(self, loan: Loan) -> Loan:
        loan.id=self._next_id
        self._loans[loan.id] = loan
        self._next_id += 1
        return loan

    def get_by_id(self, loan_id: int) -> Optional[Loan]:
        return self._loans.get(loan_id)

    def list_active_by_student(self, student_id: int) -> list[Loan]:
        loans: list[Loan] = []
        for loan in self._loans.values():
            if loan.student_id == student_id and loan.return_date is None:
                loans.append(loan)
        return loans

    def find_active_by_copy(self, copy_id: int) -> Optional[Loan]:
        for loan in self._loans.values():
            if loan.copy_id == copy_id and loan.return_date is None:
                return loan
        return None