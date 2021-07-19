# Problem Statement 
# Given an array of numbers and a number ‘k’, 
# find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

# Example 1:
# Input: nums=[1, 2, -1, 3, 5], k = 2
# Output: [1.5, 0.5, 1.0, 4.0]
# Explanation: Lets consider all windows of size ‘2’:
# [1, 2, -1, 3, 5] -> median is 1.5
# [1, 2, -1, 3, 5] -> median is 0.5
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 4.0

# Example 2:
# Input: nums=[1, 2, -1, 3, 5], k = 3
# Output: [1.0, 2.0, 3.0]
# Explanation: Lets consider all windows of size ‘3’:
# [1, 2, -1, 3, 5] -> median is 1.0
# [1, 2, -1, 3, 5] -> median is 2.0
# [1, 2, -1, 3, 5] -> median is 3.0

# O(NK) where ‘N’ is the total number of elements in the input array and ‘K’ is the size of the sliding window. 

# This is due to the fact that we are going through all the ‘N’ numbers and, while doing so, we are doing two things:
# 1. Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)
# 2. Removing the element going out of the sliding window. 
# This will take O(K) as we will be searching this element in an array of size ‘K’ (i.e., a heap).

# space: O(K)

from heapq import *
import heapq

class Sliding_Median:
    def __init__(self) -> None:
        self.max_heap = []
        self.min_heap = []
    
    def find_sliding_window_median(self, arr, k):
        result =  [0.0 for i in range(len(arr) - k + 1)]
        for i in range(len(arr)):
            if not self.max_heap or -self.max_heap[0] >= arr[i]:
                heappush(self.max_heap, -arr[i])
            else:
                heappush(self.min_heap, arr[i])
        
            self.rebalance_heap()

            if i - k + 1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result[i - k + 1] = (-self.max_heap[0] + self.min_heap[0]) /2.0
                else:
                    result[i - k + 1] = -self.max_heap[0] / 1.0
                
                element_to_removed = arr[i - k + 1]
                if element_to_removed <= -self.max_heap[0]:
                    self.remove_element(self.max_heap, -element_to_removed)
                else:
                    self.remove_element(self.min_heap, element_to_removed)
                
            self.rebalance_heap()

        return result 

    def rebalance_heap(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def remove_element(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        del heap[-1]
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

sliding_window = Sliding_Median()
print(sliding_window.find_sliding_window_median([1, 2, -1, 3, 5], 2))

sliding_window = Sliding_Median()
print(sliding_window.find_sliding_window_median([1, 2, -1, 3, 5], 3))
