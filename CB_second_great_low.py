"""
Have the function SecondGreatLow(arr) take the array of numbers stored in arr and return the second lowest and second greatest numbers, respectively, separated by a space.
For example: if arr contains [7, 7, 12, 98, 106] the output should be 12 98.
The array will not be empty and will contain at least 2 numbers.
It can get tricky if there's just two numbers!

Examples:
Input: [1, 42, 42, 180]
Output: 42 42

Input: [4, 90]
Output: 90 4
"""


def SecondGreatLow(arr):
  unique_sorted = sorted(set(arr))  # get unique values in order

  # Second lowest
  if len(unique_sorted) >= 2:
    second_lowest = unique_sorted[1]
  else:
    second_lowest = unique_sorted[0]

  # Second greatest
  if len(unique_sorted) >= 2:
    second_greatest = unique_sorted[-2]
  else:
    second_greatest = unique_sorted[0]

  return f"{second_lowest} {second_greatest}"

# keep this function call here
# print(SecondGreatLow(input()))


# Testing:
arr1 = [1, 42, 42, 180] # "42 42"
arr2 = [4, 90] # "90 4"
arr3 = [7, 7, 12, 98, 106] # "12 98"

print(SecondGreatLow(arr1))
print(SecondGreatLow(arr2))
print(SecondGreatLow(arr3))
