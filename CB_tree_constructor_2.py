"""
Have the function TreeConstructorTwo(strArr) take the array of strings stored in strArr, which will contain pairs of integers in the following format: (i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1.
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:

    4
   /
  2
 /\
1  7

which you can see forms a proper binary tree.
Your program should, in this case, return the string true because a valid binary tree can be formed.
If a proper binary tree cannot be formed with the integer pairs, then return the string false.
All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.

Examples:
Input: ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"]
Output: true

Input: ["(1,2)", "(1,3)"]
Output: false
"""


def TreeConstructorTwo(strArr):
    if not strArr:  # empty tree valid
        return "true"

    # build dictionaries
    child_to_parent = {}
    parent_to_children = {}
    nodes = set()

    # parse pairs
    for pair in strArr:
        pair = pair.strip("()")
        child, parent = map(int, pair.split(","))
        nodes.add(child)
        nodes.add(parent)

        # validate constraints
        # each child at most one parent
        # check if child already has a parent
        if child in child_to_parent:
            return "false"
        child_to_parent[child] = parent

        # add child to parent's children set
        if parent not in parent_to_children:
            parent_to_children[parent] = set()
        parent_to_children[parent].add(child)

        # each parent no more than 2 children
        if len(parent_to_children[parent]) > 2:
            return "false"

    # find root candidate - node with no parent
    root_candidates = nodes - set(child_to_parent.keys())
    if len(root_candidates) != 1:
        return "false"
    root = root_candidates.pop()

    # no cycles (check using dfs)
    visited = set()

    def dfs(node):
        if node in visited:
            return False  # cycle detected
        visited.add(node)
        for child in parent_to_children.get(node, []):
            if not dfs(child):
                return False
        return True

    if not dfs(root):
        return "false"

    if visited != nodes:
        return "false"

    return "true"


# keep this function call here
print(TreeConstructorTwo(input()))

"""
# Testing:
arr1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] # "true"
arr2 = ["(1,2)", "(1,3)"] # "false"
arr3 = ["(1,2)", "(2,4)", "(7,2)"] # "true"
arr4 = [] # "true"
arr5 = ["(1,2)", "(2,3)", "(3,1)", "(5,4)"] # "false"

print(TreeConstructorTwo(arr1))
print(TreeConstructorTwo(arr2))
print(TreeConstructorTwo(arr3))
print(TreeConstructorTwo(arr4))
print(TreeConstructorTwo(arr5))
"""