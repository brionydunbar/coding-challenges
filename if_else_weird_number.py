"""
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
"""

def weird_or_not(n):
    if n % 2 == 0:
        if 2 <= n <= 5:
            return "Not Weird"
        if 6 <= n <= 20:
            return "Weird"
        if n > 20:
            return "Not Weird"
        else:
            return "Weird"
    else:
        return "Weird"

print(weird_or_not(3))
print(weird_or_not(24))