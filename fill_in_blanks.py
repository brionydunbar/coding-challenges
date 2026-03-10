###################################################################
# 7. Fill in blanks

# Given an array containing None values fill in the None values with most recent
# non None value in the array


def solution11(array):
    valid = 0
    res = []
    for i in array:
        if i is not None:
            res.append(i)
            valid = i
        else:
            res.append(valid)
    return res

array1 = [1, None, 2, 3, None, None, 5, None]

print(solution11(array1)) # [1, 1, 2, 3, 3, 3, 5, 5]

