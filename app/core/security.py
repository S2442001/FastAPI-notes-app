import time 
from jose import JWTError, jwt 
from passlib.context import CryptContext 
from fastapi import HTTPException,status,Depends,Security 
from fastapi.security import OAuth2PasswordBearer 
from app.database import get_db
from sqlalchemy.orm import Session



#configuration details 
SECRET_KEY="my_key"
ALGORITHM="HS256"
TOKEN_EXPIRE_SECONDS=3600

pwd_context=CryptContext(schemes=["bcrypt"], deprecated="auto") 

oauth2scheme=OAuth2PasswordBearer(tokenUrl="/auth/login") 

# code for password hashing and verifying
def get_password_hash(password):
    return pwd_context.hash(password) 

def verify_password(password, hash_password):
    return pwd_context.verify(password, hash_password)


# create JWT token
def create_access_token(data:dict):
    to_encode=data.copy()
    expire=time.time()+TOKEN_EXPIRE_SECONDS
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode,SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token:str):
    try:
        payload=jwt.decode(token,key=SECRET_KEY, algorithms=ALGORITHM)
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, details="invalid token")
    

def get_current_user(token: str = Depends(oauth2scheme),db:Session=Depends(get_db)):
    payload = decode_token(token)
    if not payload or "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )
    username=payload["sub"]
    from app.models.models import User
    user = db.query(User).filter(User.username == username).first()
        
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user

