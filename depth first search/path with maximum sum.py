# Find the path with the maximum sum in a given binary tree. 
# Write a function that returns the maximum sum. 
# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.

import math

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

class MaximumPathSum:
    def find_maximum_path_sum(self, root):
        self.result = -math.inf
        self.caculate_sum(root)
        return self.result

    def caculate_sum(self, current_node):
        if current_node is None:
            return 0
        
        max_path_sum_left = self.caculate_sum(current_node.left)
        max_path_sum_right = self.caculate_sum(current_node.right)

        max_path_sum_left = max(max_path_sum_left, 0)
        max_path_sum_right = max(max_path_sum_right, 0)

        local_max_sum = max_path_sum_left + max_path_sum_right + current_node.value
        self.result = max(self.result, local_max_sum)

        return max(max_path_sum_left, max_path_sum_right) + current_node.value

maximumPathSum = MaximumPathSum()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
print(maximumPathSum.find_maximum_path_sum(root))

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
root.right.left.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print(maximumPathSum.find_maximum_path_sum(root))

root = TreeNode(-1)
root.left = TreeNode(-2)
print(maximumPathSum.find_maximum_path_sum(root))
