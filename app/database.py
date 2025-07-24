from  sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker ,declarative_base 

#databse url
DATABASE_URL="sqlite:///notes.db"

#databse configuration for creating engine and session local
engine=create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base() 

#depedency function for getting databse object
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


