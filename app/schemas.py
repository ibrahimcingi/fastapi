from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional


class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True

class PostCreate(PostBase):
    pass
    

    class Config:
        orm_mode=True

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserResponse(BaseModel):
    id:int
    email:str
    created_at:datetime

    class Config:
        orm_mode=True

class PostResponse(PostBase):
    id:int
    created_at:datetime
    user_id:int
    user:UserResponse
    

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None

class Like(BaseModel):
    post_id:int

class Postout(BaseModel):
    Post:PostResponse
    likes:int



    



    