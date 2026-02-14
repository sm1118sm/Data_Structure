class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

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

class BSTMap():
    def __init_ (self):
        self.root = None
    def isEmpty (self):
        return self.root == None
    def findMax (self):
        return search_max_bst(self.root)
    def findMin(self):
        return search_min_bst(self.root)
    def search(self, key):
        return search_bst(self.root, key)
    def searchValue(self, value):
        return search_value_bst(self.root, value)
    def insert(self, key, value=None):
        n = BSTNode (key, value)
        self.root = insert_bst(self.root, n)
    def delete(self, key):
        self.root = delete_bst(self.root, key)
    def display(self, msg = 'BTSMap :'):
        print(msg, end='') 
        inorder(self.root)
        print()
