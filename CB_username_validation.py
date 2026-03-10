"""
Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine if the string is a valid username according to the following rules:

1. The username is between 4 and 25 characters.
2. It must start with a letter.
3. It can only contain letters, numbers, and the underscore character.
4. It cannot end with an underscore character.

If the username is valid then your program should return the string true, otherwise return the string false.
Examples
Input: "aa_"
Output: false
Input: "u__hello_world123"
Output: true
"""

def CodelandUsernameValidation(strParam):

    is_valid_length = False
    if 4 <= len(strParam) <= 25:
        is_valid_length = True
    else:
        return "false"

    letter_start = False
    if strParam[0].isalpha():
        letter_start = True
    else:
        return "false"

    correct_chars = False
    for char in strParam:
        if char.isalpha() or char.isdigit() or char == "_":
            correct_chars = True
        else:
            return "false"

    correct_end = False
    if not strParam[-1] == "_":
        correct_end = True
    else:
        return "false"

    if is_valid_length and letter_start and correct_chars and correct_end:
        return "true"


print(CodelandUsernameValidation("aaa_"))
print(CodelandUsernameValidation("H3llo_w0rld"))