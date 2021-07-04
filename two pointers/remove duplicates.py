# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example:
# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# O(N) space:O(1)
def remove_duplicates(arr):
    if len(arr) == 0:
        return 0
    
    next_non_duplicate = 0
    for i in range(len(arr)):
        if arr[next_non_duplicate-1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1

    return next_non_duplicate

print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))   
print(remove_duplicates([2, 2, 2, 11]))

# Given an unsorted array of numbers and a target ‘key’, 
# remove all instances of ‘key’ in-place and return the new length of the array.

# Example:
# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

def remove_element(arr, key):
    next_pointer = 0
    for i in range(len(arr)):
        if arr[i] != key:
            arr[next_pointer] = arr[i]
            next_pointer += 1
    return next_pointer

print(remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3))
print(remove_element([2, 11, 2, 2, 1], 2))