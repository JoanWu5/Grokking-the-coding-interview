# Given a binary tree, populate an array to represent its level-by-level traversal. 
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.

# O(N)
# space: O(N)
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None
    
def traverse(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(current_level)
    return result

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(traverse(root))