#Login Attempts

class User():

    def __init__(self, first_name, last_name, age, profession, car):
        self.first_name = first_name
        self.last_name  = last_name
        self.age = age
        self.profession = profession
        self.car = car
        self.login_attempts = 0
    
    def describe_user(self):
        msg = self.first_name.title() + " " + self.last_name.title() + " is " + str(self.age) + " years old and works as " + self.profession + " and have " + self.car.title() + " car."
        print(msg)  

    def greet_user(self):
        msg = "Hello, " + self.first_name.title()
        print(msg)
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0

# adam = User('adam', 'hopkins', 28, 'accountant', 'porshe')
# print(adam.first_name.title())
# adam.greet_user()
# adam.describe_user()  

tyler = User('tyler', 'durden', 31, 'fighter', 'ferrari')
print(tyler.login_attempts)
tyler.increment_login_attempts()
tyler.increment_login_attempts()
tyler.increment_login_attempts()
print(tyler.login_attempts)
tyler.reset_login_attempts()
print(tyler.login_attempts)