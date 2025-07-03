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


#models.Base.metadata.create_all(bind=engine)

app=FastAPI()


@app.get("/")
def root():
    return {'message':'hello Arda CNG'}


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(likes.router)




     

           
           


          
            
           
           
           



           


        
        

    
        













