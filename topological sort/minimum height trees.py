# We are given an undirected graph that has characteristics of a k-ary tree. 
# In such a graph, we can choose any node as the root to make a k-ary tree. 
# The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT). 
# There can be multiple MHTs for a graph. 
# In this problem, we need to find all those roots which give us MHTs. 
# Write a method to find all MHTs of the given graph and return a list of their roots.

# Example:
# Input: vertices: 5, Edges: [[0, 1], [1, 2], [1, 3], [2, 4]]
# Output:[1, 2]
# Explanation: Choosing '1' or '2' as roots give us MHTs. In the below diagram, 
# we can see that the height of the trees with roots '1' or '2' is three which is minimum.

# O(V + E) space: O(V + E)
from collections import deque

def minimum_height_trees(vertices, edges):
    if vertices <= 0:
        return []
    
    if vertices == 1:
        return [0]
    
    indegree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        graph[child].append(parent)
        indegree[parent] += 1
        indegree[child] += 1

    leaves = deque()
    for key, value in indegree.items():
        if value == 1:
            leaves.append(key)

    total_nodes = vertices
    while total_nodes > 2:
        leave_size = len(leaves)
        total_nodes -= leave_size
        for _ in range(leave_size):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                indegree[child] -= 1
                if indegree[child] == 1:
                    leaves.append(child)
    
    return list(leaves)

print(minimum_height_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]]))
print(minimum_height_trees(4, [[0, 1], [0, 2], [2, 3]]))
print(minimum_height_trees(4, [[0, 1], [1, 2], [1, 3]]))