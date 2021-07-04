# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example:
# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

import math
def minimum_window_sort(arr):
    left, right = 0, len(arr) - 1
    while left < len(arr)-1 and arr[left] <= arr[left + 1]:
        left += 1
    
    if left == len(arr) - 1:
        return 0

    while right > 0 and arr[right] >= arr[right - 1]:
        right -= 1
    
    subarray_min = math.inf
    subarray_max = -math.inf

    for i in range(left, right+1):
        subarray_min = min(subarray_min, arr[i])
        subarray_max = max(subarray_max, arr[i])
    
    while left > 0 and arr[left - 1] > subarray_min:
        left -= 1
    
    while right < len(arr) - 1 and arr[right + 1] < subarray_max:
        right += 1
    
    return right - left + 1

print(minimum_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
print(minimum_window_sort([1, 3, 2, 0, -1, 7, 10]))
print(minimum_window_sort([1, 2, 3]))
print(minimum_window_sort([3, 2 ,1]))

