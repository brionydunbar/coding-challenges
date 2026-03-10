"""
Have the function SimplePassword(str) take the str parameter being passed and determine if it passes as a valid password that follows the list of constraints:

1. It must have a capital letter.
2. It must contain at least one number.
3. It must contain a punctuation mark or mathematical symbol.
4. It cannot have the word "password" in the string.
5. It must be longer than 7 characters and shorter than 31 characters.

If all the above constraints are met within the string, then your program should return the string true, otherwise your program should return the string false.
For example: if str is "apple!M7" then your program should return "true".

Examples
Input: "passWord123!!!!"
Output: false
Input: "turkey90AAA="
Output: true
"""

def SimplePassword(strParam):
  symbols = set("!@#$%^&*(),.?\":{}|<>+-=*/")
  has_upper = False
  has_number = False
  has_symbols = False

  # checks for punctuation/symbols
  for char in strParam:
    if char.isupper():
      has_upper = True
    if char.isdigit():
      has_number = True
    if char in symbols:
      has_symbols = True
    # if all three conditions are met, no need to continue looping
    if has_upper and has_number and has_symbols:
      break
  contains_password = "password" in strParam.lower()
  valid_length = 8 <= len(strParam) <= 30
  # return "true" if all conditions are met, otherwise "false"
  if has_upper and has_number and has_symbols and not contains_password and valid_length:
      return "true"
  return "false"

# keep this function call here
# print(SimplePassword(input()))

# Testing:
str1 = "passWord123!!!!" # "false"
str2 = "turkey90AAA=" # true
str3 = "apple!M7" # "true"

print(SimplePassword(str1))
print(SimplePassword(str2))
print(SimplePassword(str3))