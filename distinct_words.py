"""
You are given n words. Some words may repeat. For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.

Input Format
The first line contains the integer, n.
The next n lines each contain a word.

Output Format
Output 2 lines.
On the first line, output the number of distinct words from the input.
On the second line, output the number of occurrences for each distinct word according to their appearance in the input.

Sample Input
4
bcdef
abcdefg
bcde
bcdef

Sample Output
3
2 1 1

Explanation
There are 3 distinct words.
Here, "bcdef" appears twice in the input at the first and last positions.
The other words appear once each.
The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.
"""

def distinct_words(input):
    words = []
    input = input.split()
    for word in input:
        if word.isdigit():
            continue
        else:
            words.append(word)
    distinct_words = set()
    for word in words:
        distinct_words.add(word)
    num_distinct_words = len(distinct_words)
    print(num_distinct_words)

    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    values_list = list(word_counts.values())
    print(*values_list)

distinct_words("5\n"
                "bcdef\n"
                "abcdefg\n"
                "bcde\n"
                "bcdef\n"
               "bcdefg")


# BETTER (actually works on HackerRank)

n = int(input())

word_counts = {}
for _ in range(n):
    word = input().strip()
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(len(word_counts))
print(*word_counts.values())