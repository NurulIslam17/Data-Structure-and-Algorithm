class Node:
   def __init__(self, data):
      self.data = data
      self.next = None


class Queue:
   def __init__(self):
      self.front = None
      self.rear = None

   def enqueue(self, value):
      new_node = Node(value)
      if self.rear is None:
         self.front = new_node
         self.rear = self.front
      else:
         self.rear.next = new_node
         self.rear = new_node

   def dequeue(self):
      if self.rear is None:
         print("Queue Empty !")
      else:
         self.front = self.front.next

   def traverse(self):
      cur = self.front
      while cur is not None:
         print(cur.data, end='  ')
         cur = cur.next


q = Queue()

q.enqueue(3)
q.enqueue(35)
q.enqueue(5)
# q.dequeue()
q.traverse()
