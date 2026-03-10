"""
Have the function PermutationStep(num) take the num parameter being passed and return the next number greater than num using the same digits.
For example: if num is 123 return 132, if it's 12453 return 12534.
If a number has no greater permutations, return -1 (ie. 999).

Examples:
Input: 11121
Output: 11211

Input: 41352
Output: 41523
"""

def PermutationStep(num):
  num = str(num)
  # no greater permutation if num is 1 digit
  if len(num) == 1:
    return -1
  # start from right and find first digit smaller than digit next to it
  i = len(num) - 1
  while i > 0:
    if num[i] > num[i - 1]:
      break
    i -= 1
  # if i is 0 elements in decreasing order
  # no greater element possible
  if i == 0:
    return -1
  # find smallest digit on right of (i-1)th digit greater than num(i-1)
  for j in range(len(num) - 1, i - 1, -1):
    if num[i - 1] < num[j]:
      # swap found smallest digit
      num = list(num)
      num[i - 1], num[j] = num[j], num[i - 1]
      num = "".join(num)
      break
  # reverse digits after (i-1) because digits after in decreasing order
  # will get smallest element possible from these digits
  num = list(num)
  num[i:] = reversed(num[i:])
  num = "".join(num)

  return num


# keep this function call here
# print(PermutationStep(input()))

# Testing:
num1 = 11121 # 11211
num2 = 41352 # 41523
num3 = 123 # 132
num4 = 12452 # 12534

print(PermutationStep(num1))
print(PermutationStep(num2))
print(PermutationStep(num3))
print(PermutationStep(num4))