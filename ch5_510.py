#Hello admin

current_users = ['admin', 'aga', 'kacper', 'waldek', 'danka']
new_users = ['andrew', 'AGA', 'krzysiu', 'waldek', 'mateusz']

for user in new_users:
    if user.lower() in current_users:
        print("%s - username is already taken" % user)
    else: 
        print("%s - username is available" % user)
  
