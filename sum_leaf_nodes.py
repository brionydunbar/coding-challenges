"""
TASK:
To find the sum of all *leaf* nodes:

We recursively traverse through the tree.
Check if a node is a leaf node or not.

APPROACH:
- If a node is a leaf node then add its data to total.

EXAMPLE:

        1
      /   \
    2       3
   / \     /  \
 4   5    6    7
           \
            8

sum of leaf node = 4+5+8+7 = 24

Lead Nodes = current node has .left = None and .right = None
Recurse through the tree, check if the above is true, add to list
Then left nodes can be added

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class SumLeafNodes:
    # class for finding the sum of all leaf nodes of a binary tree
    def __init__(self):
        # initialise to 0
        self.total = 0

    def sum_leaf_nodes(self, root):
        # recursive function for finding the sum of all lead nodes of a binary tree
        if root is None:  # base case
            return 0
        # if root has no left child and no right child then add its data to total
        elif root.left is None and root.right is None:
            self.total += root.data
        # recursively traverse through the tree
        else:
            self.sum_leaf_nodes(root.left)
            self.sum_leaf_nodes(root.right)

        return self.total


# creating binary tree
root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.right = Node(7)
root.right.left = Node(6)
root.right.left.right = Node(8)

# creating object
obj = SumLeafNodes()
sum = obj.sum_leaf_nodes(root)

print('Sum of all leaf nodes in BT:', sum)

"""
PSEUDOCODE

START
root.sum_of_leaves()

while root.left:
    recurse
    self.data.left != None or self.data.right != None:
        leafnodes.append(self.data)

return sum(leafnodes)
END
"""