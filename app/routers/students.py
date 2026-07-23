from fastapi import APIRouter

from app.core.dependencies import student_service
from app.schemas.student import StudentCreate

router = APIRouter(prefix="/students", tags=["students"])




@router.post("",status_code=201)
def register_student(payload:StudentCreate):
    return student_service.register_student(payload.name,payload.email)

@router.get("/{student_id}")
def get_student(student_id:int):
    return student_service.get_student(student_id)