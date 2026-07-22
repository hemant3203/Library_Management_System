from datetime import date, timedelta

from app.repositories.book_repository import InMemoryBookRepository
from app.repositories.copy_repository import InMemoryCopyRepository
from app.repositories.student_repository import InMemoryStudentRepository
from app.repositories.loan_repository import InMemoryLoanRepository
from app.repositories.fine_repository import InMemoryFineRepository
from app.services.catalog_service import CatalogService
from app.services.student_service import StudentService
from app.services.loan_service import LoanService

book_repo = InMemoryBookRepository()
copy_repo = InMemoryCopyRepository()
student_repo = InMemoryStudentRepository()
loan_repo = InMemoryLoanRepository()
fine_repo = InMemoryFineRepository()

catalog = CatalogService(book_repo, copy_repo)
students = StudentService(student_repo)
loans = LoanService(student_repo, loan_repo, copy_repo, book_repo, fine_repo)

catalog.add_book("Clean Code", "Robert Martin", 500.0, 1)
students.register_student("Ravi", "ravi@test.com")

print(loans.issue_book(1, 1))
print(copy_repo.get_by_id(1).status)

loan = loan_repo.get_by_id(1)
loan.due_date = date.today() - timedelta(days=5)   # time-travel: pretend due 5 days ago

print(loans.return_book(1))
print(copy_repo.get_by_id(1).status)
print(fine_repo.list_pending())
