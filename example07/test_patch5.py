import unittest
from unittest.mock import patch
from example07 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    @patch("example07.create_engine")
    @patch("example07.sessionmaker")
    @patch("example07.declarative_base")
    def test_engine(self, base_mock, sessionmaker_mock, engine_mock):
        self.assertIsNotNone(Engine)

    @patch("example07.create_engine")
    @patch("example07.sessionmaker")
    @patch("example07.declarative_base")
    def test_session(self, base_mock, sessionmaker_mock, engine_mock):
        session = Session()
        self.assertIsNotNone(session)
        session.close()

    @patch("example07.create_engine")
    @patch("example07.sessionmaker")
    @patch("example07.declarative_base")
    def test_base(self, base_mock, sessionmaker_mock, engine_mock):
        self.assertIsNotNone(Base)
        self.assertIsNotNone(Base.metadata)
        self.assertIsInstance(Base.metadata, object)
