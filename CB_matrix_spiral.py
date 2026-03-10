"""
Have the function MatrixSpiral(strArr) read the array of strings stored in strArr which will represent a 2D N matrix, and your program should return the elements after printing them in a clockwise, spiral order.
You should return the newly formed list of elements as a string with the numbers separated by commas.
For example: if strArr is "[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]" then this looks like the following 2D matrix:

1 2 3
4 5 6
7 8 9

So your program should return the elements of this matrix in a clockwise, spiral order which is: 1,2,3,6,9,8,7,4,5

Examples:
Input: ["[1, 2]", "[10, 14]"]
Output: 1,2,14,10

Input: ["[4, 5, 6, 5]", "[1, 1, 2, 2]", "[5, 4, 2, 9]"]
Output: 4,5,6,5,2,9,2,4,5,1,1,2
"""

def MatrixSpiral(strArr):
  # unpack the strings
  unpacked = []
  for row in strArr:
    row = row.strip("[]").split(",")
    unpacked.append([int(x) for x in row])

  m, n = len(unpacked), len(unpacked[0])
  result = []
  # initialise boundaries
  top, bottom, left, right = 0, m - 1, 0, n - 1
  # iterate until all elements printed
  while top <= bottom and left <= right:
    # print top row left to right
    for i in range(left, right + 1):
      result.append(unpacked[top][i])
    top += 1
    # print right column top to bottom
    for i in range(top, bottom + 1):
      result.append(unpacked[i][right])
    right -= 1
    # print bottom row right to left
    if top <= bottom:
      for i in range(right, left - 1, -1):
        result.append(unpacked[bottom][i])
      bottom -= 1
    # print left column bottom to top
    if left <= right:
      for i in range(bottom, top - 1, -1):
        result.append(unpacked[i][left])
      left += 1
  return ",".join(map(str, result))

# keep this function call here
# print(MatrixSpiral(input()))

# Testing:
arr1 = ["[1, 2]", "[10, 14]"] # "1,2,14,10"
arr2 = ["[4, 5, 6, 5]", "[1, 1, 2, 2]", "[5, 4, 2, 9]"] # "4,5,6,5,2,9,2,4,5,1,1,2"
arr3 = ["[1, 2, 3]", "[4, 5, 6]", "[7, 8, 9]"] # "1,2,3,6,9,8,7,4,5"

print(MatrixSpiral(arr1))
print(MatrixSpiral(arr2))
print(MatrixSpiral(arr3))