"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition.
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

google would have its logo with the letters g, o, e.

Input Format
A single line of input containing the string s.

Output Format
Print the three most common characters along with their occurrence count each on a separate line.
Sort output in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.

Sample Input
aabbbccde

Sample Output
b 3
a 2
c 2

Explanation
Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c in the alphabet.
Note: The string s has at least 3 distinct characters.
"""

from collections import Counter

def top_three_chars(s):
    letter_counts = {}
    for char in s:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    letter_counts = Counter(letter_counts)
    sorted_counts = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
    top_three = sorted_counts[:3]
    for i in top_three:
        print(i[0],i[1])


top_three_chars("aabbbccde:")