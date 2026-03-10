####################################################################
# 1. Reverse Integer

# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

def solution1(x):
    # declare rev_str variable, convert x to string and reverse
    rev_str = str(x)[::-1]
    if x < 0: # account for negative numbers by moving the - back to the start when converting back to int
        rev_int = int("-" + rev_str[:-1])
    else: # if positive, simply convert back to int
        rev_int = int(rev_str)
    return rev_int # return the reversed int

print(solution1(-147))
print(solution1(852))