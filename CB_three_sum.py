"""
Have the function ThreeSum(arr) take the array of integers stored in arr, and determine if any three distinct numbers (excluding the first element) in the array can sum up to the first element in the array.
For example: if arr is [8, 2, 1, 4, 10, 5, -1, -1] then there are actually three sets of triplets that sum to the number 8: [2, 1, 5], [4, 5, -1] and [10, -1, -1].
Your program should return the string true if 3 distinct elements sum to the first element, otherwise your program should return the string false.
The input array will always contain at least 4 elements.

Examples:
Input: [10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]
Output: true

Input: [12, 3, 1, -5, -4, 7]
Output: false
"""

def ThreeSum(arr):
  N = len(arr)
  # iterate over each element from first index
  for i in range(1, N):
    target = arr[0] - arr[i] # compute target value needed to sum with arr[i] to get arr[0]
    hash_set = set() # store elements for quick lookup
    # iterate over remaining elements after arr[i]
    for j in range(i + 1, N):
      if target - arr[j] in hash_set: # check if complement exists in set
        return "true" # found a triplet that sums to arr[0]
      hash_set.add(arr[j]) # add current element to hash set
  return "false" # no triplet found

# keep this function call here
# print(ThreeSum(input()))

# Testing:
arr1 = [10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2] # "true"
arr2 = [12, 3, 1, -5, -4, 7] # "false"
arr3 = [8, 2, 1, 4, 10, 5, -1, -1] # "true"

print(ThreeSum(arr1))
print(ThreeSum(arr2))
print(ThreeSum(arr3))