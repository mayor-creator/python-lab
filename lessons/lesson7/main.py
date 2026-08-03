from car import CarBluePrint
from inheritance import ElectricCarBluePrint

my_new_car = CarBluePrint("porsche", "gt2rs", 2027)
print(my_new_car.print_car())

my_new_car.odometer_reading = 80
print(my_new_car.read_odometer())

my_electric_car = ElectricCarBluePrint("porsche", "macan", 2030)
print(my_electric_car.print_car())
print(my_electric_car.describe_battery())

my_passat = CarBluePrint("volkswagen", "passat", 2012)
print(my_passat.print_car())
my_passat.odometer_reading = 14_500_00
print(my_passat.read_odometer())
