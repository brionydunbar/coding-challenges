"""
Have the function BinarySearchTreeLCA(strArr) take the array of strings stored in strArr, which will contain 3 elements:
the first element will be a binary search tree with all unique values in a preorder traversal array, the second and third elements will be two different values, and your goal is to find the lowest common ancestor of these two values.
For example: if strArr is ["[10, 5, 1, 7, 40, 50]", "1", "7"] then this tree looks like the following:
        10
       /  \
      5   40
    /\      \
   1  7     50


For the input above, your program should return 5 because that is the value of the node that is the LCA of the two nodes with values 1 and 7.
You can assume the two nodes you are searching for in the tree will exist somewhere in the tree.

Examples:
Input: ["[10, 5, 1, 7, 40, 50]", "5", "10"]
Output: 10

Input: ["[3, 2, 1, 12, 4, 5, 13]", "5", "13"]
Output: 12
"""


# set up tree node class
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# build BST from preorder
def build_bst(preorder):
    # use list so it's mutable inside recursion
    index = [0]

    def helper(lower=float("-inf"), upper=float("inf")):  # bounds
        if index[0] == len(preorder):  # stop if all values used
            return None
        val = preorder[index[0]]  # start at root
        if val < lower or val > upper:  # if value doesn't fit into valid BST range, skip
            return None
        index[0] += 1  # move to next index
        node = TreeNode(val)
        node.left = helper(lower, val)  # all left subtree vals must be < node.val
        node.right = helper(val, upper)  # all right subtree valls must be > node.vl
        return node

    return helper()


# find LCA in BST
def find_lca(root, p, q):
    while root:
        if p < root.val and q < root.val:  # if both smaller than root, go left
            root = root.left
        elif p > root.val and q > root.val:  # if both greater than root, go right
            root = root.right
        else:
            return root
    return None


# main function
def BinarySearchTreeLCA(strArr):
    # parse preorder string into list of ints
    preorder = list(map(int, strArr[0].strip("[]").split(",")))
    # parse p and q as ints
    p, q = int(strArr[1]), int(strArr[2])
    # build BST from preorder
    root = build_bst(preorder)
    # find LCA
    lca_node = find_lca(root, p, q)
    return str(lca_node.val)  # return as string


# keep this function call here
print(BinarySearchTreeLCA(input()))

"""
# Testing:
arr1 = ["[10, 5, 1, 7, 40, 50]", "5", "10"] # 10
arr2 = ["[3, 2, 1, 12, 4, 5, 13]", "5", "13"] # 12
arr3 = ["[10, 5, 1, 7, 40, 50]", "1", "7"] # 5

print(BinarySearchTreeLCA(arr1))
print(BinarySearchTreeLCA(arr2))
print(BinarySearchTreeLCA(arr3))
"""