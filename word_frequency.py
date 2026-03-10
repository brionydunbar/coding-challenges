"""
Word Frequency Analyzer

Write a function called analyze_text that processes a text string and returns the most frequent word.

Your function should:
1. Take a string parameter (text)
2. Convert the text to lowercase
3. Remove all punctuation marks
4. Split the text into individual words
5. Count the frequency of each word
6. Return the word that appears most frequently

"""
import string
from collections import Counter

def analyze_text(text):
    text = text.lower()
    translator = str.maketrans("", "", string.punctuation)
    clean_text = text.translate(translator)
    words = clean_text.split()
    frequency = Counter(words)
    return frequency.most_common()[0][0]

print(analyze_text("The quick brown fox jumps over the lazy dog."))  # "the"
print(analyze_text("Hello world! Hello Python. Python is fun."))  # "hello"
print(analyze_text("a a a b b c"))  # "a"
print(analyze_text("Numbers123 and letters456 should be treated as words."))  # "numbers123"

# ALTERNATIVE SOLUTION WITHOUT COUNTER
def analyze_text2(text):
    # Convert text to lowercase
    text = text.lower()
    # Replace punctuation with spaces
    for char in ".,!?;:()[]{}\"'":
        text = text.replace(char, " ")
    # Split into words
    words = text.split()
    # Count frequency
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    # Find most frequent word
    most_frequent_word = None
    highest_count = 0
    # Iterate through the original word order to maintain first occurrence priority
    for word in words:
        # Only process each unique word once
        if word in word_counts:
            count = word_counts[word]
            if count > highest_count:
                highest_count = count
                most_frequent_word = word
            # Remove word from dictionary once we've processed it
            del word_counts[word]

    return most_frequent_word

print(analyze_text2("The quick brown fox jumps over the lazy dog."))  # "the"
print(analyze_text2("Hello world! Hello Python. Python is fun."))  # "hello"
print(analyze_text2("a a a b b c"))  # "a"
print(analyze_text2("Numbers123 and letters456 should be treated as words."))  # "numbers123"