from pydantic import BaseModel,EmailStr,Field
from datetime import datetime
from typing import Optional,Annotated
class PostBase(BaseModel):
    title : str
    content : str
    published : bool = True
    
class PostCreate(PostBase):
    pass 

class UserResponse(BaseModel):
    id : int 
    email : EmailStr
    created_at : datetime
    class Config:
       from_attributes = True

# class PostResponse(BaseModel):
#     title : str
#     content : str
#     owner_id : int
#     owner : UserResponse
#     class Config:
#         from_attributes = True

# class PostOut(PostBase):
#     post : PostResponse
#     Votes : int
#     class Config:
#         from_attributes = True

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    owner_id : int
    class Config:
        from_attributes = True

class PostOut(BaseModel):
    post: PostResponse
    Votes: int

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    email : EmailStr
    password : str

class Userlogin(BaseModel):
    email : EmailStr
    password : str

class Token(BaseModel):
    access_token : str 
    token_type : str 

class Tokendata(BaseModel):
    id : str | None = None
    
class Vote(BaseModel):
    post_id : str
    dir: Annotated[int,Field(ge=0,le=1)]