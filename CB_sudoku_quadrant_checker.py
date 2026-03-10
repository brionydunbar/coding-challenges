"""
Have the function SudokuQuadrantChecker(strArr) read the strArr parameter being passed which will represent a 9x9 Sudoku board of integers ranging from 1 to 9.
The rules of Sudoku are to place each of the 9 integers integer in every row and column and not have any integers repeat in the respective row, column, or 3x3 sub-grid.
The input strArr will represent a Sudoku board and it will be structured in the following format:
["(N,N,N,N,N,x,x,x,x)","(...)","(...)",...)] where N stands for an integer between 1 and 9 and x will stand for an empty cell.
Your program will determine if the board is legal; the board also does not necessarily have to be finished.
If the board is legal, your program should return the string legal but if it isn't legal, it should return the 3x3 quadrants (separated by commas) where the errors exist.
The 3x3 quadrants are numbered from 1 to 9 starting from top-left going to bottom-right.

For example, if strArr is: ["(1,2,3,4,5,6,7,8,1)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(1,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)"] then your program should return 1,3,4 since the errors are in quadrants 1, 3 and 4 because of the repeating integer 1.

Another example, if strArr is: ["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,1,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,9)"] then your program should return 3,4,5,9.

Examples:
Input: ["(1,2,3,4,5,6,7,8,1)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(1,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)"]
Output: 1,3,4
"""

# RECURSIVE SOLUTION
def SudokuQuadrantChecker(strArr):
  # Convert strArr to a 2D board
  board = [[int(x) if x != 'x' else 0 for x in row.strip("()").split(",")] for row in strArr]
  error_quadrants = set() # store quadrants with duplicates

  def check_cell(row, col):
    if row == 9: # base case - finished all rows
      return
    if col == 9: # end of row = move to first column of next row
      check_cell(row + 1, 0)  # next row
      return

    num = board[row][col] # current cell value
    if num != 0:
      # Check row for duplicates
      for c in range(9):
        if c != col and board[row][c] == num:
          q = (row // 3) * 3 + (col // 3) + 1 # compute quadrant number
          error_quadrants.add(q)
      # Check column for duplicates
      for r in range(9):
        if r != row and board[r][col] == num:
          q = (row // 3) * 3 + (col // 3) + 1
          error_quadrants.add(q)
      # Check 3x3 sub-grid for duplicates
      startRow, startCol = 3 * (row // 3), 3 * (col // 3)
      for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if (r != row or c != col) and board[r][c] == num:
                q = (row // 3) * 3 + (col // 3) + 1
                error_quadrants.add(q)

    # recurse to the next column in same row
    check_cell(row, col + 1)  # next column

  # start recursion from top left cell
  check_cell(0, 0)

  return "legal" if not error_quadrants else ",".join(map(str, sorted(error_quadrants)))

# keep this function call here
# print(SudokuQuadrantChecker(input()))

# Testing:
arr1 = ["(1,2,3,4,5,6,7,8,1)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(1,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)"] # "1,3,4"
arr2 = ["(1,2,3,4,5,6,7,8,9)","(x,x,x,x,x,x,x,x,x)","(6,x,5,x,3,x,x,4,x)","(2,x,1,1,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,x)","(x,x,x,x,x,x,x,x,9)"] # "3,4,5,9"

print(SudokuQuadrantChecker(arr1))
print(SudokuQuadrantChecker(arr2))

"""
WITHOUT RECURSION
def SudokuQuadrantChecker(strArr):
  # convert strArr into 2D list
  board = []
  for row in strArr:
    row = row.strip("()").split(",")
    board.append([int(x) if x != "x" else 0 for x in row])

  error_quadrants = set()

  # check rows
  for i in range(9):
    seen = {}
    for j in range(9):
      num = board[i][j]
      if num != 0:
        if num in seen:
          # add all quarants this row number touches
          q_row = i // 3
          q_col1 = seen[num] // 3
          q_col2 = j // 3
          error_quadrants.add(q_row * 3 + q_col1 + 1)
          error_quadrants.add(q_row * 3 + q_col2 + 1)
        else:
          seen[num] = j

  # check columns
  for j in range(9):
    seen = {}
    for i in range(9):
      num = board[i][j]
      if num != 0:
        if num in seen:
          q_col = j // 3
          q_row1 = seen[num] // 3
          q_row2 = i // 3
          error_quadrants.add(q_row1 * 3 + q_col + 1)
          error_quadrants.add(q_row2 * 3 + q_col + 1)
        else:
          seen[num] = i

  # check 3x3 subgrids
  for i in range(0, 9, 3):
    for j in range(0, 9, 3):
      seen = {}
      for r in range(3):
          for c in range(3):
            num = board[i+r][j+c]
            if num != 0:
              if num in seen:
                error_quadrants.add((i//3)*3 + j//3 + 1)
              else:
                seen[num] = True

  if not error_quadrants:
    return "legal"
  else:
    return ",".join(str(x) for x in sorted(error_quadrants))
    """