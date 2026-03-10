"""
Have the function OverlappingRectangles(strArr) read the strArr parameter being passed which will represent two rectangles on a Cartesian coordinate plane and will contain 8 coordinates with the first 4 making up rectangle 1 and the last 4 making up rectangle 2.
It will be in the following format: ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"]
Your program should determine the area of the space where the two rectangles overlap, and then output the number of times this overlapping region can fit into the first rectangle.
For the above example, the overlapping region makes up a rectangle of area 2, and the first rectangle (the first 4 coordinates) makes up a rectangle of area 4, so your program should output 2.
The coordinates will all be integers.
If there's no overlap between the two rectangles return 0.

Examples:
Input: ["(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"]
Output: 6

Input: ["(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)"]
Output: 3
"""

def OverlappingRectangles(strArr):
  # split strArr into coordinate pairs
  coords = strArr[0].replace("(", "").replace(")", "").split(",")
  points = [(int(coords[i]), int(coords[i + 1])) for i in range(0, len(coords), 2)]
  rect1 = points[:4] # now a list of tuples for first half of strArr
  rect2 = points[4:] # same but second half
  # extract into x/y min/max
  # rect1
  x1_min = min(p[0] for p in rect1) # find smallest out of x coods
  x1_max = max(p[0] for p in rect1) # find largest out of x coords
  y1_min = min(p[1] for p in rect1) # find smallest out of y coords
  y1_max = max(p[1] for p in rect1) # find largest out of y coords
  # rect2
  x2_min = min(p[0] for p in rect2)
  x2_max = max(p[0] for p in rect2)
  y2_min = min(p[1] for p in rect2)
  y2_max = max(p[1] for p in rect2)
  # find overlap
  x_overlap = max(0, min(x1_max, x2_max) - max(x1_min, x2_min)) # find x overlap
  y_overlap = max(0, min(y1_max, y2_max) - max(y1_min, y2_min)) # find y overlap
  overlap_area = x_overlap * y_overlap # area of overlap
  if overlap_area == 0:
    return 0
  # find area of rect1
  rect1_area = (x1_max - x1_min) * (y1_max - y1_min)
  # return how many times overlap will fit into rect1
  fit_number = rect1_area // overlap_area
  return fit_number

# keep this function call here
# print(OverlappingRectangles(input()))

# Testing:
arr1 = ["(0,0),(0,-2),(3,0),(3,-2),(2,-1),(3,-1),(2,3),(3,3)"] # 6
arr2 = ["(0,0),(5,0),(0,2),(5,2),(2,1),(5,1),(2,-1),(5,-1)"] # 3
arr3 = ["(0,0),(2,2),(2,0),(0,2),(1,0),(1,2),(6,0),(6,2)"] # 2

print(OverlappingRectangles(arr1))
print(OverlappingRectangles(arr2))
print(OverlappingRectangles(arr3))