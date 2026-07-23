from app.repositories.book_repository import InMemoryBookRepository
from app.repositories.copy_repository import InMemoryCopyRepository
from app.repositories.student_repository import InMemoryStudentRepository
from app.repositories.loan_repository import InMemoryLoanRepository
from app.repositories.fine_repository import InMemoryFineRepository
from app.services.catalog_service import CatalogService
from app.services.student_service import StudentService
from app.services.loan_service import LoanService
from app.services.fine_service import FineService

book_repo = InMemoryBookRepository()
copy_repo = InMemoryCopyRepository()
student_repo = InMemoryStudentRepository()
loan_repo = InMemoryLoanRepository()
fine_repo = InMemoryFineRepository()

catalog_service = CatalogService(book_repo, copy_repo)
student_service = StudentService(student_repo)
loan_service = LoanService(student_repo, loan_repo, copy_repo, book_repo, fine_repo)
fine_service = FineService(fine_repo)
