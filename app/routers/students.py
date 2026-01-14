from fastapi import APIRouter

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

@router.get("/")
def get_students():
    return {"message": "Students API working"}
