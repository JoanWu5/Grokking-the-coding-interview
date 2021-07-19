# Next Interval (hard) 
# Given an array of intervals, find the next interval of each interval. In a list of intervals, 
# for an interval ‘i’ its next interval ‘j’ will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.
# Write a function to return an array containing indices of the next interval of each input interval. 
# If there is no next interval of a given interval, return -1. 
# It is given that none of the intervals have the same start point.

# Example:
# Input: Intervals [[2,3], [3,4], [5,6]]
# Output: [1, 2, -1]
# Explanation: The next interval of [2,3] is [3,4] having index ‘1’. 
# Similarly, the next interval of [3,4] is [5,6] having index ‘2’.
# There is no next interval for [5,6] hence we have ‘-1’.

# brute force: O(N^2) space: O(N)
import math
def next_interval(arr):
    result = [-1 for _ in range(len(arr))]
    min_interval = [math.inf for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i][1] <= arr[j][0]:
                if min_interval[i] > arr[j][0]:
                    min_interval[i] = arr[j][0]
                    result[i] = j
    return result

print(next_interval([[2,3], [3,4], [5,6]]))
print(next_interval([[3,4], [1,5], [4,6]]))

# O(NlogN) space: O(N)
from heapq import *

def find_next_interval(arr):
    start_list = []
    end_list = []
    result = [-1] * len(arr)
    for i in range(len(arr)):
        heappush(start_list, (arr[i][0], i))
        heappush(end_list, (arr[i][1], i))
    
    while end_list:
        end_value, end_index = heappop(end_list)
    
        while start_list and start_list[0][0] < end_value:
            heappop(start_list)
        
        if start_list:
            start_value, start_index = heappop(start_list)
            result[end_index] = start_index
            heappush(start_list, (start_value, start_index))
    
    return result
    
print(find_next_interval([[2,3], [3,4], [5,6]]))
print(find_next_interval([[3,4], [1,5], [4,6]]))
