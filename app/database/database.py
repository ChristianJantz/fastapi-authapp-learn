from sqlmodel import Session, SQLModel, create_engine
from pathlib import Path
import os

SQLIITE_DATABASE_URL = "sqlite:///./sql_app.db"
# specific creation string for the local db [connect_args={"check_same_thread": False}]
engine = create_engine(SQLIITE_DATABASE_URL, connect_args={"check_same_thread": False})

def get_db():
    """create a session instance of the db engine

    Yields:
        session: instance of the db_connection
    """
    with Session(engine) as session:
        yield session
        
def create_db_and_tables():
    """
    create the given DB and Tables based on the Models
    when the startup event is triggered with the CMD uvicorn app.main:app --reload
    """
    SQLModel.metadata.create_all(engine)
    
    
def find_db_and_shutdown():
    """
    search for the local database in the local directory 
    if the local database was found by her sufix(.db)
        remove the db with the shutdown Event
    """
    cwd = Path.cwd().resolve()
    db_file = [file for file in os.listdir() if file.endswith(".db")][0]
    os.remove(os.path.join(cwd, db_file))