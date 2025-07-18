from .. import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response,status,HTTPException,Depends,APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=['Authentication'])

@router.post("/login",response_model=schemas.Token)
def login(user_credential:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
  user=db.query(models.User).filter(models.User.email==user_credential.username).first()

  if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
  
  if not utils.verify(user_credential.password,user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
  
  access_token=oauth2.create_access_token({'id':str(user.id)})
  
  return {'access_token':access_token,'token_type':'bearer'}



@router.post("/custom_login",response_model=schemas.Token)
def custom_login(user_credentials:schemas.UserLogin,db:Session=Depends(get_db)):
  user=db.query(models.User).filter(models.User.email==user_credentials.email).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
  if not utils.verify(user_credentials.password,user.password):
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
  
  access_token=oauth2.create_access_token({'id':str(user.id)})

  return {'access_token':access_token,'token_type':'bearer'}

@router.get("/me",response_model=schemas.UserResponse)
def get_me(current_user:models.User=Depends(oauth2.get_current_user)):
  return current_user









  






