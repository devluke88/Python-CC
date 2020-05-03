def to_alternating_case(string):
    # new_word = ''
    # for s in string:
    #     if s.isspace() or s.isalpha() == False:
    #         new_word += s
    #     else:
    #         if s.isupper():
    #             new_word += s.lower()
    #         elif s.islower():
    #             new_word += s.upper()
            
    # return new_word
    return string.swapcase()



string = 'hello world'
test = to_alternating_case(string)
print(test)