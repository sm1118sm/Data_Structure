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
        return self._search_max_bst(self.root)

    def findMin(self):
        return self._search_min_bst(self.root)

    def search(self, key):
        return self._search_bst(self.root, key)

    def searchValue(self, value):
        return self._search_value_bst(self.root, value)

    def insert(self, key, value=None):
        new_node = BSTnode(key, value)
        self.root = self._insert_bst(self.root, new_node)

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

    def _search_max_bst(self, node):
        while node is not None and node.right is not None:
            node = node.right
        return node

    def _search_min_bst(self, node):
        while node is not None and node.left is not None:
            node = node.left
        return node

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
                successor = self._search_min_bst(node.right)
                node.key = successor.key
                node.value = successor.value
                node.right = self._delete_bst(node.right, successor.key)
        return node


data = [50, 30, 20, 40, 70, 60, 80, 10, 25, 65, 18]
value = ["오십", "삼십", "이십", "사십", "칠십", "육십", "팔십", "십", "이십오", "육오", "일팔"]

map = BSTMap()
map.display("[삽입 전] : ")

for i in range(len(data)):
    map.insert(data[i], value[i])
    map.display("[삽입 %2d] : " % data[i])

print('[최대 키] : ', map.findMax().key)
print('[최소 키] : ', map.findMin().key)
print('[탐색 26] : ', '성공' if map.search(26) is not None else '실패')
print('[탐색 25] : ', '성공' if map.search(25) is not None else '실패')
print('[탐색 일팔] : ', '성공' if map.searchValue("일팔") is not None else '실패')
print('[탐색 일칠] : ', '성공' if map.searchValue("일칠") is not None else '실패')

map.delete(10)
map.display("[삭제 10] : ")
map.delete(80)
map.display("[삭제 80] : ")
map.delete(30)
map.display("[삭제 30] : ")
map.delete(50)
map.display("[삭제 50] : ")
