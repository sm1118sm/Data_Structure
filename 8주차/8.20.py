class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def level(root, node):
    if not root:
        return 0
    
    queue = [(root, 1)]
    
    while queue:
        current, lvl = queue.pop(0)
        
        if current == node:
            return lvl
        
        if current.left:
            queue.append((current.left, lvl + 1))
        if current.right:
            queue.append((current.right, lvl + 1))
    
    return 0

root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
root.left.left = TreeNode('C')
root.left.right = TreeNode('D')
root.left.right.left = TreeNode('H')
root.right.left = TreeNode('F')
root.right.left.left = TreeNode('G')
target_node = root.right.left.left
print(level(root, target_node))