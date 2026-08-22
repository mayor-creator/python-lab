import unittest

from person_function import person


class TestPerson(unittest.TestCase):

    def test_child_person(self):
        """Test for Child"""
        child = person(7)
        self.assertEqual(child, "Child")

    def test_adolescent_person(self):
        """Test for Adolescent"""
        child = person(15)
        self.assertEqual(child, "Adolescent")

    def test_adult_person(self):
        """Test for Adult"""
        child = person(20)
        self.assertEqual(child, "Adult")

    def test_invalid_person(self):
        """Test for Invalid age"""
        child = person(-1)
        self.assertEqual(child, "Invalid age")


if __name__ == "__main__":
    unittest.main(verbosity=2)
