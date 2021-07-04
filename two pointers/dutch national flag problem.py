# Given an array containing 0s, 1s and 2s, sort the array in-place. 
# You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

# The flag of the Netherlands consists of three colors: red, white and blue; 
# and since our input array also consists of three different numbers that is why it is called Dutch National Flag problem.

# Example:
# Input: [1, 0, 2, 1, 0]
# Output: [0 0 1 1 2]

def dutch_national_flag(arr):
    left, right = 0, len(arr) - 1
    i = 0
    while i <= right:
        if arr[i] == 0:
            arr[left],arr[i] = arr[i], arr[left]
            left += 1
            i += 1
        elif arr[i] == 2:
            arr[right], arr[i] = arr[i], arr[right]
            right -= 1
        else:
            i += 1
    return arr

print(dutch_national_flag([1, 0, 2, 1, 0]))
print(dutch_national_flag([2, 2, 0, 1, 2, 0]))