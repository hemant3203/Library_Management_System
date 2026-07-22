from datetime import date ,timedelta

from app.models.fine import Fine
from app.models.loan import Loan
from app.models.enums import CopyStatus,FineReason
from app.repositories.student_repository import StudentRepository
from app.repositories.loan_repository import LoanRepository
from app.repositories.copy_repository import CopyRepository
from app.repositories.book_repository import BookRepository
from app.repositories.fine_repository import FineRepository

LOAN_DAYS=14
MAX_ACTIVE_LOANS=3
FINE_RATE_PER_DAY=0.02

class LoanService:
    def __init__(self, student_repo: StudentRepository, loan_repo: LoanRepository, copy_repo: CopyRepository,book_repo:BookRepository,fine_repo:FineRepository) -> None:
        self._student_repo = student_repo
        self._loan_repo = loan_repo
        self._copy_repo = copy_repo
        self._book_repo=book_repo
        self._fine_repo=fine_repo

    def issue_book(self,student_id:int ,book_id:int)->Loan:
        student=self._student_repo.get_by_id(student_id)
        if student is None:
            raise ValueError(f"Student with id '{student_id}' not found")
        active_loan=self._loan_repo.list_active_by_student(student_id)
        if len(active_loan) >= MAX_ACTIVE_LOANS:
            raise ValueError(f"Student with id '{student_id}' has reached the maximum {MAX_ACTIVE_LOANS} books")

        copy=self._copy_repo.find_available(book_id)
        if copy is None:
            raise ValueError(f"Book with id '{book_id}' is not available")

        loan =Loan(
            id=0,
            student_id=student_id,
            copy_id=copy.id,
            issue_date=date.today(),
            due_date=date.today() + timedelta(days=LOAN_DAYS)
        )
        copy.status=CopyStatus.ISSUED
        return self._loan_repo.add(loan)

    def return_book(self,copy_id:int)->Loan:
        loan=self._loan_repo.find_active_by_copy(copy_id)
        if loan is None:
            raise ValueError(f"No active loan found for copy with id {copy_id} ")
        loan.return_date=date.today()
        copy=self._copy_repo.get_by_id(copy_id)
        copy.status=CopyStatus.AVAILABLE
        if loan.return_date>loan.due_date:
            days_late=(loan.return_date-loan.due_date).days
            book=self._book_repo.get_by_id(copy.book_id)
            amount=days_late * FINE_RATE_PER_DAY * book.mrp
            self._fine_repo.add(Fine(id=0,loan_id=loan.id,amount=amount,reason=FineReason.LATE))
        return loan