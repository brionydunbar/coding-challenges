"""
Have the function FibonacciChecker(num) return the string yes if the number given is part of the Fibonacci sequence.
This sequence is defined by: Fn = Fn-1 + Fn-2, which means to find Fn you add the previous two numbers up.
The first two numbers are 0 and 1, then comes 1, 2, 3, 5 etc.
If num is not in the Fibonacci sequence, return the string no.

Examples:
Input: 34
Output: yes

Input: 54
Output: no
"""

def FibonacciChecker(num):
  if num == 0 or num == 1:
    return "yes"
  a, b = 0, 1
  while True:
    c = a + b
    a = b
    b = c
    if c == num:
      return "yes"
    elif c >= num:
      return "no"

# keep this function call here
# print(FibonacciChecker(input()))

# Testing:
num1 = 34 # "yes"
num2 = 54 # "no"

print(FibonacciChecker(num1))
print(FibonacciChecker(num2))