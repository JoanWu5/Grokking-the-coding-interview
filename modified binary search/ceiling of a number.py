# Given an array of numbers sorted in an ascending order, find the ceiling of a given number ‘key’. 
# The ceiling of the ‘key’ will be the smallest element in the given array greater than or equal to the ‘key’.
# Write a function to return the index of the ceiling of the ‘key’. If there isn’t any ceiling return -1.

# Example:
# Input: [4, 6, 10], key = 6
# Output: 1
# Explanation: The smallest number greater than or equal to '6' is '6' having index '1'.

# O(logN) space: O(1)
def ceiling_number(arr, key):
    if len(arr) == 0 or arr[-1] < key:
        return -1
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return start

print(ceiling_number([4, 6, 10], 6))
print(ceiling_number([1, 3, 8, 10, 15], 12))
print(ceiling_number([4, 6, 10], 17))
print(ceiling_number([4, 6, 10], -1))

# follow up:
# Given an array of numbers sorted in ascending order, find the floor of a given number ‘key’. 
# The floor of the ‘key’ will be the biggest element in the given array smaller than or equal to the ‘key’
# Write a function to return the index of the floor of the ‘key’. If there isn’t a floor, return -1.

# Example:
# Input: [1, 3, 8, 10, 15], key = 12
# Output: 3
# Explanation: The biggest number smaller than or equal to '12' is '10' having index '3'.

# O(logN) space: O(1)
def floor_number(arr, key):
    if len(arr) == 0 or arr[0] > key:
        return -1
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    return end

print(floor_number([4, 6, 10], 6))
print(floor_number([1, 3, 8, 10, 15], 12))
print(floor_number([4, 6, 10], 17))
print(floor_number([4, 6, 10], -1))
