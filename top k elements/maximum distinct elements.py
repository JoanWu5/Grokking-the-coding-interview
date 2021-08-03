# Given an array of numbers and a number ‘K’, 
# we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

# Example:
# Input: [7, 3, 5, 8, 5, 3, 3], and K=2
# Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], 
# we have to skip 5 because it is not distinct and occurred twice. 
# Another solution could be to remove one instance of '5' and '3' each to be left with three 
# distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

# O(N * logN + K * logN) space: O(N)
from heapq import *

def find_maximum_distinct_elements(nums, k):
    distinct_elements = 0
    if len(nums) <= k :
        return distinct_elements

    hashmap = dict()
    for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1
    
    minheap = []
    for num, frequency in hashmap.items():
        if frequency == 1:
            distinct_elements += 1
        else:
            heappush(minheap, (frequency, num))
    
    while k > 0 and minheap:
        frequency, num = heappop(minheap)
        k -= frequency - 1
        if k >= 0:
            distinct_elements += 1
    
    if k > 0:
        distinct_elements -= k
    
    return distinct_elements

print(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2))
print(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3))
print(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))