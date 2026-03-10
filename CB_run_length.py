"""
Have the function RunLength(str) take the str parameter being passed and return a compressed version of the string using the Run-length encoding algorithm.
This algorithm works by taking the occurrence of each repeating character and outputting that number along with a single character of the repeating sequence.
For example: "wwwggopp" would return 3w2g1o2p.
The string will not contain any numbers, punctuation, or symbols.

Examples
Input: "aabbcde"
Output: 2a2b1c1d1e
Input: "wwwbbbw"
Output: 3w3b1w
"""


def RunLength(strParam):
    # pick first char from strParam
    # append to destination string
    # count subsequent occurrences and append
    # pick next char and repeat above until end of string
    n = len(strParam)
    i = 0
    result = ""

    while i < n:
        # count occurences of current char
        count = 1
        while i < n - 1 and strParam[i] == strParam[i + 1]:
            count += 1
            i += 1

        # return char and count
        result += str(count) + strParam[i]

        # move to next char
        i += 1

    return result


# keep this function call here
# print(RunLength(input()))


# Testing:
str1 = "aabbcde" # "2a2b1c1d1e"
str2 = "wwwbbbw" # "3w3b1w"

print(RunLength(str1))
print(RunLength(str2))
