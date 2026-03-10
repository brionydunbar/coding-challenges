"""
You and Fredrick are good friends. Yesterday, Fredrick received N credit cards from ABCD Bank.
He wants to verify whether his credit card numbers are valid or not.
You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4, 5, or 6.
► It must contain exactly 16 digits.
► It must only consist of digits (-).
► It may have digits in groups of 4, separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.

Examples:
Valid Credit Card Numbers
4253625879615786
4424424424442444
5122-2368-7954-3214

Invalid Credit Card Numbers
42536258796157867       #17 digits in card number → Invalid
4424444424442444        #Consecutive digits are repeating 4 or more times → Invalid
5122-2368-7954 - 3214   #Separators other than '-' are used → Invalid
44244x4424442444        #Contains non digit characters → Invalid
0525362587961578        #Doesn't start with 4, 5 or 6 → Invalid

Input Format
The first line of input contains an integer N.
The next N lines contain credit card numbers.

Output Format
Print 'Valid' if the credit card number is valid. Otherwise, print 'Invalid'.
Do not print the quotes.

Sample Input
4123456789123456
5123-4567-8912-3456
61234-567-8912-3456
4123356789123456
5133-3367-8912-3456
5123 - 3567 - 8912 - 3456

Sample Output
Valid
Valid
Invalid
Valid
Invalid
Invalid

Explanation
4123456789123456 : Valid
5123-4567-8912-3456 : Valid
61234--8912-3456 : Invalid, because the card number is not divided into equal groups of .
4123356789123456 : Valid
51-67-8912-3456 : Invalid, consecutive digits  is repeating  times.
5123456789123456 : Invalid, because space '  ' and - are used as separators.
"""

def validate_card(num):
    if " " in num:  # reject if any spaces
        return "Invalid"
    # check hyphen grouping
    correct_grouping = False
    if "-" in num:
        parts = num.split("-")
        if len(parts) == 4 and all(len(part) == 4 for part in parts):
            correct_grouping = True
        else:
            return "Invalid"
    else:  # check length
        if len(num) == 16:
            correct_grouping = True
        else:
            return "Invalid"
    # strip hyphens
    stripped_num = num.replace("-", "")
    # check all digits
    only_digits = False
    if stripped_num.isdigit():
        only_digits = True
    else:
        return "Invalid"
        # start with 4, 5 or 6
    correct_start = False
    if stripped_num[0] in "456":
        correct_start = True
    else:
        return "Invalid"
    # no 4 consecutive repeated digits
    no_4_cons_nums = False
    for i in range(len(stripped_num) - 3):
        if not stripped_num[i] == stripped_num[i + 1] == stripped_num[i + 2] == stripped_num[i + 3]:
            no_4_cons_nums = True
        else:
            return "Invalid"

    # if all true return "Valid"
    if correct_grouping and only_digits and correct_start and no_4_cons_nums:
        return "Valid"
    else:
        return "Invalid"

print(validate_card("4143-4672-8798-2968-2968"))