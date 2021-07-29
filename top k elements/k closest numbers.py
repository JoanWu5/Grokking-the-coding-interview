# Given a sorted number array and two integers ‘K’ and ‘X’, 
# find ‘K’ closest numbers to ‘X’ in the array. 
# Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

# Example:
# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]

# O(K logK) space: O(K)
from heapq import *

class Entry:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
    
    def __lt__(self, other):
        return self.value > other.value

class ClostestNumber:
    minheap = []
    
    def __init__(self, nums, k, x) -> None:
        self.k = k
        self.x = x
        self.nums = nums
    
    def find_k_closest_numbers(self):
        for i in range(self.k):
            heappush(self.minheap, Entry(self.nums[i], self.distance_from_x(self.nums[i])))
        
        for i in range(self.k, len(self.nums)):
            if self.distance_from_x(self.nums[i]) < self.minheap[0].value:
                heappop(self.minheap)
                heappush(self.minheap, Entry(self.nums[i], self.distance_from_x(self.nums[i])))

        result = []
        while self.minheap:
            result.append(heappop(self.minheap).key)
        
        return result

    def distance_from_x(self, num):
        return abs(self.x - num)


clostestNumber = ClostestNumber([5, 6, 7, 8, 9], 3, 7)
print(clostestNumber.find_k_closest_numbers())
clostestNumber = ClostestNumber([2, 4, 5, 6, 9], 3, 6)
print(clostestNumber.find_k_closest_numbers())
clostestNumber = ClostestNumber([2, 4, 5, 6, 9], 3, 10)
print(clostestNumber.find_k_closest_numbers())

# two pointers also can solve this problem
def binary_search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return max(left - 1, 0)

# O(logN) space: O(1)
def find_k_closest_numbers_2(nums, k, x):
    index = binary_search(nums, x)
    left, right = index, index + 1
    result = []
    for _ in range(k):
        if left >= 0 and right < len(nums):
            diff1 = abs(nums[left] - x)
            diff2 = abs(nums[right] - x)
            if diff1 <= diff2:
                result.append(nums[left])
                left -= 1
            else:
                result.append(nums[right])
                right += 1
        elif left >= 0:
            result.append(nums[left])
            left -= 1
        else:
            result.append(nums[right])
            right += 1
    
    return result


print(find_k_closest_numbers_2([5, 6, 7, 8, 9], 3, 7))
print(find_k_closest_numbers_2([2, 4, 5, 6, 9], 3, 6))
print(find_k_closest_numbers_2([2, 4, 5, 6, 9], 3, 10))