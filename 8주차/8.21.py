class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_balanced(root):
    def check_height(node):
        if node is None:
            return 0
        
        left_height = check_height(node.left)
        right_height = check_height(node.right)
        
        if left_height == -1 or right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1

    return check_height(root) != -1

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('E')
root.left.left = TreeNode('C')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('H')
root.right.left = TreeNode('F')
root.right.left.left = TreeNode('G')

print(is_balanced(root))