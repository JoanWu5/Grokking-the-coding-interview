# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
# The cost of connecting two ropes is equal to the sum of their lengths.

# Example:
# Input: [1, 3, 11, 5]
# Output: 33
# Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

# O(NlogN) space: O(N)
from heapq import *

def connect_ropes(ropes):
    minheap = []
    result = 0

    for i in range(len(ropes)):
        heappush(minheap, ropes[i])
    
    while len(minheap) > 1:
        min_length = heappop(minheap) + heappop(minheap)
        result += min_length
        heappush(minheap, min_length)
    
    return result

print(connect_ropes([1, 3, 11, 5]))
print(connect_ropes([3, 4, 5, 6]))
print(connect_ropes([1, 3, 11, 5, 2]))
