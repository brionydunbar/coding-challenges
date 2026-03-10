"""
Given a mathematical equation that has *,+,-,/, reverse it as follows:

solve("100*b/y") = "y/b*100"
solve("a+b-c/d*30") = "30*d/c-b+a"
"""

def solve(eq):
    parts = [] # store parts of equation ready to reverse
    operand = "" # store numbers and letters preserving form
    for char in eq:
        if char in ["*", "+", "-", "/"]: # check if char in list and append to parts
            parts.append(operand)
            parts.append(char)
            operand = ""
        else:
            operand += char # if not a char in list, add the char to operand string
    if operand: # add the preserved operand to list
        parts.append(operand)
    return "".join(parts[::-1]) # reverse the list

print(solve("100*b/y"))
print(solve("a+b-c/d*30"))