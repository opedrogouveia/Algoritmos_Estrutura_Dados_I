from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def addHead(self, value):
        nodo = Node(value)
        if self.head != None:
            nodo.prox = self.head
        self.head = nodo
        self.show()

    def addTail(self, value):
        nodo = Node(value)
        if self.head == None:
            self.head = nodo
        else:
            aux = self.head
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.show()

    def show(self):
        print("------------------------------------------")
        if self.head == None:
            print("None Linked List!")
        else:
            aux = self.head
            while aux:
                print(aux.data)
                aux = aux.prox

    def removeHead(self):
        if self.head == None:
            print("Could not be removed!")
        else:
            self.head = self.head.prox
        self.show()

    def removeTail(self):
        if self.head == None:
            print("Could not be removed!")
        elif self.head.prox == None:
            self.head = None
        else:
            prev = self.head
            aux = self.head.prox
            while aux.prox:
                prev = aux
                aux = aux.prox
            prev.prox = None
        self.show()
    
    def remove(self, value):
        found = False
        if self.head == None:
            print("None list!")
        elif self.head.data == value:
            self.head = self.head.prox
            found = True
        else:
            prev = self.head
            aux = self.head.prox
            while aux:
                if aux.data == value:
                    prev.prox = aux.prox
                    found = True
                    break
                prev = aux
                aux = aux.prox
        if not found:
            print("------------------------------------------")
            print(value + " not found.")
        self.show()