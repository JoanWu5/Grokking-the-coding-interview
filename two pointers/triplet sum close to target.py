# Given an array of unsorted numbers and a target number, 
# find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example:
# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

# sort:O(N*logN) searchpair:O(N) for each iteration-> O(N^2)  space:O(N) for sorting

# abs(X+Y+Z - target_sum)
import math
def triplet_sum_close_to_target(arr, target_sum):
    result = math.inf
    arr.sort()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        current_result = smallest_sum(arr, target_sum-arr[i], i+1)
        result = min(result, current_result)
    return abs(result - target_sum)

def smallest_sum(arr, target_sum, left):
    right = len(arr) - 1
    result = math.inf 
    while left < right:
        current_sum = arr[left] + arr[right]
        now_sum =abs(target_sum-current_sum)
        result = min(result, now_sum)
        if current_sum == target_sum:
            return 0
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1
    return result

print(triplet_sum_close_to_target([-2, 0, 1, 2],2))
print(triplet_sum_close_to_target([-3, -1, 1, 2],1))
print(triplet_sum_close_to_target([1, 0, 1, 1],100))


        

