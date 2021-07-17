# Given a binary tree, return an array containing nodes in its right view. 
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

# O(N) space:O(N)
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def right_view_of_a_binary_tree(root):
    result = []
    if root is None:
        return result
    
    queue = deque()
    queue.append(root)

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            current_node = queue.popleft()
            if i == level_size - 1:
                result.append(current_node.value)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
    
    return result

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
root.left.left.right = TreeNode(3)
print(right_view_of_a_binary_tree(root))

# follow up:
# Problem 1: Given a binary tree, return an array containing nodes in its left view. 
# The left view of a binary tree is the set of nodes visible when the tree is seen from the left side.

# Solution: We will be following a similar approach, 
# but instead of appending the last element of each level we will be appending 
# the first element of each level to the output array.
# if i == 0: result.append(current_node.value)