"""
Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr,
which will contain only two strings, the first parameter being the string N and the second parameter being a string K of some characters,
and your goal is to determine the smallest substring of N that contains all the characters in K.
For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters
a, e, and d is "dae" located at the end of the string.
So for this example your program should return the string dae.

Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains
all of the characters in K is "aabd" which is located at the beginning of the string.
Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters
will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.
"""

# sliding window algorithm to solve minimum window substring (smallest substring)
from collections import Counter

def MinWindowSubstring(strArr):
    N = strArr[0]
    K = strArr[1]
    k_count = Counter(K) # frequency of required characters
    need = len(k_count) # how many unique characters we need for a valid window
    window = {} # dictionary counting characters in sliding window in N
    have = 0 # how many unique characters currently match the required count
    left = right = 0
    min_len = float("inf") # keep track of smallest substring
    min_window = ""

    while right < len(N): # expand the window - adding one character at a time
        char = N[right]
        window[char] = window.get(char, 0) + 1
        if char in k_count and window[char] == k_count[char]: # if char frequency matches required frequency
            have += 1
        right += 1

        while have == need: # contract the  window - until chars we have = chars we need
            curr_len = right - left
            if curr_len < min_len:
                min_len = curr_len
                min_window = N[left:right]

            char = N[left] # shrink from left when window contains all required chars in required frequencies
            window[char] -= 1
            if char in k_count and window[char] < k_count[char]:
                have -= 1
            left += 1

    return min_window


print(MinWindowSubstring(["aaabaaddae", "aed"])) # contracts to "baadda", "aadda", "adda", "dda" then "dae"
print(MinWindowSubstring(["aabdccdbcacd", "aad"]))