import unittest
from unittest.mock import patch
from example06 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    @patch("example06.Engine", autospec=True)
    def test_engine(self, engine_mock):
        self.assertIsNotNone(engine_mock)

    @patch("example06.Session", autospec=True)
    def test_session(self, session_mock):
        session_instance_mock = session_mock.return_value
        session_instance_mock.close = lambda: None
        self.assertIsNotNone(session_mock)
        session_instance_mock.close()

    @patch("example06.Base", autospec=True)
    def test_base(self, base_mock):
        base_instance_mock = base_mock.return_value
        base_instance_mock.metadata = object()
        self.assertIsNotNone(base_mock)
        self.assertIsNotNone(base_instance_mock.metadata)
        self.assertIsInstance(base_instance_mock.metadata, object)
