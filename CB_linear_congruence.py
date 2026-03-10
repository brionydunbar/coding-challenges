"""
Have the function LinearCongruence(str) read the str parameter being passed which will be a linear congruence equation in the form: "ax = b (mod m)"
Your goal is to solve for x and return the number of solutions to x.
For example: if str is "32x = 8 (mod 4)" then your program should return 4 because the answers to this equation can be either 0, 1, 2, or 3.

Examples:
Input: "12x = 5 (mod 2)"
Output: 0

Input: "12x = 4 (mod 2)"
Output: 2
"""

import math

def LinearCongruence(strParam):
  # parse string and extract a, b and m
  parts = strParam.split()
  a = int(parts[0].replace("x", ""))
  b = int(parts[2])
  m = int(parts[4].replace("(", "").replace(")", ""))

  # calculate greatest common divisor
  g = math.gcd(a, m)

  # check if b is divible by g
  if b % g == 0:
    return g # number of solutions equal to gcd
  else:
    return 0 # no solutions if not divisible

# keep this function call here
# print(LinearCongruence(input()))

# Testing:
str1 = "12x = 5 (mod 2)" # 0
str2 = "12x = 4 (mod 2)" # 2
str3 = "32x = 8 (mod 4)" # 4

print(LinearCongruence(str1))
print(LinearCongruence(str2))
print(LinearCongruence(str3))