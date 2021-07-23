# Given a set with distinct elements, find all of its distinct subsets.

# Example:
# Input: [1, 3]
# Output: [], [1], [3], [1,3]

# O(2^N) in each step, the number of subsets doubles as we add each element to all the existing subsets
# space: O(2^N)
def find_subsets(arr):
    subsets = []
    subsets.append([])
    for current_num in arr:
        n = len(subsets)
        for i in range(n):
            subset = list(subsets[i]) # create a new subset
            subset.append(current_num)
            subsets.append(subset)
    
    return subsets

print(find_subsets([1, 3]))
print(find_subsets([1, 3, 5]))