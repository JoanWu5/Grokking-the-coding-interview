# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

# Example:
# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]

# O(K * logK + (N - K) * logK) = O(N * logK)
# space: O(K)
from heapq import *

def find_k_largest_numbers(nums, k):
    minheap = []
    for i in range(k):
        heappush(minheap, nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] > minheap[0]:
            heappop(minheap)
            heappush(minheap, nums[i])
    
    return list(minheap)

print(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))