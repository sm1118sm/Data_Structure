class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

#이진탐색트리 탐색연산(순환 함수)
def search_bts(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bts(n.left, key)
    else:
        return search_bts(n.right, key)
    
#이진탐색트리 탐색연산(반복 함수)
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n = n.left
        else:
            n = n.right
    return None

#이진탐색트리 삽입 연산
#root 트리에 node 삽입
def insert_bst(root, node):
    if root == None:
        return node
    if node.key == root.key:
        return root
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else : 
        root.right = insert_bst(root.right, node)
    return root