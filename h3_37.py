#shrinking a guest list

invites = ['Ali', 'Elvis', 'Pope']

invites[2] = 'Bruce'
for invite in invites:
    print("Hello %s unfortunately I can only invite two people for dinner.\n" % invite)

invites.insert(0, 'Adam')
invites.insert(2, 'Paul')
invites.append("Tom")
print(invites)
for invite in invites:
    print("Hello %s I would like to invite you for a dinner." % invite)

while True:
    popped = invites.pop()
    if len(invites) == 2:
        print("\nSorry %s, you are the last one. I have to cancel our dinner" % popped)
        break
    else:
        print("\nSorry %s, I have to cancel our dinner" % popped)

print(len(invites))