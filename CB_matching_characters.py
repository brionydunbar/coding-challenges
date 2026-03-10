"""
Have the function MatchingCharacters(str) take the str parameter being passed and determine the largest number of unique characters that exists between a pair of matching letters anywhere in the string.
For example: if str is "ahyjakh" then there are only two pairs of matching letters, the two a's and the two h's. Between the pair of a's there are 3 unique characters: h, y, and j.
Between the h's there are 4 unique characters: y, j, a, and k.
So for this example your program should return 4.

Another example: if str is "ghececgkaem" then your program should return 5 because the most unique characters exists within the farthest pair of e characters.
The input string may not contain any character pairs, and in that case your program should just return 0.
The input will only consist of lowercase alphabetic characters.

Examples:
Input: "mmmerme"
Output: 3

Input: "abccdefghi"
Output: 0
"""

def MatchingCharacters(strParam):
  char_indices = {} # store first and last indices of each char
  max_unique_chars = 0

  # find all pairs of matching letters
  # store first and last occurences
  for i, char in enumerate(strParam):
    if char not in char_indices:
      char_indices[char] = [i, i] # first occurence
    else:
      char_indices[char][1] = i # last occurence

  # calculate unique characters for each pair
  for char, (first, last) in char_indices.items():
    # only consider chars that appear more than once
    if first != last:
      # get substring between first and last occurence
      substring = strParam[first + 1:last]
      # count unique chars in substring
      unique_count = len(set(substring))
      # update max unique chars found so far
      max_unique_chars = max(max_unique_chars, unique_count)

  return max_unique_chars

# keep this function call here
# print(MatchingCharacters(input()))

# Testing:
str1 = "mmmerme" # 3
str2 = "abccdefghi" # 0
str3 = "ahyjakh" # 4
str4 = "ghececgkaem" # 5

print(MatchingCharacters(str1))
print(MatchingCharacters(str2))
print(MatchingCharacters(str3))
print(MatchingCharacters(str4))