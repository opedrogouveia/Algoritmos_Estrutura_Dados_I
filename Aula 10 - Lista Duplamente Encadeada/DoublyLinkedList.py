from Node import Node

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addHead(self, value):
        nodo = Node(value)
        if self.head is None:
            self.head = nodo
            self.tail = nodo
        else:
            self.head.prev = nodo
            nodo.next = self.head
            self.head = nodo
        self.showForward()

    def addTail(self, value):
        nodo = Node(value)
        if self.head is None:
            self.head = nodo
            self.tail = nodo
        else:
            self.tail.next = nodo
            nodo.prev = self.tail
            self.tail = nodo
        self.showForward()

    def add(self, value, position):
        nodo = Node(value)
        if self.head is None:
            self.head = nodo
            self.tail = nodo
            return
        if position == 1:
            nodo.next = self.head
            self.head.prev = nodo
            self.head = nodo
            return
        current = self.head
        count = 1
        while current is not None and count < position - 1:
            current = current.next
            count += 1
        if current is None or current.next is None:
            print("Position out of bounds.")
            return
        nodo.next = current.next
        nodo.prev = current
        current.next.prev = nodo
        current.next = nodo
    
    def removeHead(self):
        if self.head is None:
            print("Could not be removed!")
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        self.showForward()

    def removeTail(self):
        if self.head is None:
            print("Could not be removed!")
        elif self.tail.prev is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.showForward()

    def remove(self, value):
        if self.head is None:
            print("Could not be removed!")
        else:
            found = False
            if value == self.head.data:
                self.head = self.head.next
                if self.head is not None:
                    self.head.prev = None
                found = True
            elif value == self.tail.data:
                self.tail = self.tail.prev
                if self.tail is not None:
                    self.tail.prox = None
                found = True
            else:
                current = self.head
                while current:
                    if value == current.data:
                        current.prev.next = current.next
                        if current.next is not None:
                            current.next.prev = current.prev
                        found = True
                        break
                    current = current.next
        if found:
            print(value, "was found and removed!")     
        else:
            print(value, "not found.")
        self.showForward()

    def showForward(self):
        print("\n--------------------------------")
        if self.head is None:
            print("List is empty!")
        else:
            current = self.head
            while current:
                print(current.data, end=" <-> " if current.next else "\n")
                current = current.next
    
    def showBackward(self):
        print("\n--------------------------------")
        if self.head is None:
            print("List is empty!")
        else:
            current = self.tail
            while current:
                print(current.data, end=" <-> " if current.prev else "\n")
                current = current.prev