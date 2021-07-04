# Given a sorted array, 
# create a new array containing squares of all the number of the input array in the sorted order.

# Example:
# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]

# O(N) space:O(N)

def squaring_sorted_array(arr):
    left, right = 0, len(arr) - 1
    result = [0]*len(arr)
    count = len(arr) - 1
    while left < right:
        if abs(arr[left]) == abs(arr[right]):
            result[count] = arr[left] * arr[left]
            result[count - 1] = result[count]
            left += 1
            right -= 1
            count -= 2
        elif abs(arr[left]) > abs(arr[right]):
            result[count] = arr[left] * arr[left]
            count -= 1
            left += 1
        else:
            result[count] = arr[right] * arr[right]
            count -= 1
            right -= 1
    return result

print(squaring_sorted_array([-2, -1, 0, 2, 3]))
print(squaring_sorted_array([-3, -1, 0, 1, 2]))