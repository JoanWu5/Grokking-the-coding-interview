# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.
# You can assume that the array does not have any duplicates.

# Example:
# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.

# Input: [1, 3, 8, 10]
# Output: 0
# Explanation: The array has been not been rotated.

# O(logN) space: O(1)
def count_rotation(arr):
    if len(arr) == 0:
        return 0
    
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid
        
        if arr[start] < arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

print(count_rotation([10, 15, 1, 3, 8]))
print(count_rotation([4, 5, 7, 9, 10, -1, 2]))
print(count_rotation([1, 3, 8, 10]))
            
# follow up:
# How do we find the rotation count of a sorted and rotated array that has duplicates too?
# The above code will fail on the following example!

# Example:
# Input: [3, 3, 7, 3]
# Output: 3
# Explanation: The array has been rotated 3 times

print(count_rotation([3, 3, 7, 3]))

# O(logN) space: O(1)
def count_rotation_duplicate(arr):
    if len(arr) == 0:
        return 0
    
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2

        if mid < end and arr[mid] > arr[mid + 1]:
            return mid + 1
        
        if mid > start and arr[mid - 1] > arr[mid]:
            return mid
        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            if arr[start] > arr[start + 1]:
                return start + 1
            start += 1
            if arr[end - 1] > arr[end]:
                return end
            end -= 1
        elif arr[start] < arr[mid] or (arr[start] == arr[mid] and arr[mid] > arr[end]):
            start = mid + 1
        else:
            end = mid - 1
    
    return 0

print(count_rotation_duplicate([3, 3, 7, 3]))
