"""
Have the function TwoSum(arr) take the array of integers stored in arr, and determine if any two numbers (excluding the first element) in the array can sum up to the first element in the array.
For example: if arr is [7, 3, 5, 2, -4, 8, 11], then there are actually two pairs that sum to the number 7: [5, 2] and [-4, 11].
Your program should return all pairs, with the numbers separated by a comma, in the order the first number appears in the array.
Pairs should be separated by a space.
So for the example above, your program would return: 5,2 -4,11

If there are no two numbers that sum to the first element in the array, return -1

Examples:
Input: [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7]
Output: 6,11 10,7 15,2

Input: [7, 6, 4, 1, 7, -2, 3, 12]
Output: 6,1 4,3
"""

def TwoSum(arr):
  target = arr.pop(0)
  n = len(arr)
  pairs = []
  for i in range(n):
    # for each element arr[i] check every other element arr[j] that comes after
    for j in range(i + 1, n):
      # check if sum of current pair equals target
      if arr[i] + arr[j] == target:
        pairs.append(f"{arr[i]},{arr[j]}")
  return " ".join(pairs) if pairs else -1


# keep this function call here
# print(TwoSum(input()))

# Testing:
arr1 = [17, 4, 5, 6, 10, 11, 4, -3, -5, 3, 15, 2, 7] # "6,11 10,7 15,2"
arr2 = [7, 6, 4, 1, 7, -2, 3, 12] # "6,1 4,3"
arr3 = [7, 3, 5, 2, -4, 8, 11] # "5,2 -4,11"

print(TwoSum(arr1))
print(TwoSum(arr2))
print(TwoSum(arr3))