"""
Have the function BipartiteMatching(strArr) read strArr which will be an array of hyphenated letters representing paths from the first node to the second node.
For example: ["a->d", "a->e", "b->f", "c->e"] means that there is a path from node a to d, a to e, b to f, and so on.
The graph will be bipartite meaning that it is possible to separate the nodes into two disjoint sets such that every edge only connects a node from the lefthand side to a node on the righthand side.
Your program should determine the maximum cardinality matching of the bipartite graph, which means finding the largest possible number of non-adjacent edges that are matching.
So for the example above, your program should return 3 because it is possible to connect every single node on the left to a node on the right.

The input will only contain lowercase alphabetic characters with a -> between them signifying an edge between them going from the left node to the right node.
The input will contain at least 1 edge connecting 2 nodes.

Examples:
Input: ["a->w", "a->x", "b->x", "b->y", "c->x", "c->z", "d->w"]
Output: 4

Input: ["a->b", "c->b", "c->d", "e->b"]
Output: 2
"""


def BipartiteMatching(strArr):
    # hungarian algorithm
    # parse input into bipartite graph
    # adjacency list left -> right
    left_nodes = set()
    right_nodes = set()
    edges = []

    for edge in strArr:
        u, v = edge.split("->")
        left_nodes.add(u)
        right_nodes.add(v)
        edges.append((u, v))

    # build adjacency list for left side
    graph = {u: [] for u in left_nodes}
    for u, v in edges:
        graph[u].append(v)

    # DFS helper to find augmenting pairs
    def dfs(u, seen, matched):
        # try every neighbour of u (right nodes)
        for v in graph[u]:
            if v not in seen:
                seen.add(v)  # mark v as visited
                if v not in matched or dfs(matched[v], seen, matched):
                    matched[v] = u  # match v with u
                    return True
        return False

    # match every left node
    matched = {}  # right_node -> left_node
    result = 0
    for u in left_nodes:
        seen = set()
        if dfs(u, seen, matched):
            result += 1

    return result


# keep this function call here
print(BipartiteMatching(input()))

"""
# Testing:
arr1 = ["a->w", "a->x", "b->x", "b->y", "c->x", "c->z", "d->w"] # 4
arr2 = ["a->b", "c->b", "c->d", "e->b"] # 2
arr3 = ["a->d", "a->e", "b->f", "c->e"] # 3

print(BipartiteMatching(arr1))
print(BipartiteMatching(arr2))
print(BipartiteMatching(arr3))
"""