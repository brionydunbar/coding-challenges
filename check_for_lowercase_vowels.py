"""
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

input [100,100,116,105,117,121]=>[100,100,116,"i","u",121] output Return the resulting array.
"""
from os import supports_fd


def is_vow(inp):
    vowels = ["a", "e", "i", "o", "u"]
    return [chr(num) if chr(num) in vowels else num for num in inp]

print(is_vow([0, 35, 97, 100]))


# WITHOUT LIST COMPREHENSION

def is_vow2(inp):
    vowels = ["a", "e", "i", "o", "u"]
    out = []
    for num in inp:
        if chr(num) in vowels:
            out.append(chr(num))
        else:
            out.append(num)
    return out

print(is_vow2([0, 35, 97, 100]))
