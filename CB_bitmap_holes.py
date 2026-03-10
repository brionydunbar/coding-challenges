"""
Have the function BitmapHoles(strArr) take the array of strings stored in strArr, which will be a 2D matrix of 0 and 1's, and determine how many holes, or contiguous regions of 0's, exist in the matrix.
A contiguous region is one where there is a connected group of 0's going in one or more of four directions: up, down, left, or right.
For example: if strArr is ["10111", "10101", "11101", "11111"], then this looks like the following matrix:

1 0 1 1 1
1 0 1 0 1
1 1 1 0 1
1 1 1 1 1

For the input above, your program should return 2 because there are two separate contiguous regions of 0's, which create "holes" in the matrix.
You can assume the input will not be empty.

Examples:
Input: ["01111", "01101", "00011", "11110"]
Output: 3

Input: ["1011", "0010"]
Output: 2
"""


def BitmapHoles(strArr):
    rows = len(strArr)
    cols = len(strArr[0])

    # convert bitmap to 2D list of integers
    bitmap = [[int(c) for c in row] for row in strArr]

    # keep track of visited cells
    visited = [[False] * cols for _ in range(rows)]

    def dfs(r, c):
        # Mark all connected zeros starting from (r,c)
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if visited[r][c] or bitmap[r][c] != 0:
            return
        visited[r][c] = True
        # visit neighbors (up, down, left, right)
        dfs(r - 1, c)
        dfs(r + 1, c)
        dfs(r, c - 1)
        dfs(r, c + 1)

    hole_count = 0

    for i in range(rows):
        for j in range(cols):
            # start a new hole if cell is 0 and not visited
            if bitmap[i][j] == 0 and not visited[i][j]:
                hole_count += 1
                dfs(i, j)

    return hole_count


# keep this function call here
# print(BitmapHoles(input()))

# Testing:
arr1 = ["01111", "01101", "00011", "11110"]  # 3
arr2 = ["1011", "0010"]  # 2
arr3 = ["10111", "10101", "11101", "11111"]  # 2

print(BitmapHoles(arr1))
print(BitmapHoles(arr2))
print(BitmapHoles(arr3))