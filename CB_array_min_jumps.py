"""
Have the function ArrayMinJumps(arr) take the array of integers stored in arr, where each integer represents the maximum number of steps that can be made from that position, and determine the least amount of jumps that can be made to reach the end of the array.
For example: if arr is [1, 5, 4, 6, 9, 3, 0, 0, 1, 3] then your program should output the number 3 because you can reach the end of the array from the beginning via the following steps: 1 -> 5 -> 9 -> END or
1 -> 5 -> 6 -> END.
Both of these combinations produce a series of 3 steps.
And as you can see, you don't always have to take the maximum number of jumps at a specific position, you can take less jumps even though the number is higher.

If it is not possible to reach the end of the array, return -1.

Examples:
Input: [3, 4, 2, 1, 1, 100]
Output: 2

Input: [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2]
Output: 4
"""

def ArrayMinJumps(arr):
  n = len(arr)
  # return -1 if not possible to jump
  if arr[0] == 0:
    return -1
  # return 0 if array has one element
  if n == 1:
    return 0
  # store max reachble index
  max_reach = 0
  # store number of steps we can still take
  current_reach = 0
  # store jumps needed to reach current reachable index
  jump = 0
  for i in range(n):
    max_reach = max(max_reach, i + arr[i])
    # if we can reach last index by jumping from current position
    if max_reach >= n - 1:
      return jump + 1
    # increment jump
    if i == current_reach:
      # if max reach same as current index cannot jump further
      if i == max_reach:
        return -1
      # if max reaech > current index, increment jump
      # update current reachable index
      else:
        jump += 1
        current_reach = max_reach
  return -1

# keep this function call here
#print(ArrayMinJumps(input()))


# Testing:
arr1 = [3, 4, 2, 1, 1, 100] # 2
arr2 = [1, 3, 6, 8, 2, 7, 1, 2, 1, 2, 6, 1, 2, 1, 2] # 4
arr3 = [1, 5, 4, 6, 9, 3, 0, 0, 1, 3] # 3
arr4 = [4] # 0

print(ArrayMinJumps(arr1))
print(ArrayMinJumps(arr2))
print(ArrayMinJumps(arr3))
print(ArrayMinJumps(arr4))
