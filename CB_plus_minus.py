"""
Have the function PlusMinus(num) read the num parameter being passed which will be a combination of 1 or more single digits, and determine if it's possible to separate the digits with either a plus or minus sign to get the final expression to equal zero.
For example: if num is 35132 then it's possible to separate the digits the following way, 3 - 5 + 1 + 3 - 2, and this expression equals zero.
Your program should return a string of the signs you used, so for this example your program should return -++-.
If it's not possible to get the digit expression to equal zero, return the string not possible.

If there are multiple ways to get the final expression to equal zero, choose the one that contains more minus characters.
For example: if num is 26712 your program should return -+-- and not +-+-.

Examples:
Input: 199
Output: not possible

Input: 26712
Output: -+--
"""


def PlusMinus(num):
    # parse into list
    digits = list(map(int, str(num)))
    n = len(digits)

    # recursive helper function
    def backtrack(index, current_sum, path):
        if index == n:
            if current_sum == 0:
                return path
            return None

        # Try '-' first to prioritize more minus signs
        res = backtrack(index + 1, current_sum - digits[index], path + '-')
        if res is not None:
            return res

        # Try '+'
        res = backtrack(index + 1, current_sum + digits[index], path + '+')
        if res is not None:
            return res

        return None

    # Start recursion from the second digit, first digit is taken as initial sum
    result = backtrack(1, digits[0], '')
    return result if result is not None else "not possible"


# keep this function call here
# print(PlusMinus(input()))

# Testing:
num1 = 199  # "not possible"
num2 = 26712  # "-+--"
num3 = 35132  # "-++-"

print(PlusMinus(num1))
print(PlusMinus(num2))
print(PlusMinus(num3))