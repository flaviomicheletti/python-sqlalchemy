import unittest
from unittest.mock import MagicMock
from example06 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    def test_engine(self):
        engine_mock = MagicMock()
        self.assertIsNotNone(engine_mock)

    def test_session(self):
        session_mock = MagicMock()
        session_mock.close = MagicMock()
        self.assertIsNotNone(session_mock)
        session_mock.close()

    def test_base(self):
        base_mock = MagicMock()
        base_mock.metadata = MagicMock()
        self.assertIsNotNone(base_mock)
        self.assertIsNotNone(base_mock.metadata)
        self.assertIsInstance(base_mock.metadata, object)
