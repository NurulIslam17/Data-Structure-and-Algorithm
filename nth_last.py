class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


class LinkedList:
   def __init__(self):
      self.head = None

   def append(self, val):
      new_node = Node(val)
      new_node.next = self.head
      self.head = new_node

   def printLL(self):
      cur = self.head
      while cur is not None:
         print(cur.data, end=" ")
         cur = cur.next

   def nthLast(self, val):
      cur = self.head
      prev = self.head
      for i in range(val):
         cur = cur.next
      while cur is not None:
         prev = prev.next
         cur = cur.next
      print("Result : ", prev.data)


ll = LinkedList()
ll.append(32)
ll.append(24)
ll.append(12)
ll.append(52)
ll.append(75)
ll.append(12)
ll.append(42)

ll.nthLast(2)
ll.printLL()
