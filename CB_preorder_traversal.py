"""
Have the function PreorderTraversal(strArr) take the array of strings stored in strArr, which will represent a binary tree with integer values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #.
Your goal is to return the pre-order traversal of the tree with the elements separated by a space.
For example: if strArr is ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] then this tree looks like the following tree:
        5
       / \
      2   6
     /\    \
    1  9    8
           /
          4

For the input above, your program should return the string 5 2 1 9 6 8 4 because that is the pre-order traversal of the tree.

Examples:
Input: ["4", "1", "5", "2", "#", "#", "#"]
Output: 4 1 2 5

Input: ["2", "6", "#"]
Output: 2 6
"""

def PreorderTraversal(strArr):
  res = []
  n = len(strArr)

  def dfs(i): # start at 0 (when called)
    if i >= n:
      return
    if strArr[i] != "#": # visit this node if not null
      res.append(strArr[i])
    # left child index - map between array and BT
    left = 2*i + 1
    # right child index
    right = 2*i + 2

    # if left is # but right slot exists
    # traverse right first so nodes under right sibling appear before descendants under the empty left slot
    if left < n and strArr[left] == "#" and right < n: # preorder: root -> left -> right
      dfs(right) # visit right first if left is null
      dfs(left)
    else:
      dfs(left)
      dfs(right)

  if n > 0:
    dfs(0) # start at 0
  return " ".join(res)


# keep this function call here
# print(PreorderTraversal(input()))


# Testing:
arr1 = ["4", "1", "5", "2", "#", "#", "#"] # "4 1 2 5"
arr2 = ["2", "6", "#"] # "2 6"
arr3 = ["5", "2", "6", "1", "9", "#", "8", "#", "#", "#", "#", "4", "#"] # "5 2 1 9 6 8 4"
arr4 = ["5", "2", "6", "1", "9", "#", "8", "2", "12", "#", "#", "#", "#", "#", "99"] # "5 2 1 2 12 9 6 8 99"
arr5 = ["1", "#", "2", "#", "#", "#", "3"] # "1 2 3"


print(PreorderTraversal(arr1))
print(PreorderTraversal(arr2))
print(PreorderTraversal(arr3))
print(PreorderTraversal(arr4))
print(PreorderTraversal(arr5))


