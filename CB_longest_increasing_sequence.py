"""
Have the function LongestIncreasingSequence(arr) take the array of positive integers stored in arr and return the length of the longest increasing subsequence (LIS).
A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order.
The sequence does not need to be contiguous or unique, and there can be several different subsequences.
For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6].
For this input, your program should return 3 because that is the length of the longest increasing subsequence.

Examples:
Input: [9, 9, 4, 2]
Output: 1

Input: [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
Output: 7

"""

def LongestIncreasingSequence(arr):
  # binary search approach
  n = len(arr)
  result = []
  # add first element of array
  result.append(arr[0])
  # loop through array to check subsequence
  for i in range(1, n):
    if arr[i] > result[-1]: # increasing
      result.append(arr[i]) # append current number to results
    else: # now binary search to find smallest element greater or equal to current number
      low = 0
      high = len(result) - 1
      while low < high:
        mid = low + (high - low) // 2
        if result[mid] < arr[i]:
          low = mid + 1
        else:
          high = mid
      result[low] = arr[i] # update element at found position with current number
  return len(result)


# keep this function call here
# print(LongestIncreasingSequence(input()))

# Testing:
arr1 = [9, 9, 4, 2] # 1
arr2 = [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90] # 7
arr3 = [4, 3, 5, 1, 6] # 3

print(LongestIncreasingSequence(arr1))
print(LongestIncreasingSequence(arr2))
print(LongestIncreasingSequence(arr3))