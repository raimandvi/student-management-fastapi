from pydantic import BaseModel


class StudentBase(BaseModel):
    name: str
    age: int
    email: str


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int

    class Config:
        orm_mode = True
