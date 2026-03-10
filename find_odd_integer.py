"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

def find_it(seq):
    array_size = len(seq) # gets length of input list
    for i in range(0, array_size): # starts a loop over each element seq[i] in the list
        count = 0 # resets count to 0 for each new element
        for j in range(0, array_size): # compares how many times seq[i] appears in list by comparing to every seq[j]
            if seq[i] == seq[j]:
                count += 1
        if count % 2 != 0:
            odd_number = seq[i]
    return odd_number

print(find_it([7])) # 7
print(find_it([0])) # 0
print(find_it([1,1,2])) # 2
print(find_it([0,1,0,1,0])) # 3
print(find_it([1,2,2,3,3,3,4,3,3,3,2,2,1])) # 4
