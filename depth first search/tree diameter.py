# Given a binary tree, find the length of its diameter. 
# The diameter of a tree is the number of nodes on the longest path between any two leaf nodes. 
# The diameter of a tree may or may not pass through the root.
# Note: You can always assume that there are at least two leaf nodes in the given tree.

# O(N) space:O(N)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def find_diameter(root):
    result = [0]
    caculate_height(root, result)
    return result[0]


def caculate_height(current_node, result):
    if current_node is None:
        return 0
    
    left_tree_height = caculate_height(current_node.left, result)
    right_tree_height = caculate_height(current_node.right, result)

    diameter = left_tree_height + right_tree_height + 1
    result[0] = max(result[0], diameter)

    return max(left_tree_height, right_tree_height) + 1

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(find_diameter(root))

head = TreeNode(12)
head.left = TreeNode(7)
head.right = TreeNode(1)
head.right.left = TreeNode(10)
head.right.right = TreeNode(5)
head.right.left.left = TreeNode(6)
head.right.left.right = TreeNode(8)
head.right.right.right = TreeNode(9)
head.right.left.right.right = TreeNode(11)
head.right.right.right.right = TreeNode(13)
print(find_diameter(head))