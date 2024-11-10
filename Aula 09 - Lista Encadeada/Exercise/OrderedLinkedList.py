from Node import Node

class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        print("\n--------------------------------")
        if self.head == None:
            print( "\nNone List!")
        else:
            aux = self.head
            while aux:
                print(aux.data)
                aux = aux.prox

    def add(self, value):
        nodo = Node(value)
        if self.head == None:
            self.head = nodo 
        else:
            if nodo.data < self.head.data:
                nodo.prox = self.head
                self.head = nodo
            else:
                prev = self.head
                aux = self.head.prox
                while aux:
                    if nodo.data < aux.data :
                        prev.prox = nodo
                        nodo.prox = aux
                        break
                    prev = aux
                    aux = aux.prox
                if aux == None:
                    prev.prox = nodo
        self.show()

    def remove(self, value):
        if self.head == None:
            print("Could not be removed!")
        else:
            found = False
            if value == self.head.data:
                self.head = self.head.prox
                found = True
            else:
                prev = self.head
                aux = self.head.prox
                while aux:
                    if value == aux.data:
                        prev.prox = aux.prox
                        found = True
                        break
                    else:
                        prev = aux
                        aux = aux.prox
        if found:
            print(value, " was found and removed!")     
        else:
            print("\n" + value + " not found.")
        self.show()