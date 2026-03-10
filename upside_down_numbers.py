"""
Consider the numbers 6969 and 9116.
When you rotate them 180 degrees (upside down), these numbers remain the same.
To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same.
Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range.
For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10.
They are 0, 1, 8.
"""

def solve(a, b):
    nums = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"} # a key value dictionary for the upside down numbers
    count = 0
    for i in range(a, b):
        i = str(i) # convert to string so we can loop, join then compare
        try:
            m = "".join([nums[x] for x in i[::-1]]) # goes through i in reverse and checks the key
        except KeyError: # don't care about numbers not in key so ignore them
            continue
        if i == m: # check if the original str i and the str from the key are equal and therefore reversible
            count += 1
    return count

print(solve(0, 10))
print(solve(4, 20))
print(solve(3, 5))