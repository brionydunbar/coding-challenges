"""
Have the function WaveSorting(arr) take the array of positive integers stored in arr and return the string true if the numbers can be arranged in a wave pattern: a1 > a2 < a3 > a4 < a5 > ..., otherwise return the string false.
For example, if arr is: [0, 1, 2, 4, 1, 4], then a possible wave ordering of the numbers is: [2, 0, 4, 1, 4, 1].
So for this input your program should return the string true.
The input array will always contain at least 2 elements.
More examples are given below as sample test cases.

Examples
Input: [0, 1, 2, 4, 1, 1, 1]
Output: false

Input: [0, 4, 22, 4, 14, 4, 2]
Output: true
"""

def WaveSorting(arr):
  N = len(arr)
  arr.sort() # sort ascending
  left = 0 # first half pointer
  right = N // 2 # second half pointer
  # compare corresponding elements from first half with second
  while left < (N // 2) and right < N:
    if arr[right] > arr[left]: # check if element in second half greater
      left += 1 # move to next element in first half
      right += 1 # as above for second half
    else:
      return "false" # if condition fails, wave sorting not possible
  return "true"

# keep this function call here
# print(WaveSorting(input()))

# Testing:
arr1 = [0, 1, 2, 4, 1, 1, 1] # "false"
arr2 = [0, 4, 22, 4, 14, 4, 2] # "true"
arr3 = [0, 1, 2, 4, 1, 4] # "true"

print(WaveSorting(arr1))
print(WaveSorting(arr2))
print(WaveSorting(arr3))