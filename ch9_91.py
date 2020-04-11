#Restaurant:

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        print("\nThis restaurant is called: " + self.restaurant.title() + " and cook the " + self.cuisine.title() + " style of food.")

    def open_restaurant(self):
        print(self.restaurant.title() + " is open now.")

wloska = Restaurant('wloch', 'italian')

wloska.describe_restaurant()
wloska.open_restaurant()

print("I like " + wloska.restaurant.upper() + " restaurant!")