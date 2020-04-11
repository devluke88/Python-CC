#Number Served:

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

wloska = Restaurant('wloch', 'italian')

wloska.describe_restaurant()
wloska.open_restaurant()

print("I like " + wloska.restaurant.upper() + " restaurant!")
print("This restaurant has served " + str(wloska.served) + " clients.")
wloska.number_served(5)
print("This restaurant has served " + str(wloska.served) + " clients.")
wloska.increment_number_served(50)
print("This restaurant has served " + str(wloska.served) + " clients.")