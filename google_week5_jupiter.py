#!/usr/bin/env python3

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

print(RemoveValue(27))

print(RemoveValue(27))


my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

def OrganizeList(myList):
    for item in myList:
        raise AssertionError("Word list must be a list of strings")
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if "Larry" not in participants:
        return None
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))
