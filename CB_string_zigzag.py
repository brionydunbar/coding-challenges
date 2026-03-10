"""
Have the function StringZigzag(strArr) read the array of strings stored in strArr, which will contain two elements, the first some sort of string and the second element will be a number ranging from 1 to 6.
The number represents how many rows to print the string on so that it forms a zig-zag pattern.
For example: if strArr is ["coderbyte", "3"] then this word will look like the following if you print it in a zig-zag pattern with 3 rows:

Your program should return the word formed by combining the characters as you iterate through each row, so for this example your program should return the string creoebtdy.

Examples:
Input: ["cat", "5"]
Output: cat

Input: ["kaamvjjfl", "4"]
Output: kjajfavlm
"""


def StringZigzag(strArr):
    # parse input
    string = strArr[0]
    n = int(strArr[1])

    # if only one row
    if n == 1:
        return string

    # create array for each row
    rows = [""] * n  # list of strings
    row = 0  # keeps track of current row
    down = True  # direction flag

    # traverse string
    for ch in string:
        rows[row] += ch
        if row == 0:
            down = True
        elif row == n - 1:
            down = False

        row += 1 if down else -1

    return "".join(rows)


# keep this function call here
# print(StringZigzag(input()))

# Testing:
arr1 = ["cat", "5"]  # "cat"
arr2 = ["kaamvjjfl", "4"]  # "kjajfavlm"
arr3 = ["coderbyte", "3"]  # "creoebtdy"

print(StringZigzag(arr1))
print(StringZigzag(arr2))
print(StringZigzag(arr3))