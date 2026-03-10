"""
Have the function NumberEncoding(str) take the str parameter and encode the message according to the following rule:
encode every letter into its corresponding numbered position in the alphabet.
Symbols and spaces will also be used in the input.
For example: if str is "af5c a#!" then your program should return 1653 1#!.

Examples:
Input: "hello 45"
Output: 85121215 45

Input: "jaj-a"
Output: 10110-1
"""

def NumberEncoding(strParam):
  output = ""
  for i in range(len(strParam)):
    # convert lower case to num
    if strParam[i].isalpha() and strParam[i].islower():
      num = str(ord(strParam[i]) - 96)
      output = output + num + ""
    # convert upper case to num
    elif strParam[i].isalpha() and strParam[i].isupper():
      num = str(ord(strParam[i]) - 38)
      output = output + num + ""
    # add spaces
    elif strParam[i] == " ":
      output = output + " "
    # add non-alpha chars
    else:
      output = output + strParam[i] + ""
  return output

# keep this function call here
# print(NumberEncoding(input()))

# Testing:
str1 = "hello 45" # 85121215 45
str2 = "jaj-a" # 10110-1
str3 = "af5c a#!" # 1653 1#!

print(NumberEncoding(str1))
print(NumberEncoding(str2))
print(NumberEncoding(str3))