class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key),
        inorder(root.right)

# 숫자 배열
numbers = [11, 3, 4, 1, 56, 5, 6, 2, 98, 32, 23]

root = None
for number in numbers:
    root = insert(root, number)

# 중위 순회를 이용한 정렬 출력
inorder(root)
