"""
You are given a string S.
S contains alphanumeric characters only.
Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format
A single line of input contains the string S.

Output Format
Output the sorted string S.

Sample Input
Sorting1234

Sample Output
ginortS1324
"""

def string_sort(string):
    string_list = []
    lowercase = []
    for char in string:
        if char.islower():
            lowercase.append(char)
        else:
            continue
    lowercase = sorted(lowercase)
    uppercase = []
    for char in string:
        if char.isupper():
            uppercase.append(char)
    uppercase = sorted(uppercase)
    digits = []
    for char in string:
        if char.isdigit():
            digits.append(char)
        else:
            continue
    digits = sorted(digits)
    odd_even_digits = []
    for digit in digits:
        if int(digit) % 2 == 1:
            odd_even_digits.append(digit)
        else:
            continue
    for digit in digits:
        if int(digit) % 2 == 0:
            odd_even_digits.append(digit)
    string_list = lowercase + uppercase + odd_even_digits
    new_string = "".join(string_list)
    return new_string

print(string_sort("Sorting1234"))