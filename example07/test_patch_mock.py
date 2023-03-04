from unittest.mock import Mock
import unittest
from example07 import Engine, Session, Base


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.engine_mock = Mock(spec=Engine)
        self.session_mock = Mock(spec=Session)
        self.base_mock = Mock(spec=Base)

    def test_engine(self):
        self.assertIsNotNone(self.engine_mock)

    def test_session(self):
        self.assertIsNotNone(self.session_mock)

    def test_base(self):
        self.assertIsNotNone(self.base_mock)
        self.assertIsNotNone(self.base_mock.metadata)
        self.assertIsInstance(self.base_mock.metadata, object)

