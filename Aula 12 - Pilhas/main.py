from Stack import Stack

stack = Stack()

stack.add("The Great Gatsby", "F. Scott Fitzgerald", 218)
stack.add("To Kill a Mockingbird", "Harper Lee", 324)
stack.add("1984", "George Orwell", 328)
stack.add("Pride and Prejudice", "Jane Austen", 279)
stack.add("Moby-Dick", "Herman Melville", 635)

stack.show()

print("\nRemovendo livros da pilha:")
stack.remove()
stack.remove()
stack.remove()
stack.remove()
stack.remove()

stack.remove()
