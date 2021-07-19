# Design a class to calculate the median of a number stream. The class should have the following two methods:

# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

# Example 1:

# 1. insertNum(3)
# 2. insertNum(1)
# 3. findMedian() -> output: 2
# 4. insertNum(5)
# 5. findMedian() -> output: 3
# 6. insertNum(4)
# 7. findMedian() -> output: 3.5

# O(logN) space:O(N)
from heapq import *

class Median_Stream:
    max_heap = [] # contain the smaller part
    min_heap = [] # contain the larger part

    def insert_number(self, num):
        if not self.max_heap or -self.max_heap[0] >= num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)
    
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0])/2

        return -self.max_heap[0]

median_stream = Median_Stream()
median_stream.insert_number(3)
median_stream.insert_number(1)
print(median_stream.find_median())
median_stream.insert_number(5)
print(median_stream.find_median())
median_stream.insert_number(4)
print(median_stream.find_median())
