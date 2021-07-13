# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array originally contained all the numbers from 1 to ‘n’, 
# but due to a data error, 
# one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

# Example:
# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.

# O(N) space:O(1)
def find_corrupt_pair(arr):
    i = 0
    while i < len(arr):
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            i += 1
    
    for i in range(len(arr)):
        if arr[i] != i + 1:
            return [i+1, arr[i]]
    
    return [-1, -1]

print(find_corrupt_pair([3, 1, 2, 5, 2]))
print(find_corrupt_pair([3, 1, 2, 3, 6, 4]))