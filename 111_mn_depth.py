from collections import *
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([])
        queue.append(root)
        min_depth = 0
        while len(queue) !=0:
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
