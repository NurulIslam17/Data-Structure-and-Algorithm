class Node:
   def __init__(self, data):
      self.data = data


class LinkedList:
   def __init__(self):
      self.head = None
      self.next = None

   def append(self, val):
      new_node = Node(val)
      new_node.next = self.head
      self.head = new_node

   def revList(self):
      prev = None
      curr = self.head

      while curr is not None:
         temp = curr.next
         curr.next = prev
         prev = curr
         curr = temp
      self.head = prev

   def printLL(self):
      cur = self.head
      while cur is not None:
         print(cur.data, end=" ")
         cur = cur.next


ll = LinkedList()
ll.append(3)
ll.append(2)
ll.append(1)
ll.revList()
ll.printLL()
