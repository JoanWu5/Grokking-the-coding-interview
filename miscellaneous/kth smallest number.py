# Given an unsorted array of numbers, find Kth smallest number in it.
# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

# Example:
# Input: [1, 5, 12, 2, 11, 5], K = 3
# Output: 5
# Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

# brute-force

# O (N * K) space:O(1)
import math

def find_kth_smallest_number(nums, k):
    previous_smallest_number, previous_smallest_index = -math.inf, -1
    current_smallest_number, current_smallest_index = math.inf, -1
    for _ in range(k):
        for j in range(len(nums)):
            if nums[j] > previous_smallest_number and nums[j] < current_smallest_number:
                current_smallest_number = nums[j]
                current_smallest_index = j
            elif nums[j] == previous_smallest_number and j > previous_smallest_index:
                current_smallest_number = nums[j]
                current_smallest_index = j
                break
        
        previous_smallest_number = current_smallest_number
        previous_smallest_index = current_smallest_index
        current_smallest_number = math.inf
    
    return previous_smallest_number
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number([5, 12, 11, -1, 12], 3))

# brute-force using sorting
# O(NlogN) space: O(N)
def find_kth_smallest_number_2(nums, k):
    return sorted(nums)[k - 1]

print(find_kth_smallest_number_2([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_2([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_2([5, 12, 11, -1, 12], 3))

# using max-heap
# O(NlogK) space: O(K)
from heapq import *
def find_kth_smallest_number_3(nums, k):
    maxheap = []
    for i in range(k):
        heappush(maxheap, -nums[i])
    
    for i in range(k, len(nums)):
        if -nums[i] > maxheap[0]:
            heappop(maxheap)
            heappush(maxheap, -nums[i])
    
    return -maxheap[0]

print(find_kth_smallest_number_3([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_3([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_3([5, 12, 11, -1, 12], 3))

# using min-heap
# O((N + K) * logN) space: O(N)
def find_kth_smallest_number_4(nums, k):
    minheap = []
    for num in nums:
        heappush(minheap, num)
    
    for _ in range(k - 1):
        heappop(minheap)
    
    return minheap[0]

print(find_kth_smallest_number_4([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_4([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_4([5, 12, 11, -1, 12], 3))

# using partition scheme of quicksort
# O(NlogN) space: O(N)
def find_kth_smallest_number_5(nums, k):
    return find_kth_smallest_number_rec(nums, k, 0, len(nums) - 1)

def find_kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)
    if p == k - 1:
        return nums[p]
    
    if p > k - 1:
        return find_kth_smallest_number_rec(nums, k, start, p - 1)
    
    return find_kth_smallest_number_rec(nums, k, p + 1, end)

def partition(nums, start, end):
    if start == end:
        return start
    
    pivot = nums[end]
    for i in range(start, end):
        if nums[i] < pivot:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1

    nums[start], nums[end] = nums[end], nums[start]
    return start

print(find_kth_smallest_number_5([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_5([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_5([5, 12, 11, -1, 12], 3))

# using randomized partitoning scheme of quicksort
# O(NlogN) space: O(N)
import random

def find_kth_smallest_number_6(nums, k):
    return find_kth_smallest_number_rec_2(nums, k, 0, len(nums) - 1)

def find_kth_smallest_number_rec_2(nums, k, start, end):
    p = partition_2(nums, start, end)
    if p == k - 1:
        return nums[p]
    
    if p > k - 1:
        return find_kth_smallest_number_rec_2(nums, k, start, p - 1)
    
    return find_kth_smallest_number_rec_2(nums, k, p + 1, end)

def partition_2(nums, start, end):
    if start == end:
        return start
    
    pivot_index = random.randint(start, end)
    nums[pivot_index], nums[end] = nums[end], nums[pivot_index]

    pivot = nums[end]
    for i in range(start, end):
        if nums[i] < pivot:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1

    nums[start], nums[end] = nums[end], nums[start]
    return start

print(find_kth_smallest_number_6([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_6([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_6([5, 12, 11, -1, 12], 3))

# using median of medians
# O(N) space: O(N)
def find_kth_smallest_number_7(nums, k):
    return find_kth_smallest_number_rec_3(nums, k, 0, len(nums) - 1)

def find_kth_smallest_number_rec_3(nums, k, start, end):
    p = partition_3(nums, start, end)
    if p == k - 1:
        return nums[p]
    
    if p > k - 1:
        return find_kth_smallest_number_rec_3(nums, k, start, p - 1)
    
    return find_kth_smallest_number_rec_3(nums, k, p + 1, end)

def partition_3(nums, start, end):
    if start == end:
        return start
    
    median = median_of_medians(nums, start, end)
    for i in range(start, end):
        if nums[i] == median:
            nums[i], nums[end] = nums[end], nums[i]
            break

    pivot = nums[end]
    for i in range(start, end):
        if nums[i] < pivot:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1

    nums[start], nums[end] = nums[end], nums[start]
    return start

def median_of_medians(nums, start, end):
    n = end - start + 1
    if n < 5:
        return nums[start]
    
    partitions = [nums[j:j + 5] for j in range(start, end + 1, 5)]
    full_partitions = [partition for partition in partitions if len(partition) == 5]
    sorted_partitions = [sorted(partition) for partition in full_partitions]
    medians = [partition[2] for partition in sorted_partitions]

    return partition_3(medians, 0, len(medians) - 1)

print(find_kth_smallest_number_6([1, 5, 12, 2, 11, 5], 3))
print(find_kth_smallest_number_6([1, 5, 12, 2, 11, 5], 4))
print(find_kth_smallest_number_6([5, 12, 11, -1, 12], 3))