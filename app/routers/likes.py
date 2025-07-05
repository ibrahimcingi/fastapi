from .. import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response,status,HTTPException,Depends,APIRouter
from fastapi.responses import JSONResponse


router=APIRouter(tags=['Likes'],prefix='/likes')

@router.post("/")
def like(like_request:schemas.Like,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
  existing_like=db.query(models.Like).filter(models.Like.post_id==like_request.post_id,models.Like.user_id==current_user.id).first()
  if existing_like:
    db.delete(existing_like)
    db.commit()
    return  Response(status_code=status.HTTP_204_NO_CONTENT)
  else:
    new_like = models.Like(post_id=like_request.post_id, user_id=current_user.id)
    db.add(new_like)
    db.commit()
    return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={"status": "liked", "post_id": new_like.post_id,"user_id":current_user.id}
        )
  
@router.post("/{post_id}")
def like(post_id:int,current_user:models.User=Depends(oauth2.get_current_user),db:Session=Depends(get_db)):
  post=db.query(models.Post).filter(models.Post.id==post_id).first()
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
  else:
    existing_like=db.query(models.Like).filter(models.Like.user_id==current_user.id,models.Like.post_id==post_id).first()
    if existing_like:
      db.delete(existing_like)
      db.commit()
      return  Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
      new_like=models.Like(post_id=post_id,user_id=current_user.id)
      db.add(new_like)
      db.commit()
      return JSONResponse(
              status_code=status.HTTP_201_CREATED,
              content={"status": "liked", "post_id": new_like.post_id,"user_id":current_user.id}
          )




  
