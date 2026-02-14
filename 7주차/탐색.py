def sequential_search(A, key, low, high):
    for i in range(low, high + 1):
        if A[i].key == key:
            return i
    return None

def binary_search(A, key, low, high):
    if (low > high):
        return -1
    
    middle = (low + high) // 2

    if key == A[middle]:
        return middle
    elif key < A[middle]:
        return binary_search(A, key, low, middle - 1)
    else:
        return binary_search(A, key, middle + 1, high)
    
def binary_search_iter(A, key, low, high):
    while (low <= high):
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            high = middle - 1
        else:
            low = middle + 1
    return -1

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def mystery(p) :
    if p == None :
        print("p == None => return : 0")
        return 0
    elif p.left == None and p.right == None :
        print("p.left, p.right == None => return : ",p.data)
        return p.data 
    else:
        print("p.left :",p.left.data,"p.right : ",p.right.data)
        return max(mystery(p.left), mystery(p.right))
    
root = Node(3)
root.left = Node(5)
root.right = Node(1)
root.left.left = Node(4)
root.left.right = Node(2)
root.right.left = Node(8)
root.right.right = Node(6)

print(mystery(root))
