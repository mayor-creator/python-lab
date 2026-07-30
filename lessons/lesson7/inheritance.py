class CarBluePrint:
    def __init__(self, brand, model, year):
        """Initialize brand, model and year attributes"""
        self.brand = brand
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def print_message(self):
        return f"Hello, welcome to {self.brand.title()} brand"

    def print_car(self):
        return f"{self.year} {self.model.title()} car"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it."

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# inheritance
class ElectricCarBluePrint(CarBluePrint):
    """Represent aspect of a car, specific to electric cars"""

    def __init__(self, brand, model, year):
        """Initialize attributes of the parent class"""
        super().__init__(brand, model, year)
        # defining attributes for the child class
        self.battery_size = 95

    # defining methods for the child class
    def describe_battery(self):
        return f"This car has a {self.battery_size}-kWh battery."


my_macan = ElectricCarBluePrint("porsche", "macan turbo electric", 2026)
print(my_macan.print_message())
print(my_macan.print_car())
print(my_macan.describe_battery())
