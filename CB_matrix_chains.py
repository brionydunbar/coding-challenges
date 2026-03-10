"""
Have the function MatrixChains(arr) read the array of positive integers stored in arr where every pair will represent an NxM matrix.
For example: if arr is [1, 2, 3, 4] this means you have a 1x2, 2x3, and a 3x4 matrix.
So there are N-1 total matrices where N is the length of the array.
Your goal is to determine the least number of multiplications possible after multiplying all the matrices.
Matrix multiplication is associative so (A*B)*C is equal to A*(B*C).

For the above example, let us assume the following letters represent the different matrices: A = 1x2, B = 2x3, and C = 3x4.
Then we can multiply the matrices in the following orders: (AB)C or A(BC).
The first ordering requires (1*2*3) = 6 then we multiply this new 1x3 matrix by the 3x4 matrix and we get (1*3*4) = 12.
So in total, this ordering required 6 + 12 = 18 multiplications.
Your program should therefore return 18 because the second ordering produces more multiplications.
The input array will contain between 3 and 30 elements.

Examples:
Input: [2, 3, 4]
Output: 24

Input: [1, 4, 5, 6, 8]
Output: 98

"""

def MatrixChains(arr):
  n = len(arr) - 1  # number of matrices
  dp = [[0] * n for _ in range(n)]

  # chain length L = 2 to n
  for L in range(2, n+1):
    for i in range(n-L+1):
      j = i + L - 1
      dp[i][j] = float('inf')
      for k in range(i, j):
        cost = dp[i][k] + dp[k+1][j] + arr[i] * arr[k+1] * arr[j+1]
        dp[i][j] = min(dp[i][j], cost)

  return dp[0][n-1]

# keep this function call here
# print(MatrixChains(input()))

# Testing:
arr1 = [2, 3, 4] # 24
arr2 = [1, 4, 5, 6, 8] # 98
arr3 = [1, 2, 3, 4] # 18

print(MatrixChains(arr1))
print(MatrixChains(arr2))
print(MatrixChains(arr3))