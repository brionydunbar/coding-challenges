"""
Have the function FormattedNumber(strArr) take the strArr parameter being passed, which will only contain a single element, and return the string true if it is a valid number that contains only digits with properly placed decimals and commas, otherwise return the string false.
For example: if strArr is ["1,093,222.04"] then your program should return the string true, but if the input were ["1,093,22.04"] then your program should return the string false.
The input may contain characters other than digits.

Examples:
Input: ["0.232567"]
Output: true

Input: ["2,567.00.2"]
Output: false
"""

import re

def FormattedNumber(strArr):
  num = strArr[0] # extract string
  # use regex pattern to check correct format
  pattern = r"^\d{1,3}(?:,\d{3})*(?:\.\d+)?$"
  if re.match(pattern, num):
    return "true"
  else:
    return "false"

# keep this function call here
# print(FormattedNumber(input()))

# Testing:
arr1 = ["0.232567"] # "true"
arr2 = ["2,567.00.2"] # "false"
arr3 = ["1,093,222.04"] # "true"
arr4 = ["1,093,22.04"] # "false"

print(FormattedNumber(arr1))
print(FormattedNumber(arr2))
print(FormattedNumber(arr3))
print(FormattedNumber(arr4))

"""
# The regular expression explained:
    # ^          - Matches the beginning of the string.
    # \d{1,3}    - Matches 1 to 3 digits at the start (e.g., "1", "123").
    # (?:,\d{3})* - Matches a comma followed by exactly 3 digits, zero or more times (for the thousands separator).
    #                (?:...) is a non-capturing group.
    # (?:\.\d+)?  - Optionally matches a decimal point followed by one or more digits.
    # $          - Matches the end of the string.
    # This pattern specifically looks for numbers with potentially thousands separators and a decimal part.
    pattern = r"^\d{1,3}(?:,\d{3})*(?:\.\d+)?$"
"""