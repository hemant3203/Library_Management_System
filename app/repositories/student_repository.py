from abc import ABC, abstractmethod
from typing import Optional

from app.models.student import Student

class StudentRepository(ABC):

    @abstractmethod
    def add(self, student :Student)->Student:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self,student_id:int)->Optional[Student]:
        raise NotImplementedError

    @abstractmethod
    def list_all(self)->list[Student]:
        raise NotImplementedError

    @abstractmethod
    def get_by_email(self, email:str)->Optional[Student]:
        raise NotImplementedError

class InMemoryStudentRepository(StudentRepository):

    def __init__(self)-> None:
        self._students:dict[int,Student] = {}
        self._next_id:int =1

    def add(self,student :Student)->Student:
        student.id=self._next_id
        self._students[student.id]=student
        self._next_id+=1
        return student

    def get_by_id(self, student_id:int)->Optional[Student]:
        return self._students.get(student_id)

    def list_all(self)->list[Student]:
        return list(self._students.values())

    def get_by_email(self, email:str)->Optional[Student]:
        for student in self._students.values():
            if email.lower() == student.email.lower():
                return student
        return None