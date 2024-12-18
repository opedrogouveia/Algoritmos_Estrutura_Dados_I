from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, value):
        nodo = Node(value)
        if self.head != None:
            nodo.next = self.head
        self.head = nodo
        self.show()

    def addTail(self, value):
        nodo = Node(value)
        if self.head == None:
            self.head = nodo
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = nodo
        self.show()

    def show(self):
        print("------------------------------------------")
        if self.head == None:
            print("None Linked List!")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def removeHead(self):
        if self.head == None:
            print("Could not be removed!")
        else:
            self.head = self.head.next
        self.show()

    def removeTail(self):
        if self.head == None:
            print("Could not be removed!")
        elif self.head.next == None:
            self.head = None
        else:
            prev = self.head
            current = self.head.next
            while current.next:
                prev = current
                current = current.next
            prev.next = None
        self.show()
    
    def remove(self, value):
        found = False
        if self.head == None:
            print("None list!")
        elif self.head.data == value:
            self.head = self.head.next
            found = True
        else:
            prev = self.head
            current = self.head.next
            while current:
                if current.data == value:
                    prev.next = current.next
                    found = True
                    break
                prev = current
                current = current.next
        if not found:
            print("------------------------------------------")
            print(value + " not found.")
        self.show()