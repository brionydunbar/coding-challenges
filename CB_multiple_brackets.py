"""
Have the function MultipleBrackets(str) take the str parameter being passed and return 1 #ofBrackets if the brackets are correctly matched and each one is accounted for.
Otherwise return 0.
For example: if str is "(hello [world])(!)", then the output should be 1 3 because all the brackets are matched and there are 3 pairs of brackets, but if str is "((hello [world])" then the output should be 0 because the brackets do not correctly match up.
Only "(", ")", "[", and "]" will be used as brackets.
If str contains no brackets return 1.

Examples:
Input: "(coder)[byte)]"
Output: 0

Input: "(c([od]er)) b(yt[e])"
Output: 1 5
"""

def MultipleBrackets(strParam):
  stack = []
  pairs = {")": "(", "]": "["}
  count = 0
  for char in strParam:
    if char in "([": # opening brackets
      stack.append(char)
    elif char in ")]": # closing brackets
      if not stack or stack[-1] != pairs[char]:
        return 0 # mismatch or no opening bracket
      stack.pop()
      count += 1 # count valid pairs
  if stack: # leftover unmatched
    return 0
  return f"1 {count}"

# keep this function call here
# print(MultipleBrackets(input()))


# Testing:
str1 = "(coder)[byte)]" # 0
str2 = "(c([od]er)) b(yt[e])" # 1 5
str3 = "(hello [world])(!)" # 1 3
str4 = "((hello [world])" # 0
str5 = "coder(b)(y)(t)([e))" # 0
str6 = "le[tter(s) gal](o)(r)((e])" # 0

print(MultipleBrackets(str1))
print(MultipleBrackets(str2))
print(MultipleBrackets(str3))
print(MultipleBrackets(str4))
print(MultipleBrackets(str5))
print(MultipleBrackets(str6))