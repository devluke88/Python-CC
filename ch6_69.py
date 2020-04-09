#Favorite places:

favorite_places = {
    'adam': ['eden', 'earth', 'heaven'],
    'roman': ['poland', 'egypt', 'netherland'],
    'bogdan': ['gyana', 'scotland', 'wales'],
}

for name, places in favorite_places.items():
    print("\n%s's favourite places are: " % name.title())
    for place in places:
        print("\t" + place.title())
