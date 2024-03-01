from sqlalchemy.orm import Session
from app.models import Student, Subject, Score

def create_student(db: Session, name: str):
    db_student = Student(name=name)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def create_score(db: Session, value: int, subject_id: int):
    db_score = Score(value=value, subject_id=subject_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score



# Similar CRUD operations for subjects and scores
def get_student(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def get_subject(db: Session, subject_id: int):
    return db.query(Subject).filter(Subject.id == subject_id).first()


def get_score(db: Session, score_id: int):
    return db.query(Score).filter(Score.id == score_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Student).offset(skip).limit(limit).all()


def get_subjects(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Subject).offset(skip).limit(limit).all()


def get_scores(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Score).offset(skip).limit(limit).all()


def update_student(db: Session, student_id: int, name: str):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db_student.name = name
        db.commit()
        db.refresh(db_student)
    return db_student


def update_subject(db: Session, subject_id: int, name: str, day: str, time: str):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if db_subject:
        db_subject.name = name
        db_subject.day = day
        db_subject.time = time
        db.commit()
        db.refresh(db_subject)
    return db_subject


def update_score(db: Session, score_id: int, value: int):
    db_score = db.query(Score).filter(Score.id == score_id).first()
    if db_score:
        db_score.value = value
        db.commit()
        db.refresh(db_score)
    return db_score


def delete_student(db: Session, student_id: int):
    db_student = db.query(Student).filter(Student.id == student_id).first()
    if db_student:
        db.delete(db_student)
        db.commit()
    return db_student


def delete_subject(db: Session, subject_id: int):
    db_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    if db_subject:
        db.delete(db_subject)
        db.commit()
    return db_subject


def delete_score(db: Session, score_id: int):
    db_score = db.query(Score).filter(Score.id == score_id).first()
    if db_score:
        db.delete(db_score)
        db.commit()
    return db_score
