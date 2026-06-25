# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxl = 0
        def zig(n, left, right):
            nonlocal maxl
            if n is None:
                return
            maxl = max(maxl, left, right)
            zig(n.left, right + 1, 0)
            zig(n.right, 0, left + 1)
        zig(root, 0, 0)
        return maxl

