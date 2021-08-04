# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
# Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
# Given the number of tasks and a list of prerequisite pairs, 
# write a method to find the ordering of tasks we should pick to finish all tasks.

# Example:
# Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
# Output: [0, 1, 2]
# Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
# before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 

# O(V + E) space: O(V + E)
from collections import deque

def tasks_scheduling_order(tasks, prerequisites):
    if tasks <= 0:
        return []
    
    indegree = dict()
    graph = dict()

    for i in range(tasks):
        indegree[i] = 0
        graph[i] = []
    
    for i in range(len(prerequisites)):
        parent, child = prerequisites[i][0], prerequisites[i][1]
        graph[parent].append(child)
        indegree[child] += 1
    
    sources = deque()
    for key, value in indegree.items():
        if value == 0:
            sources.append(key)

    order = []

    while sources:
        parent = sources.popleft()
        order.append(parent)
        children = graph[parent]
        for child in children:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
    
    if len(order) != tasks:
        return []
    
    return order

print(tasks_scheduling_order(3, [[0, 1], [1, 2]]))
print(tasks_scheduling_order(3, [[0, 1], [1, 2], [2, 0]]))
print(tasks_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]]))