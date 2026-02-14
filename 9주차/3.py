class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# 노드 높이 계산
def height(n):
    if n is None:
        return 0
    return 1 + max(height(n.left), height(n.right))


# 높이 차이 (balance factor)
def calc_height_diff(n):
    if n is None:
        return 0
    return height(n.left) - height(n.right)


# 회전 연산들
def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateLR(A):
    A.left = rotateRR(A.left)
    return rotateLL(A)

def rotateRL(A):
    A.right = rotateLL(A.right)
    return rotateRR(A)


# AVL 삽입 연산
def insert_avl(root, node):
    if root is None:
        return node

    if node.key < root.key:
        root.left = insert_avl(root.left, node)
    elif node.key > root.key:
        root.right = insert_avl(root.right, node)
    else:
        return root  # 중복 방지

    # 불균형 확인
    bf = calc_height_diff(root)

    # 왼쪽이 무거운 경우
    if bf > 1:
        if node.key < root.left.key:
            return rotateLL(root)
        else:
            return rotateLR(root)

    # 오른쪽이 무거운 경우
    if bf < -1:
        if node.key < root.right.key:
            return rotateRL(root)
        else:
            return rotateRR(root)

    return root


# 중위 순회 (정렬된 출력 확인용)
def inorder(n):
    if n:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

root = None
data = [45, 5, 10, 31, 21, 55]

for key in data:
    print(f"\n[삽입 {key}]")
    node = Node(key)
    root = insert_avl(root, node)
    
    print("현재 중위순회:", end=' ')
    inorder(root)
    print()
print("\n최종 트리 중위순회 결과:")
inorder(root)
print("\nAVL 트리 높이:", height(root))