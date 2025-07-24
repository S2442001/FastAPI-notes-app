from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.user import UserCreate, Token
from app.crud import auth
from app.core.security import create_access_token
from datetime import timedelta
from app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/signup", response_model=Token)
def signup(user_data: UserCreate,db:Session=Depends(get_db)):
    user = auth.create_user(db,user_data)
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user = auth.authenticate_user(db,form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
