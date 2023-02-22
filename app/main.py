from .commons import crud
from fastapi import FastAPI, Depends
from .database import database
from sqlmodel import Session
from .schemas.user import UserSchema

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
async def login(db_session: Session = Depends(database.get_db)):
    pass
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