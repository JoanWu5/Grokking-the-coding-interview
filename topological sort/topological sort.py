# Topological Sort of a directed graph (a graph with unidirectional edges) is a linear ordering of its vertices 
# such that for every directed edge (U, V) from vertex U to vertex V, U comes before V in the ordering.

# Given a directed graph, find the topological ordering of its vertices.

# Example:
# Input: Vertices=4, Edges=[3, 2], [3, 0], [2, 0], [2, 1]
# Output: Following are the two valid topological sorts for the given graph:
# 1) 3, 2, 0, 1
# 2) 3, 2, 1, 0

# O(V + E) space: O(V + E)
from collections import deque


def toposort(vertices, edges):
    sorted_order = []
    if vertices <= 0:
        return sorted_order
    
    indegree = dict()
    graph = dict()

    for i in range(vertices):
        indegree[i] = 0
        graph[i] = []
    
    for i in range(len(edges)):
        parent, child = edges[i][0], edges[i][1]
        graph[parent].append(child)
        indegree[child] += 1
    
    sources = deque()
    for key, value in indegree.items():
        if value == 0:
            sources.append(key)
    
    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        children = graph[vertex]
        for child in children:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
    
    if len(sorted_order) != vertices:
        return []
    
    return sorted_order

print(toposort(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
print(toposort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]]))
print(toposort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]]))

# follow up
# Find if a given Directed Graph has a cycle in it or not.
# Solution: If we can’t determine the topological ordering of all the vertices of a directed graph, 
# the graph has a cycle in it. This was also referred to in the above code:
# if len(sorted_order) != vertices: return []