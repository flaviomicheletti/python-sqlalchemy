from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import postegres_string


def getSession():
    Engine = create_engine(postegres_string())
    Session = sessionmaker(bind=Engine)

    return Session()
