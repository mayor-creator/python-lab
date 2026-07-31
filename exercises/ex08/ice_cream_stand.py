from restaurant import Restaurant


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


ice_cream = IceCreamStand("flavor lab", "ice cream")
print(ice_cream.describe_restaurant())

ice_cream.flavors.flavors = ["vanilla", "chocolate", "strawberry"]
ice_cream.display_flavors()
