# 6. Move zeros

# Given an array nums, write a function to move all zeroes to the end of it while maintaining the relative order of
# the non-zero elements.

array1 = [0, 1, 0, 3, 12]  # --> should be [1, 3, 12, 0, 0]
array2 = [1, 7, 0, 0, 8, 0, 10, 12, 0, 4]  # --> should be [1, 7, 8, 10, 12, 4, 0, 0, 0, 0]

def solution9(nums):
    non_zeroes = []
    zeroes = []
    for char in nums:
        if char == 0:
            zeroes.append(char)
        else:
            non_zeroes.append(char)
    new_nums = non_zeroes + zeroes
    return new_nums

print(solution9(array1))
print(solution9(array2))


def solution10(nums):
    for i in nums:
        if 0 in nums:
            nums.remove(0)
            nums.append(0)
    return nums

print(solution10(array1))
print(solution10(array2))