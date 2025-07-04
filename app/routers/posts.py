from .. import models,schemas,oauth2
from ..database import get_db
from typing import Optional
from sqlalchemy import func
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response,status,HTTPException,Depends,APIRouter
from typing import Optional,List

router=APIRouter(prefix="/posts",tags=['Users'])



@router.get("/",response_model=List[schemas.Postout])
def get_posts(db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user),limit:int=10,skip:int=0,search:Optional[str]=""):
    #print(current_user.email) #just for checking if current_user properties are working
    results=db.query(models.Post,func.count(models.Like.post_id).label('likes')).join(models.Like,models.Post.id==models.Like.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return results

    

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.PostResponse)
def create_posts(post:schemas.PostCreate,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    user_id=current_user.id
    new_post=models.Post(user_id=user_id,**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@router.get("/user/{id}",response_model=List[schemas.Postout])
def get_users_post(db:Session=Depends(get_db)):
    users_posts=db.query(models.Post,func.count(models.Like.post_id).label('likes')).join(models.Post.id==models.Like.post_id,isouter=True).group_by(models.Post.id).filter(models.Post.user_id==id).all()
    return users_posts






@router.get("/{id}",response_model=schemas.Postout)
def get_post(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    #post=db.query(models.Post).filter(models.Post.id==id).first()
    post=db.query(models.Post,func.count(models.Like.post_id).label('likes')).join(models.Like,models.Like.post_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    if(post):
        return post
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f"post with id {id} was not found")
    


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==id)
    if(post.first()):
        if(post.first().user_id==current_user.id):
            post.delete(synchronize_session=False)
            db.commit()
            return  Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
             raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You can't delete someone other's post")
             
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} was not found")

'''post = db.query(models.Post).filter(models.Post.id == id).first()

if post is None:
    raise HTTPException(status_code=404, detail="Post not found")

db.delete(post)
db.commit()
return Response(status_code=status.HTTP_204_NO_CONTENT)

solution above would also works
'''
    
    

@router.put("/{id}",response_model=schemas.PostResponse)
def update_posts(id:int,updatedpost:schemas.PostCreate,db:Session=Depends(get_db),current_user:models.User=Depends(oauth2.get_current_user)):
            post=db.query(models.Post).filter(models.Post.id==id)
            if(post.first()):
                  if(post.first().user_id==current_user.id):
                    post.update(updatedpost.dict(),synchronize_session=False)
                    db.commit()
                    return post.first()
                  else:
                       raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"You can't update someone other's post")
                       
            
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} was not found")

