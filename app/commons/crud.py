from ..schemas.user import UserSchema
from ..models.users import User
from ..commons import auth
from sqlmodel import Session

def create_user(db_session: Session, user: UserSchema) -> dict:
    """create a User 

    Args:
        db_session (Session): the given db session instances 
        user (UserSchema): the User Schema based on the models.users

    Returns:
        dict: json message if creation successed
    """
    hashed_pwd = auth.create_password_hash(user.password)
    db_user = User(
        email= user.email,
        username= user.username,
        role= user.role,
        hashed_password=hashed_pwd
    )
    db_session.add(db_user)
    db_session.commit()
    db_session.refresh(db_user)
    return {"message": "successfull created"}

def get_users(db_session: Session) -> list:
    """
    returns all users in the Database Table users based on the models.users.User class
    with the given Session we have access to query the DB based on the models that we are given
    Args:
        db_session (Session): session instance

    Returns:
        list: list of all users in the db
    """
    userlist = db_session.query(User).all()
    return userlist

def get_user_by_username(db_session: Session, username: str) -> object:
    user = db_session.query(User).filter(User.username == username).first()
    return user