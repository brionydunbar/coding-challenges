"""
Have the function LogitRegression(arr) read the input array of 4 numbers x, y, a, b, separated by space, and return an output of two numbers for updated a and b (assume the learning rate is 1).
Save up to 3 digits after the decimal points for a and b.
The output should be a string in the format: a, b

Logistic regression is a simple approach to do classification, and the same formula is also commonly used as the output layer in neural networks.
We assume both the input and output variables are scalars, and the logistic regression can be written as:

y = 1.0 / (1.0 + exp(-ax - b))

After observing a data example (x, y), the parameter a and b can be updated using gradient descent with a learning rate.

Examples:
Input: [1, 1, 1, 1]
Output: 0.881, 0.881

Input: [2.2, 0.0, 5.1, 5.7]
Output: 7.3, 6.7
"""

import math

def LogitRegression(arr):

  x=arr[0]
  y=arr[1]
  a=arr[2]
  b=arr[3]

  y_calc = 1/(1+math.exp(-a*x-b))

  return str(round(a - ((y-y_calc)*x), 3)) + ", " + str(round(b - (y-y_calc), 3))

# keep this function call here
print(LogitRegression(input()))

"""
# Testing:
arr1 = [1, 1, 1, 1] # "0.881, 0.881"
arr2 = [2.2, 0.0, 5.1, 5.7] # "7.3, 6.7"

print(LogitRegression(arr1))
print(LogitRegression(arr2))

"""