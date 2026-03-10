"""
Have the function FormattedDivision(num1,num2) take both parameters being passed, divide num1 by num2, and return the result as a string with properly formatted commas and 4 significant digits after the decimal place.
For example: if num1 is 123456789 and num2 is 10000 the output should be "12,345.6789".
The output must contain a number in the one's place even if it is a zero.

Examples:
Input: 2 & num2 = 3
Output: 0.6667
Input: 10 & num2 = 10
Output: 1.0000
"""

def FormattedDivision(num1,num2):
  result = num1 / num2
  formatted = f"{result:,.4f}" # f string with format specifier
  return formatted

# keep this function call here
# print(FormattedDivision(input()))

# Testing:
num1 = 2
num2 = 3 # "0.667"

num3 = 10
num4 = 10 # "1.0000"

num5 = 123456789
num6 = 10000 # "12,345.6789"

print(FormattedDivision(num1, num2))
print(FormattedDivision(num3, num4))
print(FormattedDivision(num5, num6))