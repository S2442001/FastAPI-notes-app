from fastapi import FastAPI 
from app.database import Base,engine
from app.api import auth,notes

app=FastAPI(title="Notes App")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(notes.router)

