# Simple challenge - eliminate all bugs from the supplied code so that the code runs and outputs the expected value. Output should be the length of the longest word, as a number.

# There will only be one 'longest' word.

def find_longest(string):
    # spl = string.split(" ")
    # longest = 0
    # i=0
    # while len(spl) > i:
    #     if len(spl[i]) > longest:
    #         longest = len(spl[i])
    #     i += 1
    # return longest
    return max(len(i) for i in string.split())
string = "The quick white fox jumped around the massive dog"
test = find_longest(string)
print(test)
