"""
Have the function AlphabetSoup(str) take the str string parameter being passed and return the string with the letters in alphabetical order (ie. hello becomes ehllo).
Assume numbers and punctuation symbols will not be included in the string.

Examples:
Input: "coderbyte"
Output: bcdeeorty

Input: "hooplah"
Output: ahhloop
"""

def AlphabetSoup(strParam):
  str_list = []
  for char in strParam:
    str_list.append(char)
  alpha_order = sorted(str_list)
  new_string = "".join(alpha_order)
  return new_string

# keep this function call here
# print(AlphabetSoup(input()))

# Testing:
str1 = "coderbyte" # "bcdeeorty"
str2 = "hooplah" # "ahhloop"
str3 = "hello" # "ehllo"

print(AlphabetSoup(str1))
print(AlphabetSoup(str2))
print(AlphabetSoup(str3))