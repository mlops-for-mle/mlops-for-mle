from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    nickname: str


class UserCreateIn(UserBase):
    pass


class UserCreateOut(UserBase):
    id: int
    status: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
