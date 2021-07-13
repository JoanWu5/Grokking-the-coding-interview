# Given an unsorted array containing numbers and a number ‘k’, 
# find the first ‘k’ missing positive numbers in the array.

# Example:
# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.

# O(N + K) space:O(1)
def find_first_k_missing_positive_number(arr, k):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] > 0 and arr[i] <= len(arr) and arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    missing_number = []
    extra_number = []

    for i in range(len(arr)):
        if k == 0:
            break
        if arr[i] != i + 1:
            missing_number.append(i + 1)
            extra_number.append(arr[i])
            k -= 1

    add_length = len(arr)
    while k > 0:
        add_length += 1
        if add_length not in extra_number:
            missing_number.append(add_length)
            k -= 1

    return missing_number

print(find_first_k_missing_positive_number([3, -1, 4, 5, 5], 3))
print(find_first_k_missing_positive_number([2, 3, 4], 3))
print(find_first_k_missing_positive_number([-2, -3, 4], 2))


