"""
Have the function LongestConsecutive(arr) take the array of positive integers stored in arr and return the length of the longest consecutive subsequence (LCS).
An LCS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in a consecutive, increasing order.
The sequence does not need to be contiguous and there can be several different subsequences.
For example: if arr is [4, 3, 8, 1, 2, 6, 100, 9] then a few consecutive sequences are [1, 2, 3, 4], and [8, 9].
For this input, your program should return 4 because that is the length of the longest consecutive subsequence.

Examples:
Input: [6, 7, 3, 1, 100, 102, 6, 12]
Output: 2

Input: [5, 6, 1, 2, 8, 9, 7]
Output: 5
"""

def LongestConsecutive(arr):
  st = set()
  result = 0
  # hash all array elements
  for value in arr:
    st.add(value)
  # check each sequence from start and update length
  for value in arr:
    # if current element is starting element of sequence
    if value in st and (value - 1) not in st:
      # then check for next elements in sequence
      current = value
      count = 0
      while current in st:
        # remove this number
        st.remove(current)
        current += 1
        count += 1
      # update optimal length
      result = max(result, count)

  return result

# keep this function call here
# print(LongestConsecutive(input()))

# Testing:
arr1 = [6, 7, 3, 1, 100, 102, 6, 12] # 2
arr2 = [5, 6, 1, 2, 8, 9, 7] # 5
arr3 = [4, 3, 8, 1, 2, 6, 100, 9] # 4

print(LongestConsecutive(arr1))
print(LongestConsecutive(arr2))
print(LongestConsecutive(arr3))