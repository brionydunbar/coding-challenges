"""
Have the function KUniqueCharacters(str) take the str parameter being passed and find the longest substring that contains k unique characters, where k will be the first character from the string.
The substring will start from the second position in the string because the first character will be the integer k.
For example: if str is "2aabbacbaa" there are several substrings that all contain 2 unique characters, namely: ["aabba", "ac", "cb", "ba"], but your program should return "aabba" because it is the longest substring.
If there are multiple longest substrings, then return the first substring encountered with the longest length.
k will range from 1 to 6.

Examples:
Input: "3aabacbebebe"
Output: cbebebe

Input: "2aabbcbbbadef"
Output: bbcbbb
"""

def KUniqueCharacters(strParam):
  # find k in string
  k = int(strParam[0])
  # remove k from string to leave letters
  s = strParam[1:]
  # set pointers start "j" and end "i"
  n = len(s)
  i = 0
  j = 0
  # keep counter to track how many unique chars in window
  count = 0
  maximum = -1
  freq = {}
  result = ""
  # expand window by moving j and include each char in frequency array of 26
  while j < n:
    freq[s[j]]= freq.get(s[j], 0) + 1
    # increment count when char appears for first time
    if freq[s[j]] == 1:
      count += 1
    # if number of unique chars exceeds k, move start pointer i forward to shrink from left
    while count > k:
      freq[s[i]] -= 1
      # update freq and count
      if freq[s[i]] == 0:
        count -= 1
        del freq[s[i]]
      i += 1
    # when num of unique chars = k, update max length so far
    if count == k and j - i + 1 > maximum:
      maximum = j - i + 1
      result = s[i:j + 1]
    j += 1
  return result

# keep this function call here
# print(KUniqueCharacters(input()))

# Testing:
str1 = "3aabacbebebe" # "cbebebe"
str2 = "2aabbcbbbadef" # "bbcbbb"
str3 = "2aabbacbaa" # "aabba"

print(KUniqueCharacters(str1))
print(KUniqueCharacters(str2))
print(KUniqueCharacters(str3))