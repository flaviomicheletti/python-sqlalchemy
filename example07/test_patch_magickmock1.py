import unittest
from unittest.mock import patch, MagicMock
from example07 import Session, Base


class TestDatabase(unittest.TestCase):
    @patch('example07.create_engine')
    def test_engine(self, engine_mock):
        self.assertIsNotNone(engine_mock)
        engine_instance_mock = engine_mock.return_value
        engine_instance_mock.connect = MagicMock(return_value=None)
        global Engine
        Engine = engine_mock

    @patch('example07.Session')
    def test_session(self, session_mock):
        session_instance_mock = session_mock.return_value
        session_instance_mock.close = MagicMock(return_value=None)
        session = Session()
        self.assertIsNotNone(session)
        session.close()

    @patch('example07.Base')
    def test_base(self, base_mock):
        base_instance_mock = base_mock.return_value
        base_instance_mock.metadata = object()
        self.assertIsNotNone(base_mock)
        self.assertIsNotNone(base_instance_mock.metadata)
        self.assertIsInstance(base_instance_mock.metadata, object)
