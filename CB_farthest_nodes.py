"""
Have the function FarthestNodes(strArr) read strArr which will be an array of hyphenated letters representing paths between those two nodes.
For example: ["a-b","b-c","b-d"] means that there is a path from node a to b (and b to a), b to c, and b to d.
Your program should determine the longest path that exists in the graph and return the length of that path.
So for the example above, your program should return 2 because of the paths a-b-c and d-b-c.
The path a-b-c also means that there is a path c-b-a.
No cycles will exist in the graph and every node will be connected to some other node in the graph.

Examples:
Input: ["b-e","b-c","c-d","a-b","e-f"]
Output: 4

Input: ["b-a","c-e","b-c","d-c"]
Output: 3
"""

from collections import deque

def FarthestNodes(strArr):
  # build adjacency list
  graph = {}
  for edge in strArr:
    a, b = edge.split("-")
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a) # undirected graph

  # BFS helper function to return farthest node and distance
  def bfs(start):
    visited = set([start])
    queue = deque([(start, 0)]) # store (node, distance)
    farthest_node = start
    max_dist = 0

    while queue:
      node, dist = queue.popleft()
      if dist > max_dist: # update farthest
        farthest_node = node
        max_dist = dist
      for neighbour in graph[node]: # explore all neighbours
        if neighbour not in visited:
          visited.add(neighbour)
          queue.append((neighbour, dist + 1))

    return farthest_node, max_dist

  # run BFS twice for start and end
  # pick any starting node
  start_node = next(iter(graph)) # grab first key from graph
  # first BFS - find farthest from start
  far_from_start, temp_dist = bfs(start_node)
  # second BFS - find farthest distance from far node
  farthest_node, longest_path = bfs(far_from_start)

  return longest_path


# keep this function call here
# print(FarthestNodes(input()))

# Testing
arr1 = ["b-e","b-c","c-d","a-b","e-f"] # 4
arr2 = ["b-a","c-e","b-c","d-c"] # 3
arr3 = ["a-b","b-c","b-d"] # 2

print(FarthestNodes(arr1))
print(FarthestNodes(arr2))
print(FarthestNodes(arr3))