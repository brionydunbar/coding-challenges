"""
In this Kata, you will be given an array of arrays and your task will be to return the number of unique arrays that can be formed by picking exactly one element from each subarray.

For example: solve([[1,2],[4],[5,6]]) = 4, because it results in only 4 possibilities.
They are [1,4,5],[1,4,6],[2,4,5],[2,4,6].

Make sure that you don't count duplicates; for example solve([[1,2],[4,4],[5,6,6]]) = 4, since the extra outcomes are just duplicates.
"""

def solve(arr):
    unique_arrays = set() # set to store each unique array combination as a tuple (hashable)
    n = len(arr) # n as number of subarrays
    indices = [0] * n # list of pointers, will tell us which element we are currently picking from subarray i

    # calculate total number of possible arrays including duplicates
    count = 1
    for a in arr:
        count *= len(a) # multiplies the count by the length of each subarray

    # iterate to generate combinations
    for _ in range(count):
        current_array = [] # builds current array by picking indices[i] from subarray[i]
        for i in range(n):
            current_array.append(arr[i][indices[i]])
        unique_arrays.add(tuple(current_array)) # convert to tuple be hashable and puts into unique_arrays set to eliminate duplicates

        # increment indices to move to next combination
        for i in range(n - 1, -1, -1): # for each position i from right to left
            indices[i] += 1 # try to increment it
            if indices[i] < len(arr[i]): # if the position exceeds subarray length, reset to 0 and continue to next left position
                break
            else:
                indices[i] = 0

    return  len(unique_arrays) # return the unique count


print(solve([[1,2], [4], [5,6]])) # total of 2 * 1 * 2 = 4 possibilities
print(solve([[1,2], [4,4], [5,6,6]])) # total of 2 * 1 * 2 = 4 possibilities (removing duplicates)
print(solve([[1,2], [3,4], [5,6,7]])) # total of 2 * 2 * 3 = 12 possibilities