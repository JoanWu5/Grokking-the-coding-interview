# Given a sorted array of numbers, find if a given number ‘key’ is present in the array. 
# Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
# You should assume that the array can have duplicates.
# Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

# Example:
# Input: [4, 6, 10], key = 10
# Output: 2

# O(logN) space: O(1)
def order_agnostic_binary_search(arr, key):
    if len(arr) == 0:
        return -1
    
    start, end = 0, len(arr) - 1
    is_ascend = arr[start] < arr[end]
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        
        if is_ascend:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    
    return -1

print(order_agnostic_binary_search([4, 6, 10], 10))
print(order_agnostic_binary_search([1, 2, 3, 4, 5, 6, 7], 5))
print(order_agnostic_binary_search([10, 6, 4], 10))
print(order_agnostic_binary_search([10, 6, 4], 5))