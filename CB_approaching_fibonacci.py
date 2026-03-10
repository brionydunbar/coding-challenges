"""
Have the function ApproachingFibonacci(arr) take the arr parameter being passed which will be an array of integers and determine the smallest positive integer (including zero) that can be added to the array to make the sum of all of the numbers in the array add up to the next closest Fibonacci number.
For example: if arr is [15, 1, 3], then your program should output 2 because if you add up 15 + 1 + 3 + 2 you get 21 which is the closest Fibonacci number.

Examples:
Input: [5,2,1]
Output: 0

Input: [1,20,2,5]
Output: 6
"""

def ApproachingFibonacci(arr):
  # find current sum of array
  current_sum = sum(arr)
  # edge case - sum is 0
  if current_sum == 0:
    return 0
  # generate fibs and find closest
  # fib_a is previous fib number F(n-1)
  # fib_b is current F(n)
  fib_a, fib_b = 0, 1
  while fib_b < current_sum: # find first that is greater than or equal to sum
    fib_a, fib_b = fib_b, fib_a + fib_b # fib_a becomes old fib_b, fib_b becomes fib_a + fib_b (next fib number)

  #if current_sum is fib, next fib is fib_b
  # otherwise fib_b is closest one greater than current_sum

  #calculate diff
  difference = fib_b - current_sum

  return difference

# keep this function call here
# print(ApproachingFibonacci(input()))

# Testing:
arr1 = [5,2,1] # 0
arr2 = [1,20,2,5] # 6
arr3 = [15, 1, 3] # 2

print(ApproachingFibonacci(arr1))
print(ApproachingFibonacci(arr2))
print(ApproachingFibonacci(arr3))


"""
RECURSIVE:

def ApproachingFibonacci(arr):
    current_sum = sum(arr)

    def next_fib(a, b):
        # Recursive helper that finds the smallest Fibonacci number >= current_sum.
        # a = F(n-1), b = F(n)
        if b >= current_sum:
            return b  # base case: found the Fibonacci >= current_sum
        return next_fib(b, a + b)  # recurse to the next pair

    fib_b = next_fib(0, 1)   # start recursion with F(0)=0, F(1)=1
    return fib_b - current_sum
    
"""