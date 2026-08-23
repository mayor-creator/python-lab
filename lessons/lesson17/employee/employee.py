class Employee:

    def __init__(self, f_name, l_name, annual_salary):
        self.first_name = f_name
        self.last_name = l_name
        self.annual_salary = annual_salary

    def get_raise(self, pay_raise=5_000):
        new_salary = self.annual_salary + pay_raise
        return new_salary
