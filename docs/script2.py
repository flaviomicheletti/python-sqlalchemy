from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.models import Person

engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=engine)

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

def update_person(name, age, email):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    person.age = age
    person.email = email
    session.commit()
    session.close()

def delete_person(name):
    session = Session()
    person = session.query(Person).filter_by(name=name).first()
    session.delete(person)
    session.commit()
    session.close()


"""
create_person('John', 30, 'john@example.com')
john = read_person('John')
update_person('John', 31, 'john@example.org')
delete_person('John')
"""