from sqlalchemy import Column,Integer,String,Float,DateTime,ForeignKey 
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,nullable=False)
    hashed_password=Column(String)

class Note(Base):
    __tablename__="notes"
    id=Column(Integer, primary_key=True,index=False)
    title=Column(String,nullable=False)
    content=Column(String)
    created_at = Column(DateTime, default=datetime.utcnow())
    user_id=Column(Integer,ForeignKey("users.id"))
