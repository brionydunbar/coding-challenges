"""
Have the function BinaryTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements: the first element will be a binary tree with all unique values in a format similar to how a binary heap is implemented with NULL nodes at any level represented with a #, the second and third elements will be two different values, and your goal is to find the lowest common ancestor of these two values.

For example: if strArr is ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"] then this tree looks like the following:



For the input above, your program should return 5 because that is the value of the node that is the LCA of the two nodes with values 6 and 4. You can assume the two nodes you are searching for in the tree will exist somewhere in the tree.
Examples
Input: ["[5, 2, 6, 1, #, 8, #]", "2", "6"]
Output: 5
Input: ["[5, 2, 6, 1, #, 8, 12, #, #, #, #, #, #, 3, #]", "3", "12"]
Output: 12
"""


# create tree node class
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

# build tree using recursive indices
def build_tree(arr, i=0):
  if i >= len(arr) or arr[i] == "#":
      return None
  node = TreeNode(int(arr[i]))
  node.left = build_tree(arr, 2*i + 1)
  node.right = build_tree(arr, 2*i + 2)
  return node

# find LCA
def find_lca(root, p, q):
  if root is None:
    return None
  # if current node matches p or q, could be LCA
  if root.val == p or root.val == q:
    return root
  # recurse on left and right subtrees
  left = find_lca(root.left, p, q)
  right = find_lca(root.right, p, q)
  # if p and q in different subtrees, root is LCA
  if left and right:
    return root
  # otherwise return whichever subtree contains a node or None
  return left if left else right

# main function
def BinaryTreeLCA(strArr):
  # parse input
  arr = strArr[0].strip("[]").split(",")
  arr = [x.strip() for x in arr] # remove whitespace
  # parse target node as ints
  p = int(strArr[1])
  q = int(strArr[2])

  # build tree
  root = build_tree(arr)
  # find LCA
  lca_node = find_lca(root, p, q)
  return str(lca_node.val) # return as string

# keep this function call here
print(BinaryTreeLCA(input()))

"""
# Testing:
arr1 = ["[5, 2, 6, 1, #, 8, #]", "2", "6"] # 5
arr2 = ["[5, 2, 6, 1, #, 8, 12, #, #, #, #, #, #, 3, #]", "3", "12"] # 12
arr3 = ["[12, 5, 9, 6, 2, 0, 8, #, #, 7, 4, #, #, #, #]", "6", "4"] # 5

print(BinaryTreeLCA(arr1))
print(BinaryTreeLCA(arr2))
print(BinaryTreeLCA(arr3))
"""