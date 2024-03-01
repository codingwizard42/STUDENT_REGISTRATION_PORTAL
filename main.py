from fastapi import FastAPI
from app.database import engine 
from app.routers import student, subject, score

app = FastAPI()

# Include routers
app.include_router(student.router)
app.include_router(subject.router)
app.include_router(score.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)