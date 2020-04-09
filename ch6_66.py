#Polling

favourite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}

should_list = ['jen', 'bart', 'paul', 'phil', 'adam']

for name in should_list:
    if name in favourite_languages:
        print("Thank you %s for taking part in poll." % name.title() )
    else:
        print("%s you are invited to take part in a poll!!!" % name.title())