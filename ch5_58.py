#Hello admin

users = ['admin', 'aga', 'kacper', 'waldek', 'danka']
entered_user = 'danka'

for user in users:
    if user == 'admin':
        print("Hello %s, would you like to see a status report?" % user)
    else:
        print("Hello %s, thank you for logging in again." %user)

