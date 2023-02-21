from sqlmodel import Session, SQLModel, create_engine
from pathlib import Path
import os

SQLIITE_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLIITE_DATABASE_URL, connect_args={"check_same_thread": False})

def get_db():
    with Session(engine) as session:
        yield session
        
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    
    
def find_db_and_shutdown():
    cwd = Path.cwd().resolve()
    db_file = [file for file in os.listdir() if file.endswith(".db")][0]
    os.remove(os.path.join(cwd, db_file))