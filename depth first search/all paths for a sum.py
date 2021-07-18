# Given a binary tree and a number ‘S’, 
# find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

# O(N^2) best time: O(NlogN)
# space: O(N) best: O(logN)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def all_paths_for_a_sum(current_node, sum_value, current_path, all_paths):
    if current_node is None:
        return

    current_path.append(current_node.value)
    if current_node.value == sum_value and current_node.left is None and current_node.right is None:
        all_paths.append(current_path.copy()) # must use copy, or the array will be empty in the end
    else:
        all_paths_for_a_sum(current_node.left, sum_value - current_node.value, current_path, all_paths)
        all_paths_for_a_sum(current_node.right, sum_value - current_node.value, current_path, all_paths)

    current_path.pop()
    return

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
all_paths = []
all_paths_for_a_sum(root, 23, [], all_paths)
print(all_paths)

# follow up :
# Problem 1: Given a binary tree, return all root-to-leaf paths.
# Solution: We can follow a similar approach. We just need to remove the “check for the path sum”.

# Problem 2: Given a binary tree, find the root-to-leaf path with the maximum sum.
# Solution: We need to find the path with the maximum sum. 
# As we traverse all paths, we can keep track of the path with the maximum sum.

    
