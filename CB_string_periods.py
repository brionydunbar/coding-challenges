"""
Have the function StringPeriods(str) take the str parameter being passed and determine if there is some substring K that can be repeated N > 1 times to produce the input string exactly as it appears.
Your program should return the longest substring K, and if there is none it should return the string -1.

For example: if str is "abcababcababcab" then your program should return abcab because that is the longest substring that is repeated 3 times to create the final string.
Another example: if str is "abababababab" then your program should return ababab because it is the longest substring.
If the input string contains only a single character, your program should return the string -1.

Examples:
Input: "abcxabc"
Output: -1

Input: "affedaaffed"
Output: -1
"""


def StringPeriods(strParam):
    length = len(strParam)
    for i in range(length // 2, 0, -1):
        if length % i:
            continue
        substring = strParam[0:i]
        result = substring
        repeat_number = (length // i) - 1

        for j in range(repeat_number):
            substring += result
        if substring == strParam:
            return result
    return "-1"


# keep this function call here
# print(StringPeriods(input()))

# Testing:
str1 = "abcababcababcab"  # "abcab"
str2 = "abababababab"  # "ababab"
str3 = "abcxabc"  # "-1"
str4 = "affedaaffed"  # "-1"

print(StringPeriods(str1))
print(StringPeriods(str2))
print(StringPeriods(str3))
print(StringPeriods(str4))