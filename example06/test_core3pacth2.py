import unittest
from unittest.mock import patch, Mock
from example06 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    @patch("example06.create_engine")
    def test_engine(self, engine_mock):
        self.assertIsNotNone(engine_mock)

    @patch("example06.sessionmaker")
    def test_session(self, sessionmaker_mock):
        session_mock = sessionmaker_mock()()
        session_mock.close = lambda: None
        self.assertIsNotNone(session_mock)
        session_mock.close()

    def test_base(self):
        with patch("example06.declarative_base") as base_mock:
            base_mock.metadata = Mock()
            self.assertIsNotNone(base_mock)
            self.assertIsNotNone(base_mock.metadata)
            self.assertIsInstance(base_mock.metadata, object)
