# def greet_user(username):
#     print('Hello, ' + username.title() )

# greet_user('james')

#pets
# def describe_pet(animal_type, pet_name):
#     print("\nI have a " + animal_type + ".")
#     print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# describe_pet('hamster', 'harry')

#formatted name
# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = first_name + ' ' + middle_name + ' ' + last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()

# musician = get_formatted_name('jimi', 'hendrix', 'hooker')
# print(musician)

#Person
# def build_person(first_name, last_name, age=''):
#     person = {'first' : first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person

# musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

#Greeter
# def get_formatted_name(first_name, last_name):
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# while True:
#     print("\nPlease tell me your name: ")
#     print("(enter 'q' at any time to quit)")
#     f_name = input("First name: ")
#     if f_name == 'q':
#         break

#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
    

#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

#greet_users 
# def greet_user(names):
#     for name in names:
#         msg = "Hello, " + name.title() + "!"
#         print(msg)
# usernames = ['andrew', 'adam', 'susan']
# greet_user(usernames)

#printing models
# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_desing = unprinted_designs.pop()
#         print("Printing model: " + current_desing)
#         completed_models.append(current_desing)
#     return completed_models

# def show_completed(completed_models):
#     print("The following models has been printed: ")
#     for design in completed_models:
#         print(design)

# unprinted = ['iphone case', 'robot pendant', 'dodecahedron']
# completed = []

# printed = print_models(unprinted, completed)
# show_completed(printed)

#pizza
# def make_pizza(*toppings):
#     # print(toppings)
#     for topping in toppings:
#         print("- " + topping)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# def make_pizza(size, *toppings):
#     print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
#     for topping in toppings:
#         print("- " + topping)

# make_pizza(16, 'pepperoni')
# make_pizza(21, 'mushrooms', 'green peppers', 'extra cheese')

#user profile
# def build_profile(first, last, **user_info):
#     profile = {}
#     profile['first'] = first
#     profile['last'] = last
#     for k, v in user_info.items():
#         profile[k] = v
#     return profile

# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# print(user_profile)



def build_profile(first, last, **user_info):
    profile = {}
    profile['first'] = first.title()
    profile['last'] = last.title()
    for key, val in user_info.items():
        profile[key] = val.title()
    return profile

user = build_profile('adam', 'hopkins', field="IT", location="oxford", powers="routine")
print(user)