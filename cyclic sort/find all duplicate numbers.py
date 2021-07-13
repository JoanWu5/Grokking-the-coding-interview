# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array has some duplicates, find all the duplicate numbers without using any extra space.
# Example:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]

# O(N) space:O(1)
def find_all_duplicate_numbers(arr):
    i = 0 
    result = []
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1

    for i in range(len(arr)):
        if i + 1 != arr[i]:
            result.append(arr[i])
    return result

print(find_all_duplicate_numbers([3, 4, 4, 5, 5]))
print(find_all_duplicate_numbers([5, 4, 7, 2, 3, 5, 3]))
