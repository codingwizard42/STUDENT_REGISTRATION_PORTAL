from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Student
from app.crud import create_student
from app.crud import create_student, get_students, get_student, update_student, delete_student
router = APIRouter()

@router.post("/students/")
def create_student_api(name: str, db: Session = Depends(SessionLocal)):
    return create_student(db=db, name=name)
 


@router.get("/students/", response_model=list[Student])
def get_students_api(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return get_students(db=db, skip=skip, limit=limit)

@router.get("/students/{student_id}", response_model=Student)
def get_student_api(student_id: int, db: Session = Depends(SessionLocal)):
    return get_student(db=db, student_id=student_id)

@router.put("/students/{student_id}", response_model=Student)
def update_student_api(student_id: int, name: str, db: Session = Depends(SessionLocal)):
    return update_student(db=db, student_id=student_id, name=name)

@router.delete("/students/{student_id}", response_model=Student)
def delete_student_api(student_id: int, db: Session = Depends(SessionLocal)):
    return delete_student(db=db, student_id=student_id)
