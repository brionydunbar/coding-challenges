"""
Have the function BinaryConverter(str) return the decimal form of the binary value.
For example: if 101 is passed return 5, or if 1000 is passed return 8.

Examples:
Input: "100101"
Output: 37
Input: "011"
Output: 3
"""

def BinaryConverter(strParam):
  # convert to decimal
  binary = strParam
  decimal = 0 # initialise to 0
  for digit in binary:
    decimal = decimal*2 + int(digit)
  return decimal

# keep this function call here
# print(BinaryConverter(input()))

# Testing:
str1 = "100101" # 37
str2 = "011" # 3

print(BinaryConverter(str1))
print(BinaryConverter(str2))