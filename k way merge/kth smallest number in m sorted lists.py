# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Example:
# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
# list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

# O(K * logM) space: O(M)
from heapq import *

def kth_smallest_number_in_sorted_lists(arrs, k):
    minheap = []
    for i in range(len(arrs)):
        heappush(minheap, (arrs[i][0], 0, i))
    
    number = 0
    while minheap and k > 0:
        number, i, list_index = heappop(minheap)
        k -= 1
        if i + 1 < len(arrs[list_index]):
            heappush(minheap, (arrs[list_index][i + 1], i + 1, list_index))
    
    return number

print(kth_smallest_number_in_sorted_lists([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))

