from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

engine = create_engine('sqlite:///person.db')
Session = sessionmaker(bind=engine)

def read_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    session.close()
    return person