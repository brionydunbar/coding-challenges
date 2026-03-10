"""
Have the function NumberSearch(str) take the str parameter, search for all the numbers in the string, add them together, then return that final number divided by the total amount of letters in the string.
For example: if str is "Hello6 9World 2, Nic8e D7ay!" the output should be 2.
First if you add up all the numbers, 6 + 9 + 2 + 8 + 7 you get 32.
Then there are 17 letters in the string.
32 / 17 = 1.882, and the final answer should be rounded to the nearest whole number, so the answer is 2.
Only single digit numbers separated by spaces will be used throughout the whole string (So this won't ever be the case: hello44444 world).
Each string will also have at least one letter.

Examples:
Input: "H3ello9-9"
Output: 4

Input: "One Number*1*"
Output: 0
"""


def NumberSearch(strParam):
    nums = []
    letters = []
    for char in strParam:
        if char.isdigit():
            num = int(char)
            nums.append(num)
        elif char.isalpha():
            letters.append(char)
        else:
            continue
    length = len(letters)
    total = sum(nums)
    final_number = total / length
    if final_number - int(final_number) == 0.5:
        return int(final_number) + 1
    else:
        rounded = round(final_number)
        return rounded


# keep this function call here
# print(NumberSearch(input()))


# Testing:
str1 = "H3ello9-9"  # 4
str2 = "One Number*1*"  # 0
str3 = "Hello6 9World 2, Nic8e D7ay!"  # 2
str4 = "3ko6"  # 5

print(NumberSearch(str1))
print(NumberSearch(str2))
print(NumberSearch(str3))
print(NumberSearch(str4))