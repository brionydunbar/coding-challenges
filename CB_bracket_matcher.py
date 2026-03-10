"""
Challenge:
    Have the function bracket_matcher(a_string) take the a_string parameter being passed and return 1 if the brackets are correctly matched and each one is accounted for.
    Otherwise, return 0. For example: if a_string is "(hello (world))", then the output should be 1, but if a_string is "((hello (world))" then the output should be 0 because the brackets do not correctly match up.
    Only "(" and ")" will be used as brackets. If a_string contains no brackets return 1.

Requirements:
    Function name: bracket_matcher(a_string)
    Return 1 if brackets are correctly matched, 0 otherwise
    Only parentheses ( and ) are used as brackets
    Must handle nested brackets correctly
    If no brackets exist in the string, return 1
    Must ensure brackets are in correct order (opening before closing)

Test Cases:
    "(hello (world))" → should return 1
    "((hello (world))" → should return 0 (missing closing bracket)
    "hi()" → should return 1
    "(hi" → should return 0 (unmatched opening bracket

"""


def bracket_matcher(a_string):
    count = 0
    for char in a_string: # using all ifs means each step is executed
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0: # for edge cases of ")("
            return 0
    if count == 0:
        return 1
    else:
        return 0

print(bracket_matcher("(hello (world))")) # return 1
print(bracket_matcher("((hello (world))")) # return 0 (missing closed bracket)
print(bracket_matcher("hi()")) # return 1
print(bracket_matcher("(hi")) # return 0 (unmatched opening bracket)
print(bracket_matcher(")()(")) # return 0 as brackets ar wrong way