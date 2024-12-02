from Wagon import Wagon

class Train:
    def __init__(self):
        self.locomotive_A = None
        self.locomotive_B = None
        self.counter = 0

    def add(self, wagon_num):
        new_wagon = Wagon(wagon_num)
        if self.locomotive_A is None:
            self.locomotive_A = new_wagon
        else:
            self.locomotive_B.next = new_wagon
        self.locomotive_B = new_wagon
        self.counter += 1
        self.show()

    def remove(self):
        if self.locomotive_A is None:
            print("\n--------------------------------")
            print("The queue is empty, nothing to remove.")
            return
        else:
            self.locomotive_A = self.locomotive_A.next
            if self.locomotive_A is None:
                self.locomotive_B = None
            self.counter -= 1
        self.show()

    def show(self):
        print("\n--------------------------------")
        if self.locomotive_A is None:
            print("List is empty!")
        else:
            print("Queue with", self.counter, "elements")
            current = self.locomotive_A
            while current:
                print(current.num, end=" <-> " if current.next else "\n")
                current = current.next