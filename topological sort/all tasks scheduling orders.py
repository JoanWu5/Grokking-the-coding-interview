# There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. 
# Each task can have some prerequisite tasks which need to be completed before it can be scheduled. 
# Given the number of tasks and a list of prerequisite pairs, 
# write a method to print all possible ordering of tasks meeting all prerequisites.

# Example:
# Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
# Output: 
# 1) [3, 2, 0, 1]
# 2) [3, 2, 1, 0]
# Explanation: There are two possible orderings of the tasks meeting all prerequisites.

# O(V! * E) space: O(V! * E)
from collections import deque

def tasks_scheduling_order(tasks, prerequisites):
    if tasks <= 0:
        return ""
    
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

    result = []
    print_all_toposort(graph, indegree, sources, [],result)
    return result

def print_all_toposort(graph, indegree, sources, sorted_order,result):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)
            sources_for_next_call.remove(vertex)
            
            for child in graph[vertex]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    sources_for_next_call.append(child)
            
            print_all_toposort(graph, indegree, sources_for_next_call, sorted_order, result)

            sorted_order.remove(vertex)
            for child in graph[vertex]:
                indegree[child] += 1
    
    if len(sorted_order) == len(indegree):
        result.append(list(sorted_order))

print(tasks_scheduling_order(4, [[3, 2], [3, 0], [2, 0], [2, 1]]))
print(tasks_scheduling_order(3, [[0, 1], [1, 2]]))
result = tasks_scheduling_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
print(result, len(result))