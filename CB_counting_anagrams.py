"""
Have the function CountingAnagrams(str) take the str parameter and determine how many anagrams exist in the string.
An anagram is a new word that is produced from rearranging the characters in a different word, for example: cars and arcs are anagrams.
Your program should determine how many anagrams exist in a given string and return the total number.
For example: if str is "aa aa odg dog gdo" then your program should return 2 because "dog" and "gdo" are anagrams of "odg".
The word "aa" occurs twice in the string but it isn't an anagram because it is the same word just repeated.
The string will contain only spaces and lowercase letters, no punctuation, numbers, or uppercase letters.

Examples:
Input: "aa aa odg dog gdo"
Output: 2

Input: "a c b c run urn urn"
Output: 1
"""

def CountingAnagrams(strParam):
  words = strParam.split() # split string into words
  word_map = {} # map of sorted letters: set of unique words

  # group words by sorted letters
  for word in words:
    sorted_word = "".join(sorted(word))
    if sorted_word not in word_map:
      word_map[sorted_word] = set()
    word_map[sorted_word].add(word)

  # count anagram pairs
  anagrams = 0
  for word_list in word_map.values():
    unique_words = set(word_list)
    # count only words that have at least one other distinct word
    if len(unique_words) > 1:
      # add number of words excluding any repeats of the same word
      anagrams += len(word_list) - 1 # only count words that have distinct anagrams

  return anagrams


# keep this function call here
# print(CountingAnagrams(input()))

# Testing:
str1 = "aa aa odg dog gdo" # 2
str2 = "a c b c run urn urn" # 1

print(CountingAnagrams(str1))
print(CountingAnagrams(str2))
