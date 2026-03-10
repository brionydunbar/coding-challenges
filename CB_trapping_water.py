"""
Have the function TrappingWater(arr) take the array of non-negative integers stored in arr, and determine the largest amount of water that can be trapped.
The numbers in the array represent the height of a building (where the width of each building is 1) and if you imagine it raining, water will be trapped between the two tallest buildings.
For example: if arr is [3, 0, 0, 2, 0, 4] then this array of building heights looks like the following picture if we draw it out:
               __
 __           |  |
|  |     __   |  |
|  |    |  |  |  |
|  |____|  |__|  |
Now if you imagine it rains and water gets trapped in this picture, then it'll look like the following (the x's represent water):
               __
 __           |  |
|  |xxxxxxxxxx|  |
|  |xxxx|  |xx|  |
|  |xxxx|  |xx|  |

This is the most water that can be trapped in this picture, and if you calculate the area you get 10, so your program should return 10.

Examples:
Input: [1, 2, 1, 2]
Output: 1

Input: [0, 2, 4, 0, 2, 1, 2, 6]
Output: 11

"""

def TrappingWater(arr):
  left = 1
  right = len(arr) - 2
  l_max = arr[left - 1]
  r_max = arr[right + 1]

  result = 0
  while left <= right:
    if r_max <= l_max: # decide amount for right
      result += max(0, r_max - arr[right]) # add water for right
      r_max = max(r_max, arr[right]) # update right max
      right -= 1 # update right pointer
    else: # for left
      result += max(0, l_max - arr[left])
      l_max = max(l_max, arr[left])
      left += 1
  return result


# keep this function call here
# print(TrappingWater(input()))

# Testing:
arr1 = [1, 2, 1, 2] # 1
arr2 = [0, 2, 4, 0, 2, 1, 2, 6] # 11
arr3 = [3, 0, 0, 2, 0, 4] # 10

print(TrappingWater(arr1))
print(TrappingWater(arr2))
print(TrappingWater(arr3))