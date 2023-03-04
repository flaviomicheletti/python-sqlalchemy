import unittest
from unittest.mock import patch
from sqlalchemy.orm import sessionmaker, declarative_base


class TestDatabase(unittest.TestCase):
    @patch('sqlalchemy.create_engine')
    def test_engine(self, engine_mock):
        Engine = engine_mock.return_value
        Session = sessionmaker(bind=Engine)
        Base = declarative_base()

        self.assertIsNotNone(Engine)

    @patch('sqlalchemy.orm.sessionmaker')
    def test_session(self, sessionmaker_mock):
        session_mock = sessionmaker_mock()()
        session_mock.close = lambda: None

        self.assertIsNotNone(session_mock)
        session_mock.close()

    @patch('sqlalchemy.ext.declarative.declarative_base')
    def test_base(self, declarative_base_mock):
        Base = declarative_base_mock()
        Base.metadata = object()

        self.assertIsNotNone(Base)
        self.assertIsNotNone(Base.metadata)
        self.assertIsInstance(Base.metadata, object)


"""
Here's an alternative way to rewrite the code using patch that doesn't 
involve modifying the setUp method:
"""