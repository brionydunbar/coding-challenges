"""
Have the function LetterCount(str) take the str parameter being passed and return the first word with the greatest number of repeated letters.
For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's.
If there are no words with repeating letters return -1.
Words will be separated by spaces.

Examples:
Input: "Hello apple pie"
Output: Hello
Input: "No words"
Output: -1
"""

def LetterCount(strParam):
  words = strParam.split()
  max_repeats = 0
  result = "-1"

  for word in words:
    # lowercase and only letters
    clean_word = "".join([char.lower() for char in word if char.isalpha()])
    frequency = [0] * 26

    for char in clean_word:
      frequency[ord(char) - ord("a")] += 1

    # find maximum frequency in this word
    word_max = max(frequency)
    if word_max > 1 and word_max > max_repeats:
      max_repeats = word_max
      result = word

  return result

# keep this function call here
# print(LetterCount(input()))

# Testing:
str1 = "Hello apple pie" # Hello
str2 = "No words" # -1
str3 = "Today, is the greatest day ever!" # greatest

print(LetterCount(str1))
print(LetterCount(str2))
print(LetterCount(str3))