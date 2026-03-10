"""
Have the function SeatingStudents(arr) read the array of integers stored in arr which will be in the following format: [K, r1, r2, r3, ...] where K represents the number of desks in a classroom, and the rest of the integers in the array will be in sorted order and will represent the desks that are already occupied.
All of the desks will be arranged in 2 columns, where desk #1 is at the top left, desk #2 is at the top right, desk #3 is below #1, desk #4 is below #2, etc.
Your program should return the number of ways 2 students can be seated next to each other.
This means 1 student is on the left and 1 student on the right, or 1 student is directly above or below the other student.

For example: if arr is [12, 2, 6, 7, 11] then this classrooms looks like the following picture:
1 /2\
3  4
5 /6\
/7\ 8
9  10
/11\ 12

Based on above arrangement of occupied desks, there are a total of 6 ways to seat 2 new students next to each other.
The combinations are: [1, 3], [3, 4], [3, 5], [8, 10], [9, 10], [10, 12].
So for this input your program should return 6.
K will range from 2 to 24 and will always be an even number.
After K, the number of occupied desks in the array can range from 0 to K.

Examples:
Input: [6, 4]
Output: 4

Input: [8, 1, 8]
Output: 6
"""


def SeatingStudents(arr):
    K = arr[0]
    occupied = set(arr[1:])
    count = 0

    for i in range(1, K + 1):
        if i in occupied:  # skip for occupied desks
            continue
        # check for horizontal pair (if desk is left)
        if i % 2 != 0 and i + 1 <= K and (i + 1) not in occupied:
            count += 1
        # check for vertical pair (if desk in top row)
        if i + 2 <= K and (i + 2) not in occupied:
            count += 1

    return count


# keep this function call here
# print(SeatingStudents(input()))

# Testing:
arr1 = [6, 4]  # 4
arr2 = [8, 1, 8]  # 6
arr3 = [12, 2, 6, 7, 11]  # 6

print(SeatingStudents(arr1))
print(SeatingStudents(arr2))
print(SeatingStudents(arr3))