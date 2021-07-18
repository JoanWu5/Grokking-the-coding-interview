# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

# O(N) space:O(N)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def find_path(root, sequence):
    if root is None:
        return len(sequence) == 0
    
    return find_path_with_sequence(root, sequence, 0)

def find_path_with_sequence(current_node, sequence, sequence_index):
    if current_node is None:
        return False
    
    if sequence_index >= len(sequence) or current_node.value != sequence[sequence_index]:
        return False
    
    if current_node.left is None and current_node.right is None and sequence_index == len(sequence) - 1:
        return True
    
    return find_path_with_sequence(current_node.left, sequence, sequence_index + 1) or \
        find_path_with_sequence(current_node.right, sequence, sequence_index + 1)

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(9)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(find_path(root, [12, 7, 9]))
print(find_path(root, [12, 10, 6]))
