# Grade book
# Complete the function so that it finds the mean of the three scores passed to it and returns the letter value associated with that grade.

# Numerical Score	Letter Grade
# 90 <= score <= 100	'A'
# 80 <= score < 90	'B'
# 70 <= score < 80	'C'
# 60 <= score < 70	'D'
# 0 <= score < 60	'F'
# Tested values are all between 0 and 100. Theres is no need to check for negative values or values greater than 100.

def get_grade(s1, s2, s3):
    lst = [s1, s2, s3]
    score = sum(lst)/len(lst)
    if score >= 90 and score <=100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    elif score >= 0 and score < 60:
        return "F"

test = get_grade(90, 95, 93)
print(test)