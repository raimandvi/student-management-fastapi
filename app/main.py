from fastapi import FastAPI

from .database import engine
from . import models
from .routers import students

app = FastAPI(title="Student Management System")

models.Base.metadata.create_all(bind=engine)

app.include_router(students.router)


@app.get("/")
def root():
    return {"message": "Student Management System API"}

