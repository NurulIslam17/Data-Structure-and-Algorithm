class Node:
   def __init__(self, value):
      self.data = value
      self.next = None


class Stack:
   def __init__(self):
      self.top = None

   def push(self, value):
      new_node = Node(value)
      new_node.next = self.top
      self.top = new_node

   def pop(self):
      if self.top is None:
         print("Stack is Empty")
      else:
         self.top = self.top.next

   def show(self):
      cur = self.top
      while cur is not None:
         print(cur.data)
         cur = cur.next


S = Stack()
S.push(29)
S.push(30)
S.show()
