"""
Have the function ThreeFiveMultiples(num) return the sum of all the multiples of 3 and 5 that are below num.
For example: if num is 10, the multiples of 3 and 5 that are below 10 are 3, 5, 6, and 9, and adding them up you get 23, so your program should return 23.
The integer being passed will be between 1 and 100.

Examples:

Input: 6
Output: 8

Input: 1
Output: 0
"""

def ThreeFiveMultiples(num):
    total = 0
    for n in range(1, num):
      if n % 3 == 0 or n % 5 == 0:
        total += n
    return total


# keep this function call here
# print(ThreeFiveMultiples(input()))

# Testing:
num1 = 6 # 8
num2 = 1 # 0
num3 = 10 # 23

print(ThreeFiveMultiples(num1))
print(ThreeFiveMultiples(num2))
print(ThreeFiveMultiples(num3))