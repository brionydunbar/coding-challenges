###################################################################
# 5. Monotonic Array

# Given an array of integers, determine whether the array is monotonic or not.

"""
An array is monotonic if and only if it is monotone increasing, or monotone decreasing
"""

def solution7(nums):
    x, y = [], [] # copy the array into two different arrays with extend()
    x.extend(nums)
    y.extend(nums)
    x.sort() # sort first array in ascending order to check if nums matches monotonic increasing
    y.sort(reverse=True) # sort second array in descending order to check if nums matches monotonic decreasing
    if x == nums or y == nums:
        return True
    return False


A = [100, 6, 5, 4, 4]
B = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
C = [1, 1, 2, 3, 7, 11, 22]

print(solution7(A)) # True
print(solution7(B)) # False
print(solution7(C)) # True


def solution8(nums):
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or (all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1)))

print(solution8(A)) # True
print(solution8(B)) # False
print(solution8(C)) # True