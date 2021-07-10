# Given two lists of intervals, find the intersection of these two lists. 
# Each list consists of disjoint intervals sorted on their start time.

# Example:
# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.

def interval_intersection(arr1, arr2):
    i, j = 0, 0
    start, end = 0, 1
    result = []
    while i < len(arr1) and j < len(arr2):
        if ((arr1[i][start] >= arr2[j][start] and arr1[i][start] <= arr2[j][end])
        or (arr2[j][start] >= arr1[i][start] and arr2[j][start] <= arr1[i][end])):
            result.append([max(arr1[i][start], arr2[j][start]), min(arr1[i][end], arr2[j][end])])

        if arr1[i][end] < arr2[j][end]:
            i += 1
        else:
            j += 1
    
    return result

print(interval_intersection([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
print(interval_intersection([[1, 3], [5, 7], [9, 12]], [[5, 10]]))

