# Given a binary tree, populate an array to represent the averages of all of its levels.

# O(N) space:O(N)
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def level_average(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        sum_level = 0.0
        level_size = len(queue)

        for _ in range(level_size):
            current_node = queue.popleft()

            sum_level += current_node.value

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(sum_level/level_size)
    
    return result

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(level_average(root))

# follow up:
# Problem 1: Find the largest value on each level of a binary tree.

# Solution: We will follow a similar approach, 
# but instead of having a running value we will track the maximum value of each level.
# maxValue = max(maxValue, currentNode.val)