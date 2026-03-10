"""
Have the function HistogramArea(arr) read the array of non-negative integers stored in arr which will represent the heights of bars on a graph (where each bar width is 1), and determine the largest area underneath the entire bar graph.
For example: if arr is [2, 1, 3, 4, 1] then this looks like the following bar graph:



You can see in the above bar graph that the largest area underneath the graph is covered by the x's.
The area of that space is equal to 6 because the entire width is 2 and the maximum height is 3, therefore 2 * 3 = 6.
Your program should return 6.
The array will always contain at least 1 element.

Examples:
Input: [6, 3, 1, 4, 12, 4]
Output: 12

Input: [5, 6, 7, 4, 1]
Output: 16
"""

def HistogramArea(arr):
  n = len(arr)
  stack = []
  result = 0

  for i in range(n):
    # process stack while current element smaller than corresponding element to top of stack
    while stack and arr[stack[-1]] >= arr[i]:
      # popped item to be considered as smallest element of histogram
      tp = stack.pop()
      # for popped item, previous smaller element is just below it in the stack and next smaller element is i
      width = i if not stack else i - stack[-1] - 1
      # update result if needed
      result = max(result, arr[tp] * width)
    stack.append(i)

  # for remanining items, next smaller does not exist - previous smaller is item just below in stack
  while stack:
    tp = stack.pop()
    width = n if not stack else n - stack[-1] - 1
    result = max(result, arr[tp] * width)

  return result

# keep this function call here
# print(HistogramArea(input()))

# Testing:
arr1 = [6, 3, 1, 4, 12, 4] # 12
arr2 = [5, 6, 7, 4, 1] # 16
arr3 = [2, 1, 3, 4, 1] # 6

print(HistogramArea(arr1))
print(HistogramArea(arr2))
print(HistogramArea(arr3))