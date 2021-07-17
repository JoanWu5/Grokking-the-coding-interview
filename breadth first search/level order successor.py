# Given a binary tree and a node, find the level order successor of the given node in the tree. 
# The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def level_order_successor(root, key):
    if root is None:
        return None
    
    queue = deque()
    queue.append(root)
    while queue:
        current_node = queue.popleft()
        if current_node.left:
            queue.append(current_node.left)
            
        if current_node.right:
            queue.append(current_node.right)

        if current_node.value == key:
            break
    
    return queue[0].value if queue else None

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(level_order_successor(root, 12))
print(level_order_successor(root, 9))

