# Given a set of numbers that might contain duplicates, find all of its distinct subsets.
# Example:
# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]

# O(2^N) space: O(2^N)
def find_subsets_with_duplicates(arr):
    arr.sort()
    subsets = []
    subsets.append([])
    start_index, end_index = 0, 0
    for i in range(len(arr)):
        start_index = 0
        if i > 0 and arr[i] == arr[i - 1]:
            start_index = end_index + 1
        
        end_index = len(subsets) - 1
        for j in range(start_index, end_index + 1):
            subset = list(subsets[j])
            subset.append(arr[i])
            subsets.append(subset)
    
    return subsets

print(find_subsets_with_duplicates([1, 3, 3]))
print(find_subsets_with_duplicates([1, 5, 5, 3, 3]))