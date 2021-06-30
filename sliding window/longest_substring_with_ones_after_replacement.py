# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
# find the length of the longest contiguous subarray having all 1s.

# Example:
# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

# sliding window:O(N) space:O(1)
def longest_substring_with_ones_after_k_replacement(arr, k):
    max_one_repeat_times = 0
    result = 0
    window_start = 0
    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char == 1:
            max_one_repeat_times += 1
        if window_end - window_start + 1 - max_one_repeat_times > k:
            left_char = arr[window_start]
            if left_char == 1:
                max_one_repeat_times -= 1
            window_start += 1
        result = max(result, window_end - window_start + 1)
    return result

print(longest_substring_with_ones_after_k_replacement([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
print(longest_substring_with_ones_after_k_replacement([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
