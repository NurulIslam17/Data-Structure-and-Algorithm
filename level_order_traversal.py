from collections import *


class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class LevelOrderTraverse:
   def __init__(self):
      self.root = None

   def traverse(self, root):
      bfs = []
      if root is None:
         return bfs
      queue = deque([])
      queue.append(self.root)
      while len(queue) != 0:
         cur_len = len(queue)
         curr_level = []
         for i in range(cur_len):
            curr = queue.popleft()
            curr_level.append(curr.data)

            if curr.left is not None:
               queue.append(curr.left)
            if curr.right is not None:
               queue.append(curr.right)
         bfs.append(curr_level)
      return bfs


if __name__ == "__main__":
   t = LevelOrderTraverse()
   t.root = Node(12)
   t.root.left = Node(7)
   t.root.right = Node(1)
   t.root.left.right = Node(9)
   t.root.right.left = Node(10)
   t.root.right.right = Node(5)
   print(t.traverse(t.root))
