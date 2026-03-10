"""
Have the function PalindromicSubstring(str) take the str parameter being passed and find the longest palindromic substring, which means the longest substring which is read the same forwards as it is backwards.
For example: if str is "abracecars" then your program should return the string racecar because it is the longest palindrome within the input string.

The input will only contain lowercase alphabetic characters.
The longest palindromic substring will always be unique, but if there is none that is longer than 2 characters, return the string none.

Examples:
Input: "hellosannasmith"
Output: sannas

Input: "abcdefgg"
Output: none
"""

def PalindromicSubstring(strParam):
  n = len(strParam)
  longest = "" # track the current longest
  # iterate through starting points of substring
  for i in range(n):
    # iterate through ending points of substing
    for j in range(i, n):
      sub = strParam[i:j + 1] # slice the substring
      # check if palindrome and if longer than current
      if sub == sub[::-1] and len(sub) > len(longest):
        longest = sub # replace longest
  # if longest not longer than 2
  if len(longest) <= 2:
    return "none"
  else:
    return longest

# keep this function call here
# print(PalindromicSubstring(input()))

# Testing:
str1 = "hellosannasmith" # "sannas"
str2 = "abcdefgg" # "none"
str3 = "abracecars" # "racecar"

print(PalindromicSubstring(str1))
print(PalindromicSubstring(str2))
print(PalindromicSubstring(str3))