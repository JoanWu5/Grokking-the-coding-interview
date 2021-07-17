# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to a null node.

# O(N) space:O(N)
from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.next = None
    
    def print_level_order(self):
        level_node_root = self
        while level_node_root:
            current_node = level_node_root
            level_node_root = None
            while current_node:
                print(str(current_node.value) + "", end="")
                if level_node_root is None:
                    if current_node.left:
                        level_node_root = current_node.left
                    elif current_node.right:
                        level_node_root = current_node.right
                
                current_node = current_node.next
            print()

def connect_level_order_siblings(root):
    if root is None:
        return root
    
    queue = deque()
    queue.append(root)

    while queue:
        previous_node = None
        level_size = len(queue)
        for _ in range(level_size):
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            
            if previous_node:
                previous_node.next = current_node
            else:
                previous_node = current_node
    

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
connect_level_order_siblings(root)
root.print_level_order()