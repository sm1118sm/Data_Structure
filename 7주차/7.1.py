# 정렬된 리스트를 이용한 집합
class SetSorted:
    def __init__(self):
        self.array = []
    
    def size(self):
        return len(self.array)
    
    def contains(self, e):
        left, right = 0, self.size() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.array[mid] == e:
                return True
            elif self.array[mid] < e:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    def insert(self, e):
        if self.contains(e):
            return
        self.array.append(e)
        
        for i in range(self.size()-1, 0, -1):
            if self.array[i-1] <= self.array[i]:
                break
            self.array[i-1], self.array[i] = self.array[i], self.array[i-1]

    def delete(self, e):
        if not self.contains(e):
            return
        self.array.remove(e)

    def display(self, msg):
        print(msg, self.array)
    
    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for i in range(self.size()):
            if self.array[i] != setB.array[i]:
                return False
        return True

    def union(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.array[i], setB.array[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                setC.insert(b)
                j += 1
            
        while i < self.size():
            setC.insert(self.array[i])
            i += 1

        while j < setB.size():
            setC.insert(setB.array[j])
            j += 1

        return setC
    
    def intersect(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.array[i], setB.array[j]
            if a == b:
                setC.insert(a)
                i += 1
                j += 1
            elif a < b:
                i += 1
            else:
                j += 1
        return setC
    
    def difference(self, setB):
        setC = SetSorted()
        i, j = 0, 0
        while i < self.size() and j < setB.size():
            a, b = self.array[i], setB.array[j]
            if a == b:
                i += 1
                j += 1
            elif a < b:
                setC.insert(a)
                i += 1
            else:
                j += 1
        while i < self.size():
            setC.insert(self.array[i])
            i += 1
        return setC

# 정렬되지 않은 리스트를 이용한 집합
class ArraySet:
    def __init__(self):
        self.array = []
        self.size = 0
    
    def is_empty(self):
        return self.size == 0
    
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    def insert(self, e):
        if not self.contains(e):
            self.array.append(e)
            self.size += 1

    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return

    def display(self, msg):
        print(msg, self.array)
    
    def __eq__(self, setB):
        if self.size != setB.size:
            return False
        for i in range(self.size):
            if self.array[i] != setB.array[i]:
                return False
        return True

    def union(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            setC.insert(self.array[i])
        for i in range(setB.size):
            if not setC.contains(setB.array[i]):
                setC.insert(setB.array[i])
        return setC
    
    def intersect(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC
    
    def difference(self, setB):
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])
        return setC

setA = SetSorted()
setA.insert(3)
setA.insert(2)
setA.insert(1)
setA.insert(4)
setA.insert(6)
setA.insert(7)
setA.insert(5)
setA.display("정렬된 집합 A:")

setB = SetSorted()
setB.insert(2)
setB.insert(1)
setB.insert(8)
setB.display("정렬된 집합 B:")

setC = setA.union(setB)
setC.display("A와 B 합집합:")

setD = setA.intersect(setB)
setD.display("A와 B 교집합:")

setE = setA.difference(setB)
setE.display("A와 B 차집합")

print("A가 1 포함?:", setA.contains(1))
print("A가 2 포함?:", setA.contains(2))
print("A 와 B는 같다:", setA == setB)

setF = ArraySet()
setF.insert(1)
setF.insert(5)
setF.insert(9)
setF.insert(2)
setF.display("정렬되지않은 집합 F")

setG = ArraySet()
setG.insert(2)
setG.insert(1)
setG.insert(15)
setG.insert(6)
setG.display("정렬되지않은 집합 G")

setV = setF.union(setG)
setV.display("F와 G 합집합:")

setM = setF.intersect(setG)
setM.display("F와 G 교집합:")

setL = setF.difference(setG)
setL.display("F와 G 차집합")

print("F가 1 포함?:", setF.contains(1))
print("G가 2 포함?:", setG.contains(2))
print("F 와 G는 같다:", setF == setG)