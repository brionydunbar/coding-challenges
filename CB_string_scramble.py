"""
Have the function StringScramble(str1,str2) take both parameters being passed and return the string true if a portion of str1 characters can be rearranged to match str2,
otherwise return the string false.
For example: if str1 is "rkqodlw" and str2 is "world" the output should return true.
Punctuation and symbols will not be entered with the parameters.

Examples:
Input: "cdore" & str2 = "coder"
Output: true
Input: "h3llko" & str2 = "hello"
Output: false
"""

from collections import Counter

def StringScramble(str1,str2):
  count1 = Counter(str1) # frequency map for str1
  count2 = Counter(str2) # frequency map for str2

  for char in count2: # check every char
    if count2[char] > count1.get(char, 0):
      return "false"
  return "true"

# keep this function call here
# print(StringScramble(input()))

# Testing:
str1 = "cdore"
str2 = "coder" # "true"

str3 = "h3llko"
str4 = "hello" # "false"

str5 = "win33er"
str6 = "winner" # false

print(StringScramble(str1, str2))
print(StringScramble(str3, str4))
print(StringScramble(str5, str6))