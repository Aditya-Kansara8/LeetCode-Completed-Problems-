# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        maxl = 0
        def zig(n,d,l):
            nonlocal maxl
            if n is None:
                return 0
            maxl = max(maxl,l)
            zig(n.right,1, l+1 if d == 0 else 1)
            zig(n.left,0, l+1 if d == 1 else 1)
        zig(root.left,0,1)
        zig(root.right,1,1)
        return maxl

