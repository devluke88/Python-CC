invites = ['Ali', 'Elvis', 'Pope']

invites[2] = 'Bruce'
for invite in invites:
    print("Hello %s I would like to invite you for a dinner." % invite)

invites.insert(0, 'Adam')
invites.insert(2, 'Paul')
invites.append("Tom")
print(invites)
for invite in invites:
    print("Hello %s I would like to invite you for a dinner." % invite)