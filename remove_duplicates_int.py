"""
Remove the duplicates from a list of integers, keeping the last (rightmost) occurrence of each element.

Example:
For input: [3, 4, 4, 3, 6, 3]

remove the 3 at index 0
remove the 4 at index 1
remove the 3 at index 3
Expected output: [4, 6, 3]
"""

def solve(arr):
    duplicates = []
    for i in arr:
        if i not in duplicates:
            duplicates.append(i)
        else:
            del duplicates[duplicates.index(i)]
            duplicates.append(i)
    return duplicates

print(solve([3, 4, 4, 3, 6, 3])) # [4, 6, 3]