"""
Have the function LongestMatrixPath(strArr) take the array of strings stored in strArr, which will be an NxM matrix of positive single-digit integers, and find the longest increasing path composed of distinct integers.
When moving through the matrix, you can only go up, down, left, and right.
For example: if strArr is ["345", "326", "221"], then this looks like the following matrix:

3 4 5
3 2 6
2 2 1

For the input above, the longest increasing path goes from: 3 -> 4 -> 5 -> 6.
Your program should return the number of connections in the longest path, so therefore for this input your program should return 3.
There may not necessarily always be a longest path within the matrix.

Examples:
Input: ["12256", "56219", "43215"]
Output: 5

Input: ["67", "21", "45"]
Output: 3
"""

def LongestMatrixPath(strArr):
  # parse the input
  matrix = [[int(c) for c in row] for row in strArr]

  # define DFS function
  def dfs(i, j):
    if not dp[i][j]: # if cell hasn't been computed yet, calculate longest path
        value = matrix[i][j] # current cell value
        # memoise path
        dp[i][j] = 1 + max(
            dfs(i - 1, j) if i and value > matrix[i - 1][j] else 0,
            dfs(i + 1, j) if i < M - 1 and value > matrix[i + 1][j] else 0,
            dfs(i, j - 1) if j and value > matrix[i][j - 1] else 0,
            dfs(i, j + 1) if j < N - 1 and value > matrix[i][j + 1] else 0)
    return dp[i][j] # return computed path

  # memoisation table
  M, N = len(matrix), len(matrix[0])
  dp = [[0] * N for i in range(M)]
  return max(dfs(x, y) for x in range(M) for y in range(N)) - 1

# keep this function call here
#print(LongestMatrixPath(input()))

# Testing:
arr1 = ["12256", "56219", "43215"] # 5
arr2 = ["67", "21", "45"] # 3
arr3 = ["345", "326", "221"] # 3

print(LongestMatrixPath(arr1))
print(LongestMatrixPath(arr2))
print(LongestMatrixPath(arr3))