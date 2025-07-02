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


while True:
    try:
        conn=psycopg2.connect(host="localhost",database="fastapi",user="postgres",password='340721',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print('database connection completed succesfully')
        break
    except Exception as error:
        print("database connection failed.Error:{error}" )
        time.sleep(2)

@app.get("/")
def root():
    return {'message':'hello world'}


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(likes.router)




     

           
           


          
            
           
           
           



           


        
        

    
        













