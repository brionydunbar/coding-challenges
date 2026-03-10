"""
In the Python file, you are provided with a function named find_duplicate_integer which takes a list of integers from 1 to n as its argument. This list contains n + 1 integers, implying one duplicate.

Your task is to modify the function to return the duplicated integer from the list. The starter code has two logical errors that needs to be corrected.

Example Input
[1, 3, 4, 2, 2]

Example Output
2
"""

"""
SKELETON CODE
def find_duplicate_integer(integers):
    n = len(integers)
    expected_sum = n * (n - 2) // 2
    actual_sum = sum(integers)
    
    return actual_sum - expected_sum

print(find_duplicate_integer([1, 3, 4, 2, 2]))
"""


def find_duplicate_integer(integers):
    n = len(integers) - 1 # n is one less than the length of the list
    expected_sum = n * (n + 1) // 2 # correct formula for expected sum
    actual_sum = sum(integers) # return the difference between the actual sum, which gives the duplicate return actual_sum = expected_sum

    return actual_sum - expected_sum


print(find_duplicate_integer([1, 3, 4, 2, 2]))