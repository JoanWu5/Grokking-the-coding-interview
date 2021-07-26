# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. 
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

# Example:
# Input: [4, 6, 6, 6, 9], key = 6
# Output: [1, 3]

def number_range(arr, key):
    result = [-1, -1]
    if len(arr) == 0 or arr[0] > key or arr[-1] < key:
        return result
    
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            temp = mid
            while temp >= 0 and arr[temp] == key:
                temp -= 1
            result[0] = temp + 1

            temp = mid
            while temp < len(arr) and arr[temp] == key:
                temp += 1
            result[1] = temp - 1

            return result

        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    
    return result

print(number_range([4, 6, 6, 6, 9], 6))
print(number_range([1, 3, 8, 10, 15], 10))
print(number_range([1, 3, 8, 10, 15], 12))

