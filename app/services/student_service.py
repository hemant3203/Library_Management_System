from datetime import date

from app.models.student import Student
from app.repositories.student_repository import StudentRepository
from app.exceptions.errors import ConflictError, NotFoundError


class StudentService:
    def __init__(self, student_repo: StudentRepository) -> None:
        self._student_repo = student_repo

    def register_student(self, name: str, email: str) -> Student:
        existing = self._student_repo.get_by_email(email)
        if existing is not None:
            raise ConflictError(f"Email '{email}' is already registered")
        student = Student(0, name, email, date.today())
        return self._student_repo.add(student)

    def get_student(self,student_id:int)->Student:
        student=self._student_repo.get_by_id(student_id)
        if student is None:
            raise NotFoundError(f"Student with id '{student_id}' not found")
        return student
    