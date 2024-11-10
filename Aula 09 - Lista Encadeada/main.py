from LinkedList import LinkedList

list = LinkedList()

list.show()

list.addHead("Guilherme")
list.addHead("Daniel")
list.addTail("João")
list.addHead("Camila")
list.addTail("Leonardo")

list.removeHead()
list.removeTail()

list.remove("Guilherme")
list.remove("Pedro")