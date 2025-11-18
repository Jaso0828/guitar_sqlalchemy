from sqlalchemy.orm import Session, declarative_base, sessionmaker
from sqlalchemy import create_engine

from config import DATABASE_PATH

engine = create_engine(DATABASE_PATH, echo = True)

Base = declarative_base()

def get_session() -> Session:
    return Session(bind=engine)