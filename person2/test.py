import unittest
from unittest.mock import MagicMock, patch
from person2 import read_person, model
from person2.db import getSession


class TestPerson2(unittest.TestCase):

    @patch('person2.db.create_engine')
    @patch('person2.db.sessionmaker')
    def test_get_session(self, mock_sessionmaker, mock_create_engine):
        # Set up the mocks
        mock_session = MagicMock()
        mock_sessionmaker.return_value = MagicMock(return_value=mock_session)
        mock_engine = MagicMock()
        mock_create_engine.return_value = mock_engine

        result = getSession()

        # Assertions
        mock_create_engine.assert_called_once_with('sqlite:///person2.db')
        mock_sessionmaker.assert_called_once_with(bind=mock_engine)
        self.assertEqual(result, mock_session)


    @patch('person2.db.getSession')
    def test_read_person(self, mock_get_session):
        # Create a mock session and person object
        mock_person = MagicMock()
        mock_person.name = "John Doe"

        # Configure the mock session to return the mock person object
        mock_session = MagicMock()
        mock_session.query.return_value.filter_by.return_value.first.return_value = mock_person

        # Configure the mock getSession to return the mock session
        mock_get_session.return_value = mock_session

        # Call the read_person function
        result = read_person("John Doe")

        # Assertions
        self.assertEqual(result, mock_person)

        # Verify that getSession was called
        mock_get_session.assert_called_once()

        # Verify that query was called with the correct model
        mock_session.query.assert_called_once_with(model.Person)

        # Verify that filter_by was called with the correct argument
        mock_session.query.return_value.filter_by.assert_called_once_with(name="John Doe")

        # Verify that first was called
        mock_session.query.return_value.filter_by.return_value.first.assert_called_once()

        # Verify that close was called on the session
        mock_session.close.assert_called_once()