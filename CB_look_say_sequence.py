"""
Have the function LookSaySequence(num) take the num parameter being passed and return the next number in the sequence according to the following rule: to generate the next number in a sequence read off the digits of the given number, counting the number of digits in groups of the same digit.
For example, the sequence beginning with 1 would be: 1, 11, 21, 1211, ...
The 11 comes from there being "one 1" before it and the 21 comes from there being "two 1's" before it.
So your program should return the next number in the sequence given num.

Examples:
Input: 1211
Output: 111221

Input: 2466
Output: 121426
"""

def LookSaySequence(num):
  s = str(num) # convert num to str to iterate
  result = ""
  count = 1

  # loop through digits
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      count += 1
    else:
      # when digit changes, append count + previous digit
      result += str(count) + s[i - 1]
      count = 1
  # last group
  result += str(count) + s[-1]

  return result
# keep this function call here
# print(LookSaySequence(input()))

# Testing:
num1 = 1211 # 111221
num2 = 2466 # 121426

print(LookSaySequence(num1))
print(LookSaySequence(num2))