class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_complete_binary_tree(root):
    if not root:
        return True
    
    queue = [root]
    end = False
    
    while queue:
        node = queue.pop(0)
        
        if node:
            if end:
                return False
            queue.append(node.left)
            queue.append(node.right)
        else:
            end = True
    
    return True


root = TreeNode('A')
root.left = TreeNode('B')
root.right = TreeNode('C')
print(is_complete_binary_tree(root))