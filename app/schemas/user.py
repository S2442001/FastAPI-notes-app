from pydantic import BaseModel

# For signup
class UserCreate(BaseModel):
    name: str
    password: str

# For token response
class Token(BaseModel):
    access_token: str
    token_type: str
