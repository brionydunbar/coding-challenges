"""
Have the function DashInsertII(str) insert dashes ('-') between each two odd numbers and insert asterisks ('*') between each two even numbers in str.
For example: if str is 4546793 the output should be 454*67-9-3.
Don't count zero as an odd or even number.

Examples:
Input: 99946
Output: 9-9-94*6

Input: 56647304
Output: 56*6*47-304
"""

def DashInsertII(num):
  string = str(num)
  result = [string[0]]
  for i in range(1, len(string)):
    previous, current = int(string[i - 1]), int(string[i])
    # check if odd next to odd
    if previous % 2 == 1 and current % 2 == 1:
      result.append("-")
    # check if even next to even
    elif previous % 2 == 0 and current % 2 == 0 and previous != 0 and current != 0:
      result.append("*")
    result.append(string[i])
  return "".join(result)

# keep this function call here
# print(DashInsertII(input()))

# Testing:
num1 = 99946 # "9-9-94*6"
num2 = 56647304 # "56*6*47-304"
num3 = 4546793 # "454*67-9-3"

print(DashInsertII(num1))
print(DashInsertII(num2))
print(DashInsertII(num3))
