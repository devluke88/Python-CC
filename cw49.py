# Challenge from Codewars
# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'

# Test.assert_equals(solution('world'), 'dlrow')
# Test.assert_equals(solution('hello'), 'olleh')
# Test.assert_equals(solution(''), '')
# Test.assert_equals(solution('h'), 'h')

def solution(string):
    return string[::-1]