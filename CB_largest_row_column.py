"""
Have the function LargestRowColumn(strArr) read the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with positive integers.
Your goal is to determine the largest number that can be found by adding up three digits in the matrix that are within the same path, where being on the same path means starting from one of the elements and then moving either up, down, left, or right onto the next element without reusing elements.
One caveat though, and that is when you calculate the sum of three digits, you should split the sum into two digits and treat the new digits as a row/column position in the matrix.
So your goal is actually to find the sum of three digits that sums to the largest position in the matrix without going out of the bounds.
For example: if strArr is ["345", "326", "221"] then this looks like the following matrix:

3 4 5
3 2 6
2 2 1

The solution to this problem is to sum the bolded elements, 4 + 2 + 6, which equals 12.
Then you take the solution, 12, and split it into two digits: 1 and 2 which represents row 1, column 2 in the matrix.
This is the largest position you can get in the matrix by adding up 3 digits so your program should return 12.
If you for example added up 4 + 5 + 6 in the matrix you would get 15 which is larger than 12, but row 1, column 5 is out of bounds.
It's also not possible with the current matrix to sum to any of the following numbers: 20, 21, 22.
If you find a sum that is only a single digit, you can treat that as row 0, column N where N is your sum.

Examples:
Input: ["234", "999", "999"]
Output: 22

Input: ["11111", "22222"]
Output: 4
"""


def LargestRowColumn(strArr):
    # parse input into matrix
    matrix = [[int(ch) for ch in row] for row in strArr]
    rows, columns = len(matrix), len(matrix[0])
    # set directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_sum = -1

    # define DFS function
    def dfs(r, c, path, total):
        nonlocal max_sum
        # if path length = 3, interpret sum as coors
        if len(path) == 3:
            # Split the sum into digits to represent row/col
            s = total
            if s < 10:
                r_pos, c_pos = 0, s
            else:
                r_pos, c_pos = divmod(s, 10)
            # if valid position, update maximum sum
            if 0 <= r_pos < rows and 0 <= c_pos < columns:
                max_sum = max(max_sum, s)
            return

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < columns and (nr, nc) not in path:
                dfs(nr, nc, path + [(nr, nc)], total + matrix[nr][nc])

    # start DFS from every cell
    for r in range(rows):
        for c in range(columns):
            dfs(r, c, [(r, c)], matrix[r][c])

    return max_sum


# keep this function call here
# print(LargestRowColumn(input()))

# Testing:
arr1 = ["234", "999", "999"]  # 22
arr2 = ["11111", "22222"]  # 4
arr3 = ["345", "326", "221"]  # 12

print(LargestRowColumn(arr1))
print(LargestRowColumn(arr2))
print(LargestRowColumn(arr3))