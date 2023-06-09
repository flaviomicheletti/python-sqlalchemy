from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def getSession():
    """Get a session to the database"""
    engine = create_engine('sqlite:///person2.db')
    session = sessionmaker(bind=engine)

    return session()
