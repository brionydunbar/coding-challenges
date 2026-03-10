"""
Have the function MeanMode(arr) take the array of numbers stored in arr and return 1 if the mode equals the mean, 0 if they don't equal each other (ie. [5, 3, 3, 3, 1] should return 1 because the mode (3) equals the mean (3)).
The array will not be empty, will only contain positive integers, and will not contain more than one mode.

Examples:
Input: [1, 2, 3]
Output: 0

Input: [4, 4, 4, 6, 2]
Output: 1
"""

import statistics

def MeanMode(arr):
  mode = statistics.mode(arr)
  mean = statistics.mean(arr)

  if mode == mean:
    return 1
  else:
    return 0

# keep this function call here
# print(MeanMode(input()))

# Testing:

arr1 = [1, 2, 3] # 0
arr2 = [4, 4, 4, 6, 2] # 1
arr3 = [5, 3, 3, 3, 1] # 1

print(MeanMode(arr1))
print(MeanMode(arr2))
print(MeanMode(arr3))