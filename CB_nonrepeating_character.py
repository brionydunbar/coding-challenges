"""
Have the function NonrepeatingCharacter(str) take the str parameter being passed, which will contain only alphabetic characters and spaces, and return the first non-repeating character.
For example: if str is "agettkgaeee" then your program should return k.
The string will always contain at least one character and there will always be at least one non-repeating character.

Examples:
Input: "abcdef"
Output: a

Input: "hello world hi hey"
Output: w
"""


def NonrepeatingCharacter(strParam):
    # define limit - this assumes lowercase
    max_char = 26
    visited = [-1] * max_char  # -1 if char not seen, -2 if repeated, >=0 index of first occurrence if seen once

    # traverse string and record positions/repeats
    for i, ch in enumerate(strParam):
        if ch == " ":
            continue
        index = ord(strParam[i]) - ord("a")
        if visited[index] == -1:
            # store index when char first seen
            visited[index] = i
        else:
            # mark char as repeated
            visited[index] = -2

    index = -1  # index of the result character in string
    # find smallest index of non-repeating chars
    for i in range(max_char):
        if visited[i] >= 0 and (index == -1 or visited[i] < visited[index]):
            index = i

    return strParam[visited[index]] if index != -1 else None


# keep this function call here
# print(NonrepeatingCharacter(input()))

# Testing:
str1 = "abcdef"  # "a"
str2 = "hello world hi hey"  # "w"
str3 = "agettkgaeee"  # "k"

print(NonrepeatingCharacter(str1))
print(NonrepeatingCharacter(str2))
print(NonrepeatingCharacter(str3))

