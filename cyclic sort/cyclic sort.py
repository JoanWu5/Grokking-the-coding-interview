# We are given an array containing ‘n’ objects. Each object, when created, 
# was assigned a unique number from 1 to ‘n’ based on their creation sequence. 
# This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

# Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. 
# For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, 
# though each number is actually an object.

# Example:
# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]

# O(N) space:O(1)
def cyclic_sort(arr):
    start = 0
    while start < len(arr):
        index = arr[start] - 1
        if arr[index] == arr[start]:
            start += 1
        else:
            arr[index], arr[start] = arr[start], arr[index]
    return arr

print(cyclic_sort([3, 1, 5, 4, 2]))
print(cyclic_sort([2, 6, 4, 3, 1, 5]))
print(cyclic_sort([1, 5, 6, 4, 3, 2]))