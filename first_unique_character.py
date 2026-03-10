# 4. First unique character

# Given an input string, find the first non-repeating character

def solution5(s):
    unique = [ch for ch in s if s.count(ch) == 1]
    return unique[0]

s = 'aabccbdcbe'

print(solution5(s))



def solution6(s):
    return (ch for ch in s if s.count(ch == 1).__next__())

print(solution6(s))