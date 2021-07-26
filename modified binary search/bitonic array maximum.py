# Find the maximum value in a given Bitonic array.
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. 
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Example:
# Input: [1, 3, 8, 12, 4, 2]
# Output: 12
# Explanation: The maximum number in the input bitonic array is '12'.

# O(logN) space:O(1)
def bitonic_array_maximum(arr):
    if len(arr) == 0:
        return None
    
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return arr[start]

print(bitonic_array_maximum([1, 3, 8, 12, 4, 2]))
print(bitonic_array_maximum([3, 8, 3, 1]))
print(bitonic_array_maximum([8, 3, 1]))
print(bitonic_array_maximum([1, 2, 3, 10]))