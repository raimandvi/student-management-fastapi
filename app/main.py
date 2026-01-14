from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Student Management API")

app.include_router(router)
