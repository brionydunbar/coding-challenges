"""
Have the function EvenPairs(str) take the str parameter being passed and determine if a pair of adjacent even numbers exists anywhere in the string.
If a pair exists, return the string true, otherwise return false.
For example: if str is "f178svg3k19k46" then there are two even numbers at the end of the string, "46" so your program should return the string true.
Another example: if str is "7r5gg812" then the pair is "812" (8 and 12) so your program should return the string true.

Examples:
Input: "3gy41d216"
Output: true

Input: "f09r27i8e67"
Output: false

"""

import re

def EvenPairs(strParam):
  # extract all numbers
  nums = re.findall(r"\d+", strParam)
  # check for subsplits
  for num in nums:
    for i in range(1, len(num)):
      left, right = int(num[:i]), int(num[i:])
      if left % 2 == 0 and right % 2 == 0:
        return "true"
  # check adjacent numbers
  for i in range(len(nums) - 1):
    if int(nums[i]) % 2 == 0 and int(nums[i + 1]) % 2 == 0:
      return "true"
  return "false"

# keep this function call here
# print(EvenPairs(input()))

# Testing:
str1 = "3gy41d216" # "true"
str2 = "f09r27i8e67" # "false"
str3 = "7r5gg812" # "true"
str4 = "f178svg3k19k46" # true

print(EvenPairs(str1))
print(EvenPairs(str2))
print(EvenPairs(str3))
print(EvenPairs(str4))