"""
Have the function OffBinary(strArr) read the array of strings stored in strArr, which will contain two elements, the first will be a positive decimal number and the second element will be a binary number.
Your goal is to determine how many digits in the binary number need to be changed to represent the decimal number correctly (either 0 change to 1 or vice versa).
For example: if strArr is ["56", "011000"] then your program should return 1 because only 1 digit needs to change in the binary number (the first zero needs to become a 1) to correctly represent 56 in binary.

Examples:
Input: ["5624", "0010111111001"]
Output: 2

Input: ["44", "111111"]
Output: 3
"""


def OffBinary(strArr):
    # parse
    decimal, binary = strArr
    # convert decimal to correct binary
    correct_binary = bin(int(decimal))[2:]

    # pad with leading zeros for comparison
    max_len = max(len(correct_binary), len(binary))
    correct_binary = correct_binary.zfill(max_len)
    binary = binary.zfill(max_len)

    changes = 0
    # count mismatches
    for i in range(max_len):
        if correct_binary[i] != binary[i]:
            changes += 1

    return changes


# keep this function call here
# print(OffBinary(input()))

# Testing:
arr1 = ["5624", "0010111111001"]  # 2
arr2 = ["44", "111111"]  # 3
arr3 = ["56", "011000"]  # 1

print(OffBinary(arr1))
print(OffBinary(arr2))
print(OffBinary(arr3))