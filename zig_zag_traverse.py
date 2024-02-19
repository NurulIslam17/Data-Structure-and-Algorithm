from collections import *


class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class Tree:
   def __init__(self):
      self.root = None

   def traverse(self, root):
      btf = []
      left_to_right = True

      if root is None:
         return btf

      queue = deque([])
      queue.append(self.root)
      while len(queue) != 0:
         cur_len = len(queue)
         curr_level = deque()
         for i in range(cur_len):
            cur = queue.popleft()

            if left_to_right:
               curr_level.append(cur.data)
            else:
               curr_level.appendleft(cur.data)

            if cur.left is not None:
               queue.append(cur.left)
            if cur.right is not None:
               queue.append(cur.right)

         btf.append(list(curr_level))
         left_to_right = not left_to_right
      return btf


if __name__ == "__main__":
   t = Tree()
   t.root = Node(12)
   t.root.left = Node(7)
   t.root.right = Node(1)
   t.root.left.right = Node(9)
   t.root.right.left = Node(10)
   t.root.right.right = Node(5)
   t.root.left.right.left = Node(12)
   t.root.left.right.right = Node(13)

   print(t.traverse(t.root))
