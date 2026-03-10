"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

Examples:

* 'abc' =>  ['ab', 'c_']
* 'abcdef' => ['ab', 'cd', 'ef']
"""

def solution(s):
    n = 2
    output = []
    for i in range(0, len(s), n): # step by n
        output.append(s[i:i+n])
    if len(s) % 2 == 1:
        output.pop()
        output.append(s[len(s)-1:] + "_")
    else:
        pass
    return output

print(solution("abcdef"))
print(solution("abcdefg"))