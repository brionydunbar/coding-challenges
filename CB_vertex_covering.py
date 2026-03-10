"""
Have the function VertexCovering(strArr) take strArr which will be an array of length three.
The first part of the array will be a list of vertices in a graph in the form (A,B,C,...), the second part of the array will be the edges connecting the vertices in the form (A-B,C-D,...) where each edge is bidirectional.
The last part of the array will be a set of vertices in the form (X,Y,Z,...) and your program will have to determine whether or not the set of vertices given covers every edge in the graph such that every edge is incident to at least one vertex in the set.

For example: if strArr is ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(A,B)"] then the vertices (A,B) are in fact one of the endpoints of every edge in the graph, so every edge has been accounted for.
Therefore your program should return the string yes.
But, if for example the last part of the array was (C,B) then these vertices don't cover all the edges because the edge connecting A-D is left out.
If this is the case your program should return the edges given in the second part of the array that are left out in the same order they were listed, so for this example your program should return (A-D).

The graph will have at least 2 vertices and all the vertices in the graph will be connected.
The third part of the array listing the vertices may be empty, where it would only contain the parenthesis with no values within it: "()"

Examples:
Input: ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C)"]
Output: (A-B,A-D,B-D)

Input: ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z)","(Z,Y,Q)"]
Output: yes
"""

def VertexCovering(strArr):
  # vertex cover check problem
  # parse input, ignore empty case ()
  vertices = strArr[0].strip("()").split(",") if strArr[0] != "()" else []
  edges = strArr[1].strip("()").split(",") if strArr[1] != "()" else []
  # use set for 0(1) lookup
  cover_set = set(strArr[2].strip("()").split(",")) if strArr[2] != "()" else set()

  # track edges not covered
  uncovered = []

  # for each edge, check if one of its endpoints is in the cover_set
  for edge in edges:
    u, v = edge.split("-") # split from A-B
    if u not in cover_set and v not in cover_set:
      uncovered.append(edge)

  # if all edges covered, return "yes"
  if not uncovered:
    return "yes"

  # otherwise return uncovered edges in input order
  return f"({','.join(uncovered)})"

# keep this function call here
# print(VertexCovering(input()))

# Testing:
arr1 = ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(A,B)"] # "yes"
arr2 = ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,B)"] # "(A-D)"
arr3 = ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C)"] # "(A-B,A-D,B-D)"
arr4 = ["(X,Y,Z,Q)","(X-Y,Y-Q,Y-Z)","(Z,Y,Q)"] # "yes"

print(VertexCovering(arr1))
print(VertexCovering(arr2))
print(VertexCovering(arr3))
print(VertexCovering(arr4))