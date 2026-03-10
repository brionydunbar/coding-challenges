"""
Have the function MatrixPath(strArr) take the strArr parameter being passed which will be a 2D matrix of 0 and 1's of some arbitrary size, and determine if a path of 1's exists from the top-left of the matrix to the bottom-right of the matrix while moving only in the directions: up, down, left, and right.
If a path exists your program should return the string true, otherwise your program should return the number of locations in the matrix where if a single 0 is replaced with a 1, a path of 1's will be created successfully.
If a path does not exist and you cannot create a path by changing a single location in the matrix from a 0 to a 1, then your program should return the string not possible.
For example: if strArr is ["11100", "10011", "10101", "10011"] then this looks like the following matrix:

1 1 1 0 0
1 0 0 1 1
1 0 1 0 1
1 0 0 1 1

For the input above, a path of 1's from the top-left to the bottom-right does not exist.
But, we can change a 0 to a 1 in 2 places in the matrix, namely at locations: [0,3] or [1,2].
So for this input your program should return 2.
The top-left and bottom-right of the input matrix will always be 1's.

Examples:
Input: ["10000", "11011", "10101", "11001"]
Output: 1

Input: ["1000001", "1001111", "1010101"]
Output: not possible
"""

from collections import deque


def MatrixPath(strArr):
    # parse input into subarrays
    matrix = [[int(c) for c in row] for row in strArr]
    rows, columns = len(matrix), len(matrix[0])

    # create a BFS function
    def bfs(matrix):
        visited = [[False] * columns for val in range(rows)]
        queue = deque([(0, 0)])
        visited[0][0] = True
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while queue:
            row, column = queue.popleft()
            if row == rows - 1 and column == columns - 1:
                return True
            for d_row, d_column in directions:
                # calculate new coords
                new_row, new_column = row + d_row, column + d_column
                # check if newe cell inside grid
                in_bounds = 0 <= new_row < rows and 0 <= new_column < columns
                # check if new cell visited
                not_visited = not visited[new_row][new_column] if in_bounds else False
                # check if new cell has 1
                is_path = matrix[new_row][new_column] == 1 if in_bounds else False
                if in_bounds and not_visited and is_path:
                    visited[new_row][new_column] = True
                    queue.append((new_row, new_column))
        return False

    # check if path exists
    if bfs(matrix):
        return "true"

    # check for single 0 flips
    count = 0
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 0:
                matrix[row][column] = 1
                if bfs(matrix):
                    count += 1
                matrix[row][column] = 0  # flip back

    if count > 0:
        return count
    else:
        return "not possible"


# keep this function call here
# print(MatrixPath(input()))

# Testing:
arr1 = ["10000", "11011", "10101", "11001"]  # 1
arr2 = ["1000001", "1001111", "1010101"]  # "not possible"
arr3 = ["11100", "10011", "10101", "10011"]  # 2

print(MatrixPath(arr1))
print(MatrixPath(arr2))
print(MatrixPath(arr3))