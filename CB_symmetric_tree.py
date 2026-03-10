"""
Have the function SymmetricTree(strArr) take the array of strings stored in strArr, which will represent a binary tree, and determine if the tree is symmetric (a mirror image of itself).
The array will be implemented similar to how a binary heap is implemented, except the tree may not be complete and NULL nodes on any level of the tree will be represented with a #.
For example: if strArr is ["1", "2", "2", "3", "#", "#", "3"] then this tree looks like the following:

        1
       /  \
      2    2
    /\     /\
   3  #   #  3

For the input above, your program should return the string true because the binary tree is symmetric.

Examples:
Input: ["4", "3", "4"]
Output: false

Input: ["10", "2", "2", "#", "1", "1", "#"]
Output: true
"""


# create tree node class
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


# build tree from heap-style array
def build_tree(arr, i=0):
  if i >= len(arr) or arr[i] == "#":  # base case
    return None
  node = TreeNode(int(arr[i]))  # create node with current value
  node.left = build_tree(arr, 2 * i + 1)  # build left child recursively
  node.right = build_tree(arr, 2 * i + 2)  # build right child recursively
  return node


# recursivee check to see if mirror
def is_mirror(left, right):
  if left is None and right is None:  # if both are None, symmetric
    return True
  # is values differ or one None, not symmetric
  if left is None or right is None:
    return False
  if left.val != right.val:
    return False
  return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)


# main function
def SymmetricTree(strArr):
  # build tree
  root = build_tree(strArr)
  # if empty, symmetric
  if root is None:
    return "true"

  return "true" if is_mirror(root.left, root.right) else "false"


# keep this function call here
print(SymmetricTree(input()))

"""
# Testing:
arr1 = ["4", "3", "4"] # "false"
arr2 = ["10", "2", "2", "#", "1", "1", "#"] # "true"
arr3 = ["1", "2", "2", "3", "#", "#", "3"]  # "true"

print(SymmetricTree(arr1))
print(SymmetricTree(arr2))
print(SymmetricTree(arr3))
"""