import unittest
from unittest.mock import MagicMock
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class UserService:
    def __init__(self, engine):
        self.engine = engine

    def add_user(self, name, email):
        session = sessionmaker(bind=self.engine)()
        user = User(name=name, email=email)
        session.add(user)
        session.commit()

    def get_user_by_email(self, email):
        session = sessionmaker(bind=self.engine)()
        return session.query(User).filter_by(email=email).first()


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(self.engine)

    def test_add_user(self):
        service = UserService(self.engine)
        service.add_user("John", "john@example.com")

        session = sessionmaker(bind=self.engine)()
        user = session.query(User).filter_by(name="John").first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, "john@example.com")

    def test_get_user_by_email(self):
        service = UserService(self.engine)
        service.add_user("John", "john@example.com")
        service.add_user("Jane", "jane@example.com")

        user = service.get_user_by_email("john@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "John")

        user = service.get_user_by_email("jane@example.com")
        self.assertIsNotNone(user)
        self.assertEqual(user.name, "Jane")

    def tearDown(self):
        Base.metadata.drop_all(self.engine)
