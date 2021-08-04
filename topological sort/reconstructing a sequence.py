# Given a sequence originalSeq and an array of sequences, 
# write a method to find if originalSeq can be uniquely reconstructed from the array of sequences.

# Unique reconstruction means that we need to find if originalSeq is the only sequence 
# such that all sequences in the array are subsequences of it.

# Example:
# Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
# Output: true
# Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct   
# [1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers in the 'originalSeq'. 

# O(V + N) space: O(V + N)
from collections import deque


def can_construct(original_seq, seqs):
    sorted_order = []
    if len(original_seq) <= 0:
        return False
    
    indegree = dict()
    graph = dict()
    for seq in seqs:
        for num in seq:
            indegree[num] = 0
            graph[num] = []
    
    for seq in seqs:
        for i in range(1, len(seq)):
            parent, child = seq[i - 1], seq[i]
            graph[parent].append(child)
            indegree[child] += 1
    
    if len(indegree) != len(original_seq):
        return False
    
    sources = deque()
    for key, value in indegree.items():
        if value == 0:
            sources.append(key)
    
    while sources:
        if len(sources) > 1:
            return False
        
        if original_seq[len(sorted_order)] != sources[0]:
            return False
        
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            indegree[child] -= 1
            if indegree[child] == 0:
                sources.append(child)
    
    return len(sorted_order) == len(original_seq)

print(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]]))
print(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]]))
print(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]]))
