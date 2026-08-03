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


class IceCreamFlavors:
    """To model ice cream flavors for an ice cream stand"""

    def __init__(self, flavors=None):
        """Initialize the flavor's attributes"""
        self.flavors = flavors or []


class IceCreamStand(Restaurant):
    """Represent aspect of a restaurant specific to ice cream stands"""

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = IceCreamFlavors()

    def describe_restaurant(self):
        """Return a description of ice stand"""
        return f"{self.restaurant_name.title()} ice cream stand that serves different kind of flavors."

    def display_flavors(self):
        """Display ice cream flavors"""
        for flavor in self.flavors.flavors:
            print(flavor.title())
