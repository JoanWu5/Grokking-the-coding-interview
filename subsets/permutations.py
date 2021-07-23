# Given a set of distinct numbers, find all of its permutations.

# Permutation is defined as the re-arranging of the elements of the set. 
# For example, {1, 2, 3} has the following six permutations:
# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have n!n! permutations.

# Example:
# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

# O(N * N!) space: O(N * N!)
from collections import deque

def permutations(arr):
    num_length = len(arr)
    result = []
    permutations = deque()
    permutations.append([])
    for current_num in arr:
        n = len(permutations)
        for _ in range(n):
            old_permutation = permutations.popleft()
            for j in range(len(old_permutation) + 1):
                new_permutataion = list(old_permutation)
                new_permutataion.insert(j, current_num)
                if len(new_permutataion) == num_length:
                    result.append(new_permutataion)
                else:
                    permutations.append(new_permutataion)
    
    return result

print(permutations([1, 3, 5]))
            
def recursive_permutation(arr):
    result = []
    generate_permutations_recursive(arr, 0, [], result)
    return result

def generate_permutations_recursive(arr, index, current_permutation, result):
    if index == len(arr):
        result.append(current_permutation)
    else:
        for i in range(len(current_permutation) + 1):
            new_permutation = list(current_permutation)
            new_permutation.insert(i, arr[index])
            generate_permutations_recursive(arr, index + 1, new_permutation, result)


print(recursive_permutation([1, 3, 5]))
