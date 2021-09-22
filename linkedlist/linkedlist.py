class Node:
    # constructor
    def __init__(self, data = None, next=None): 
        self._data = data
        self._next = next

class LinkedList:
    def __init__(self):
        self._length = 1
        self._head = None

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self._head
            while(current._next):
                current = current._next
            current._next = newNode
        else:
            self._head = newNode

    def printLL(self):
        current = self._head
        while (current):
            print(current._data)
            current = current._next

#    def pop(self, data):

