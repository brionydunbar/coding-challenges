"""
Have the function MissingDigitII(str) take the str parameter, which will be a simple mathematical formula with three numbers, a single operator (+, -, *, or /) and an equal sign (=) and return the two digits that complete the equation.
In two of the numbers in the equation, there will be a single ? character, and your program should determine what digits are missing and return them separated by a space.
For example, if str is "38?5 * 3 = 1?595" then your program should output 6 1.

The ? character will always appear in both the first number and the last number in the mathematical expression.
There will always be a unique solution.

Examples:
Input: "56? * 106 = 5?678"
Output: 3 9

Input: "18?1 + 9 = 189?"
Output: 8 0
"""

def MissingDigitII(strParam):
  # split into left and right
  left, right = strParam.split("=")
  left = left.strip()
  right = right.strip()
  # store operator
  operator = None
  for char in left:
    if char in "+-*/":
      operator = char
      break
  # split left into nums
  num1_temp, num2_temp = [d.strip() for d in left.split(operator)]
  num3_temp = right

  # iterator over possible digits for ?
  for d1 in range(10):
    for d2 in range(10):
      candidate1 = num1_temp.replace("?", str(d1))
      candidate2 = num2_temp.replace("?", str(d1))
      candidate3 = num3_temp.replace("?", str(d2))

      try:
        if operator == "+":
          if int(candidate1) + int(candidate2) == int(candidate3):
            return f"{d1} {d2}"
        elif operator == "-":
          if int(candidate1) - int(candidate2) == int(candidate3):
            return f"{d1} {d2}"
        elif operator == "*":
          if int(candidate1) * int(candidate2) == int(candidate3):
            return f"{d1} {d2}"
        elif operator == "/":
          if int(candidate1) / int(candidate2) == int(candidate3) and int(candidate2) != 0:
            return f"{d1} {d2}"
      except (ValueError, ZeroDivisionError):
        continue
  return "No solution"

# keep this function call here
# print(MissingDigitII(input()))

# Testing:
str1 = "56? * 106 = 5?678" # 3 9
str2 = "18?1 + 9 = 189?" # 8 0
str3 = "38?5 * 3 = 1?595" # 6 1

print(MissingDigitII(str1))
print(MissingDigitII(str2))
print(MissingDigitII(str3))
