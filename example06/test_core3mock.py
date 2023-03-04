import unittest
from unittest.mock import Mock
from example06 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    def test_engine(self):
        engine_mock = Mock()
        self.assertIsNotNone(engine_mock)

    def test_session(self):
        session_mock = Mock()
        session_mock.close = Mock()
        self.assertIsNotNone(session_mock)
        session_mock.close()

    def test_base(self):
        base_mock = Mock()
        base_mock.metadata = Mock()
        self.assertIsNotNone(base_mock)
        self.assertIsNotNone(base_mock.metadata)
        self.assertIsInstance(base_mock.metadata, object)
