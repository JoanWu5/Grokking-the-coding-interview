# Given an array of points in the a 2D2D plane, find ‘K’ closest points to the origin.

# Example:
# Input: points = [[1,2],[1,3]], K = 1
# Output: [[1,2]]
# Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
# The Euclidean distance between (1, 3) and the origin is sqrt(10).
# Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

# Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
# Output: [[1, 3], [2, -1]]

# O(N * logK) space: O(K)
from heapq import *

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __lt__(self, other):
        return self.distance_from_origin() > other.distance_from_origin()

    def distance_from_origin(self):
        return self.x * self.x + self.y * self.y

    def print_point(self):
        print("[" + str(self.x) + "," + str(self.y) + "]", end = '')

def find_k_closest_to_origin(nums, k):
    maxheap = []
    for i in range(k):
        heappush(maxheap, Point(nums[i][0], nums[i][1]))
    
    for i in range(k, len(nums)):
        if Point(nums[i][0], nums[i][1]).distance_from_origin() < maxheap[0].distance_from_origin():
            heappop(maxheap)
            heappush(maxheap, Point(nums[i][0], nums[i][1]))
    
    return list(maxheap)

result = find_k_closest_to_origin([[1, 3], [3, 4], [2, -1]], 2)
for point in result:
    point.print_point()
print()


result = find_k_closest_to_origin([[1,2],[1,3]], 1)
for point in result:
    point.print_point()
print()