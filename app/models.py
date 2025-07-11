from sqlalchemy import Integer,String,Boolean,Column,ForeignKey
from sqlalchemy.sql.expression import null,text
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Post(Base):
  __tablename__="posts"

  id=Column(Integer,primary_key=True,nullable=False)
  title=Column(String,nullable=False)
  content=Column(String,nullable=False)
  published=Column(Boolean,server_default='TRUE',nullable=False)
  created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
  user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

  user=relationship("User")


class User(Base):
  __tablename__="users"
  id=Column(Integer,primary_key=True,nullable=False)
  email=Column(String,nullable=False,unique=True)
  password=Column(String,nullable=False)
  created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))


class Like(Base):
  __tablename__="likes"
  user_id=Column(Integer,ForeignKey('users.id',ondelete="CASCADE"),primary_key=True,nullable=False)
  post_id=Column(Integer,ForeignKey('posts.id',ondelete="CASCADE"),primary_key=True,nullable=False)

  user=relationship("User")
  post=relationship("Post")







