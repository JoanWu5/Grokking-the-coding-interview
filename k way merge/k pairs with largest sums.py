# Given two sorted arrays in descending order, 
# find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

# Example:
# Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
# Output: [9, 3], [9, 6], [8, 6] 
# Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

# O(N * M * logK) space: O(K)
from heapq import *

def find_k_pairs_with_largest_sum(nums1, nums2, k):
    minheap = []
    result = []
    
    for i in range(0, min(k, len(nums1))):
        for j in range(0, min(k, len(nums2))):
            if len(minheap) < k:
                heappush(minheap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < minheap[0][0]:
                    break
                else:
                    heappop(minheap)
                    heappush(minheap, (nums1[i] + nums2[j], i, j))
    
    while minheap:
        _, i, j = heappop(minheap)
        result.append([nums1[i], nums2[j]])
    
    return result

print(find_k_pairs_with_largest_sum([9, 8, 2], [6, 3, 1], 3))
print(find_k_pairs_with_largest_sum([5, 2, 1], [2, -1], 3))
