class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a message describing the restaurant."""
        print(f"A modern day {self.restaurant_name} restaurant.")
        print("And simple meals made daily with local ingredients.")

    def open_restaurant(self):
        """Print a message indicating open hours."""
        print("The restaurant opens on Monday - Saturday from 10am - 8pm.")


restaurant = Restaurant("Local Kitchen", "African")
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()
