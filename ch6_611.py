#cities:

cities = {
    'chicago': {
        'country': 'USA',
        'population': '2.7mln',
        'fact' : 'test1',
    },
    'warsaw': {
        'country': 'poland',
        'population': '1.7mln',
        'fact' : 'test2',
    },
    'berlin': {
        'country': 'germany',
        'population': '3.7mln',
        'fact' : 'test3',
    }
}

for city, city_info in cities.items():
    print("\nCity: " + city.title() + " and their details: ")
    print("\tContry: " + city_info['country'].title())
    print("\tPopulation: " + city_info['population'])
    print("\tFact: " + city_info['fact'])
    