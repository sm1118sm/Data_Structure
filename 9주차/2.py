
class BSTnode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BSTMap:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def findMax(self):
        return self._search_max_bst1(self.root)

    def findMin(self):
        return self._search_min_bst1(self.root)

    def search(self, key):
        return self._search_bst(self.root, key)

    def searchValue(self, value):
        return self._search_value_bst(self.root, value)

    #삽입 연산을 반복 구조를 이용해 다시 구현하라.
    def insert_new(self, key, value=None):
        new_node = BSTnode(key, value)
        
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if key < current.key:
                if current.left is None:
                    current.left = new_node
                    break
                current = current.left
            elif key > current.key:
                if current.right is None:
                    current.right = new_node
                    break
                current = current.right
            else:
                break

    def delete(self, key):
        self.root = self._delete_bst(self.root, key)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(f"{node.key}", end=' ')
            self.inorder(node.right)

    def display(self, msg='BSTMap: '):
        print(msg, end='')
        self.inorder(self.root)
        print()

    def _search_bst(self, node, key):
        if node is None:
            return None
        elif key == node.key:
            return node
        elif key < node.key:
            return self._search_bst(node.left, key)
        else:
            return self._search_bst(node.right, key)

    def _search_value_bst(self, node, value):
        if node is None:
            return None
        if node.value == value:
            return node
        left_result = self._search_value_bst(node.left, value)
        if left_result is not None:
            return left_result
        return self._search_value_bst(node.right, value)
    
    # 최대 키를 가진 노드를 탐색하는 함수를 순환구조를 이용해 다시 구현하라
    def _search_max_bst1(self, node):
        if node is None:
            return None
        elif node.right is None:
            return node
        return self._search_max_bst1(node.right)


    # 최소 키를 가진 노드를 탐색하는 함수를 순환구조를 이용해 다시 구현하라
    def _search_min_bst1(self, node):
        if node is None:
            return None
        elif node.left is None:
            return node
        return self._search_min_bst1(node.left)

    def _insert_bst(self, node, new_node):
        if node is None:
            return new_node
        if new_node.key < node.key:
            node.left = self._insert_bst(node.left, new_node)
        elif new_node.key > node.key:
            node.right = self._insert_bst(node.right, new_node)
        return node

    def _delete_bst(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete_bst(node.left, key)
        elif key > node.key:
            node.right = self._delete_bst(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None

            elif node.left is None:
                return node.right

            elif node.right is None:
                return node.left

            else:
                successor = self._search_min_bst1(node.right) 
                node.key = successor.key
                node.value = successor.value
                node.right = self._delete_bst(node.right, successor.key)

        return node



data = [55, 20, 35, 45, 75, 62, 90, 5, 32, 77]
value = ["오십오", "이십", "삼십오", "사십오", "칠십오", "육십이", "구십", "오", "삼십이", "칠십칠"]

map = BSTMap()
map.display("[삽입 전] : ")
for i in range(len(data)):
    map.insert_new(data[i], value[i])
    map.display("[삽입 %2d] : " % data[i])

print('[탐색 33] : ', '성공' if map.search(33) is not None else '실패')
print('[탐색 32] : ', '성공' if map.search(32) is not None else '실패')
print('[탐색 "육십이"] : ', '성공' if map.searchValue("육십이") is not None else '실패')
print('[탐색 "사십이"] : ', '성공' if map.searchValue("사십이") is not None else '실패')

print("\n[테스트] 최대/최소 키 탐색")
max_node = map.findMax()
min_node = map.findMin()

if max_node is not None:
    print("최대 키:", max_node.key, ", 값:", max_node.value)
else:
    print("최대 키 노드가 없습니다.")

if min_node is not None:
    print("최소 키:", min_node.key, ", 값:", min_node.value)
else:
    print("최소 키 노드가 없습니다.")

map.delete(20)
map.display("[삭제 20] : ")
map.delete(62)
map.display("[삭제 62] : ")
map.delete(32)  
map.display("[삭제 32] : ")
map.delete(55)
map.display("[삭제 55] : ")
