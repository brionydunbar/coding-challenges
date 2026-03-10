"""
Have the function MissingDigit(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the digit that completes the equation.
In one of the numbers in the equation, there will be an x character, and your program should determine what digit is missing.
For example, if str is "3x + 12 = 46" then your program should output 4.
The x character can appear in any of the three numbers and all three numbers will be greater than or equal to 0 and less than or equal to 1000000.

Examples:
Input: "4 - 2 = x"
Output: 2

Input: "1x0 * 12 = 1200"
Output: 0
"""


def MissingDigit(strParam):
  # iterate through 0-9 to check if equation balances
  for digit in range(10):
    # replace x with current digit
    equation = strParam.replace("x", str(digit))
    try:
      # split equation to right and left
      left, right = equation.split("=")
      # evaluate if both sides now equal
      left_num = eval(left.strip())
      right_num = int(right.strip()) # convert to int to avoid leading 0 error

      if left_num == right_num:
        return digit
    except ZeroDivisionError:
      continue
    except SyntaxError:
      continue
# keep this function call here
# print(MissingDigit(input()))


# Testing:
str1 = "4 - 2 = x" # 2
str2 = "1x0 * 12 = 1200" # 0
str3 = "3x + 12 = 46" # 4
str4 = "24 / x = 12" # 2
str5 = "1 + 1111 = x112" # 1

print(MissingDigit(str1))
print(MissingDigit(str2))
print(MissingDigit(str3))
print(MissingDigit(str4))
print(MissingDigit(str5))