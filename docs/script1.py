from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.models import Person

# create an engine to connect to a SQLite database
engine = create_engine("sqlite:///:memory:")

# create a session factory using the engine
Session = sessionmaker(bind=engine)

# create a new session to interact with the database
session = Session()

# create a new person object and add it to the session
person = Person(name="John", age=30, email="john@example.com")
session.add(person)

# commit the transaction to save the person object to the database
session.commit()

# retrieve a person object from the database by name
john = session.query(Person).filter_by(name="John").first()

# update the person's email address
john.email = "johnny@example.com"

# commit the transaction to save the changes to the database
session.commit()

# delete the person object from the database
session.delete(john)
session.commit()

# close the session to free up resources
session.close()
