class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class Tree:
   def __init__(self):
      self.root = None

   def nodesNum(self, root):
      if root is None:
         return 0
      return 1 + self.nodesNum(root.left) + self.nodesNum(root.right)


if __name__ == "__main__":
   t = Tree()
   t.root = Node(1)
   t.root.left = Node(2)
   t.root.right = Node(3)

   t.root.left.left = Node(4)
   t.root.left.right = Node(5)

   t.root.right.left = Node(6)
   t.root.right.right = Node(7)

   print(t.nodesNum(t.root))
