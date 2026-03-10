"""
Simple Password Validation Challenge

Challenge:
    Write a function simple_password(password_str) that validates if a password
    meets security requirements.

Requirements:
    Your password must satisfy ALL of these conditions:

    1. Length: Between 8-30 characters (inclusive)
    2. Uppercase: Contains at least one uppercase letter (A-Z)
    3. Number: Contains at least one digit (0-9)
    4. Punctuation: Contains at least one of these symbols: . , ! ? : ;
    5. No "password": Must NOT contain the word "password" (case-insensitive)

Return Value:
    - Return "true" if password meets ALL requirements
    - Return "false" if password fails ANY requirement

Examples:
    simple_password("apple!M7")          # → "true"
    simple_password("passWord123!!!!")   # → "false" (contains "password")
    simple_password("turkey90AAA!")      # → "true"
    simple_password("short")             # → "false" (multiple failures)

"""


def simple_password(password_str):
    punctuation = [".", ",", "!", "?", ":", ";"]
    has_upper = False
    has_number = False
    has_punc = False
    for char in password_str:
        if char.isupper():
            has_upper = True
        if char.isdigit():
            has_number = True
        if char in punctuation:
            has_punc = True
        if has_upper and has_number and has_punc:
            break
    valid_length = 8 <= len(password_str) <= 30
    contains_password = "password" in password_str.lower()
    if has_upper and has_number and has_punc and valid_length and not contains_password:
        return "true"
    return "false"


print(simple_password("apple!M7")) # true
print(simple_password("passWord123!!!!")) # false
print(simple_password("turkey90AAA!")) # true
print(simple_password("short")) # false


# ALTERNATIVE SOLUTION

def simple_password2(password_str):
    # length between 8 and 30 chars inclusive
    if len(password_str) < 8 or len(password_str) > 30: # inclusive range
        return "false" # rather than doing 8 <= len(password_str) <= 30 here as this would be true
    # check for at least one uppercase letter with a flag
    has_one_upper = False
    for char in password_str:
        if char.isupper():
            has_one_upper = True
            break # break as it has found one so doesn't need to iterate anymore
    if not has_one_upper:
        return "false"
    # check it contains at least one digit 0-9
    has_one_digit = False
    for char in password_str:
        if char.isdigit():
            has_one_digit = True
            break
    if not has_one_digit:
        return "false"
    # check it contains .,!?:;
    has_one_punc = False
    for char in password_str:
        if char in ".,!?:;":
            has_one_punc = True
            break
    if not has_one_punc:
        return "false"
    # check if no "password" in text - make sure not case-sensitive
    if "password" in password_str.lower():
        return "false"
    return "true"


print(simple_password2("apple!M7")) # true
print(simple_password2("passWord123!!!!")) # false
print(simple_password2("turkey90AAA!")) # true
print(simple_password2("short")) # false