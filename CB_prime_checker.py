"""
Have the function PrimeChecker(num) take num and return 1 if any arrangement of num comes out to be a prime number, otherwise return 0.
For example: if num is 910, the output should be 1 because 910 can be arranged into 109 or 019, both of which are primes.

Examples:
Input: 98
Output: 1

Input: 598
Output: 1
"""

import math
from itertools import permutations

def _is_prime(n): # helper function
  if n < 2:
    return False
  for i in range(2, int(math.isqrt(n)) + 1):
    if n % i == 0:
      return False
  return True

def PrimeChecker(num):

  digits = str(num)
  # try all permutations
  for r in range(1, len(digits) + 1):
    for perm in permutations(digits, r):
      candidate = int("".join(perm))
      if _is_prime(candidate):
        return 1
  return 0

# keep this function call here
# print(PrimeChecker(input()))

# Testing:
num1 = 98 # 1
num2 = 598 # 1
num3 = 910 # 1

print(PrimeChecker(num1))
print(PrimeChecker(num2))
print(PrimeChecker(num3))