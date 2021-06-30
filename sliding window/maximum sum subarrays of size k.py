# Given an array of positive numbers and a positive number ‘k’, 
# find the maximum sum of any contiguous subarray of size ‘k’.
# Example:
# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# brute force: O(NK)
# sliding window: O(N) space complexity : O(1)

def max_sum_subarray_of_k(array, size):
    maxSum = 0
    windowSum, windowStart = 0, 0
    for windowEnd in range(len(array)):
        windowSum += array[windowEnd]
        if windowEnd >= size-1:
            if maxSum < windowSum:
                maxSum = windowSum
            windowSum -= array[windowStart]
            windowStart +=1
    return maxSum

array = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray_of_k(array, k))
