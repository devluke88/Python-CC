#People

people = {
    'ahopkins': {
        'first_name' : 'Adam',
        'last_name' : 'Hopkins',
        'age' : '32',
        'city' : 'New York',
    },
    'agolota': {
        'first_name' : 'Andrew',
        'last_name' : 'Golota',
        'age' : '47',
        'city' : 'Chicago',
    },
    'escorupko': {
        'first_name' : 'Eva',
        'last_name' : 'Scorupko',
        'age' : '30',
        'city' : 'Sidney',
    },
}

for username, user_info in people.items():
    print("\nPerson: " + username)
    full_name = user_info['first_name'] + " " + user_info['last_name']
    age = user_info['age']
    city = user_info['city']

    print("\tFull name: " + full_name.title())
    print("\tAge: " + age)
    print("\tFull name: " + city.title())

print("\nEND")
