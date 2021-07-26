# Given an array of numbers sorted in ascending order, 
# find the element in the array that has the minimum difference with the given ‘key’.

# Example:
# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

# O(logN) space: O(1)
def minimum_difference_element(arr, key):
    if len(arr) == 0:
        return None
    
    if arr[0] > key:
        return arr[0]
    
    if arr[-1] < key:
        return arr[-1]
    
    start, end = 0, len(arr) - 1
    
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    if arr[start] - key < key - arr[end]:
        return arr[start]
    else:
        return arr[end]

print(minimum_difference_element([4, 6, 10], 7))
print(minimum_difference_element([4, 6, 10], 4))
print(minimum_difference_element([4, 6, 10], 17))
print(minimum_difference_element([1, 3, 8, 10, 15], 12))