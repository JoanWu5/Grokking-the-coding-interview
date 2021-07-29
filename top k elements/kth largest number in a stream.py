# Design a class to efficiently find the Kth largest element in a stream of numbers.
# The class should have the following two things:
# The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) which will store the given number and return the Kth largest number.

# Example:
# Input: [3, 1, 5, 12, 2, 11], K = 4
# 1. Calling add(6) should return '5'.
# 2. Calling add(13) should return '6'.
# 2. Calling add(4) should still return '6'.

# O(logK) space: O(K)
from heapq import *

class KthlargestStream:
    minheap = []

    def __init__(self, nums, k) -> None:
        self.k = k
        for num in nums:
            self.add(num)
    
    def add(self, num):
        heappush(self.minheap, num)

        if len(self.minheap) > self.k:
            heappop(self.minheap)
        
        return self.minheap[0]

kthlargestStream = KthlargestStream([3, 1, 5, 12, 2, 11], 4)
print(kthlargestStream.add(6))
print(kthlargestStream.add(13))
print(kthlargestStream.add(4))



    
    