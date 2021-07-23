# Given a number ‘n’, 
# write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

# Example 1:
# Input: 3
# Output: 5
# Explanation: Here are all the structurally unique BSTs storing all numbers from 1 to 3

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

# time: O(N^2) space: O(N)
def find_unique_trees(n):
    return find_unique_trees_recursive({}, n)


def find_unique_trees_recursive(map, n):
    if n in map:
        return map[n]
    
    if n == 0 or n == 1:
        return 1
    
    result = 0
    for i in range(n):
        result += find_unique_trees(i) * find_unique_trees(n - i - 1)
    
    return result

print(find_unique_trees(2))
print(find_unique_trees(3))

# O(N * 2^N) space: O(N * 2^N)

def draw_unique_binary_search_trees(n):
    if n <= 0:
        return []
    return draw_unique_binary_search_trees_recursive(1, n)

def draw_unique_binary_search_trees_recursive(start, end):
    result = []
    if start > end:
        result.append(None)
        return result
    
    for i in range(start, end + 1):
        left_part = draw_unique_binary_search_trees_recursive(start, i - 1)
        right_part = draw_unique_binary_search_trees_recursive(i + 1, end)
        
        for left in left_part:
            for right in right_part:
                root = TreeNode(i)
                root.left = left
                root.right = right
                result.append(root)
    
    return result

print(len(draw_unique_binary_search_trees(2)))
print(len(draw_unique_binary_search_trees(3)))