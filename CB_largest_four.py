"""
Have the function LargestFour(arr) take the array of integers stored in arr, and find the four largest elements and return their sum.
For example: if arr is [4, 5, -2, 3, 1, 2, 6, 6] then the four largest elements in this array are 6, 6, 4, and 5 and the total sum of these numbers is 21, so your program should return 21.
If there are less than four numbers in the array your program should return the sum of all the numbers in the array.

Examples:
Input: [1, 1, 1, -5]
Output: -2

Input: [0, 0, 2, 3, 7, 1]
Output: 13
"""

def LargestFour(arr):
  ordered = sorted(arr, reverse=True)
  four_largest = ordered[0:4]
  total_sum = sum(four_largest)
  return total_sum

# keep this function call here
# print(LargestFour(input()))

# Testing:
arr1 = [1, 1, 1, -5] # -2
arr2 = [0, 0, 2, 3, 7, 1] # 13
arr3 = [4, 5, -2, 3, 1, 2, 6, 6] # 21

print(LargestFour(arr1))
print(LargestFour(arr2))
print(LargestFour(arr3))