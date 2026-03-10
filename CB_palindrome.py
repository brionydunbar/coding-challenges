"""
Have the function Palindrome(str) take the str parameter being passed and return the string true if the parameter is a palindrome, (the string is the same forward as it is backward) otherwise return the string false.
For example: "racecar" is also "racecar" backwards.
Punctuation and numbers will not be part of the string.
"""

def Palindrome(strParam):
  no_spaces = strParam.replace(" ", "")
  reversed_str = no_spaces[::-1]
  if reversed_str == no_spaces:
    return "true"
  else:
    return "false"

# keep this function call here
# print(Palindrome(input()))

# Testing:
str1 = "never odd or even" # "true"
str2 = "eye" # "true"
str3 = "racecar" # "true"

print(Palindrome(str1))
print(Palindrome(str2))
print(Palindrome(str3))