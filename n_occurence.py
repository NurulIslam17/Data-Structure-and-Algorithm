import random


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

   def printlist(self):
      cur = self.head
      while cur is not None:
         print(cur.data, end=" | ")
         cur = cur.next

   def nOccurences(self, n):
      count = 0
      cur = self.head
      while cur is not None:
         if cur.data == n:
            count += 1
         cur = cur.next
      print(f'{n} repeated {count} times.')


ll = LinkedList()

for i in range(0, 9):
   ll.append(random.randint(1, 9))

ll.nOccurences(random.randint(1, 9))
ll.printlist()
