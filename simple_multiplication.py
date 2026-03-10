"""
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""

def simple_multiplication(number):
    if number % 2 == 0:
        return number * 8
    elif number % 2 == 1:
        return number * 9
    else:
        pass

print(simple_multiplication(2)) # multiply by 8
print(simple_multiplication(5)) # multiply by 9