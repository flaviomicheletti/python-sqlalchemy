import unittest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///:memory:")
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)


class TestUser(unittest.TestCase):
    def setUp(self):
        self.session = Session()
        Base.metadata.create_all(engine)

    def tearDown(self):
        self.session.rollback()
        Base.metadata.drop_all(engine)

    def test_create_user(self):
        user = User(name="Alice", email="alice@example.com")
        self.session.add(user)
        self.session.commit()

        result = self.session.query(User).filter_by(name="Alice").one()
        self.assertEqual(result.name, "Alice")
        self.assertEqual(result.email, "alice@example.com")

    def test_duplicate_email(self):
        user1 = User(name="Alice", email="alice@example.com")
        self.session.add(user1)
        self.session.commit()

        user2 = User(name="Bob", email="alice@example.com")
        self.session.add(user2)
        with self.assertRaises(Exception):
            self.session.commit()


# if __name__ == '__main__':
#     unittest.main(verbosity=2)
