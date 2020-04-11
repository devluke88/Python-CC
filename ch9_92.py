#Three Restaurants:

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print("\nThis restaurant is called: " + self.restaurant.title() + " and cook the " + self.cuisine.title() + " style of food.")

    def open_restaurant(self):
        print(self.restaurant.title() + " is open now.")

kp = Restaurant('kuchnia polska', 'polish')
buona = Restaurant('buona', 'italian')
hungary = Restaurant('gary', 'hungarian')

kp.open_restaurant()
kp.describe_restaurant()

buona.describe_restaurant()
buona.open_restaurant()

hungary.describe_restaurant()
hungary.open_restaurant()