from Book import Book

class Stack:
    def __init__(self):
        self.top = None

    def add(self, title, author, pages):
        new_book = Book(title, author, pages)
        if self.top is None:
            self.top = new_book
        else:
            new_book.next = self.top
            self.top = new_book
        self.show()

    def remove(self):
        if self.top is None:
            print("\n--------------------------------")
            print("The queue is empty, nothing to remove.")
            return
        else:
            self.top = self.top.next
        self.show()

    def show(self):
        print("\n--------------------------------")
        if self.top is None:
            print("Stack is empty!")
        else:
            current = self.top
            while current:
                print(f"\n Title: {current.title} - Author: {current.author} - Pages: {current.pages}")
                current = current.next