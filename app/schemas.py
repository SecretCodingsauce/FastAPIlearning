from pydantic import BaseModel,EmailStr
from typing import Literal
from datetime import datetime

class PostBase(BaseModel):
    title : str
    content : str
    published : bool=True

class UserOut(BaseModel):

    id: int
    email: EmailStr
    created_at:datetime

    class Config:
            orm_mode= True


class Post(PostBase):
    created_at : datetime
    user_id : int
    user: UserOut
    class Config:
        orm_mode= True

class PostOut(Post):
     votes: int

class createPost(PostBase):
    pass

class User(BaseModel):

    email: EmailStr
    password: str



class UserLogin(User):
     pass


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: int | None = None  


class Vote(BaseModel):
     post_id: int
     direction: Literal[0,1]