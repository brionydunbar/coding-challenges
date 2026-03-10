"""
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]
"""

def digitize(n):
    array = [int(digit) for digit in str(n)]
    array.reverse()
    return array

print(digitize(35231))
print(digitize(0))


# WITHOUT LIST COMPREHENSION

def digitize2(n):
    array = []
    for digit in str(n):
        array.append(int(digit))
    array.reverse()
    return array

print(digitize2(35231))
print(digitize2(0))