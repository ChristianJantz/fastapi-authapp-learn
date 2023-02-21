from schemas.user import UserSchema
from models.users import User
from sqlmodel import Session

def create_user(db_session: Session, user: UserSchema):
    hashed_pwd = user.password
    