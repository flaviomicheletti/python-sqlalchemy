import unittest
from unittest.mock import MagicMock, patch
from person2.db import getSession
from config import postegres_string


class TestPerson2(unittest.TestCase):

    @patch('person2.db.create_engine', return_value=MagicMock())
    @patch('person2.db.sessionmaker', return_value=MagicMock())
    def test_get_session(self, mock_sessionmaker, mock_create_engine):
        result = getSession()

        # Assertions
        self.assertEqual(result, mock_sessionmaker.return_value.return_value)
        mock_create_engine.assert_called_once()
        mock_sessionmaker.assert_called_once_with(bind=mock_create_engine.return_value)
