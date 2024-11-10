from Node import Node

class LinkedList:
    def __init__(self):
        self.start = None

    def addStart(self, value):
        nodo = Node(value)
        if self.start != None:
            nodo.prox = self.start
        self.start = nodo
        self.show()

    def addLast(self, value):
        nodo = Node(value)
        if self.start == None:
            self.start = nodo
        else:
            aux = self.start
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.show()

    def show(self):
        print("------------------------------------------")
        if self.start == None:
            print("\nNone Linked List!")
        else:
            aux = self.start
            while aux:
                print(aux.data)
                aux = aux.prox

    def removeStart(self):
        if self.start == None:
            print("Could not be removed!")
        else:
            self.start = self.start.prox
        self.show()

    def removeLast(self):
        if self.start == None:
            print("Could not be removed!")
        elif self.start.prox == None:
            self.start = None
        else:
            prev = self.start
            aux = self.start.prox
            while aux.prox:
                prev = aux
                aux = aux.prox
            prev.prox = None
        self.show()
    
    def remove(self, value):
        found = False
        if self.start == None:
            print("None list!")
        elif self.start.data == value:
            self.start = self.start.prox
            found = True
        else:
            prev = self.start
            aux = self.start.prox
            while aux:
                if aux.data == value:
                    prev.prox = aux.prox
                    found = True
                    break
                prev = aux
                aux = aux.prox
        if not found:
            print("\n" + value + " not found.")
        self.show()