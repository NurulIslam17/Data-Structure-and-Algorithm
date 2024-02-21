from collections import *


class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class Tree:
   def __init__(self):
      self.root = None

   def rightView(self, root):
      right_view = []
      if root is None:
         return right_view
      queue = deque([])
      queue.append(self.root)

      while len(queue) != 0:
         last = len(queue)
         for i in range(last):
            curr = queue.popleft()
            if i == last-1:
               right_view.append(curr.data)
            if curr.left is not None:
               queue.append(curr.left)
            if curr.right is not None:
               queue.append(curr.right)
      return right_view


if __name__ == "__main__":
   t = Tree()
   t.root = Node(2)
   t.root.left = Node(1)
   t.root.right = Node(4)
   t.root.left.left = Node(5)
   t.root.right.left = Node(6)
   t.root.right.right = Node(8)
   t.root.right.left.left = Node(9)
   print(t.rightView(t.root))
