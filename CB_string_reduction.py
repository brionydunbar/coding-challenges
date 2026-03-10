"""
Have the function StringReduction(str) take the str parameter being passed and return the smallest number you can get through the following reduction method.
The method is: Only the letters a, b, and c will be given in str and you must take two different adjacent characters and replace it with the third.
For example "ac" can be replaced with "b" but "aa" cannot be replaced with anything.
This method is done repeatedly until the string cannot be further reduced, and the length of the resulting string is to be outputted.

For example: if str is "cab", then "ca" can be reduced to "b" and you get "bb" (you can also reduce it to "cc").
The reduction is done so the output should be 2.
If str is "bcab", "bc" reduces to "a", so you have "aab", then "ab" reduces to "c", and the final string "ac" is reduced to "b" so the output should be 1.

Examples:
Input: "abcabc"

Output: 2
Input: "cccc"
Output: 4

"""

def StringReduction(strParam):
  n = len(strParam)
  # count occurrences of a b and c
  count = [0] * 3
  for i in range(n):
    count[ord(strParam[i]) - ord("a")] += 1
  # if all chars are same
  if (count[0] == n or count[1] == n or count[2] == n):
    return n
  # if all chars are present even or odd number of times
  if ((count[0] % 2) == (count[1] % 2) and (count[1] % 2) == (count[2] % 2)):
    return 2
  # answer is 1 for all other cases
  return 1

# keep this function call here
# print(StringReduction(input()))

# Testing:
str1 = "abcabc" # 2
str2 = "cccc" # 4
str3 = "cab" # 2
str4 = "bcab" # 1

print(StringReduction(str1))
print(StringReduction(str2))
print(StringReduction(str3))
print(StringReduction(str4))