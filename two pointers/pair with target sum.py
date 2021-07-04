# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Example:
# Input: [1, 2, 3, 4, 6], target=6
# Output: [1, 3]
# Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

# Input: [2, 5, 9, 11], target=11
# Output: [0, 2]
# Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11

# brute force: O(N^2)
# two pointers: O(N) space:O(1)

def pair_with_target_sum(arr, target_sum):
    left, right = 0, len(arr)-1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
    
    return [-1, -1]

print(pair_with_target_sum([1, 2, 3, 4, 6],6))
print(pair_with_target_sum([2, 5, 9, 11], 11))

# hashTable: O(N) space:O(N)
def pair_with_target_sum_method_2(arr, target_sum):
    nums = dict()
    for index, num in enumerate(arr):
        if target_sum - num in nums:
            return [nums[target_sum-num], index]
        else:
            nums[num] = index
    
    return [-1, -1]

print(pair_with_target_sum_method_2([1, 2, 3, 4, 6],6))
print(pair_with_target_sum_method_2([2, 5, 9, 11], 11))
