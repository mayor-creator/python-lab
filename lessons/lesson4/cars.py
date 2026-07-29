cars = ["bmw", "audi", "toyota", "porsche", "mercedes"]
print(f"Original cars list: {cars}")

# sorting a list permanently
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# sorting a list temporarily
temporal_sorted_cars = sorted(cars)
print(temporal_sorted_cars)

# finding the length of a list
cars_length = len(cars)
print(f"The length of cars list: {cars_length}")
