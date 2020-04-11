#Ice Cream Stand:

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
        self.served = 0
    
    def describe_restaurant(self):
        print("\nThis restaurant is called: " + self.restaurant.title() + " and cook the " + self.cuisine.title() + " style of food.")

    def open_restaurant(self):
        print(self.restaurant.title() + " is open now.")
    
    def number_served(self, clients_served):
        self.served = clients_served
    
    def increment_number_served(self, increment_served):
        self.served += increment_served

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanila', 'strawberry', 'chocolate', 'nuts']
    
    def display_flavors(self):
        print("Available flavors are: ")
        for flavor in self.flavors:
            print("- " + flavor)


grycan = IceCreamStand('Grycan')
grycan.describe_restaurant()
grycan.display_flavors()