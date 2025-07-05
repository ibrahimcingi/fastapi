from .. import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response,status,HTTPException,Depends,APIRouter
from typing import List



router=APIRouter(prefix="/users",tags=['Users'])

@router.get("/",response_model=List[schemas.UserResponse])
def get_users(db:Session=Depends(get_db)):
     users=db.query(models.User).all()
     return users
     



@router.post("/register",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def register_user(userinfo:schemas.UserCreate,db:Session=Depends(get_db)):
    userinfo.password=utils.hash(userinfo.password)

    new_user=models.User(**userinfo.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model=schemas.UserResponse)
def get_user(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    user=db.query(models.User).filter(models.User.id==id).first()
    if user:
         return user
    else:
         raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"user with id {id} was not found")
         