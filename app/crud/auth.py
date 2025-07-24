from sqlalchemy.orm import Session
from app.models.models import User
from app.schemas.user import UserCreate
from app.core.security import verify_password, get_password_hash
from fastapi import HTTPException, status

# Create a new user
def create_user(db: Session, user_data: UserCreate):
    existing_user = db.query(User).filter(User.username == user_data.name).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    hashed_password = get_password_hash(user_data.password)
    user = User(username=user_data.name, hashed_password=hashed_password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# Authenticate an existing user
def authenticate_user(db: Session, name: str, password: str) :
    user = db.query(User).filter(User.username == name).first()
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

# Optional: Get user by name
def get_user_by_name(db: Session, name: str) :
    return db.query(User).filter(User.username == name).first()

# Optional: Get user by ID
def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
