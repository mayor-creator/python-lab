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
