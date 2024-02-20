from collections import *


class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class Tree:
   def __init__(self):
      self.root = None

   def levelOrderSuccessor(self, root, key):
      if root is None:
         return
      queue = deque([])
      queue.append(self.root)
      while len(queue) != 0:
         cur = queue.popleft()
         if cur.left is not None:
            queue.append(cur.left)
         if cur.right is not None:
            queue.append(cur.right)
         if cur.data == key:
            break
      return queue.popleft().data


if __name__ == "__main__":
   t = Tree()
   t.root = Node(1)
   t.root.left = Node(2)
   t.root.right = Node(3)
   t.root.left.left = Node(4)
   t.root.left.left.left = Node(5)
   t.root.right.left = Node(6)
   t.root.right.right = Node(7)
   t.root.right.right.left = Node(8)
   print(t.levelOrderSuccessor(t.root, 7))
