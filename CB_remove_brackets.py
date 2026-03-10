"""
Have the function RemoveBrackets(str) take the str parameter being passed, which will contain only the characters "(" and ")", and determine the minimum number of brackets that need to be removed to create a string of correctly matched brackets.
For example: if str is "(()))" then your program should return the number 1.
The answer could potentially be 0, and there will always be at least one set of matching brackets in the string.

Examples:
Input: "(())()((("
Output: 3

Input: "(()("
Output: 2
"""

def RemoveBrackets(strParam):
  stack = list()
  for i in strParam:
    if len(stack) == 0:
      stack.append(i)
    else:
      if i == ")" and stack[-1] == "(":
        stack.pop() # remove if matching
      else:
        stack.append(i)
  return len(stack)

# keep this function call here
# print(RemoveBrackets(input()))

# Testing:
str1 = "(())()(((" # 3
str2 = "(()(" # 2
str3 = "(()))" # 1

print(RemoveBrackets(str1))
print(RemoveBrackets(str2))
print(RemoveBrackets(str3))