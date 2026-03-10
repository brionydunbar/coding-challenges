"""
Have the function LetterCountI(str) take the str parameter being passed and return the first word with the greatest number of repeated letters.
For example: "Today, is the greatest day ever!" should return greatest because it has 2 e's (and 2 t's) and it comes before ever which also has 2 e's.
If there are no words with repeating letters return -1.
Words will be separated by spaces.

Examples:
Input: "Hello apple pie"
Output: Hello

Input: "No words"
Output: -1

"""


def LetterCountI(strParam):
    repeats = 1  # highest number of repeats
    repeat_word = ""

    # split to individual words
    words = strParam.split()

    # loop through words
    for word in words:
        # loop through letters
        for letter in word:
            # count how many times letter appears in word
            if word.count(letter) > repeats:
                # update highest repeat count
                repeats = word.count(letter)
                # store word with repeated letter
                repeat_word = word

    if repeat_word:
        return repeat_word
    else:
        return -1


# keep this function call here
# print(LetterCountI(input()))


# Testing:
str1 = "Hello apple pie"  # "Hello"
str2 = "No words"  # -1
str3 = "Today, is the greatest day ever!"  # "greatest"

print(LetterCountI(str1))
print(LetterCountI(str2))
print(LetterCountI(str3))