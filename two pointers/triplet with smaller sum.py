# Given an array arr of unsorted numbers and a target sum, 
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
# Write a function to return the count of such triplets.

# Example:
# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# sort:O(N*logN) searchpair:O(N) for each iteration-> O(N^2)  space:O(N) for sorting
def triplet_with_smaller_sum(arr, target_sum):
    result = 0
    arr.sort()
    for i in range(len(arr)):
        result += search_pair(arr, target_sum-arr[i], i+1)
    return result

def search_pair(arr, target_sum, left):
    right = len(arr) - 1
    count = 0
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum < target_sum:
            count += right - left
            left += 1
        else:
            right -= 1
    return count
    
print(triplet_with_smaller_sum([-1, 0, 2, 3],3))
print(triplet_with_smaller_sum([-1, 4, 2, 1, 3],5))

# follow up : 
# Problem: Write a function to return the list of all such triplets instead of the count.
# How will the time complexity change in this case?

# O(N^3)
def triplet_with_smaller_sum_2(arr, target_sum):
    result = []
    arr.sort()
    for i in range(len(arr)):
        search_pair_2(arr, target_sum-arr[i], i+1, result)
    return result

def search_pair_2(arr, target_sum, left, result):
    right = len(arr) - 1
    first = left - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum < target_sum:
            for i in range(right, left, -1):
                result.append([arr[first], arr[left], arr[i]])
            left += 1
        else:
            right -= 1
    return result


print(triplet_with_smaller_sum_2([-1, 0, 2, 3],3))
print(triplet_with_smaller_sum_2([-1, 4, 2, 1, 3],5))