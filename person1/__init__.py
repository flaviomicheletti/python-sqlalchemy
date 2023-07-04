from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from config import postegres_string

Engine = create_engine(postegres_string(), echo=True)
Session = sessionmaker(bind=Engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)


def read_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    session.close()
    return person
