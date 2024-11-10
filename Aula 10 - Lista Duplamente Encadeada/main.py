from DoublyLinkedList import DoublyLinkedList

dll = DoublyLinkedList()
    
print("AddHead(10)")
dll.addHead(10)
print("AddTail(20)")
dll.addTail(20)
print("AddHead(5)")
dll.addHead(5)
print("AddTail(25)")
dll.addTail(25)

print("\nShow list forward:")
dll.showForward()
print("\nShow list backward:")
dll.showBackward()

print("\nAdd(15, position=2)")
dll.add(15, 2)
print("\nShow list forward after adding 15 at position 2:")
dll.showForward()

print("\nRemoveHead")
dll.removeHead()
print("\nRemoveTail")
dll.removeTail()

print("\nRemove(15)")
dll.remove(15)
print("\nRemove(100) (element not in list)")
dll.remove(100)