from Node import Node

class OrderedLinkedList:
    def __init__(self):
        self.start = None

    def show(self):
        print("\n--------------------------------")
        if self.start == None:
            print( "\nNone List!")
        else:
            aux = self.start
            while aux:
                print(aux.data)
                aux = aux.prox

    def add(self, value):
        nodo = Node(value)
        if self.start == None:
            self.start = nodo 
        else:
            if nodo.data < self.start.data:
                nodo.prox = self.start
                self.start = nodo
            else:
                prev = self.start
                aux = self.start.prox
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
        if self.start == None:
            print("Could not be removed!")
        else:
            found = False
            if value == self.start.data:
                self.start = self.start.prox
                found = True
            else:
                prev = self.start
                aux = self.start.prox
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