"""
Have the function ArithGeoII(arr) take the array of numbers stored in arr and return the string "Arithmetic" if the sequence follows an arithmetic pattern
or return "Geometric" if it follows a geometric pattern.
If the sequence doesn't follow either pattern return -1.
An arithmetic sequence is one where the difference between each of the numbers is consistent,
where as in a geometric sequence, each term after the first is multiplied by some constant or common ratio.
Arithmetic example: [2, 4, 6, 8] and
Geometric example: [2, 6, 18, 54].
Negative numbers may be entered as parameters, 0 will not be entered, and no array will contain all the same elements.

Examples:
Input: [5,10,15]
Output: Arithmetic
Input: [2,4,16,24]
Output: -1
"""

import operator

def ArithGeoII(arr):
  if len(arr) < 2:
    return -1 # not enough numbers for pattern

  diff = list(map(operator.sub, arr[1:], arr[:-1]))
  arith = False
  result = all(num == diff[0] for num in diff)
  if result == True:
    return "Arithmetic"
  else:
    ratio = arr[1]/float(arr[0])
    for i in range(1, len(arr)):
      if arr[i]/float(arr[i-1]) != ratio:
        return -1
    return "Geometric"

# keep this function call here
# print(ArithGeoII(input()))

# Testing:
arr1 = [5, 10, 15] # "Arithmetic"
arr2 = [2, 4, 16, 24] # -1
arr3 = [2, 6, 18, 54] # "Geometric"

print(ArithGeoII(arr1))
print(ArithGeoII(arr2))
print(ArithGeoII(arr3))