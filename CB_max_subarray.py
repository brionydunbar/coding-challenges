"""
Have the function MaxSubarray(arr) take the array of numbers stored in arr and determine the largest sum that can be formed by any contiguous subarray in the array.
For example, if arr is [-2, 5, -1, 7, -3] then your program should return 11 because the sum is formed by the subarray [5, -1, 7].
Adding any element before or after this subarray would make the sum smaller.

Examples:
Input: [1, -2, 0, 3]
Output: 3

Input: [3, -1, -1, 4, 3, -1]
Output: 8
"""

def MaxSubarray(arr):
  # store result of max sum so far
  result = arr[0]
  # max sum of subarray ending at current position
  max_ending = arr[0]
  for i in range(1, len(arr)):
    # extend prev subarray or start new from current element
    max_ending = max(max_ending + arr[i], arr[i])
    # update result if new subarray sum is larger
    result = max(result, max_ending)
  return result

# keep this function call here
# print(MaxSubarray(input()))

# Testing:
arr1 = [1, -2, 0, 3] # 3
arr2 = [3, -1, -1, 4, 3, -1] # 8
arr3 = [-2, 5, -1, 7, -3] # 11

print(MaxSubarray(arr1))
print(MaxSubarray(arr2))
print(MaxSubarray(arr3))