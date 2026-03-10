"""
Have the function StringCalculate(str) take the str parameter being passed and evaluate the mathematical expression within in.
The double asterisks (**) represent exponentiation.

For example, if str were "(2+(3-1)*3)**3" the output should be 512.
Another example: if str is "(2-0)(6/2)" the output should be 6.
There can be parenthesis within the string so you must evaluate it properly according to the rules of arithmetic.
The string will contain the operators: +, -, /, *, (, ), and **.
If you have a string like this: #/#*# or #+#(#)/#, then evaluate from left to right.
So divide then multiply, and for the second one multiply, divide, then add.
The evaluations will be such that there will not be any decimal operations, so you do not need to account for rounding.

Examples:
Input: "6*(4/2)+3*1"
Output: 15

Input: "100*2**4"
Output: 1600

"""

import re

def StringCalculate(strParam):
  # handle implicit multiplication (where no * but use of brackets)
  strParam = re.sub(r"(\d)\(", r"\1*(", strParam) # number followed by (
  strParam = re.sub(r"\)(\d)", r")*\1", strParam) # ) followed by number
  strParam = re.sub(r"\)\(", r")*(", strParam) # ) followed by (

  try:
    # evaluate expression
    result = eval(strParam)
    return int(result) # no decimals so int fine
  except Exception as e:
    return "invalid expression"

# keep this function call here
# print(StringCalculate(input()))

# Testing:
str1 = "6*(4/2)+3*1" # 15
str2 = "100*2**4" # 1600
str3 = "(2+(3-1)*3)**3" # 512
str4 = "(2-0)(6/2)" # 6

print(StringCalculate(str1))
print(StringCalculate(str2))
print(StringCalculate(str3))
print(StringCalculate(str4))