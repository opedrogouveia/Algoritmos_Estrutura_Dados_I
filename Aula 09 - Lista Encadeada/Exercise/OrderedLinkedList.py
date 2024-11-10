from Node import Node

class OrderedLinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        print("\n--------------------------------")
        if self.head == None:
            print( "\nNone List!")
        else:
            current = self.head
            while current:
                print(current.data)
                current = current.next

    def add(self, value):
        nodo = Node(value)
        if self.head == None:
            self.head = nodo 
        else:
            if nodo.data < self.head.data:
                nodo.next = self.head
                self.head = nodo
            else:
                prev = self.head
                current = self.head.next
                while current:
                    if nodo.data < current.data :
                        prev.next = nodo
                        nodo.next = current
                        break
                    prev = current
                    current = current.next
                if current == None:
                    prev.next = nodo
        self.show()

    def remove(self, value):
        if self.head == None:
            print("Could not be removed!")
        else:
            found = False
            if value == self.head.data:
                self.head = self.head.next
                found = True
            else:
                prev = self.head
                current = self.head.next
                while current:
                    if value == current.data:
                        prev.next = current.next
                        found = True
                        break
                    else:
                        prev = current
                        current = current.next
        if found:
            print(value, " was found and removed!")     
        else:
            print("\n" + value + " not found.")
        self.show()