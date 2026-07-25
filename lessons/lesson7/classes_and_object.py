# Object Oriented Programming


# creating a class
class CarBluePrint:
    def __init__(self, brand, model, year):
        """Initialize brand, model and year attributes"""
        self.brand = brand
        self.model = model
        self.year = year

    # create methods for the class
    def print_message(self):
        return f"Hello, welcome to {self.brand.title()} brand"

    def print_car(self):
        return f"{self.year} {self.model.title()} car"


# making an instance from a class
my_car = CarBluePrint("volkswagen", "passat", 2012)
print(f"My car is {my_car.year} {my_car.model.title()}")

# accessing attributes using dot notation
brand_name = my_car.brand
print(brand_name.title())

# calling methods
greetings = my_car.print_message()
print(greetings)

car_year_name = my_car.print_car()
print(car_year_name)
