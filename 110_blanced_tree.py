# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def isBalanced(self, root: Optional[TreeNode]) -> bool:

      def solve(root):
         if root is None:
            return 0
         l = solve(root.left)
         r = solve(root.right)

         if (l == -1 or r == -1 or abs(l - r) > 1):
            return -1
         else:
            return 1 + max(l, r)

      return solve(root) != -1
