from queue import Queue

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):
    if root is None:
        return
    queue = Queue()
    queue.put(root)
    while not queue.empty():
        n = queue.get()
        if n is not None:
            print(n.data, end=' ')
            # 왼쪽 자식과 오른쪽 자식을 큐에 추가
            if n.left is not None:
                queue.put(n.left)
            if n.right is not None:
                queue.put(n.right)

#노드 개수
def count_node(n):
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right)
    
#단말 노드 개수
def count_leaf(n):
    if n is None:
        return 0
    elif n.left is None and n.right is None:
        return 1
    else:
        return count_leaf(n.left) + count_leaf(n.right)

#트리 높이
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if hLeft > hRight:
        return hLeft + 1
    else:
        return hRight + 1

# 예제 노드 생성
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# 레벨 오더 출력
levelorder(root)