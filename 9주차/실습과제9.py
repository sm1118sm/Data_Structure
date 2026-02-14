class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
        return self.root == None
    
    def findMax (self):
        return search_max_bst2(self.root)
    
    def findMin(self):
        return search_min_bst2(self.root)
    
    def search(self, key):
        return search_bst(self.root, key)
    
    def searchValue(self, value):
        return search_value_bst(self.root, value)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        self.root = insert_bst2(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def display(self, msg = 'BTSMap :'):
        print(msg, end="") 
        inorder(self.root)
        print()

#우선순위 큐 클래스
class PriorityQueue:
    def __init__(self):
        self.bst = BSTMap()

    def isEmpty(self):
        return self.bst.isEmpty()

    def insert(self, key, value=None):
        self.bst.insert(key, value)

    def delete(self):
        if self.isEmpty():
            print("우선순위 큐가 비어있습니다.")
            return None
        max_node = self.bst.findMax()
        self.bst.delete(max_node.key)
        return max_node

    def peek(self):
        if self.isEmpty():
            print("우선순위 큐가 비어있습니다.")
            return None
        return self.bst.findMax()
    
    def display(self):
        self.bst.display()

def inorder(node):
    if node is not None:
        inorder(node.left)
        print(f'{node.key}', end=" ")
        inorder(node.right)

#최대값 탐색 반복적 방법
def search_max_bst(n) :
    while n != None and n.right != None:
        n = n.right
    return n
#최소값 탐색 반복적 방법
def search_min_bst(n) :
    while n != None and n.left != None:
        n = n.left
    return n

#최대값 탐색 재귀적 방법
def search_max_bst2(n):
    if n == None or n.right == None:
        return n
    return search_max_bst(n.right)

#최소값 탐색 재귀적 방법
def search_min_bst2(n):
    if n == None or n.left == None:
        return n
    return search_min_bst(n.left)

#이진탐색트리의 탐색 연산(순환 구조)
def search_bst(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left, key)
    else:
        return search_bst(n.right, key)

#이진탐색트리의 탐색 연산(반복 구조)    
def search_bst_iter(n, key):
    while n != None:
        if key == n.key:
            return n
        
        elif key < n.key:
            n = n.left
            
        else:
            n = n.right
            
    return None

def search_value_bst(n, value) :
    if n == None : return None
    elif value == n.value:
        return n
    res = search_value_bst(n.left, value)
    if res is not None :
        return res
    else :
        return search_value_bst(n.right, value)

#삽입 재귀적 방법
def insert_bst(root, node):
    if root == None:
        return node
    
    if node.key == root.key:
        return root
    
    if node.key < root.key:
        root.left = insert_bst(root.left,node)
    else:
        root.right = insert_bst(root.right, node)
        
    return root

#삽입 반복적 방법
def insert_bst2(root, node):
    if root == None:
        return node

    current = root
    parent = None

    while True:
        parent = current
        if node.key < current.key:
            current = current.left
            if current == None:
                parent.left = node
                return root
        else:
            current = current.right
            if current == None:
                parent.right = node
                return root

def delete_bst (root, key) :
    #공백 트리
    if root == None :
        return root
    
    #왼쪽 서브트리 이동
    if key < root.key :
        root.left = delete_bst (root.left, key)
    
    #오른쪽 서브트리 이동
    elif key > root.key :
        root.right = delete_bst(root.right, key)
    
    #key 값 루트의 key와 같을 떼
    else :
        #단말 노드 경우
        #오른쪽 자식만 있는 경우
        if root.left == None :
            return root.right
        #왼쪽 자식만 있는 경우
        if root.right == None :
            return root.left
        #두 자식 모두 있는 경우
        succ = search_min_bst(root.right)
        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)
    return root

# 테스트 코드
pq = PriorityQueue()
# 삽입 연산 테스트
pq.insert(50, "오십")
print("오십 insert")
pq.display()
print()
pq.insert(40, "사십")
print("사십 insert")
pq.display()
print()
pq.insert(30, "삼십")
print("삼십 insert")
pq.display()
print()
pq.insert(20, "이십")
print("이십 insert")
pq.display()
print()
# peek 연산 테스트
print("피크 연산: ", pq.peek().value)  # 오십
pq.display()
print()

# 삭제 연산 테스트
print("삭제 연산: ", pq.delete().value)  # 오십
pq.display()
print()
print("피크 연산: ", pq.peek().value)  # 사십
pq.display()
print()
print("삭제 연산: ", pq.delete().value)  # 사십
pq.display()
print() 
print("피크 연산: ", pq.peek().value)  # 삼십
pq.display()
print()

 # 삽입 테스트
data = [60, 30, 90, 20, 40, 70, 100, 10, 50, 80, 110]
value=["육십", "삼십", "구십", "이십", "사십", "칠십", "백", "십", "오십", "팔십", "백십"]

map = BSTMap()  # 새로운 맵 생성

for i in range(len(data)) :
    map.insert(data[i],value[i])
    map.display("[삽입 %2d] : "%data[i])

    # 최대, 최소 키 탐색 테스트
    print('[최대 키] :', map.findMax().key)
    print('[최소 키] :', map.findMin().key)

    # 키를 이용한 탐색 테스트
    print('[탐색 120] :', '성공' if map.search(120) != None else '실패')
    print('[탐색 80] :', '성공' if map.search(80) != None else '실패')

    # 값(value)를 이용한 탐색 테스트
    print('[탐색 백]:', '성공' if map.searchValue("백") != None else '실패')
    print('[탐색 백십]:', '성공' if map.searchValue("백십") != None else '실패')

    # 삽입 테스트 (중복된 키, 새로운 키)
    map.insert(120,"백이십")
    map.display("[삽입 %2d] : "%120)
    map.insert(60,"육십")
    map.display("[삽입 %2d] : "%60)
    map.insert(130,"백삼십")
    map.display("[삽입 %2d] : "%130)

    # 삭제 테스트 (있는 키, 없는 키)
    map.delete(140)   
    map.display("[삭제 140] : ") 
    map.delete(60)
    map.display("[삭제 60] : ") 
    map.delete(130)
    map.display("[삭제 130] : ")
    map.delete(120)  
    map.display("[삭제 120] : ")

data = [11, 3, 4, 1, 56, 5, 6, 2, 98, 32, 23]

map = BSTNode(11)  # 새로운 맵 생성
for i in range(1, len(data)) :
    insert_bst(map, BSTNode(data[i]))
    

