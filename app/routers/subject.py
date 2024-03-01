from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Subject
from app.crud import create_subject, get_subjects, get_subject, update_subject, delete_subject, create_score

router = APIRouter()

@router.post("/subjects/", response_model=Subject)
def create_subject_api(name: str, day: str, time: str, db: Session = Depends(SessionLocal)):
    db_subject = create_subject(db=db, name=name, day=day, time=time)
    # Assume the subject creation is associated with creating scores for that subject
    create_score(db=db, value=0, subject_id=db_subject.id)
    return db_subject
