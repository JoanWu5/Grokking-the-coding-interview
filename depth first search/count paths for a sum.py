# Given a binary tree and a number ‘S’, 
# find all paths in the tree such that the sum of all the node values of each path equals ‘S’. 
# Please note that the paths can start or end at any node 
# but all paths must follow direction from parent to child(top to bottom).

# worst: O(N^2) best:O(NlogN)
# space: O(N)
class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def count_paths(root, sum_value):
    return count_paths_recursive(root, sum_value, [])

def count_paths_recursive(current_node, sum_value, current_path):
    if current_node is None:
        return 0
    
    current_path.append(current_node.value)
    path_count, path_sum = 0, 0
    for i in range(len(current_path)-1, -1, -1):
        path_sum += current_path[i]

        if path_sum == sum_value:
            path_count += 1
    
    path_count += count_paths_recursive(current_node.left, sum_value, current_path)
    path_count += count_paths_recursive(current_node.right, sum_value, current_path)

    del current_path[-1]
    return path_count

root = TreeNode(12)
root.left = TreeNode(7)
root.right = TreeNode(1)
root.left.left = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(5)
print(count_paths(root, 11))


