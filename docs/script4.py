from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Engine = create_engine('sqlite:///example.db')
Session = sessionmaker(bind=Engine)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email


def create_person(name, age, email):
    session = Session()
    person = Person(name=name, age=age, email=email)
    session.add(person)
    session.commit()
    session.close()
    return person


def read_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    session.close()
    return person


def update_person(name, new_name=None, new_age=None, new_email=None):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    if new_name is not None:
        person.name = new_name
    if new_age is not None:
        person.age = new_age
    if new_email is not None:
        person.email = new_email
    session.commit()
    session.close()
    return person


def delete_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    session.delete(person)
    session.commit()
    session.close()


"""
# Example usage
person1 = create_person('John', 30, 'john@example.com')
person2 = create_person('Jane', 25, 'jane@example.com')

print(person1.id)  # 1
print(person2.id)  # 2

person = read_person('John')
print(person.name, person.age, person.email)  # John 30 john@example.com

person = update_person('John', new_age=40)
print(person.age)  # 40

delete_person('Jane')
person = read_person('Jane')
print(person)  # None
"""