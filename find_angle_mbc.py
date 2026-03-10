"""
ABC is a right triangle, 90degrees at B.
Therefore, ABC = 90 degrees.

Point M is the midpoint of hypotenuse AC.

You are given the lengths AB and BC.
Your task is to find MBC in degrees.

Input Format
The first line contains the length of side AB.
The second line contains the length of side BC

Output format
Angle MBC in degrees
"""

import math

def find_angle_mbc(AB, BC):
    m = math.sqrt((AB**2)+(BC**2)) # m = square root(AB^2 + BC^2) - length of hypotenuse AC
    theta = math.acos(BC/m) # use inverse cosine function (acos) - BC adjacent side, m hypotenuse - finds angle at point where BC meets hypotenuse
    return str(round(math.degrees(theta)))+chr(176) # convert radians to degrees, round and add degrees symbol

print(find_angle_mbc(10, 10))
print(find_angle_mbc(5, 10))
print(find_angle_mbc(15, 15))