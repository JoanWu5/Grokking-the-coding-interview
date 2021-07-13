# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. 
# Find all those missing numbers.

# Example:
# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

# O(N) space:O(1)
def find_all_missing_number(arr):
    i = 0
    while i < len(arr):
        temp = arr[i] - 1
        if arr[i] != arr[temp]:
            arr[i], arr[temp] = arr[temp], arr[i]
        else:
            i += 1

        print(i, arr)

    result = []
    for i in range(len(arr)):
        if arr[i] != i + 1:
            result.append(i+1)
    
    return result

print(find_all_missing_number([2, 3, 1, 8, 2, 3, 5, 1]))