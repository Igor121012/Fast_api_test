from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel): # Можно добавить аннотации
    name: str
    email: str
    record: Optional[float] = None

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: str
    password: str  # Только email и пароль для входа

class UserRecord(BaseModel):
    id: int
    record: float # Только id и record для обновления рекорда

class User(UserBase):
    id: int

    class Config: # Нужен для базы данных
        orm_model = True

# Доделать остальную часть !!!
class PostBase(BaseModel):
    title: str
    body: str
    author_id: int

class Post(PostBase):
    id: int
    author: User

    class Config:
        orm_model = True


class PostCreate(PostBase):
    pass