# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to the first node of the next level.

# O(N) space:O(N)
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.next = None
    
    def print_tree(self):
        current = self
        while current:
            print(str(current.value) + " ", end = "")
            current = current.next
        print()

def connect_all_level_order_siblings(root):
    if root is None:
        return
    
    queue = deque()
    queue.append(root)

    previous_node = None
    while queue:
        current_node = queue.popleft()
        
        if previous_node:
            previous_node.next = current_node
        previous_node = current_node

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return
    
root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_all_level_order_siblings(root)
root.print_tree()