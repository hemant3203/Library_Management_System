from abc import ABC, abstractmethod
from typing import Optional

from app.models.fine import Fine
from app.models.enums import FineStatus


class FineRepository(ABC):

    @abstractmethod
    def add(self, fine: Fine) -> Fine:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, fine_id: int) -> Optional[Fine]:
        raise NotImplementedError

    @abstractmethod
    def list_by_loan(self, loan_id: int) -> list[Fine]:
        raise NotImplementedError

    @abstractmethod
    def list_pending(self) -> list[Fine]:
        raise NotImplementedError
   


class InMemoryFineRepository(FineRepository):

    def __init__(self):
        self._fines = {}
        self._next_id = 1

    def add(self, fine: Fine) -> Fine:
        fine.id=self._next_id
        self._fines[fine.id] = fine
        self._next_id += 1
        return fine

    def get_by_id(self, fine_id: int) -> Optional[Fine]:
        return self._fines.get(fine_id)

    def list_by_loan(self, loan_id: int) -> list[Fine]:
        fines: list[Fine] = []
        for fine in self._fines.values():
            if fine.loan_id == loan_id:
                fines.append(fine)
        return fines

    def list_pending(self) -> list[Fine]:
        fines: list[Fine] = []
        for fine in self._fines.values():
            if fine.status == FineStatus.PENDING:
                fines.append(fine)
        return fines