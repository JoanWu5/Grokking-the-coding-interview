# Given an array of positive numbers and a positive number ‘S’, 
# find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. 
# Return 0, if no such subarray exists.

# Example:
# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

# brute force: O(N^2)
# sliding window: O(N) space complexity : O(1)

import math
def smallest_subarray_with_given_sum(array, sum):
    result = math.inf
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        while windowSum >= sum:
            if result >= windowEnd - windowStart + 1:
                result = windowEnd - windowStart + 1
            windowSum -= array[windowStart]
            windowStart += 1
    if result == math.inf:
        return 0
    return result

print(smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7))
print(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7))
print(smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8))
