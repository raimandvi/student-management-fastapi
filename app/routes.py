from typing import List
from fastapi import APIRouter
from .models import Student

router = APIRouter()
students_db: List[Student] = []

@router.post("/students")
def add_student(student: Student):
    students_db.append(student)
    return {"message": "Student added"}

@router.get("/students")
def get_students():
    return students_db
