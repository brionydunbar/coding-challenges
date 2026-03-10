"""
Have the function DistinctList(arr) take the array of numbers stored in arr and determine the total number of duplicate entries.
For example if the input is [1, 2, 2, 2, 3] then your program should output 2 because there are two duplicates of one of the elements.

Examples:
Input: [0,-2,-2,5,5,5]
Output: 3

Input: [100,2,101,4]
Output: 0
"""

def DistinctList(arr):
  # find duplicates
  seen = set()
  duplicates = 0
  for num in arr:
    if num in seen:
      duplicates += 1
    else:
      seen.add(num)
  return duplicates

# keep this function call here
# print(DistinctList(input()))

# Testing:
arr1 = [0,-2,-2,5,5,5] # 3
arr2 = [100,2,101,4] # 0
arr3 = [1, 2, 2, 2, 3] # 2

print(DistinctList(arr1))
print(DistinctList(arr2))
print(DistinctList(arr3))