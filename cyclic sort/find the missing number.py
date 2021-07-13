# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
# Example:
# Input: [4, 0, 3, 1]
# Output: 2

# O(N) space:O(1)
def find_missing_number(arr):
    i = 0
    while i < len(arr):
        temp = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[temp]:
            arr[temp], arr[i] = arr[i], arr[temp]
        else:
            i += 1
    
    for i in range(len(arr)):
        if arr[i] != i:
            return i
    
    return len(arr)

print(find_missing_number([4, 0, 3, 1]))
print(find_missing_number([7, 3, 5, 2, 4, 6, 0, 1]))