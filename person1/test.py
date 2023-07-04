import unittest
from unittest.mock import patch
from person1 import Person, read_person


class TestReadPerson(unittest.TestCase):
    @patch("person1.Session")
    def test_read_person(self, mock_session):

        mock_person = Person(name="John", age=30, email="john@example.com")
        mock_session.return_value.query.return_value.filter_by.return_value.first.return_value = (
            mock_person
        )

        result = read_person("John")

        self.assertEqual(result.name, "John")
        self.assertEqual(result.age, 30)
        self.assertEqual(result.email, "john@example.com")
