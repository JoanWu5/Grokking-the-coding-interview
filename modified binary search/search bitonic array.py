# Given a Bitonic array, find if a given ‘key’ is present in it. 
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

# Example:

# Input: [1, 3, 8, 4, 3], key=4
# Output: 3

# O(logN) space:O(1)
def search_bitonic_array(arr, key):
    if len(arr) == 0:
        return -1
    
    max_index = find_max(arr)
    key_index = binary_search(arr, key, 0, max_index)
    if key_index != -1:
        return key_index
    return binary_search(arr, key, max_index + 1, len(arr) - 1)


def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    
    return start

def binary_search(arr, key, start, end):
    is_ascend = arr[start] < arr[end]
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return mid
        if is_ascend:
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[mid] > key:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

print(search_bitonic_array([1, 3, 8, 4, 3], 4))
print(search_bitonic_array([3, 8, 3, 1], 8))
print(search_bitonic_array([1, 2, 3, 10], 10))
print(search_bitonic_array([10, 9, 3, 1], 8))