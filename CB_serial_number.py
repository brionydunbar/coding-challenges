"""Coderbyte - Serial Number
Have the function SerialNumber(str) take the str parameter being passed and determine
if it is a valid serial number with the following constraints:

1. It needs to contain three sets each with three digits (1 through 9) separated by a period
2. The first set of digits must add up to an even number
3. The second set of digits must add up to an odd number
4. The last digit in each set must be larger than the two previous digits in the same set

If all of the above constraints are met within the string, then your program should return the string true,
otherwise your program should return the string false
For example, if str is "224.315.218" then your program shoudld return "true"

e.g. Input "11.124.667"
Output "false"

Input "114.568.112"
Output "true"
"""

def SerialNumber(strParam):
    three_sets_three_digits = False
    if "." in strParam:
        sets = strParam.split(".")
        if len(sets) != 3:
            return "false"
        set1 = sets[0]
        set2 = sets[1]
        set3 = sets[2]
        if len(sets) == 3:
            if len(set1) == 3 and len(set2) == 3 and len(set3) == 3:
                three_sets_three_digits = True
            else:
                return "false"
        else:
            return "false"
    else:
        return "false"

    set1_even = False
    total = int(set1[0]) + int(set1[1]) + int (set1[2])
    if total % 2 == 0:
        set1_even = True
    else:
        return "false"

    set2_odd = False
    total = int(set2[0]) + int(set2[1]) + int(set2[2])
    if total % 2 == 1:
        set2_odd = True
    else:
        return "false"

    correct_last_digits = False
    if int(set1[2]) > int(set1[0]) and int(set1[2]) > int(set1[1]):
        if int(set2[2]) > int(set2[0]) and int (set2[2]) > int(set2[1]):
            if int(set3[2]) > int(set3[0]) and int(set3[2]) > int(set3[1]):
                correct_last_digits = True
            else:
                return "false"
        else:
            return "false"
    else:
        return "false"

    if three_sets_three_digits and set1_even and set2_odd and correct_last_digits:
        return "true"
    else:
        return "false"

print(SerialNumber("11.124.667"))
print(SerialNumber("114.568.112"))