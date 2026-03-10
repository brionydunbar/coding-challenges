"""
Have the function PalindromeTwo(str) take the str parameter being passed and return the string true if the parameter is a palindrome,
(the string is the same forward as it is backward) otherwise return the string false.
The parameter entered may have punctuation and symbols but they should not affect whether the string is in fact a palindrome.
For example: "Anne, I vote more cars race Rome-to-Vienna" should return true.

Examples:
Input: "Noel - sees Leon"
Output: true
Input: "A war at Tarawa!"
Output: true
"""

import string

def PalindromeTwo(strParam):
  # strip string of punc
  clean_string = "".join([char for char in strParam if char not in string.punctuation])
  # remove spaces
  no_spaces = clean_string.replace(" ", "")
  # remove caps
  new_str = no_spaces.lower()
  # compare if reversed string is same
  return "true" if new_str == new_str[::1] else "false"

# keep this function call here
# print(PalindromeTwo(input()))

# Testing:
input1 = "Noel - sees Leon" # "true"
input2 = "A war at Tarawa!" # "false"

print(PalindromeTwo(input1))
print(PalindromeTwo(input2))