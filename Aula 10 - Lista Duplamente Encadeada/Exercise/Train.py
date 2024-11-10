from Wagon import Wagon

class Train:
    def __init__(self):
        self.locomotive_A = None
        self.locomotive_B = None

    def add(self, wagon_num):
        new_wagon = Wagon(wagon_num)
        if self.locomotive_A is None:
            self.locomotive_A = new_wagon
            self.locomotive_B = new_wagon
        else:
            if new_wagon.num < self.locomotive_A.num:
                new_wagon.next = self.locomotive_A
                self.locomotive_A.prev = new_wagon
                self.locomotive_A = new_wagon
            else:
                prev = self.locomotive_A
                current = self.locomotive_A.next
                while current:
                    if new_wagon.num < current.num:
                        prev.next = new_wagon
                        current.prev = new_wagon
                        new_wagon.prev = prev
                        new_wagon.next = current
                        break
                    prev = current
                    current = current.next
                if current is None:
                    prev.next = new_wagon
                    new_wagon.prev = prev
                    self.locomotive_B = new_wagon
        self.showForward()

    def showForward(self):
        print("\n--------------------------------")
        if self.locomotive_A is None:
            print("List is empty!")
        else:
            current = self.locomotive_A
            while current:
                print(current.num, end=" <-> " if current.next else "\n")
                current = current.next
    
    def showBackward(self):
        print("\n--------------------------------")
        if self.locomotive_A is None:
            print("List is empty!")
        else:
            current = self.locomotive_B
            while current:
                print(current.num, end=" <-> " if current.prev else "\n")
                current = current.prev