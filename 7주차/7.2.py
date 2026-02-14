class Node:
    def __init__(self, value, link):
        self.value = value
        self.link = None

M = 17
table = [None] * M

#선형 조사법
def hashFn(key):
    return key% M

def insert(key):
    i = hashFn(key)
    count = M
    while count>0 :
        if table[i] == None:
            break
        i = (i+1) % M
        count -= 1

    if count > 0:
        table[i] = key

def search(key):
    i = hashFn(key)
    count = M
    while count >0:
        if table[i] == None:
            return None
        if table[i] == key:
            return table[i]
        i = (i + 1) % M
        count -= 1
    
    return None

def delete(key):
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == key:
            table[i] = -1
            return
        if table[i] == None or table[i] == -1:
            return
        i = (i+1) % M
        count -= 1

#이차 조사법
def insert_q(key):
    i = hashFn(key)
    j = 1
    count = M

    while count > 0:
        idx = (i + j*j) % M
        if table[idx] == None or table[idx] == -1:
            table[idx] = key
            return
        j += 1
        count -= 1

def search_q(key):
    i = hashFn(key)
    j = 0
    count = M

    while count > 0:
        idx = (i + j*j) % M
        if table[idx] == None:
            return None
        if table[idx] == key:
            return table[idx]
        j += 1
        count -= 1
    return None

def delete_q(key):
    i = hashFn(key)
    j = 0
    count = M

    while count > 0:
        idx = (i + j*j) % M
        if table[idx] == None:
            return
        if table[idx] == key:
            table[idx] = -1  # 삭제 마크
            return
        j += 1
        count -= 1

#이중 해싱법
def insert_c(key):
    k = hashFn(key)
    n = Node(key)
    n.link = table[k]
    table[k] = n

def search_c(key):
    k = hashFn(key)
    n = table[k]
    while n is not None:
        if n.data == key:
            return n.data
        n = n.link
    return None 

def delete_c(key):
    k = hashFn(key)
    n = table[k]
    before = None
    while n is not None:
        if n.data == key:
            if before == None :
                table[k] = n.link
            else:
                before.link = n.link
            return n.data
        before = n
        n = n.link
    


#선형 조사법 출력 결과

print("선형 조사법 출력 결과 : ")

for d in data:
    print("h(%d)=%2d"%(d,hashFn(d)),end=' ')
    insert(d)
    print(table)

print("2 탐색-->", search(2))
print("15 탐색-->", search(15))
print("25 탐색-->", search(25))

print("5 삭제-->", end='')
delete(5)
print(table)
print("12 삭제-->", end='')
delete(12)
print(table)
print()
print()

#이차 조사법 출력 결과
table = [None] * M
print("이차 조사법 출력 결과 : ")
for d in data:
    print("h(%d)=%2d"%(d,hashFn(d)), end=' ')
    insert_q(d)
    print(table)

print("2 탐색-->", search_q(2))
print("15 탐색-->", search_q(15))
print("25 탐색-->", search_q(25))

print("5 삭제-->", end='')
delete_q(5)
print(table)
print("12 삭제-->", end='')
delete_q(12)
print(table)
