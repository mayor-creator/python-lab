class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # Default attribute value
        self.number_served = 0

    def describe_restaurant(self):
        """Print a message describing the restaurant."""
        print(
            f"A modern day {self.restaurant_name} restaurant serves {self.cuisine_type}."
        )
        print("And simple meals made daily with local ingredients.")

    def open_restaurant(self):
        """Print a message indicating open hours."""
        print("The restaurant opens on Monday - Saturday from 10am - 8pm.")

    def number_customers_served(self):
        """Print the number of customers served"""
        print(f"The number of customers served is {self.number_served}")

    def set_number_served(self, customers):
        """Set the number of customers served"""
        if customers < 0:
            return "Number served can't be negative"
        else:
            self.number_served = customers

    def increment_number_served(self, customers):
        """Increment the number of served"""
        if customers < 0:
            return "Number served can't be negative"
        else:
            self.number_served += customers


restaurant = Restaurant("Local Kitchen", "African")
print(restaurant.restaurant_name)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant.set_number_served(20)
restaurant.number_customers_served()

restaurant.increment_number_served(30)
restaurant.number_customers_served()
