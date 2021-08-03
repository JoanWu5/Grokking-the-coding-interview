# Given ‘M’ sorted arrays, 
# find the smallest range that includes at least one number from each of the ‘M’ lists.

# Example:
# Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
# Output: [4, 7]
# Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

from heapq import *
import math

def find_smallest_number_range(lists):
    range_start, range_end = 0, math.inf
    current_max = -math.inf
    minheap = []

    for i in range(len(lists)):
        heappush(minheap, (lists[i][0], 0, i))
        current_max = max(current_max, lists[i][0])
    
    while len(minheap) == len(lists):
        num, i, list_index = heappop(minheap)
        if range_end - range_start > current_max - num:
            range_start = num
            range_end = current_max
        
        if i < len(lists[list_index]) - 1:
            heappush(minheap, (lists[list_index][i + 1], i + 1, list_index))
            current_max = max(current_max, lists[list_index][i + 1])
    
    return [range_start, range_end]

print(find_smallest_number_range([[1, 5, 8], [4, 12], [7, 8, 10]]))
print(find_smallest_number_range([[1, 9], [4, 12], [7, 10, 16]]))