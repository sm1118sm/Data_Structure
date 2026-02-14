class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def total_path_length(root):
    def calculate_path_length(node, current_length):
        if node is None:
            return 0
        
        
        total_length = current_length
        total_length += calculate_path_length(node.left, current_length + 1)
        total_length += calculate_path_length(node.right, current_length + 1)
        return total_length

    return calculate_path_length(root, 0)


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')

print(total_path_length(root))