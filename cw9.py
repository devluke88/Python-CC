# Abbreviate a Two Word Function:

# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

# The output should be two capital letters with a dot separating them.

# It should look like this:

# Sam Harris => S.H

# Patrick Feeney => P.F
def abbrevName(name):
    splited = name.split()
    f = splited[0][0]
    l = splited[1][0]
    return f.title() + "." + l.title()

test = abbrevName("Sam Harris")
print(test)
