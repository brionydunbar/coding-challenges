"""
Have the function TreeConstructor(strArr) take the array of strings stored in strArr,
which will contain pairs of integers in the following format:
(i1,i2), where i1 represents a child node in a tree and the second integer i2 signifies that it is the parent of i1.
For example: if strArr is ["(1,2)", "(2,4)", "(7,2)"], then this forms the following tree:
      4
     /
    2
  /   \
 1     7

which you can see forms a proper binary tree.
Your program should, in this case, return the string true because a valid binary tree can be formed.
If a proper binary tree cannot be formed with the integer pairs, then return the string false.
All of the integers within the tree will be unique, which means there can only be one node in the tree with the given integer value.
"""

def TreeConstructor(strArr):
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
    # exactly one root
  root_candidates = nodes - set(child_to_parent.keys())
  if len(root_candidates) != 1:
    return "false"
    # no cycles (not needed here, all unique ints)

  return "true"

# keep this function call here
print(TreeConstructor(input()))

"""
# Testing:
arr1 = ["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"] # "true"
arr2 = ["(1,2)", "(3,2)", "(2,12)", "(5,2)"] # "false"
arr3 = ["(1,2)", "(2,4)", "(7,2)"] # "true"

print(TreeConstructor(arr1))
print(TreeConstructor(arr2))
print(TreeConstructor(arr3))
"""