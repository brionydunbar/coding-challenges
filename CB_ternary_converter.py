"""
Have the function TernaryConverter(num) take the num parameter being passed, which will always be a positive integer, and convert it into a ternary representation.
For example: if num is 12 then your program should return 110.

Examples:
Input: 21
Output: 210

Input: 67
Output: 2111
"""

def TernaryConverter(num):
  e = num // 3
  q = num % 3
  if num == 0:
    return "0"
  elif e == 0:
    return str(q)
  else:
    return TernaryConverter(e) + str(q)

# keep this function call here
# print(TernaryConverter(input()))

# Testing:
num1 = 21 # 210
num2 = 67 # 2111
num3 = 12 # 110

print(TernaryConverter(num1))
print(TernaryConverter(num2))
print(TernaryConverter(num3))