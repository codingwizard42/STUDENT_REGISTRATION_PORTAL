from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Score
from app.crud import create_score, get_scores, get_score, update_score, delete_score

router = APIRouter()

@router.get("/scores/", response_model=list[Score])
def get_scores_api(skip: int = 0, limit: int = 10, db: Session = Depends(SessionLocal)):
    return get_scores(db=db, skip=skip, limit=limit)

@router.get("/scores/{score_id}", response_model=Score)
def get_score_api(score_id: int, db: Session = Depends(SessionLocal)):
    return get_score(db=db, score_id=score_id)

@router.put("/scores/{score_id}", response_model=Score)
def update_score_api(score_id: int, value: int, db: Session = Depends(SessionLocal)):
    return update_score(db=db, score_id=score_id, value=value)

@router.delete("/scores/{score_id}", response_model=Score)
def delete_score_api(score_id: int, db: Session = Depends(SessionLocal)):
    return delete_score(db=db, score_id=score_id)
