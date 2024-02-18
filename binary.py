class Node:
   def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None


class BinaryTree:
   def __init__(self):
      self.root = None

   def preOrder(self, root):
      if root is None:
         return
      print(root.data, end=" ")
      self.preOrder(root.left)
      self.preOrder(root.right)

   def inOrder(self, root):
      if root is None:
         return
      self.inOrder(root.left)
      print(root.data, end=" ")
      self.inOrder(root.right)

   def postOrder(self, root):
      if root is None:
         return
      self.postOrder(root.left)
      self.postOrder(root.right)
      print(root.data, end=" ")


if __name__ == "__main__":
   bt = BinaryTree()

   bt.root = Node(1)
   bt.root.left = Node(2)
   bt.root.right = Node(3)
   bt.root.left.left = Node(4)
   bt.root.left.right = Node(5)
   bt.root.right.left = Node(6)
   bt.root.right.right = Node(7)

   print("Pre-Order Traversal (DLR):")
   bt.preOrder(bt.root)
   print()

   print("In-Order Traversal (LDR):")
   bt.inOrder(bt.root)
   print()

   print("Post-Order Traversal (LDR):")
   bt.postOrder(bt.root)
   print()
