"""
Have the function ThreePoints(strArr) read the array of strings stored in strArr which will always contain 3 elements and be in the form: ["(x1,y1)", "(x2,y2)", "(x3,y3)"].
Your goal is to first create a line formed by the first two points (that starts from the first point and moves in the direction of the second point and that stretches in both directions through the two points), and then determine what side of the line point 3 is on.
The result will either be right, left, or neither.
For example: if strArr is ["(1,1)", "(3,3)", "(2,0)"] then your program should return the string right because the third point lies to the right of the line formed by the first two points.

Examples:
Input: ["(0,-3)", "(-2,0)", "(0,0)"]
Output: right

Input: ["(0,0)", "(0,5)", "(0,2)"]
Output: neither
"""

def ThreePoints(strArr):
  # parse input strings into integers
  points = [tuple(map(int, p.strip("()").split(","))) for p in strArr]
  (x1, y1), (x2, y2), (x3, y3) = points

  # cross product
  cross = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

  if cross > 0:
    return "left"
  elif cross < 0:
    return "right"
  else:
    return "neither"

# keep this function call here
# print(ThreePoints(input()))

# Testing:
arr1 = ["(0,-3)", "(-2,0)", "(0,0)"] # "right"
arr2 = ["(0,0)", "(0,5)", "(0,2)"] # "neither"
arr3 = ["(1,1)", "(3,3)", "(2,0)"] # "right"

print(ThreePoints(arr1))
print(ThreePoints(arr2))
print(ThreePoints(arr3))