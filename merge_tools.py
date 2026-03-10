"""
Consider the following:

A string, s, of length n where s = C0C1...Cn-1
An integer, k, where k is a factor of n.
We can split s into n/k substrings where each substring, Ti, consists of a contiguous block of k characters in s.
Then, use each Ti to create string Ui such that:

The characters in Ui are a subsequence of the characters in Ti.
Any repeat occurrence of a character is removed from the string such that each character in Ui occurs exactly once.
In other words, if the character at some index j in Ti occurs at a previous index < j in Ti, then do not include the character in string Ui.
Given s and k, print n/k lines where each line i denotes string Ui.

e.g. s="AAABCADDE"
k = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so U1 = "A".
The second substring has all distinct characters, so U2 = "BCA".
The third substring has 2 different characters, so U3 = "DE".
Note that a subsequence maintains the original order of characters encountered.
The order of characters in each subsequence shown is important.

Complete the merge_the_tools function with the parameters:
string s - the string to analyse
int k - the size of the substrings to analyse

Print each substring on a new line.
There will be n/k of them. No return value is expected
"""

def merge_the_tools(string, k):
    while string: # continues while string not empty
        seen = ""
        s = string[0:k] # s is the next substring of length k
        for char in s: # remove duplicates
            if char not in seen:
                seen += char
        print(seen) # prints the processed substring
        string = string[k:] # removes first k characters from string to move to next chunk

merge_the_tools("AAABCADDE", 3)
merge_the_tools("AABCAAADA", 3)
merge_the_tools("AABCAAADA", 4)