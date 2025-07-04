from fastapi import FastAPI, Response,status,HTTPException,Depends
from fastapi.params import Body
from typing import Optional,List
import uuid
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models,schemas,utils
from .database import get_db,engine
from sqlalchemy.orm import Session
from .routers import users,posts,auth,likes
from fastapi.middleware.cors import CORSMiddleware


#models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {'message':'hello Arda CNG'}

@app.get("/post")
def get_posts(db:Session=Depends(get_db)):
    posts=db.query(models.Post).all()
    return posts



app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(likes.router)




     

           
           


          
            
           
           
           



           


        
        

    
        













