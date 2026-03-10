"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""

def find_uniq(arr):
    n_arr = [x for x in set(arr) if arr.count(x) == 1] # convert to set to keep only unique values, loop over x and keep only if equal to 1
    n = n_arr[0] # take first and only element in new array
    return n


print(find_uniq([1, 1, 1, 2, 1, 1]))
print(find_uniq([0, 0, 0.55, 0, 0]))


# WITHOUT LIST COMPREHENSION

def find_uniq2(arr):
    n_arr = []
    for x in set(arr):
        if arr.count(x) == 1:
            n_arr.append(x)
    n = n_arr[0]
    return n


print(find_uniq2([1, 1, 1, 2, 1, 1]))
print(find_uniq2([0, 0, 0.55, 0, 0]))