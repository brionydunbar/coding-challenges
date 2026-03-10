"""
Have the function ShortestPath(strArr) take strArr which will be an array of strings which models a non-looping Graph.
The structure of the array will be as follows:
The first element in the array will be the number of nodes N (points) in the array as a string.
The next N elements will be the nodes which can be anything (A, B, C .. Brick Street, Main Street .. etc.).
Then after the Nth element, the rest of the elements in the array will be the connections between all of the nodes.
They will look like this: (A-B, B-C .. Brick Street-Main Street .. etc.).
Although, there may exist no connections at all.

An example of strArr may be: ["4","A","B","C","D","A-B","B-D","B-C","C-D"].
Your program should return the shortest path from the first Node to the last Node in the array separated by dashes.
So in the example above the output should be A-B-D. Here is another example with strArr being ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"].
The output for this array should be A-E-D-F-G.
There will only ever be one shortest path for the array.
If no path between the first and last node exists, return -1.
The array will at minimum have two nodes.
Also, the connection A-B for example, means that A can get to B and B can get to A.

Examples:
Input: ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"]
Output: A-C-D-F

Input: ["4","X","Y","Z","W","X-Y","Y-Z","X-W"]
Output: X-W
"""

from collections import deque

def ShortestPath(strArr):
  # number of nodes
  N = int(strArr[0])
  nodes = strArr[1:N+1] # node names
  edges = strArr[N+1:] # connections

  # build adjacency list
  graph = {}
  for node in nodes:
    graph[node] = []

  for edge in edges:
    a, b = edge.split("-") # split edge into two nodes
    # add b as neighbour of a
    graph[a].append(b)
    # add a as neighbour of b
    graph[b].append(a) # undirected graph

  start, end = nodes[0], nodes[-1] # start and end nodes

  # BFS to find shortest path
  queue = deque([[start]]) # store paths
  visited = set([start]) # track visited nodes

  while queue:
    path = queue.popleft() # get first path
    node = path[-1] # current node is last in path

    if node == end: # if target reached, return path
      return "-".join(path)

    # explore neighbours
    for neighbour in graph[node]:
      if neighbour not in visited:
        visited.add(neighbour) # mark neighbour as visited
        queue.append(path + [neighbour]) # append new path to queue

  return -1 # no path found

# keep this function call here
# print(ShortestPath(input()))

# Testing:
arr1 = ["5","A","B","C","D","F","A-B","A-C","B-C","C-D","D-F"] # "A-C-D-F"
arr2 = ["4","X","Y","Z","W","X-Y","Y-Z","X-W"] # "X-W"
arr3 = ["7","A","B","C","D","E","F","G","A-B","A-E","B-C","C-D","D-F","E-D","F-G"] # "A-E-D-F-G"
arr4 = ["4","A","B","C","D","A-B","B-D","B-C","C-D"] # "A-B-D"

print(ShortestPath(arr1))
print(ShortestPath(arr2))
print(ShortestPath(arr3))
print(ShortestPath(arr4))