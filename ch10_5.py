#Programming Poll:

filename = 'responses.txt'

while True:
    ans = input("Why do you like programming? Enter 'q' if you want to quit. ")
    if ans == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(ans + "\n")