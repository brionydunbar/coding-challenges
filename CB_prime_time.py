"""
Have the function PrimeTime(num) take the num parameter being passed and return the string true if the parameter is a prime number, otherwise return the string false. The range will be between 1 and 2^16.

"""

import math


def PrimeTime(num):
    # check if num is 1 or 0 (not prime)
    if num <= 1:
        return "false"
    # check if num is 2 or 3 (is prime)
    if num == 2 or num == 3:
        return "true"
    # check if num is divisible by 2 or 3 (not prime)
    if num % 2 == 0 or num % 3 == 0:
        return "false"
    # check from 5 to sqrt of num
    # iterate i by (i+6)
    i = 5
    while i <= math.sqrt(num):
        if num % i == 0 or num % (i + 2) == 0:
            return "false"
        i += 6

    return "true"


# keep this function call here
# print(PrimeTime(input()))


# Testing:
num1 = 19 # expect "true"
num2 = 110 # except "false"

print(PrimeTime(num1))
print(PrimeTime(num2))