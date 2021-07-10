# Given an array of intervals representing ‘N’ appointments, 
# find out if a person can attend all the appointments.

# Example:
# Appointments: [[1,4], [2,5], [7,9]]
# Output: false
# Explanation: Since [1,4] and [2,5] overlap, a person cannot attend both of these appointments.

# O(NlogN) 
# space:O(N) (sort uses Timsort, which needs O(N) space)
def is_conflicting_appointment(arr):
    start, end = 0, 1
    arr.sort(key = lambda x: x[0])
    
    for i in range(1, len(arr)):
        if arr[i-1][end] > arr[i][start]:
            return False
    
    return True

print(is_conflicting_appointment([[1,4], [2,5], [7,9]]))
print(is_conflicting_appointment([[6,7], [2,4], [8,12]]))
print(is_conflicting_appointment([[4,5], [2,3], [3,6]]))

# follow up: Given a list of appointments, find all the conflicting appointments.
# Example:
# Appointments: [[4,5], [2,3], [3,6], [5,7], [7,8]]
# Output: 
# [4,5] and [3,6] conflict. 
# [3,6] and [5,7] conflict.

# O(N^2) space:O(N)
def conflicting_appointment(arr):
    start, end = 0, 1
    arr.sort(key = lambda x: x[0])
    result = []

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i][end] > arr[j][start]:
                result.append([arr[i], arr[j]])
    
    return result


print(conflicting_appointment([[1,4], [2,5], [7,9]]))
print(conflicting_appointment([[6,7], [2,4], [8,12]]))
print(conflicting_appointment([[4,5], [2,3], [3,6]]))
print(conflicting_appointment([[4,5], [2,3], [3,6], [5,7], [7,8]]))