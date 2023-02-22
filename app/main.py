from .commons import crud
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .database import database
from sqlmodel import Session
from .schemas.user import UserSchema
from .commons import auth

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    database.create_db_and_tables()
    
@app.on_event("shutdown")
async def shutdown_event():
    database.find_db_and_shutdown()
    
@app.post("/register")
async def register_user(user: UserSchema, db_session: Session = Depends(database.get_db))-> dict:
    """create a register entrypoint to create a userlogin

    Args:
        user (UserSchema): based on the models.users 
        db_session (Session, optional): instance of the DB connection. Defaults to Depends(database.get_db).

    Returns:
        dict: the parameters of the create user
    """
    db_user = crud.create_user(db_session=db_session, user=user)
    return db_user

@app.post("/login")
async def login(db_session: Session = Depends(database.get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    db_user = crud.get_user_by_username(db_session=db_session, username=form_data.username)
    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect User ord Password")
    if auth.verify_pwassword(plain_password=form_data.password, hashed_password=db_user.hashed_password):
        token = auth.create_access_token(user=db_user)
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid User or Password")

@app.get("/users")
async def list_all_users(db_session: Session = Depends(database.get_db)) -> list:
    """list all users

    Args:
        db_session (Session, optional): the DB connection instance Session. Defaults to Depends(database.get_db).

    Returns:
        list: list of all users in the DB
    """
    users = crud.get_users(db_session=db_session)
    return users

@app.get("/secure")
async def list_all_users(db_session: Session = Depends(database.get_db), token = Depends(auth.oauth2_schema)) -> list:
    """list all users

    Args:
        db_session (Session, optional): the DB connection instance Session. Defaults to Depends(database.get_db).

    Returns:
        list: list of all users in the DB
    """
    users = crud.get_users(db_session=db_session)
    return users