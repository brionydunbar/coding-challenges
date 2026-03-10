"""
Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero,
and return the number of valid combinations that can be formed with num pairs of parentheses.
For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis, namely:
()()(), are ()()(), ()(()), (())(), ((())), and (()()).
There are 5 total combinations when the input is 3, so your program should return 5.
"""

# catalan number problem for n = num
# nth catalan number gives:
    # the number of valid ways to arrange n pairs of parentheses so they are balanced
    # Cn = (2n)! / (n + 1)!n!
    # this translates to BracketCombinations(num) = Cn = (2 * num)! / (num + 1)! * (num)!

from math import factorial

def BracketCombinations(num):
    return int(factorial(num*2) / (factorial(num + 1) * factorial((num))))

print(BracketCombinations(3))
print(BracketCombinations(7))
print(BracketCombinations(20))