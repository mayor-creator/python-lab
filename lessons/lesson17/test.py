# unit test verifies that one specific aspect of a function's behavior is correct.
# test case is a collection of unit tests that together prove that a function
# behaves as it's supposed to.

import unittest

from name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Test for name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name("janis", "joplin")
        self.assertEqual(formatted_name, "Janis Joplin")

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name(
            f_name="janis", m_name="middle", l_name="joplin"
        )
        self.assertEqual(formatted_name, "Janis Middle Joplin")


if __name__ == "__main__":
    unittest.main()
