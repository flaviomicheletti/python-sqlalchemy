from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Engine = create_engine('sqlite:///:memory:')
Session = sessionmaker(bind=Engine)
session = Session()
Base = declarative_base()

class Person(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)

    def __repr__(self):
        return f"<Person(name='{self.name}', age='{self.age}', email='{self.email}')>"

# Create a new person
new_person = Person(name='John', age=30, email='john@example.com')
session.add(new_person)
session.commit()

# Read a person
person = session.query(Person).filter_by(name='John').first()
print(person)

# Update a person
person.age = 31
session.commit()

# Delete a person
session.delete(person)
session.commit()

# Close the session
session.close()
