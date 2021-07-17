# Find the minimum depth of a binary tree.
# The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
    
def minimum_depth(root):
    if root is None:
        return 0
    
    min_level = 0
    queue = deque()
    queue.append(root)
    
    while queue:
        min_level += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left is None and current_node.right is None:
                return min_level

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return min_level

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(minimum_depth(root))

# follow up:
# Problem 1: Given a binary tree, find its maximum depth (or height).
def maximum_depth(root):
    if root is None:
        return 0
    
    max_level = 0
    queue = deque()
    queue.append(root)
    
    while queue:
        max_level += 1
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return max_level

print(maximum_depth(root))