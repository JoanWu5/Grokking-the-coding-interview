# Given a binary tree, populate an array to represent its zigzag level order traversal. 
# You should populate the values of all nodes of the first level from left to right, 
# then right to left for the next level and 
# keep alternating in the same manner for the following levels.

# O(N) space:O(N)
from collections import deque


class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def zigzag_traversal(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)
    flag = True
    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            current_node = queue.popleft()
            
            if flag:
                current_level.append(current_node.value)
            else:
                current_level.insert(0, current_node.value)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
        result.append(current_level)
        flag = not flag
    
    return result

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(zigzag_traversal(root))
