# Given a binary tree and a number ‘S’, 
# find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

# O(N) space:O(N)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None
    
def binary_tree_path_sum(root, sum_value):
    if root is None:
        return False
    
    if root.value == sum_value and root.left is None and root.right is None:
        return True
    
    return binary_tree_path_sum(root.left, sum_value - root.value) or binary_tree_path_sum(
        root.right, sum_value - root.value)


root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(binary_tree_path_sum(root, 23))
print(binary_tree_path_sum(root, 16))
