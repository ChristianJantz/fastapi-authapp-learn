from passlib.context import CryptContext
from ..models.users import User
from jose import jwt
from datetime import datetime, timedelta
from ..commons import settings
from fastapi.security import OAuth2PasswordBearer

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def create_password_hash(password: str) -> str:
    """create a hashed password by given the password

    Args:
        password (str): given password as string

    Returns:
        str: hashed password
    """
    return pwd_context.hash(password)

def verify_pwassword(plain_password: str, hashed_password: str) -> bool:
    """verify the password form the database

    Args:
        plain_password (str): given password by user
        hashed_password (str): hashed password from the database

    Returns:
        bool: True = if the given password is correct password in the DB 
              False = if the given password is not correct password in the DB
    """
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(user: User)-> str:
    claims = {
        "sub": user.username,
        "email": user.email,
        "role": user.role,
        "active": user.is_active,
        "exp": datetime.utcnow() + timedelta(minutes=120)
    }
    return jwt.encode(claims=claims, key=settings.JWT_SECRET, algorithm=settings.ALGORRITHUS)