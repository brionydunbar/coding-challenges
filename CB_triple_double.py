"""
Have the function TripleDouble(num1,num2) take both parameters being passed, and return 1 if there is a straight triple of a number at any place in num1 and also a straight double of the same number in num2.
For example: if num1 equals 451999277 and num2 equals 41177722899, then return 1 because in the first parameter you have the straight triple 999 and you have a straight double, 99, of the same number in the second parameter.
If this isn't the case, return 0.

Examples:
Input: 465555 & num2 = 5579
Output: 1

Input: 67844 & num2 = 66237
Output: 0
"""

def TripleDouble(num1,num2):
  list_num1 = list(str(num1))
  str_num2 = str(num2)
  for i in range(len(list_num1) - 2):
    if len(set(list_num1[i:i+3])) == 1:
      double = 2 * str(list_num1[i])
      if double in str_num2:
        return 1
  return 0

# keep this function call here
# print(TripleDouble(input()))

# Testing:
num1 = 465555
num2 = 5579 # 1

num3 = 67844
num4 = 66237 # 0

num5 = 451999277
num6 = 41177722899 # 1

print(TripleDouble(num1, num2))
print(TripleDouble(num3, num4))
print(TripleDouble(num5, num6))