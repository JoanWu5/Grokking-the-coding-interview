# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
# find if a given ‘key’ is present in it.

# Write a function to return the index of the ‘key’ in the rotated array. 
# If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

# Example:
# Input: [10, 15, 1, 3, 8], key = 15
# Output: 1
# Explanation: '15' is present in the array at index '1'.

# O(logN) space:O(1)
def search_in_rotated_array(arr, key):
    if len(arr) == 0:
        return -1
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        
        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return  -1

print(search_in_rotated_array([10, 15, 1, 3, 8], 15))
print(search_in_rotated_array([4, 5, 7, 9, 10, -1, 2], 10)) 

# follow up: How do we search in a sorted and rotated array that also has duplicates?
print(search_in_rotated_array([3, 7, 3, 3, 3], 7))


# best: O(logN) worst:O(N) space:O(1)
def search_in_rotated_duplicate_array(arr, key):
    if len(arr) == 0:
        return -1
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        
        if arr[start] == arr[mid] and arr[end] == arr[mid]:
            start += 1
            end -= 1

        if arr[start] <= arr[mid]:
            if key >= arr[start] and key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key > arr[mid] and key <= arr[end]:
                start = mid + 1
            else:
                end = mid - 1
    
    return  -1

print(search_in_rotated_duplicate_array([3, 7, 3, 3, 3], 7))