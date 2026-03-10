"""
Longest Word Challenge

Challenge:
    Write a function longest_word(sentence) that finds and returns the largest
    word in a string.

Requirements:
    1. Return the longest word in the string
    2. If multiple words have the same length, return the FIRST one encountered
    3. Ignore all punctuation (keep only letters a-z, A-Z, and spaces)
    4. Assume the input string will not be empty
    5. Words are separated by spaces

Return Value:
    - Return the longest word as a string (without punctuation)

Examples:
    longest_word("fun&!! time")                    # → "time"
    longest_word("I love dogs")                    # → "love" (first of equal length)
    longest_word("a beautiful sentence^&!")       # → "beautiful"
    longest_word("letter after letter!!")         # → "letter" (first occurrence)
    longest_word("confusing /:sentence:/[ this is not!!!!!!!~")  # → "confusing"

Challenge Level: Easy
Source: Coderbyte
Most Popular: 140,000+ solutions
"""


import string
def longest_word(sentence):
    clean_sentence = "".join([char for char in sentence if char not in string.punctuation])
    word_list = clean_sentence.split()
    longest_word = ""
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word
        elif len(word) == len(longest_word):
            longest_word = longest_word
    return longest_word


print(longest_word("fun&!! time")) # time - fun not longest when punctuation removed
print(longest_word("I love dogs")) # love - first longest word
print(longest_word("a beautiful sentence^&!")) # beautiful
print(longest_word("letter after letter!!")) # letter
print(longest_word("confusing /:sentence:/[ this is not!!!!!!!~")) # confusing


# ALTERNATIVE SOLUTION
def longest_word2(sentence):
    # clean the string
    clean_sentence = "" # set a container for the cleaned string
    for char in sentence:
        if char.isalpha() or char == " ":
            clean_sentence += char
    # split string into strings in a list
    words = clean_sentence.split() # automatically splits at empty space
    # count them against each other using iteration
    current_longest_word = "" # container for the longest word - starts empty then adds first word
    for word in words: # goes through rest of content and replaces longest word if longer
        if len(word) > len(current_longest_word):
            current_longest_word = word
    return current_longest_word
    # return a string - the longest word

print(longest_word2("fun&!! time"))  # time - fun not longest when punctuation removed
print(longest_word2("I love dogs"))  # love - first longest word
print(longest_word2("a beautiful sentence^&!"))  # beautiful
print(longest_word2("letter after letter!!"))  # letter
print(longest_word2("confusing /:sentence:/[ this is not!!!!!!!~"))  # confusing

