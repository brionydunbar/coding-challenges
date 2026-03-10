"""
Have the function Primes(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false.
The range will be between 1 and 2^16.

Examples:
Input: 4
Output: false

Input: 1709
Output: true
"""

import math

def Primes(num):
  if num <= 1:
    return "false"
  else:
    is_prime = True
    for i in range(2, int(math.sqrt(num)) + 1):
      if num % i == 0:
        is_prime = False
        break
  if is_prime:
    return "true"
  else:
    return "false"

# keep this function call here
# print(Primes(input()))

# Testing:
num1 = 4 # "false"
num2 = 1709 # "true"

print(Primes(num1))
print(Primes(num2))

