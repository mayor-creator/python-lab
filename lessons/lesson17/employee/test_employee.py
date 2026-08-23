import unittest

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.new_employee = Employee("Juliette", "Lucas", 95_000)

    def test_default_pay_rise(self):
        """Test for default pay raise value"""
        pay_increase = self.new_employee.get_raise()
        self.assertEqual(pay_increase, 100_000.00)

    def test_change_of_pay_raise(self):
        """Test for change of pay raise default value"""
        pay_raise = self.new_employee.get_raise(pay_raise=10_000)
        self.assertEqual(pay_raise, 105_000.00)


if __name__ == "__main__":
    unittest.main(verbosity=2)
