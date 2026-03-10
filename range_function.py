"""
Create range generator function that will take up to 3 parameters - start value, step and stop value.
This function should return an iterable object with numbers.
For simplicity, assume all parameters to be positive numbers.

Examples:

range(5) --> 1,2,3,4,5
range(3, 7) --> 3,4,5,6,7
range(2, 3, 15) --> 2,5,8,11,14
"""

def range_function(*args):
    num_args = len(args)
    if num_args == 1: # only stop
        start = 1
        step = 1
        stop = args[0]
    elif num_args == 2: # start and stop
        start = args[0]
        step = 1
        stop = args[1]
    elif num_args == 3: # start, step and stop
        start, step, stop = args
    else:
        raise TypeError("range_function expected at most 3 arguments, got {}".format(num_args))

    current = start
    while current <= stop:
        yield current
        current += step

for n in range_function(5):
    print(n)
for n in range_function(3, 7):
    print(n)
for n in range_function(2, 3, 15):
    print(n)