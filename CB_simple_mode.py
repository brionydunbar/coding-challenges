"""
Have the function SimpleMode(arr) take the array of numbers stored in arr and return the number that appears most frequently (the mode).
For example: if arr contains [10, 4, 5, 2, 4] the output should be 4.
If there is more than one mode return the one that appeared in the array first (ie. [5, 10, 10, 6, 5] should return 5 because it appeared first).
If there is no mode return -1.
The array will not be empty.

Examples:
Input: [5,5,2,2,1]
Output: 5
Input: [3,4,1,6,10]
Output: -1
"""

from collections import Counter

def SimpleMode(arr):
  counts = Counter(arr)
  # find highest freq number
  num, freq = counts.most_common(1)[0]
  # if highest is 1, no mode
  if freq == 1:
    return -1
  return num

# keep this function call here
# print(SimpleMode(input()))

# Testing:
arr1 = [5, 5, 2, 2, 1] # 5
arr2 = [3, 4, 1, 6, 10] # -1
arr3 = [5, 10, 10, 6, 5] # 5

print(SimpleMode(arr1))
print(SimpleMode(arr2))
print(SimpleMode(arr3))

