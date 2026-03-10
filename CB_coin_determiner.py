"""
Have the function CoinDeterminer(num) take the input, which will be an integer ranging from 1 to 250, and return an integer output that will specify the least number of coins, that when added, equal the input integer.
Coins are based on a system as follows:
there are coins representing the integers 1, 5, 7, 9, and 11.
So for example: if num is 16, then the output should be 2 because you can achieve the number 16 with the coins 9 and 7.
If num is 25, then the output should be 3 because you can achieve 25 with either 11, 9, and 5 coins or with 9, 9, and 7 coins.

Examples:
Input: 6
Output: 2

Input: 16
Output: 2
"""

import math

def CoinDeterminer(num):
  if num < 5:
    return num
  count = num / 11
  if (num % 11) % 2 == 0:
    return math.floor(count) + 2
  else:
    return math.floor(count) + 1

# keep this function call here
# print(CoinDeterminer(input()))


# Testing:
num1 = 6 # 2
num2 = 16 # 2
num3 = 25 # 3
num4 = 2 # 2
num5 = 4 # 4

print(CoinDeterminer(num1))
print(CoinDeterminer(num2))
print(CoinDeterminer(num3))
print(CoinDeterminer(num4))
print(CoinDeterminer(num5))
