###################################################################
# 3. Add strings

# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Notes:
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.

def solution3(num1, num2): # this one is a bit cheaty
    return str(eval(num1) + eval(num2))



def solution4(num1, num2):
    n1, n2 = 0, 0
    m1, m2 = 10 ** (len(num1) - 1), 10 ** (len(num2) - 1)

    for i in num1:
        n1 += (ord(i) - ord("0")) * m1
        m1 = m1 // 10

    for i in num2:
        n2 += (ord(i) - ord("0")) * m2
        m2 = m2 // 10

    return str(n1 + n2)


num1 = '257'
num2 = '2754'

print(solution3(num1, num2))
print(solution4(num1, num2))