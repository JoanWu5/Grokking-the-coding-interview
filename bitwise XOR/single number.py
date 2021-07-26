# In a non-empty array of integers, every number appears twice except for one, find that single number.
# Example:

# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4

# O(N) space: O(1)
def find_single_number(arr):
    arr_xor = arr[0]
    for i in range(1, len(arr)):
        arr_xor = arr_xor ^ arr[i]
    
    return arr_xor

print(find_single_number([1, 4, 2, 1, 3, 2, 3]))