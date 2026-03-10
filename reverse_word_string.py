"""
Please write a function that accepts a string of words separated by one or more whitespaces.
The function must return a string that has these words in reverse order

Quick example:
“Coding is great” → “great is coding”

• A word can contain special characters, punctuation and numbers.
• The input string is not guaranteed to always contain words
• If  the  words  in  the  original  string  were  separated  by  one  or  more  whitespaces,  then  the
reversed string must contain the same whitespaces as the original one:
Quick example:
“Whitespaces     5” → “5     Whitespaces”

VERY IMPORTANT:
• You are NOT allowed to use in-build functions or methods such as “split” or “reverse”
• You ARE allowed to use join method/function


Sample Input
    String = "CFG is awesome!"
Sample Output
 “awesome! Is CFG”
"""

def reverse_words_string(input_string):
    split_string = []
    temp_word = ""
    for char in input_string:
        if char != " ": # if char is not space
            temp_word += char # add char to current word
        else:
            split_string.append(temp_word) # add word to result
            split_string.append(char) # add space as separate element
            temp_word = "" # result temp word
    if temp_word: # add list word if it exists
        split_string.append(temp_word)
    reversed_list = split_string[::-1] # reverse the new list
    reversed_string = "".join(reversed_list) # convert to string
    return reversed_string


# Testing
str1 = "CFG is awesome!" # "awesome! is CFG"
str2 = "APPLE PEAR PLUM ORANGE" # "ORANGE PLUM PEAR APPLE"
str3 = "1 12 23 34 56" # "56 34 23 12 1"
str4 = "this-is-one-word" # "this-is-one-word"
str5 = "this      string     has a     lot of   whitespace" # "whitespace   of lot     a has     string      this"

print(reverse_words_string(str1))
print(reverse_words_string(str2))
print(reverse_words_string(str3))
print(reverse_words_string(str4))
print(reverse_words_string(str5))