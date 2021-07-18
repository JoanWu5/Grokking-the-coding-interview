# Given a binary tree where each node can only have a digit (0-9) value, 
# each root-to-leaf path will represent a number. 
# Find the total sum of all the numbers represented by all paths.

# O(N) space:O(N)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def sum_of_path_numbers(current_node, path_sum):
    if current_node is None:
        return 0
    
    path_sum = path_sum * 10 + current_node.value
    if current_node.left is None and current_node.right is None:
        return path_sum
    
    return sum_of_path_numbers(current_node.left, path_sum) + sum_of_path_numbers(current_node.right, path_sum)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
print(sum_of_path_numbers(root, 0))