# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Example:
# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'

# O(N) space:O(1)
def find_the_smallest_missing_positive_number(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return i + 1

    return -1

print(find_the_smallest_missing_positive_number([-3, 1, 5, 4, 2]))
print(find_the_smallest_missing_positive_number([3, -2, 0, 1, 2]))
print(find_the_smallest_missing_positive_number([3, 2, 5, 1]))
