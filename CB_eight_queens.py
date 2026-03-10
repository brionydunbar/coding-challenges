"""
Have the function EightQueens(strArr) read strArr which will be an array consisting of the locations of eight Queens on a standard 8x8 chess board with no other pieces on the board.
The structure of strArr will be the following: ["(x,y)", "(x,y)", ...] where (x,y) represents the position of the current queen on the chessboard (x and y will both range from 1 to 8 where 1,1 is the bottom-left of the chessboard and 8,8 is the top-right).
Your program should determine if all of the queens are placed in such a way where none of them are attacking each other.
If this is true for the given input, return the string true otherwise return the first queen in the list that is attacking another piece in the same format it was provided.

For example: if strArr is ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] then your program should return the string true.
The corresponding chessboard of queens for this input is below (taken from Wikipedia).

Examples:
Input: ["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"]
Output: (2,1)

Input: ["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"]
Output: (5,3)
"""

def EightQueens(strArr):
  queens = []
  # Parse the input strings into (x, y) coordinate pairs
  for queen_str in strArr:
    # Remove parentheses and split by comma
    coords = queen_str.strip("()").split(",")
    x = int(coords[0])
    y = int(coords[1])
    queens.append({"x": x, "y": y, "original": queen_str})

  # Iterate through all pairs of queens to check for attacks
  for i in range(len(queens)):
    for j in range(i + 1, len(queens)):
      queen1 = queens[i]
      queen2 = queens[j]

      # Check for attack in the same column
      if queen1["x"] == queen2["x"]:
        return queen1["original"]

      # Check for attack in the same row
      if queen1["y"] == queen2["y"]:
        return queen1["original"]

      # Check for attack on the same diagonal
      if abs(queen1["x"] - queen2["x"]) == abs(queen1["y"] - queen2["y"]):
        return queen1["original"]

  # If no attacks were found after checking all pairs
  return "true"

# keep this function call here
# print(EightQueens(input()))

# Testing:
arr1 = ["(2,1)", "(4,3)", "(6,3)", "(8,4)", "(3,4)", "(1,6)", "(7,7)", "(5,8)"] # (2,1)
arr2 = ["(2,1)", "(5,3)", "(6,3)", "(8,4)", "(3,4)", "(1,8)", "(7,7)", "(5,8)"] # (5, 3)
arr3 = ["(2,1)", "(4,2)", "(6,3)", "(8,4)", "(3,5)", "(1,6)", "(7,7)", "(5,8)"] # "true"

print(EightQueens(arr1))
print(EightQueens(arr2))
print(EightQueens(arr3))