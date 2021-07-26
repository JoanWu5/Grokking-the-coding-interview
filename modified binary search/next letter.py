# Given an array of lowercase letters sorted in ascending order, 
# find the smallest letter in the given array greater than a given ‘key’.
# Assume the given array is a circular list, 
# which means that the last letter is assumed to be connected with the first letter. 
# This also means that the smallest letter in the given array is greater than the last letter of the array 
# and is also the first letter of the array.

# Write a function to return the next letter of the given ‘key’.

# Example 1:

# Input: ['a', 'c', 'f', 'h'], key = 'f'
# Output: 'h'
# Explanation: The smallest letter greater than 'f' is 'h' in the given array.

# Input: ['a', 'c', 'f', 'h'], key = 'm'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.

# O(logN) space:O(1)
def next_letter(arr, key):
    if len(arr) == 0:
        return None
    
    if key < arr[0] or key > arr[-1]:
        return arr[0]
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if key == mid:
            return arr[mid]
        elif key < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
        
    return arr[start]

print(next_letter(['a', 'c', 'f', 'h'], 'f'))
print(next_letter(['a', 'c', 'f', 'h'], 'b'))
print(next_letter(['a', 'c', 'f', 'h'], 'm'))