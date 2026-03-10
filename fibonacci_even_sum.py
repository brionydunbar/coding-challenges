"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
and return the sum of all even Fibonacci numbers.
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def even_fibonacci_sum(limit):
    fib_numbers = []
    for num in range(0, limit):
        fib_num = fib(num)
        fib_numbers.append(fib_num)
    even_fib = []
    for num in fib_numbers:
        if num % 2 == 0:
            even_fib.append(num)
        else:
            continue
    even_sum = sum(even_fib)
    return even_sum


##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0



"""
CFG code:

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def even_fibonacci_sum(limit):
    indexes = [x for x in range(limit)]
    print('indexes: ', indexes)

    even_fibs = [fibonacci(i) for i in indexes if fibonacci(i) % 2 == 0]
    print('even Fib numbers: ', even_fibs)

    return sum(even_fibs)


# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0"""