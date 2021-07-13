# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

# Example:
# Input: [1, 4, 4, 3, 2]
# Output: 4

# O(N) space:O(1)
def find_the_duplicate_number(arr):
    i = 0
    while i < len(arr) - 1:
        j = arr[i] - 1
        if i != j:
            if arr[i] != arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
            else:
                return arr[i]
        else:
            i += 1

    return -1

print(find_the_duplicate_number([1, 4, 4, 3, 2]))
print(find_the_duplicate_number([2, 1, 3, 3, 5, 4]))
print(find_the_duplicate_number([2, 4, 1, 4, 4]))

# follow up: Can we solve the above problem in O(1) space and without modifying the input array?
def find_start_of_cycle_2(arr, cycle_length):
    pointer1, pointer2 = arr[0], arr[0]
    for _ in range(cycle_length):
        pointer1 = arr[pointer1]
    
    while pointer1 != pointer2:
        pointer1 = arr[pointer1]
        pointer2 = arr[pointer2]
    
    return pointer1

def find_the_duplicate_number_2(arr):
    slow, fast = 0, 0
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]

        if slow == fast:
            break
    
    current = arr[slow]

    cycle_length = 0
    while True:
        current = arr[current]
        cycle_length += 1
        if current == arr[slow]:
            break
    
    return find_start_of_cycle_2(arr, cycle_length)

print(find_the_duplicate_number_2([1, 4, 4, 3, 2]))
print(find_the_duplicate_number_2([2, 1, 3, 3, 5, 4]))
print(find_the_duplicate_number_2([2, 4, 1, 4, 4]))
