"""
Have the function SwapII(str) take the str parameter and swap the case of each character.
Then, if a letter is between two numbers (without separation), switch the places of the two numbers.
For example: if str is "6Hello4 -8World, 7 yes3" the output should be 4hELLO6 -8wORLD, 7 YES3.

Examples:
Input: "Hello -5LOL6"
Output: hELLO -6lol5

Input: "2S 6 du5d4e"
Output: 2s 6 DU4D5E
"""

def SwapII(strParam):
  chars = list(strParam)
  n = len(chars)
  i = 0

  while i < n:
    if chars[i].isalpha():
    # Start of a letter block
      start = i
      while i < n and chars[i].isalpha():
        # Swap case on the fly
        chars[i] = chars[i].upper() if chars[i].islower() else chars[i].lower()
        i += 1
      end = i - 1  # last letter index

      # Swap surrounding digits if they exist
      if start > 0 and end < n - 1:
        if chars[start - 1].isdigit() and chars[end + 1].isdigit():
          chars[start - 1], chars[end + 1] = chars[end + 1], chars[start - 1]
    else:
      i += 1

  return ''.join(chars)


# keep this function call here
# print(SwapII(input()))

# Testing:
str1 = "Hello -5LOL6" # "hELLO - 6lol5"
str2 = "2S 6 du5d4e" # "2s 6 DU4D5E"
str3 = "6Hello4 -8World, 7 yes3" # "4hELLO6 -8wORLD, 7 YES3"

print(SwapII(str1))
print(SwapII(str2))
print(SwapII(str3))