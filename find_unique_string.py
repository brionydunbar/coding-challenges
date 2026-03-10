"""
There is an array of strings. All strings contain similar letters except one. Try to find it!

find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters. E.g. string that contains only spaces is like empty string.

It’s guaranteed that array contains more than 2 strings.
"""

def find_uniq(arr):
    sets = []
    for st in arr:
        sets.append(set(st.lower())) # build sets of chars
    for i in range(len(sets)):
        count = 0 # manually count how many times each set appears
        for j in range(len(sets)):
            if sets[i] == sets[j]:
                count += 1
        if count == 1: # this is the unique one
            return arr[i]

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])) # BbBb
print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])) #foo


# To optimise for huge arrays
def find_uniq2(arr):
    frequency = {} # initialise empty dictionary to count unique set of chars across all strings
    for st in arr:
        chars = set()
        for char in st:
            chars.add(char.lower()) # build set of lowercase
        chars = frozenset(chars) # freezes the set - makes it hashable

        if chars in frequency:
            frequency[chars] += 1 # adds one to frequency for that key
        else:
            frequency[chars] = 1 # keeps as 1

    # now find the unique one
    for st in arr:
        chars = set()
        for char in st:
            chars.add(char.lower()) # build the set for each string
        chars = frozenset(chars)

        if frequency[chars] == 1: # check if it appears once in frequency
            return st

print(find_uniq2([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])) # BbBb
print(find_uniq2([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])) #foo