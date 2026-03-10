"""
Problem: Counting Unique Connections in a Fully Connected Network

Description:
Given 'n' computers in a fully connected network, each computer connects to every other computer exactly once.
Write a function to calculate the total number of unique connections.

Example:
Input: n = 5
Output: 10 (since each computer connects with every other exactly once)


##### TESTING (There will be no testing in exam but needed for final project) #####
Additional Requirement:
Create a test suite with at least 5 test cases to verify the correctness of the function.


"""


def count_connections(n):
    unique_connections = n * (n - 1) // 2
    return unique_connections  # Implement the function here

if __name__ == "__main__":
    print(count_connections(5)) # expect to see 10

# fully connected network
# connects to every other exactly once
# unique connections

# draw the problem

# google the formula
# n * (n - 1) / 2

# use floor division // to return int instead of float
# can also use int(unique_connections) to convert to int