"""
Have the function ScaleBalancing(strArr) read strArr which will contain two elements, the first being the two positive integer weights on a balance scale (left and right sides) and the second element being a list of available weights as positive integers.
Your goal is to determine if you can balance the scale by using the least amount of weights from the list, but using at most only 2 weights.
For example: if strArr is ["[5, 9]", "[1, 2, 6, 7]"] then this means there is a balance scale with a weight of 5 on the left side and 9 on the right side.
It is in fact possible to balance this scale by adding a 6 to the left side from the list of weights and adding a 2 to the right side.
Both scales will now equal 11 and they are perfectly balanced.
Your program should return a comma separated string of the weights that were used from the list in ascending order, so for this example your program should return the string 2,6

There will only ever be one unique solution and the list of available weights will not be empty. It is also possible to add two weights to only one side of the scale to balance it.
If it is not possible to balance the scale then your program should return the string not possible.

Examples:
Input: ["[3, 4]", "[1, 2, 7, 7]"]
Output: 1

Input: ["[13, 4]", "[1, 2, 3, 6, 14]"]
Output: 3,6
"""

from itertools import combinations


def ScaleBalancing(strArr):
    # parse input into lists of integers
    left, right = eval(strArr[0])
    weights = eval(strArr[1])

    # try all possible solutions using 1 or 2 weights
    # 1 weight
    for w in weights:
        # add to left
        if left + w == right:
            return str(w)
        # add to right
        if right + w == left:
            return str(w)

    # 2 weights
    for w1, w2 in combinations(weights, 2):
        # both left
        if left + w1 + w2 == right:
            return ",".join(map(str, sorted([w1, w2])))
        # both right
        if right + w1 + w2 == left:
            return ",".join(map(str, sorted([w1, w2])))
        # one each side
        if left + w1 == right + w2:
            return ",".join(map(str, sorted([w1, w2])))
        if left + w2 == right + w1:
            return ",".join(map(str, sorted([w1, w2])))

    # if no solution found
    return "not possible"


# keep this function call here
# print(ScaleBalancing(input()))

# Testing:
arr1 = ["[3, 4]", "[1, 2, 7, 7]"]  # 1
arr2 = ["[13, 4]", "[1, 2, 3, 6, 14]"]  # 3,6
arr3 = ["[5, 9]", "[1, 2, 6, 7]"]  # 2,6

print(ScaleBalancing(arr1))
print(ScaleBalancing(arr2))
print(ScaleBalancing(arr3))