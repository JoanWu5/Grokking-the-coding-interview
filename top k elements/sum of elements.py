# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

# Example:
# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).


# O(N * logN) space: O(N)
from heapq import *

def sum_of_elements(nums, k1, k2):
    minheap = []
    for num in nums:
        heappush(minheap, num)

    for _ in range(k1):
        heappop(minheap)

    numsum = 0
    for _ in range(k2 - k1 - 1):
        numsum += heappop(minheap)
    
    return numsum

print(sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6))
print(sum_of_elements([3, 5, 8, 7], 1, 4))

# to reduce the time complexity
# O(N * logk2) space:O(k2)
def sum_of_elements_2(nums, k1, k2):
    maxheap = []
    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(maxheap, -nums[i])
        elif nums[i] < -maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -nums[i])
    
    numsum = 0
    for _ in range(k2 - k1 - 1):
        numsum += -heappop(maxheap)
    
    return numsum

print(sum_of_elements_2([1, 3, 12, 5, 15, 11], 3, 6))
print(sum_of_elements_2([3, 5, 8, 7], 1, 4))
    
