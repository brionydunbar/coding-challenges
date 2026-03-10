"""
Have the function BoggleSolver(strArr) read the array of strings stored in strArr, which will contain 2 elements: the first element will represent a 4x4 matrix of letters, and the second element will be a long string of comma-separated words each at least 3 letters long, in alphabetical order, that represents a dictionary of some arbitrary length.
For example: strArr can be: ["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"].
Your goal is to determine if all the comma separated words as the second parameter exist in the 4x4 matrix of letters.
For this example, the matrix looks like the following:

r b f g
u k o p
f g u b
m n r y

The rules to make a word are as follows:

1. A word can be constructed from sequentially adjacent spots in the matrix, where adjacent means moving horizontally, vertically, or diagonally in any direction.
2. A word cannot use the same location twice to construct itself.

The rules are similar to the game of Boggle.
So for the example above, all the words exist in that matrix so your program should return the string true.
If all the words cannot be found, then return a comma separated string of the words that cannot be found, in the order they appear in the dictionary.

Examples:
Input: ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]
Output: true

Input: ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]
Output: rumk,yes
"""


def BoggleSolver(strArr):
    # use dfs for each word in dictionary
    # parse input into 4x4 grid and word list
    grid = [list(row.replace(" ", "")) for row in strArr[0].split(",")]
    words = strArr[1].split(",")

    rows, columns = 4, 4
    # define 8 boggle moves
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # implement dfs search - recursive function
    def dfs(row, column, word, visited):  # current cell coords, remaining letters, set of coords
        if not word:
            return True  # base case - all letters matched
        # check if currrent cell outside grif
        out_of_bounds = row < 0 or row >= rows or column < 0 or column >= columns
        # check if current cell already used in this search
        already_visited = (row, column) in visited
        if out_of_bounds or already_visited:
            return False
        # check if letter in cell matches expected letter in word
        letter_mismatch = grid[row][column] != word[0]
        if out_of_bounds or already_visited or letter_mismatch:
            return False
        visited.add((row, column))  # mark cell as used
        for d_row, d_column in directions:
            if dfs(row + d_row, column + d_column, word[1:], visited):
                return True
        visited.remove((row, column))  # backtrack
        return False

    # collect not found words
    missing_words = []
    for word in words:
        found = False
        for row in range(rows):
            for column in range(columns):
                if dfs(row, column, word, set()):
                    found = True
                    break
            if found:
                break
        if not found:
            missing_words.append(word)

    # return result
    if not missing_words:
        return "true"
    else:
        return ",".join(missing_words)


# keep this function call here
# print(BoggleSolver(input()))

# Testing:
arr1 = ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,tall,true,trum"]  # "true"
arr2 = ["aaey, rrum, tgmn, ball", "all,ball,mur,raeymnl,rumk,tall,true,trum,yes"]  # "rumk,yes"
arr3 = ["rbfg, ukop, fgub, mnry", "bog,bop,gup,fur,ruk"]  # "true"

print(BoggleSolver(arr1))
print(BoggleSolver(arr2))
print(BoggleSolver(arr3))