"""
Have the function PrimeMover(num) return the numth prime number.
The range will be from 1 to 10^4.
For example: if num is 16 the output should be 53 as 53 is the 16th prime number.
Examples
Input: 9
Output: 23
Input: 100
Output: 541
"""

def PrimeMover(num):
  primes = []
  candidate = 2

  while len(primes) < num:
    # check if prime
    is_prime = True
    for p in primes:
      if p * p > candidate:
        break
      if candidate % p == 0:
        is_prime = False
        break
    if is_prime:
      primes.append(candidate)
    candidate += 1

  return primes[-1]

# keep this function call here
# print(PrimeMover(input()))

# Testing:
num1 = 9 # 23
num2 = 100 # 541

print(PrimeMover(num1))
print(PrimeMover(num2))