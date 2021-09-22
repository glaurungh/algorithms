class MinHeap():
    def __init__(self):
        self._heap = []

    def getParentPosition(self, i):
        return (i-1)//2

    def getParent(self,i):
        return self._heap(self.getParentPosition(i))

    def getLeftChildPosition(self,i):
        return i*2+1

    def getRightChildPosition(self,i):
        return i*2+2

    def hasParent(self, i):
        return self.getParentPosition(i) < len(self._heap)

    def hasLeftChild(self, i):
        return self.getLeftChildPosition(i) < len(self._heap)

    def hasRightChild(self, i):
        return self.getRightChildPosition(i) < len(self._heap)

    def insert(self, key):
        self._heap.append(key)
        self.heapify(len(self._heap) - 1)

    def getMin(self):
        return self._heap[0]

    def heapify(self, i):
        while(self.hasParent(i) and self._heap[i] < self._heap[self.getParentPosition(i)]):
            self._heap[i], self._heap[self.getParentPosition(i)] = self._heap[self.getParentPosition(i)], self._heap[i]
            i = self.getParentPosition(i)

    def printHeap(self):
        print(self._heap)
