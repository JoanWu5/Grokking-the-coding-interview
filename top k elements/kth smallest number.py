# Given an unsorted array of numbers, find Kth smallest number in it.
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

# Example:

# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

# O(N * logK) space: O(K)
from heapq import *

def find_kth_smallest_number(nums, k):
    maxheap = []
    for i in range(k):
        heappush(maxheap, -nums[i])
    
    for i in range(k, len(nums)):
        if nums[i] < -maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -nums[i])
    
    return -maxheap[0]

print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number([5, 12, -1, 11, 12], 3))