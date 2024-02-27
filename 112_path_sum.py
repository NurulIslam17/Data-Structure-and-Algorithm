# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def calculateSum(node,sum):
            if node is None:
                return False
            sum += node.val
            if node.left is None and node.right is None:
                return sum == targetSum
            return (calculateSum(node.left,sum) or calculateSum(node.right,sum))
        return calculateSum(root,0)

