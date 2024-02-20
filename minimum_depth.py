from collections import *


class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class Tree:
   def __init__(self):
      self.root = None

   def minimumDepth(self, root):
      min_depth = 0
      if root is None:
         return min_depth
      queue = deque([])
      queue.append(self.root)
      while len(queue) is not None:
         min_depth +=1
         cur_len = len(queue)
         for i in range(cur_len):
            curr = queue.popleft()

            if curr.left is None and curr.right is None:
               return min_depth
            if curr.left is not None:
               queue.append(curr.left)
            if curr.right is not None:
               queue.append(curr.right)
      return min_depth


if __name__ == "__main__":
   t = Tree()
   t.root = Node(6)
   t.root.left = Node(4)
   t.root.right = Node(3)
   t.root.left.left = Node(2)
   t.root.left.right = Node(1)
   t.root.left.right.left = Node(8)
   print(t.minimumDepth(t.root))
